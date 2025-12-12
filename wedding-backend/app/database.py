from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

class Database:
    client: AsyncIOMotorClient = None

    def connect(self):
        self.client = AsyncIOMotorClient(settings.MONGO_URL)
        print("Connected to MongoDB via Motor")

    def close(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed")

    def get_db(self):
        return self.client[settings.DB_NAME]

db = Database()

# Helper to get the master collection
def get_master_collection():
    return db.get_db()["companies"]

# Helper to get a dynamic tenant collection
def get_tenant_collection(company_name: str):
    sanitized_name = company_name.lower().replace(" ", "_")
    return db.get_db()[f"tenant_{sanitized_name}"]