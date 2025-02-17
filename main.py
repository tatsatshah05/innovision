from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai

# Set your OpenAI API key here (for production, use environment variables)
openai.api_key = "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"
app = FastAPI()

# Enable CORS so the frontend can access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to your frontend domain(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Pydantic model for the request body
class SpeechInput(BaseModel):
    text: str

# Basic GET endpoint to check if the server is running
@app.get("/")
def home():
    return {"message": "FastAPI Backend Running!"}

# POST endpoint to analyze and improve the speech text
@app.post("/analyze")
async def analyze_speech(speech: SpeechInput):
    user_text = speech.text
    try:
        # Call OpenAI's ChatCompletion API to improve the sentence politely
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Changed model from gpt-4 to gpt-3.5-turbo
            messages=[{"role": "user", "content": f"Improve this sentence politely: {user_text}"}]
        )
        improved_text = response["choices"][0]["message"]["content"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"original": user_text, "improved": improved_text}
