import os
import sqlite3
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# In real deployments, use a secure environment variable instead
app.secret_key = os.environ.get("SECRET_KEY", "dev_secret_key_change_me")

DATABASE = "database.db"

# ---------- Database helpers ----------
def get_db():
    """Open a connection (one per request)."""
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exc):
    """Close database connection after request."""
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    """Create users table if it doesn't exist."""
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    db.commit()
    db.close()

# ---------- Simple login helper ----------
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to view that page.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

# ---------- Simple AI-ish response function ----------
def simple_ai_response(text: str) -> str:
    t = text.lower().strip()
    if not t:
        return "Please type a question."
    if "hello" in t or "hi" in t:
        return "Hello 👋! I'm your student support assistant. Ask me about courses, schedules or help with projects."
    if "course" in t or "courses" in t:
        return "We support courses like Python, Web Development, Data Science and AI."
    if "project" in t:
        return "For mini projects: pick a small problem, build steadily, commit code often, and write a README."
    if "register" in t or "signup" in t:
        return "To register: go to Register, choose a unique username and a secure password."
    if "thank" in t:
        return "You're welcome! 🙂"
    if "bye" in t or "logout" in t:
        return "Goodbye — come back soon!"
    # default fallback
    return "I’m still learning. Could you ask in a different way or be more specific?"

# ---------- Routes ----------
@app.route("/")
def index():
    return render_template("index.html", username=session.get("username"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if not username or not password:
            flash("Please provide both username and password.", "danger")
            return render_template("register.html")

        db = get_db()
        try:
            hashed = generate_password_hash(password)
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
            db.commit()
            flash("Registration successful. Please log in.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username already taken. Choose another.", "danger")
            return render_template("register.html")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if user and check_password_hash(user["password"], password):
            # store minimal data in session
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            # reset chat history on login
            session["history"] = []
            flash("Logged in successfully.", "success")
            return redirect(url_for("chatbot"))
        else:
            flash("Invalid username or password.", "danger")
            return render_template("login.html")

    return render_template("login.html")

@app.route("/chatbot", methods=["GET", "POST"])
@login_required
def chatbot():
    history = session.get("history", [])
    bot_reply = None

    if request.method == "POST":
        user_message = request.form.get("message", "").strip()
        if user_message:
            # append user message
            history.append(("You", user_message))
            bot_reply = simple_ai_response(user_message)
            history.append(("Bot", bot_reply))
            # save back to session
            session["history"] = history
            session.modified = True

    return render_template("chatbot.html", history=history, username=session.get("username"))

@app.route("/logout")
def logout():
    session_keys = ["user_id", "username", "history"]
    for k in session_keys:
        session.pop(k, None)
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))

# ---------- Run ----------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
