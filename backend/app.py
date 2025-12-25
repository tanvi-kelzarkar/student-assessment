from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---- Student Report Data (In-Memory) ----
student_report = {
    "studentName": "Demo Student",
    "overall": 8,
    "maxScore": 9,
    "skills": {
        "pronunciation": 7,
        "fluency": 6,
        "vocabulary": 8,
        "grammar": 7
    }
}

# ---- Test Route ----
@app.route("/")
def home():
    return jsonify({
        "message": "Flask backend is running successfully!"
    })

# ---- Report API ----
@app.route("/api/report")
def get_report():
    return jsonify(student_report)

if __name__ == "__main__":
    app.run(debug=True)
