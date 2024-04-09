from typing import Optional
from fastapi import APIRouter, HTTPException, Path
from models.lms import StudentCreate,StudentUpdate,Student
from config.database import students_collection
from schema.schemas import StudentResponse
import uuid


router =APIRouter()

@router.post("/students", response_model=dict, status_code=201)
async def create_students(student: StudentCreate):
    student_dict = student.model_dump()
   
    student_uuid = uuid.uuid4()
    student_dict["id"] = str(student_uuid)
    
    # Insert the student record into the collection
    result = await students_collection.insert_one(student_dict)
    
  
    return {"id": str(student_uuid)}

@router.get("/students", response_model=dict, status_code=200)
async def list_students(country: Optional[str] = None, age: Optional[int] = None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}


    students = await students_collection.find(query).to_list(length=None)

    formatted_students = [{"name": student["name"], "age": student["age"]} for student in students]

    return {"data": formatted_students}

@router.get("/students/{id}", response_model=StudentResponse)
async def Fetch_student(id: str = Path(...)):
    student = await students_collection.find_one({"id": id})
    if student:
        
        return Student(**student)
    raise HTTPException(status_code=404, detail="Student not found")

@router.patch("/students/{id}", status_code=204)
async def update_student(id: str, student_data: StudentUpdate):
    
    student_data_dict = student_data.model_dump(exclude_unset=True) 
    

    
    result = await students_collection.update_one({"id": id}, {"$set": student_data_dict})
    
    if result.modified_count == 1:
        return
    else:
        raise HTTPException(status_code=404, detail="Student not found")
    
@router.delete("/students/{id}", status_code=200, summary="Delete student")
async def delete_student(id: str):
        
        result = await students_collection.delete_one({"id": id})
               
        if result.deleted_count == 1:
            return {"message": "Student deleted successfully"}
       