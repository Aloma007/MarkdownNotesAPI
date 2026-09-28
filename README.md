# Markdown Note-taking API

A RESTful backend service for creating, managing, and processing markdown notes. This API handles raw text, converts markdown to HTML, and integrates a third-party grammar checking engine.

This project is a solution to the [Markdown Note-taking App challenge on roadmap.sh](https://roadmap.sh/projects/markdown-note-taking-app).

## Features

- **CRUD Operations**: Create and retrieve markdown notes.
- **HTML Rendering**: Dedicated endpoint to parse raw markdown into valid HTML.
- **Grammar Checking**: Integration with the LanguageTool API to analyze note content for grammatical and spelling errors.
- **Data Persistence**: Local SQLite database integration using SQLAlchemy ORM.
- **Automatic Documentation**: Interactive API documentation provided by FastAPI (Swagger UI).

## Tech Stack

- **Framework**: Python / FastAPI
- **Database**: SQLite / SQLAlchemy
- **Validation**: Pydantic
- **Markdown Parsing**: `markdown` standard library
- **External API**: LanguageTool (via `requests`)

## Local Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/markdown-notes-api.git
   cd markdown-notes-api
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic markdown requests
   ```

4. **Run the development server**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to interact with the endpoints.

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/notes/` | Create a new markdown note. |
| `GET` | `/notes/` | Retrieve a list of all saved notes (supports pagination). |
| `GET` | `/notes/{id}/html` | Return the rendered HTML version of a specific markdown note. |
| `GET` | `/notes/{id}/grammar` | Analyze the note's text and return grammar correction suggestions. |

