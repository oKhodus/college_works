from flask import Flask, jsonify

app = Flask(__name__)

cv_data = {
    "name": "Oleksii Khodus",
    "expereince": [
        {"company": "GlobyAi", "role": "Wordpress Developer", "years": "0.3"},
    ],
    "skills": ["Python", "JavaScript", "Flask", "Git", "OOP", "Algorithms and Data Structures", "WordPress", "Bash", "pytest", "CSS", "HTML"],
    "contact": {
        "email": "exalchel@gmail.com",
        "linkedin": "https://www.linkedin.com/in/oleksii-khodus-235b32263/",
        "github": "github.com/oKhodus",
    },
    "education": [
        {"degree": "BSc IT Systems Development", "year": "2027", "university": "University of Tartu"}
    ],
    "projects": [
        {"title": "Tomate!", "year": 2024, "description": "Simple Pomodoro timer built with Python, tkinter and pygame"},
        {"title": "toodoo", "year": 2025, "description": "A simple command line interface (CLI) was made to track what you need to do"},
    ],
}

@app.route("/cv", methods=["GET"])
def get_cv():
    return jsonify(cv_data)

@app.route("/cv/experience", methods=["GET"])
def get_experience():
    return jsonify({"experience": cv_data["experience"]})

@app.route("/cv/skills", methods=["GET"])
def get_skills():
    return jsonify({"skills": cv_data["skills"]})

@app.route("/cv/contact", methods=["GET"])
def get_contact():
    return jsonify({"contact": cv_data["contact"]})

@app.route("/cv/education", methods=["GET"])
def get_education():
    return jsonify({"education": cv_data["education"]})

@app.route("/cv/projects", methods=["GET"])
def get_projects():
    return jsonify({"projects": cv_data["projects"]})

if __name__ == "__main__":
    app.run(debug=True)