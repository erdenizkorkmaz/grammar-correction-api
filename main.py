from fastapi import FastAPI
from transformers import pipeline
import asyncio

app = FastAPI()

nlp_model = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", max_length=46)

@app.get("/summarize")
async def summarize(text: str = ""):
    if text == "":
        return {"error": "No text provided for summarization."}

    summarise_text = "Summarise this using B2 level English: " + text
    try:
        print(summarise_text)
        response = await asyncio.get_event_loop().run_in_executor(None, nlp_model, summarise_text)
        print(response)
        return {"data": response}
    except Exception as e:
        return {"error": str(e)}