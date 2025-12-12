Welcome to your Wedding Backend Project

This repository contains the backend for a multi-tenant wedding management platform built using FastAPI, MongoDB, and JWT authentication.
Each wedding company receives its own isolated data store while shared metadata is kept in a master collection.

Project Info

Backend Tech Stack:

FastAPI

Python 3.10+

MongoDB (Motor)

Pydantic

JWT Auth (python-jose)

Passlib (bcrypt)

How can I edit this code?

There are several ways to work with and modify this application.

✅ Use Your Preferred IDE

If you want to develop locally using VS Code, PyCharm, or any editor of your choice, follow these steps:

1. Clone the repository
git clone <YOUR_GIT_URL>

2. Navigate into the project directory
cd <YOUR_PROJECT_NAME>

3. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

4. Install dependencies
pip install -r requirements.txt

5. Start the development server
uvicorn main:app --reload


Your backend will be available at:

http://localhost:8000


Interactive API docs:

http://localhost:8000/docs

📝 Edit files directly on GitHub

You can also make quick changes in GitHub:

Browse to the file you want to modify

Click the Edit (pencil icon)

Commit your changes to the repo

These changes will be reflected wherever the project is deployed.

🧪 Use GitHub Codespaces

No setup required — everything runs in the cloud.

Go to your repository

Click Code → Codespaces

Click New codespace

Edit the project directly in your browser

Commit and push changes when done

Project Technologies

This backend is built using:

FastAPI – lightning-fast web framework

Motor – async MongoDB client

Pydantic – type-safe data validation

Passlib – secure password hashing

python-jose – JWT signing & verification

Uvicorn – ASGI server

How to Deploy the Backend

Since this is a Python API, you can deploy it to:

Popular deployment platforms:

Render

Railway

AWS EC2

Azure App Service

Google Cloud Run

Vercel (via serverless functions)

Docker + any container hosting provider

If you want, I can generate:

A Dockerfile

Deployment instructions for Render/Railway/AWS

CI/CD workflow (GitHub Actions)

Just tell me!

Environment Variables

Create a .env file in the project root:

MONGO_URL=<your mongodb uri>
DB_NAME=wedding_master_db
SECRET_KEY=<your jwt secret>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
