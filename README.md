📄 Documentation Generator Agent

The Documentation Generator Agent is an AI-powered backend application that automatically generates technical documentation from user prompts.
It is built using FastAPI and integrates the ScaleDown API to leverage Large Language Models (LLMs) for intelligent content generation.

This project is designed as a 1D Python backend project and follows a clean, modular architecture.

🚀 Features

AI-powered documentation generation

FastAPI-based backend

ScaleDown LLM API integration

Secure API key handling using environment variables

Swagger UI for easy API testing

Postman collection for API testing

Modular and scalable project structure

🛠 Tech Stack

Language: Python 3.9+

Backend Framework: FastAPI

Server: Uvicorn

AI API: ScaleDown API

Data Validation: Pydantic

Testing Tool: Postman

📂 Project Structure
Documentation-Generator-Agent/
│
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI app entry point
│   │   ├── config.py               # Environment variable configuration
│   │   │
│   │   ├── routes/
│   │   │   └── generate.py         # API route for documentation generation
│   │   │
│   │   ├── services/
│   │   │   └── scaledown_client.py # ScaleDown API integration logic
│   │   │
│   │   ├── schemas/
│   │   │   └── generate_schema.py  # Request/response models
│   │   │
│   │   └── __init__.py
│   │
│   ├── requirements.txt            # Python dependencies
│   └── __init__.py
│
├── frontend/
│   ├── index.html                  # Simple user interface
│   ├── style.css                   # Basic styling
│   └── script.js                   # Backend API calls
│
├── postman/
│   └── documentation-generator.postman_collection.json
│
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignored files
└── README.md                       # Project documentation

🔑 Environment Configuration

Create a .env file inside the backend folder and add your ScaleDown API key:

SCALEDOWN_API_KEY=your_scaledown_api_key_here


⚠️ The .env file is ignored in GitHub to keep API keys secure.

▶️ How to Run the Project Locally
Step 1: Navigate to backend folder
cd backend

Step 2: Create virtual environment
python -m venv venv

Step 3: Activate virtual environment

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

Step 4: Install dependencies
pip install -r requirements.txt

Step 5: Start the server
uvicorn app.main:app --reload

🌐 Access the Application

API Root:

http://127.0.0.1:8080

Swagger Documentation:

http://127.0.0.1:8080/docs

📬 API Usage
Endpoint
POST /generate/

Request Body (JSON)
{
  "prompt": "Generate documentation for a user authentication API"
}

Sample Response
{
  "documentation": "Generated documentation content..."
}

🧪 Testing the API

Use Swagger UI (/docs)

Or import the Postman collection from the postman/ folder

🔐 Security

API keys are stored using environment variables

.env file is excluded from version control

No sensitive data is exposed in the repository

📌 Future Enhancements

Frontend UI (React / HTML)

Export documentation as PDF or Markdown

User authentication

Support for multiple LLM providers

Deployment to cloud platforms

👩‍💻 Author
Anjali Gupta
B.Tech – Computer Science & Engineering (Data Science)



