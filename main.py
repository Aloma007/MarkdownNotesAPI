from fastapi import FastAPI

# Initialize the application
app = FastAPI(title="Markdown Notes API")

# Create a basic endpoint to test if it works
@app.get("/")
def read_root():
    return {"message": "Welcome to the Markdown Notes API 🚀"}