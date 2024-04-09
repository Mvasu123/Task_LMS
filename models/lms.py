from pydantic import BaseModel

# class Address(BaseModel):
#     city:str
#     country:str


# class student(BaseModel):
#     name: str
#     age:int
#     address:Address
class Address(BaseModel):
    city: str
    country: str

class StudentBase(BaseModel):
    name: str
    age: int
    address: Address

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class Student(StudentBase):
    id: str

