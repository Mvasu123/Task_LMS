
from models.lms import Address,BaseModel
class StudentResponse(BaseModel):
    name: str
    age: int
    address: Address