"""
Example API endpoints for HSK Exam System
FastAPI implementation
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
import json

app = FastAPI(title="HSK Exam API", version="1.0.0")

# Load exam data
with open('output.json', 'r', encoding='utf-8') as f:
    EXAM_DATA = json.load(f)


# Models
class Option(BaseModel):
    option: str
    text: str


class Question(BaseModel):
    question_number: int
    question_text: str
    image: Optional[str]
    options: List[Option]
    correct_answer: Optional[str]


class Part(BaseModel):
    part_number: int
    part_title: str
    description: str
    question_type: str
    questions: List[Question]


class ExamResponse(BaseModel):
    exam_url: str
    exam_title: str
    audio_file: Optional[str]
    total_parts: int
    total_questions: int
    parts: List[Part]


class SubmitAnswersRequest(BaseModel):
    answers: Dict[int, str]  # {question_number: answer}


class SubmitAnswersResponse(BaseModel):
    score: int
    total: int
    percentage: float
    correct_answers: Dict[int, str]
    user_answers: Dict[int, str]
    results: Dict[int, bool]


# Endpoints
@app.get("/")
def root():
    return {
        "message": "HSK Exam API",
        "version": "1.0.0",
        "endpoints": {
            "GET /exam": "Get full exam data",
            "GET /exam/part/{part_number}": "Get specific part",
            "GET /exam/question/{question_number}": "Get specific question",
            "POST /exam/submit": "Submit answers and get score",
            "GET /exam/audio": "Get audio file URL"
        }
    }


@app.get("/exam", response_model=ExamResponse)
def get_full_exam():
    """Get complete exam with all parts and questions"""
    return EXAM_DATA


@app.get("/exam/part/{part_number}")
def get_part(part_number: int):
    """Get a specific part by number (1-4)"""
    for part in EXAM_DATA["parts"]:
        if part["part_number"] == part_number:
            return part
    raise HTTPException(status_code=404, detail=f"Part {part_number} not found")


@app.get("/exam/question/{question_number}")
def get_question(question_number: int):
    """Get a specific question by number (1-20)"""
    for part in EXAM_DATA["parts"]:
        for question in part["questions"]:
            if question["question_number"] == question_number:
                return {
                    "part": part["part_number"],
                    "question": question
                }
    raise HTTPException(status_code=404, detail=f"Question {question_number} not found")


@app.get("/exam/audio")
def get_audio():
    """Get audio file URL"""
    return {
        "audio_file": EXAM_DATA["audio_file"],
        "format": "mp3"
    }


@app.post("/exam/submit", response_model=SubmitAnswersResponse)
def submit_answers(submission: SubmitAnswersRequest):
    """
    Submit answers and get score
    
    Example request body:
    {
        "answers": {
            "1": "TRUE",
            "2": "FALSE",
            "6": "A",
            "16": "A"
        }
    }
    """
    # Note: This is a demo. In production, correct_answer should be stored separately
    # and not sent to client
    correct_answers = {
        1: "TRUE", 2: "FALSE", 3: "TRUE", 4: "FALSE", 5: "TRUE",
        6: "B", 7: "A", 8: "C", 9: "B", 10: "A",
        11: "A", 12: "C", 13: "E", 14: "B", 15: "F",
        16: "A", 17: "C", 18: "B", 19: "A", 20: "C"
    }
    
    user_answers = submission.answers
    results = {}
    correct_count = 0
    
    for q_num, correct_ans in correct_answers.items():
        user_ans = user_answers.get(q_num)
        is_correct = user_ans == correct_ans
        results[q_num] = is_correct
        if is_correct:
            correct_count += 1
    
    total_questions = len(correct_answers)
    percentage = (correct_count / total_questions) * 100
    
    return {
        "score": correct_count,
        "total": total_questions,
        "percentage": round(percentage, 2),
        "correct_answers": correct_answers,
        "user_answers": user_answers,
        "results": results
    }


# Run with: uvicorn api_example:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
