📌 AI Task Manager API

A simple AI-powered Task Management API built with FastAPI, PostgreSQL, and JWT Authentication.
This project is designed for learning backend development, REST APIs, and authentication systems.

🚀 Features
👤 User registration & login
🔐 JWT authentication
📋 Create, read, update, delete (CRUD) tasks
🔒 User-specific task isolation
🧠 Secure password hashing
📖 Auto-generated Swagger API documentation
🐘 PostgreSQL database integration
🛠️ Tech Stack
Python 3.10+
FastAPI
PostgreSQL
SQLAlchemy
Pydantic
JWT (python-jose)
Uvicorn

📁 Project Structure
app/
├── main.py
├── database.py
├── models/
│   ├── user.py
│   └── task.py
├── schemas/
│   ├── user.py
│   └── task.py
├── crud.py
├── dependencies/
│   └── auth.py
├── routers/
│   ├── auth.py
│   └── task_router.py
⚙️ Installation
1. Clone the repository
git clone https://github.com/yourusername/ai-task-manager.git
cd ai-task-manager
2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Install dependencies
pip install -r requirements.txt
4. Setup environment variables

Create a .env file:

DATABASE_URL=postgresql://postgres:password@localhost:5432/taskdb
SECRET_KEY=your_secret_key
ALGORITHM=HS256
5. Run the application
uvicorn app.main:app --reload
📖 API Documentation

After running the project, open:

http://127.0.0.1:8000/docs

You can test all endpoints using Swagger UI.

🔐 Authentication Flow
Register a user
Login to get JWT token
Click Authorize in Swagger
Use token to access protected endpoints

📋 API Endpoints
Auth
POST /auth/register → Register user
POST /auth/login → Login and get token
Tasks
POST /tasks → Create task
GET /tasks → Get all user tasks
GET /tasks/{id} → Get single task
PUT /tasks/{id} → Update task
DELETE /tasks/{id} → Delete task

🧠 Learning Goals

This project helps you learn:

FastAPI backend development
REST API design
JWT authentication
PostgreSQL with SQLAlchemy
Clean project architecture
📌 Future Improvements
🤖 AI task suggestion system
🐳 Docker containerization
🧪 Unit testing with PyTest
☁️ Cloud deployment (AWS / Render)
📊 Analytics dashboard
👨‍💻 Author

Built for learning backend development with FastAPI.