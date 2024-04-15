import logging
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
logging.basicConfig(level=logging.INFO)

corrector = pipeline('text2text-generation','pszemraj/flan-t5-large-grammar-synthesis',)

class Prompt(BaseModel):
    text: str

@app.get("/")
async def health_check():
    return {"status": "healthy"}

@app.post("/correct_grammar")
async def correct_grammar(prompt: Prompt):
    text = prompt.text
    logging.info(f"Received text for grammar correction: {text}")
    if not text:
        logging.error("No text provided for grammar correction")
        return {"error": "No text provided for grammar correction"}, 400

    try:
        # Correct grammar
        corrected_text = corrector(text)

        logging.info("Grammar correction successful")
        return {"original_text": text, "corrected_text": corrected_text[0]['generated_text']}
    except Exception as e:
        logging.exception("Error during grammar correction")
        return {"error": str(e)}, 500
