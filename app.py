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
        return "Please type a question so I can help you."

    # 1. Greetings
    if "hello" in t or "hi" in t or "hey" in t:
        return "Hello 👋! How can I assist you today?"

    # 2. Basic course info
    if "course" in t or "courses" in t:
        return "We offer Python, Web Development, Data Science, Machine Learning, Java, and more."

    # 3. Project help
    if "project" in t:
        return "For projects, pick a topic you like, break it into sections, research each part, and build step-by-step."

    # 4. Registration
    if "register" in t or "signup" in t:
        return "To register, go to the Register page, fill your details, and create a strong password."

    # 5. Thanks
    if "thank" in t:
        return "You're welcome 😊! Let me know if you need more help."

    # 6. Goodbye
    if "bye" in t or "logout" in t:
        return "Goodbye 👋! Study well and come back anytime."

    # 7. ML Recommendation
    if "recommend" in t or "suggest" in t:
        return "Based on your learning pattern, I recommend focusing on Python fundamentals and practicing daily."

    # 8. Attendance-related
    if "attendance" in t:
        return "Your attendance must be above 75% to avoid academic alerts."

    # 9. Low attendance
    if "low attendance" in t or "attendance drop" in t:
        return "Your attendance is low. Please attend upcoming classes regularly to avoid warnings."

    # 10. Performance
    if "performance" in t or "result" in t:
        return "Your recent performance shows improvement. Keep solving assignments regularly."

    # 11. How to improve
    if "improve" in t:
        return "To improve academically, revise notes daily and solve previous assignments."

    # 12. Study material
    if "material" in t or "notes" in t:
        return "Study materials are available in the Resources tab of your dashboard."

    # 13. Dashboard
    if "dashboard" in t:
        return "Your student dashboard shows your performance graph, attendance, and course progress."

    # 14. Admin dashboard
    if "admin" in t:
        return "The admin dashboard helps manage students, performance, and attendance alerts."

    # 15. Forgot password
    if "forgot" in t and "password" in t:
        return "Click the 'Forgot Password' option on the login page to reset it."

    # 16. Login issue
    if "login" in t or "can't login" in t:
        return "Make sure your username and password are correct. If not, reset your password."

    # 17. Student login credentials info
    if "student login" in t:
        return "Use your student ID and password to log in to your dashboard."

    # 18. Admin credentials
    if "admin login" in t:
        return "Only admins with verified credentials can access the admin panel."

    # 19. Attendance meaning
    if "what is attendance" in t:
        return "Attendance represents class participation percentage. Stay above 75%."

    # 20. Course timing
    if "timing" in t or "schedule" in t:
        return "Classes are available in morning, afternoon, and evening batches."

    # 21. When is next class?
    if "next class" in t:
        return "Check your dashboard calendar for your next class schedule."

    # 22. Assignments
    if "assignment" in t:
        return "Assignments are released weekly. Submit on time for best performance."

    # 23. Late submission
    if "late" in t and "assignment" in t:
        return "Late submissions may receive reduced marks. Please inform your instructor."

    # 24. Exams
    if "exam" in t:
        return "Exams are conducted online with multiple-choice and programming tasks."

    # 25. Exam date
    if "exam date" in t:
        return "Your exam date is available in the Exam Schedule section."

    # 26. Study tips
    if "study tips" in t or "how to study" in t:
        return "Follow a daily study plan, practice coding, and revise previous lessons."

    # 27. Career guidance
    if "career" in t or "future" in t:
        return "Based on your skills, careers like Data Analyst, Web Developer, or ML Engineer suit you."

    # 28. Machine learning
    if "machine learning" in t:
        return "ML is about making computers learn from data. Start with Python and linear regression."

    # 29. Python help
    if "python" in t:
        return "Python is beginner-friendly. Start with variables, loops, functions, and file handling."

    # 30. Java help
    if "java" in t:
        return "Java is great for OOP and enterprise apps. Practice classes and objects daily."

    # 31. C programming help
    if "c program" in t or "c language" in t:
        return "C language is great for logic building. Start with variables, loops, and arrays."

    # 32. C++ programming help
    if "c++" in t or "cpp" in t:
        return "C++ is useful for competitive programming. Practice OOP concepts and STL."

    # 33. HTML help
    if "html" in t:
        return "HTML is the structure of web pages. Start with tags, forms, and basic layouts."

    # 34. CSS help
    if "css" in t:
        return "CSS controls styling. Learn selectors, flexbox, grid, and responsive design."

    # 35. JavaScript help
    if "javascript" in t or "js" in t:
        return "JavaScript powers web interactivity. Begin with variables, events, and DOM."

    # 36. Data science info
    if "data science" in t:
        return "Data Science combines statistics and programming. Start with Python and pandas."

    # 37. AI help
    if "ai" in t or "artificial intelligence" in t:
        return "AI focuses on building intelligent systems. Learn Python, ML, and neural networks."

    # 38. Deep learning
    if "deep learning" in t:
        return "Deep learning uses neural networks for AI. Begin with TensorFlow or PyTorch."

    # 39. Database help
    if "database" in t or "sql" in t:
        return "SQL manages data. Learn SELECT, INSERT, UPDATE, DELETE, and JOIN queries."

    # 40. MySQL help
    if "mysql" in t:
        return "MySQL is a relational database. Practice table creation and CRUD operations."

    # 41. SQLite help
    if "sqlite" in t:
        return "SQLite is lightweight and perfect for local apps. No server installation needed."

    # 42. Flask help
    if "flask" in t:
        return "Flask is a Python web framework. Learn routing, templates, and forms."

    # 43. Django help
    if "django" in t:
        return "Django is a powerful backend framework. Start with models, views, and templates."

    # 44. API meaning
    if "api" in t:
        return "API allows systems to communicate. Learn GET, POST, PUT, DELETE methods."

    # 45. Debugging help
    if "debug" in t or "error" in t:
        return "Debugging involves checking code line by line. Review errors carefully."

    # 46. IDE recommendation
    if "ide" in t or "editor" in t:
        return "VS Code is recommended. It's lightweight and supports many languages."

    # 47. Learning path
    if "learning path" in t or "roadmap" in t:
        return "Start slow, follow a roadmap, practice daily, and build mini projects."

    # 48. Time management
    if "time management" in t:
        return "Use a study schedule and break tasks into smaller pieces."

    # 49. Stress
    if "stress" in t or "tired" in t:
        return "Take breaks, sleep well, and study in sessions to avoid burnout."

    # 50. Motivation
    if "motivate" in t or "motivation" in t:
        return "Stay consistent. Small daily learning leads to big success!"

    # 51. Online class link
    if "class link" in t:
        return "Your class link is available on the student dashboard."

    # 52. Marks
    if "marks" in t or "score" in t:
        return "Your marks are updated after evaluation. Check the results section."

    # 53. Low marks
    if "low marks" in t or "bad score" in t:
        return "Don't worry. Review mistakes and practice similar questions."

    # 54. High marks
    if "high marks" in t or "good score" in t:
        return "Great job! Keep performing consistently."

    # 55. Performance warning
    if "warning" in t:
        return "Your performance needs attention. Focus on assignments and attendance."

    # 56. Password change
    if "change password" in t:
        return "Go to settings and update your password in the security section."

    # 57. Email issue
    if "email" in t and "issue" in t:
        return "Check your spam folder, and ensure you entered the correct email."

    # 58. Contact admin
    if "contact admin" in t:
        return "You can reach admin through the Contact Admin page."

    # 59. Profile update
    if "update profile" in t or "edit profile" in t:
        return "You can edit your profile details under the Profile Settings page."

    # 60. Mobile app
    if "app" in t or "mobile" in t:
        return "Our mobile app is in development and will be released soon."

    # 61. Course completion
    if "complete course" in t or "course completed" in t:
        return "Once you complete a course, your certificate will be generated automatically."

    # 62. Certificate download
    if "download certificate" in t or "certificate" in t:
        return "You can download your certificate from the Certificates section in your dashboard."

    # 63. Course progress
    if "progress" in t:
        return "Your course progress is updated daily. Check the progress bar for details."

    # 64. Extra classes
    if "extra class" in t or "special class" in t:
        return "Extra classes are scheduled for students who need additional support."

    # 65. Doubt session
    if "doubt" in t or "help session" in t:
        return "Doubt-clearing sessions happen every Friday."

    # 66. Holidays information
    if "holiday" in t or "vacation" in t:
        return "The holiday list is available in your dashboard."

    # 67. Fees
    if "fee" in t or "fees" in t:
        return "Fees vary by course. Check the Fees section for course-wise charges."

    # 68. Refund policy
    if "refund" in t:
        return "Refunds are available only within the first 3 days of enrollment."

    # 69. Payment methods
    if "payment" in t or "pay" in t:
        return "We accept UPI, net banking, debit/credit cards, and wallets."

    # 70. Installment option
    if "installment" in t:
        return "Installment options are available for selected long-term courses."

    # 71. Classroom rules
    if "rules" in t:
        return "Maintain discipline, attend regularly, and submit assignments on time."

    # 72. Study hours
    if "study hours" in t:
        return "Study at least 1–2 hours daily for consistent improvement."

    # 73. Group study
    if "group study" in t:
        return "Group study can help, but ensure you focus on your weak areas."

    # 74. Self-study
    if "self study" in t:
        return "Self-study strengthens your understanding. Set a fixed schedule."

    # 75. Internet issues
    if "internet" in t or "wifi" in t:
        return "Please ensure a stable internet connection for smooth learning."

    # 76. Laptop requirements
    if "laptop" in t or "system" in t:
        return "A basic laptop with 4–8GB RAM is enough for most courses."

    # 77. Phone usage
    if "phone" in t or "mobile" in t:
        return "You can attend classes on mobile, but coding works best on a laptop."

    # 78. Slow performance
    if "slow" in t or "lag" in t:
        return "Restart your system and close unnecessary apps for better performance."

    # 79. Update browser
    if "browser" in t:
        return "Please use the latest version of Chrome, Edge, or Firefox."

    # 80. Video not playing
    if "video" in t or "class video" in t:
        return "Try refreshing the page or checking your internet speed."

    # 81. Audio issue
    if "audio" in t or "sound" in t:
        return "Ensure your speakers or headphones are properly connected."

    # 82. Camera issue
    if "camera" in t or "webcam" in t:
        return "Give your browser permission to access the camera."

    # 83. Microphone issue
    if "mic" in t or "microphone" in t:
        return "Allow microphone access and check sound settings."

    # 84. Attendance correction
    if "correct attendance" in t:
        return "Contact your instructor for manual attendance correction."

    # 85. Wrong marks
    if "wrong marks" in t or "marks mistake" in t:
        return "Report the issue to your instructor or admin for correction."

    # 86. Reset progress
    if "reset progress" in t:
        return "Progress can only be reset manually by an admin."

    # 87. New courses
    if "new course" in t:
        return "New courses are added every month. Check the Updates section."

    # 88. Course difficulty
    if "difficulty" in t or "hard" in t:
        return "Start with basics and practice regularly. Ask for help if needed."

    # 89. Easy subjects
    if "easy subject" in t:
        return "HTML, CSS, and Python basics are great choices for beginners."

    # 90. Hard subjects
    if "hard subject" in t:
        return "Subjects like AI, ML, and Data Science need consistent practice."

    # 91. Revision advice
    if "revision" in t or "revise" in t:
        return "Revise your notes every weekend to strengthen your understanding."

    # 92. Daily schedule
    if "daily schedule" in t or "routine" in t:
        return "Follow a routine: 1 hour study + 30 minutes practice + 10 minutes review."

    # 93. Breaks
    if "break" in t or "rest" in t:
        return "Take short breaks every 45 minutes to improve focus."

    # 94. Memory improvement
    if "memory" in t or "remember" in t:
        return "Write short notes and revise them regularly to improve memory."

    # 95. Performance alerts
    if "alert" in t:
        return "Alerts notify students about attendance drops or low performance."

    # 96. Attendance report
    if "attendance report" in t:
        return "Your attendance report is available in the Attendance section."

    # 97. Performance report
    if "performance report" in t:
        return "Your performance report shows subject-wise strengths and weaknesses."

    # 98. Subject weakness
    if "weak" in t:
        return "Identify weak subjects and practice them more frequently."

    # 99. Subject strength
    if "strong" in t:
        return "Great! Use your strong subjects to boost overall performance."

    # 100. Internet speed
    if "speed" in t:
        return "A minimum of 5 Mbps internet speed is recommended."

    # 101. Quiz help
    if "quiz" in t:
        return "Quizzes help test your knowledge. Attempt them regularly."

    # 102. Test preparation
    if "prepare" in t or "preparation" in t:
        return "Start preparing early. Revise notes and solve past questions."

    # 103. Exam results
    if "result" in t:
        return "Results are updated once evaluations are complete."

    # 104. Skills recommendation
    if "skills" in t:
        return "Improve your skills by practicing coding, reading PDFs, and watching lectures."

    # 105. Internship eligibility
    if "eligible for internship" in t:
        return "You become eligible for internships after completing 70% of your course."

    # 106. Job placement
    if "job" in t or "placement" in t:
        return "We offer placement guidance and resume-building support."

    # 107. Resume help
    if "resume" in t or "cv" in t:
        return "Upload your resume in the Resume Builder section for feedback."

    # 108. Portfolio tips
    if "portfolio" in t:
        return "Create a portfolio with your best projects to impress recruiters."

    # 109. Project ideas
    if "project idea" in t:
        return "Try building a weather app, chatbot, attendance system, or portfolio website."

    # 110. Coding practice
    if "coding" in t or "code" in t:
        return "Practice coding daily to improve your problem-solving skills."

    # 111. Practice websites
    if "practice website" in t:
        return "You can practice coding on HackerRank, CodeChef, and LeetCode."

    # 112. Lab timing
    if "lab timing" in t:
        return "Labs are available 24/7 for students to practice."

    # 113. Attendance reminder
    if "remind" in t or "reminder" in t:
        return "We send reminders when your attendance drops below 80%."

    # 114. Leave application
    if "leave" in t:
        return "Submit your leave request through the Leave Application section."

    # 115. Class recording
    if "recording" in t or "recorded class" in t:
        return "Class recordings are uploaded within 24 hours."

    # 116. Batch change
    if "batch change" in t or "change batch" in t:
        return "You can request a batch change once per course."

    # 117. Course upgrade
    if "upgrade course" in t:
        return "You can upgrade your course from the Payments section."

    # 118. Course downgrade
    if "downgrade" in t:
        return "Course downgrades require admin approval."

    # 119. Contact teacher
    if "contact teacher" in t or "message teacher" in t:
        return "Use the Messages section to contact your teacher."

    # 120. Contact support
    if "support" in t:
        return "Our support team is available 9AM–9PM daily for assistance."

    # 121. Technical support
    if "technical issue" in t or "tech problem" in t:
        return "Please describe your technical issue. I’ll guide you through the solution."

    # 122. Forgot username
    if "forgot username" in t:
        return "Contact support to retrieve your username."

    # 123. Reset email
    if "change email" in t or "update email" in t:
        return "You can update your email in the Profile Settings."

    # 124. Wrong email
    if "wrong email" in t:
        return "Please enter the correct email or contact support for correction."

    # 125. Profile photo
    if "profile picture" in t or "photo" in t:
        return "Upload your profile picture in the Profile section."

    # 126. Notification settings
    if "notifications" in t:
        return "You can enable or disable notifications in Settings."

    # 127. Email verification
    if "verify email" in t:
        return "A verification link has been sent to your email. Please check your inbox."

    # 128. Account locked
    if "account locked" in t:
        return "Your account was locked due to multiple failed attempts. Contact support to unlock."

    # 129. Two-factor authentication
    if "2fa" in t or "two factor" in t:
        return "Two-factor authentication adds extra security to your account."

    # 130. Update password
    if "update password" in t:
        return "Go to security settings and update your password safely."

    # 131. Marks improvement tips
    if "improve marks" in t:
        return "Practice past papers and revise weekly to improve marks."

    # 132. Weak attendance
    if "weak attendance" in t:
        return "Attend upcoming classes regularly to improve your attendance."

    # 133. Performance analytics
    if "analytics" in t:
        return "Performance analytics show your progress, accuracy, and learning trends."

    # 134. Course recommendation
    if "which course" in t:
        return "I recommend Data Science or Web Development based on current student trends."

    # 135. Beginner course
    if "beginner" in t:
        return "Start with Python basics, HTML, CSS, and simple projects."

    # 136. Advanced course
    if "advanced" in t:
        return "For advanced learning, try AI, ML, and full-stack development."

    # 137. Chatbot help
    if "chatbot" in t:
        return "Our chatbot helps with academic queries, performance updates, and general support."

    # 138. Server issue
    if "server" in t:
        return "The server may be updating. Please try again after a few minutes."

    # 139. Page not loading
    if "page not load" in t or "page not opening" in t:
        return "Refresh the page or clear your browser cache."

    # 140. App crashing
    if "crash" in t:
        return "Restart the app and check for updates."

    # 141. Update app
    if "update app" in t:
        return "Updates improve performance. Please install the latest app version."

    # 142. Video quality
    if "quality" in t or "blurry" in t:
        return "Adjust the video quality settings or check your internet speed."

    # 143. Exam rules
    if "exam rules" in t:
        return "Follow exam rules: no cheating, camera on, and stable internet."

    # 144. Exam time
    if "exam time" in t:
        return "Exam times vary for each subject. Refer to the exam schedule."

    # 145. Assignment deadline
    if "deadline" in t:
        return "Assignment deadlines are shown in the Assignments tab."

    # 146. Submission failed
    if "submission failed" in t or "cannot submit" in t:
        return "Try uploading the file again or reduce its size."

    # 147. File size limit
    if "file size" in t:
        return "The maximum file size allowed is 10MB."

    # 148. Plagiarism
    if "plagiarism" in t or "copy" in t:
        return "Please submit original work. Plagiarism can reduce your marks."

    # 149. Project submission
    if "project submit" in t:
        return "Submit your project in the Projects section before the deadline."

    # 150. Project feedback
    if "project feedback" in t:
        return "Project feedback will be available within 3–5 days after submission."

    # 151. Teacher feedback
    if "teacher feedback" in t:
        return "Teacher feedback helps you understand your strengths and weaknesses."

    # 152. Re-evaluation
    if "recheck" in t or "reevaluate" in t:
        return "You can request re-evaluation through the Marks section."

    # 153. Unit test schedule
    if "unit test" in t:
        return "Unit test dates are available in the Exam Schedule section."

    # 154. Study strategy
    if "strategy" in t or "plan" in t:
        return "Use the 50-10 study rule: 50 minutes study, 10 minutes break."

    # 155. Class timings change
    if "change timing" in t or "class time change" in t:
        return "Timing changes require approval from your instructor."

    # 156. New announcement
    if "announcement" in t:
        return "New announcements are posted on your student dashboard."

    # 157. Update profile photo
    if "change photo" in t:
        return "Go to profile settings and upload a new picture."

    # 158. Course language
    if "language" in t:
        return "Courses are available in English and will support more languages soon."

    # 159. Online exam
    if "online exam" in t:
        return "Online exams require a stable internet connection and camera access."

    # 160. Exam instructions
    if "instructions" in t:
        return "Read exam instructions carefully before starting."

    # 161. Attendance marking time
    if "mark attendance" in t:
        return "Attendance is marked automatically when you join class."

    # 162. Exam syllabus
    if "syllabus" in t:
        return "Your syllabus is available in the Subjects section."

    # 163. Python projects
    if "python project" in t:
        return "Try building a calculator, chatbot, or student management system."

    # 164. Web development projects
    if "web project" in t or "website project" in t:
        return "Try creating a portfolio website, login system, or gallery page."

    # 165. Data science projects
    if "data science project" in t:
        return "Start with simple projects like Titanic survival prediction or sales forecasting."

    # 166. Internship certificate
    if "internship certificate" in t:
        return "Internship certificates are provided after successful completion."

    # 167. Attendance improvement tips
    if "attendance improve" in t:
        return "Attend regularly and avoid missing continuous classes."

    # 168. Study hours suggestion
    if "how many hours" in t:
        return "Study at least 1–2 hours daily for best results."

    # 169. Eligibility
    if "eligible" in t:
        return "Eligibility depends on your attendance and academic performance."

    # 170. Project partner
    if "partner" in t or "group project" in t:
        return "You may choose a partner for group projects with teacher approval."

    # 171. Extra credit
    if "extra credit" in t:
        return "Extra credit is awarded for active participation and project excellence."

    # 172. Missing files
    if "file missing" in t:
        return "Try re-uploading the file. If the issue continues, contact support."

    # 173. Update marks
    if "update marks" in t or "change marks" in t:
        return "Marks can only be updated by the instructor."

    # 174. Wrong question
    if "wrong question" in t:
        return "Report the wrong question to your instructor immediately."

    # 175. Upload photo
    if "upload photo" in t:
        return "Use the Upload section to add your photo."

    # 176. Notifications on
    if "turn on notifications" in t:
        return "Enable notifications in Settings > Notifications."

    # 177. Notifications off
    if "turn off notifications" in t:
        return "Disable notifications in Settings > Notifications."

    # 178. Dashboard error
    if "dashboard error" in t:
        return "Please refresh the dashboard or clear your browser cache."

    # 179. Password strength
    if "strong password" in t:
        return "Use at least 8 characters with a mix of letters, numbers, and symbols."

    # 180. File format
    if "file format" in t:
        return "Upload files in PDF, JPG, PNG, or DOCX format."

    # 181. Class attendance time
    if "when attendance" in t:
        return "Attendance is marked within the first 10 minutes of class."

    # 182. Device support
    if "device" in t:
        return "You can use mobile, laptop, or tablet for online classes."

    # 183. Reset settings
    if "reset settings" in t:
        return "You can reset settings from the Profile > Reset Settings option."

    # 184. Join meeting
    if "join meeting" in t or "join class" in t:
        return "Use the Join Class button available on your dashboard."

    # 185. Change subject
    if "change subject" in t:
        return "Subject changes require approval from your coordinator."

    # 186. Add subject
    if "add subject" in t:
        return "You can add subjects from the Course Enrollment section."

    # 187. Remove subject
    if "remove subject" in t:
        return "Contact admin to remove the subject from your list."

    # 188. Performance graph
    if "graph" in t or "chart" in t:
        return "Your performance graph is updated after every test."

    # 189. Monthly report
    if "monthly report" in t:
        return "Monthly performance reports are generated automatically."

    # 190. Study reminders
    if "study reminder" in t:
        return "Study reminders help you stay consistent. Enable them in Settings."

    # 191. AI recommendations
    if "ai recommend" in t:
        return "AI recommendations are based on your performance, attendance, and activity."

    # 192. Data update
    if "update data" in t:
        return "Your data is updated after each class, test, or activity by the system."

    # 193. Server maintenance
    if "maintenance" in t:
        return "The server is under maintenance. Please try again later."

    # 194. Logout help
    if "how to logout" in t:
        return "Click the Logout button in the top-right corner of the dashboard."

    # 195. Improve coding
    if "improve coding" in t:
        return "Practice coding daily, solve small problems, and try building mini projects."

    # 196. Study motivation
    if "no motivation" in t:
        return "It's normal to feel low. Take a break and restart with small tasks."

    # 197. Weak network
    if "weak network" in t:
        return "Try switching networks or moving closer to your Wi-Fi router."

    # 198. Exam preparation tips
    if "exam tips" in t:
        return "Revise notes, practice previous exams, and avoid last-minute cramming."

    # 199. Course switching
    if "switch course" in t:
        return "Course switching is allowed within the first 7 days of enrollment."

    # 200. Unknown query fallback
    if "help" in t or "question" in t:
        return "I’m here to assist you. Please ask your question clearly."

    # default fallback
    return "I’m still learning. Could you ask in a different way or be more specific?"


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
