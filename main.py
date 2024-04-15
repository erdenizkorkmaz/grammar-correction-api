import re
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# App Initialization
app = FastAPI()

# Model Configuration and Initialization - Cached globally
checker_model_name = "textattack/roberta-base-CoLA"
corrector_model_name = "vennify/t5-base-grammar-correction"

def initialize_models():
    # We only need the corrector model as we are skipping the checks
    corrector = pipeline("text2text-generation", model=corrector_model_name, max_length=240)
    return corrector

corrector = initialize_models()

# Utility Functions
def split_text(text: str) -> list:
    # Optimized regex: Making sure it's efficient and suited for purpose
    sentences = re.split(r"\.\s+(?=[A-Z])", text)
    sentence_batches = []
    temp_batch = []
    
    for sentence in sentences:
        temp_batch.append(sentence)
        if len(temp_batch) >= 2 and len(temp_batch) <= 3 or sentence == sentences[-1]:
            sentence_batches.append(temp_batch)
            temp_batch = []
    
    return sentence_batches

# Data Model
class Prompt(BaseModel):
    text: str

# API Endpoints
@app.get("/")
async def health_check():
    return {"status": "healthy"}

@app.post("/correct_grammar")
async def correct_grammar(prompt: Prompt):
    sentence_batches = split_text(prompt.text)
    if not sentence_batches:
        return {"error": "No text provided for grammar correction"}, 400

    try:
        corrected_text = []
        for batch in sentence_batches:
            raw_text = " ".join(batch)
            corrected_batch = corrector(raw_text)
            corrected_text.append(corrected_batch[0]["generated_text"])
        corrected_text = " ".join(corrected_text)
        return corrected_text
    except Exception as e:
        return {"error": str(e)}, 500