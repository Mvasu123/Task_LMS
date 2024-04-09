from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://papis123:fTX2mkJv1Tm3Kazt@lms.efkc32o.mongodb.net/?retryWrites=true&w=majority&appName=LMS"

# Connect to MongoDB Atlas
client = AsyncIOMotorClient(MONGO_URI)
db = client.get_database("LMS")  # Replace "your_database_name" with your actual database name
students_collection = db.get_collection("students")  # Replace "students" with your actual collection name
