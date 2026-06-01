# Receipt Vault API

Receipt Vault API is a FastAPI backend project that allows users to store receipt information and use AI to extract useful details from receipt images.

The goal of the project is to help users keep track of receipts, return windows, warranty information, purchase dates, and total amounts in one place.

> Note: This project is currently in development. The database and base backend structure are set up, and the next major step is completing JWT authentication and protected receipt routes.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- OpenAI API
- Swagger UI
- Git
- VS Code

## Features

### Current Features

- FastAPI server setup
- Swagger UI documentation
- PostgreSQL database connection
- SQLAlchemy database models
- Users table
- Receipts table
- Receipt ownership through foreign keys
- Layered backend structure with routes, schemas, models, services, and business logic files

### Planned Features

- User registration
- User login
- JWT authentication
- Protected receipt routes
- Upload receipt images
- AI-powered receipt scanning with OpenAI
- Extract receipt details:
  - Store name
  - Total amount
  - Purchase date
  - Return window
  - Warranty information
- Get all receipts for a logged-in user
- Get a single receipt by ID
- Delete receipts
- Add pytest tests
- Docker support
- Cloud deployment

## Project Structure

```text
receipt-vault-api/
├── main.py
├── database.py
├── auth.py
├── models/
│   ├── user_model.py
│   └── receipt_model.py
├── schemas/
│   ├── user_schema.py
│   └── receipt_schema.py
├── routes/
│   ├── users.py
│   └── receipts.py
├── viewmodels/
│   ├── auth_viewmodel.py
│   └── receipt_viewmodel.py
├── services/
│   └── openai_service.py
├── requirements.txt
├── .env.example
└── README.md
```

## Architecture Explanation

This project uses a layered backend structure.

- `models/` defines the database tables using SQLAlchemy.
- `schemas/` defines API request and response shapes using Pydantic.
- `routes/` defines the API endpoints.
- `viewmodels/` contains business logic for authentication and receipt actions.
- `services/` handles external tools and APIs, such as OpenAI.
- `database.py` connects the FastAPI app to PostgreSQL.
- `main.py` starts the FastAPI application and includes the API routes.

## Database Tables

### Users Table

The `users` table stores user account information.

```text
users
- id
- email
- hashed_password
- created_at
```

### Receipts Table

The `receipts` table stores receipt information connected to a user.

```text
receipts
- id
- user_id
- store_name
- amount
- date
- return_window
- warranty_until
- warranty_info
- image_url
- created_at
```

## Environment Variables

Create a `.env` file in the root folder:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/receiptvault
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-api-key
```

The `.env` file should not be uploaded to GitHub. Use `.env.example` to show the required variables without exposing real secrets.

## Run the Project Locally

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run the FastAPI server

```powershell
uvicorn main:app --reload
```

### 4. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

## Project Status

This project is currently in development. The database connection, SQLAlchemy models, and base backend structure are set up. The next major step is implementing JWT authentication and protected receipt routes.

## What I Learned

Through this project, I am learning how to structure a backend API using FastAPI, PostgreSQL, SQLAlchemy, Pydantic schemas, and route-based API design.

I am also learning how authentication, database relationships, request validation, and external AI API integration work together in a real backend system.

## Future Improvements

- Complete JWT authentication
- Add protected receipt routes
- Add image upload support
- Connect OpenAI Vision for receipt extraction
- Add pytest tests
- Add Docker support
- Deploy the API to the cloud
