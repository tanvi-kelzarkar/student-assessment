# Student Speaking Assessment Report (Full Stack)

This project is a Student Speaking Assessment Report Page inspired by platforms like SpeechAce / IELTS score reports.  
It is built as a functional prototype to demonstrate frontend UI skills, basic backend handling, and feedback logic.

---

## Tech Stack Used

Frontend:
- React
- HTML, CSS, JavaScript

Backend:
- Python
- Flask
- Flask-CORS

Data Source:
- In-memory Python object (no database)

---

## Features Implemented

- Overall speaking score (out of 9)
- Skill-wise scores:
  - Pronunciation
  - Fluency
  - Vocabulary
  - Grammar
- Color-coded progress bars for each skill
- Descriptive feedback based on score ranges
- React frontend connected to Flask backend API
- Loading state while fetching data from backend

---

## Feedback Logic

Feedback is generated automatically based on score:

- Score ≥ 8 → Excellent performance with strong control
- Score 6–7 → Good performance with minor inaccuracies
- Score < 6 → Needs improvement

Feedback updates automatically when score values change.

---

## UI Details

- Clean, SpeechAce-inspired layout
- Highlighted overall score badge
- Color legend for easy interpretation:
  - Green – Strong performance
  - Yellow – Average performance
  - Red – Needs improvement
- Focus on clarity and readability

---


## Where the Scores Are Stored

Scores are stored in the backend file:

backend/app.py

Inside an in-memory Python dictionary:

student_report = {
  "studentName": "Demo Student",
  "overall": 7,
  "maxScore": 9,
  "skills": {
    "pronunciation": 7,
    "fluency": 6,
    "vocabulary": 8,
    "grammar": 7
  }
}

Changing these values automatically updates the frontend UI.


## How to Run the Project

**Backend (Flask)**

backend/

python -m venv venv  
venv\Scripts\activate  

pip install flask flask-cors  

python app.py  

http://127.0.0.1:5000

---

**Frontend (React)**

frontend/

npm install  

npm start  

http://localhost:3000

