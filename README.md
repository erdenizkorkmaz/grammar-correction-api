# **Grammar Correction API**

This project provides a RESTful API for correcting English grammar in text input. It's built with FastAPI and utilizes models from Hugging Face's Transformers library to ensure high accuracy in text correction.

## **Features**

- **Grammar Correction**: Uses a machine learning model to correct grammar in English sentences.
- **FastAPI Framework**: Offers high performance with asynchronous request handling.
- **Scalable**: Designed to handle multiple requests efficiently with batch processing.

## **Models**

- **Grammar Correction Model**: Utilizes **`vennify/t5-base-grammar-correction`** from Hugging Face for correcting English grammar.

## **Installation**

Ensure you have Python 3.6+ installed, then follow these steps to set up the project environment:

Clone the repository:

```bash
git clone https://github.com/yourusername/grammar-correction-api.git
cd grammar-correction-api

```

Install dependencies:

```
pip install fastapi uvicorn transformers

```

Start the API server:

```css
uvicorn main:app --reload

```

## **Usage**

The API provides two endpoints:

- **`/`**: A simple health check to confirm the API is running.
- **`/correct_grammar`**: Accepts a POST request with a JSON body containing the text for grammar correction.

### **Making a Request**

You can use **`curl`** to make a request to the API:

```bash
curl -X POST http://127.0.0.1:8000/correct_grammar -H "Content-Type: application/json" -d '{"text": "Your incorrect sentence here."}'

```

### **Example Response**

The response will include the corrected text:

```json
{
  "corrected_text": "Your corrected sentence here."
}

```

## **Development**

- **Pre-commit Hooks**: Ensure code formatting and lint checks are performed before commits.
- **Testing**: Includes basic tests for API endpoints to ensure reliability.

## **Contributors**

Thanks to the following people who have contributed to this project:

@erdenizkorkmaz

## **Contact**

If you want to contact me, you can reach me at erdeniz@dakik.co.uk.

## **License**

This project is licensed under the MIT License - see the LICENSE file for details.
