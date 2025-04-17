from fastapi import FastAPI
from pydantic import BaseModel
from methods.getAttendance import getAttendance  
from auth.login import getCookies  
from parser.attendance_parser import parse_attendance_data  

class Student(BaseModel):
    email: str
    password: str

app = FastAPI()

@app.get('/')
def home():
    return {
        "message": "Welcome to the Backademia API. Backademia is the easiest-to-use abstraction to scrape data from SRM Academia.",
        "routes": [
            {
                "path": "/attendance",
                "method": "POST",
                "description": "Fetch attendance data",
                "body": {
                    "email": "string",
                    "password": "string"
                },
            }
        ]
    }

@app.post('/attendance')
def attendance(student: Student):
    cookies = dict(getCookies(student.email, student.password))
    attendance_response = getAttendance(cookies)
    
    if attendance_response.status_code == 200:
        html_content = attendance_response.text
        final = parse_attendance_data(html_content)
        return final
    else:
        return {"error": "Failed to fetch attendance data", "status_code": attendance_response.status_code}