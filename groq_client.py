# groq_client.py
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=GROQ_API_KEY)

def get_completion(messages, model="llama-3.3-70b-versatile", temperature=1, max_completion_tokens=1024, top_p=1, stop=None):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_completion_tokens=max_completion_tokens,
        top_p=top_p,
        stream=False,
        stop=stop,
    )
    return response.choices[0].message.content

def stream_completion(messages, model="llama-3.3-70b-versatile", temperature=1, max_completion_tokens=1024, top_p=1, stop=None):
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_completion_tokens=max_completion_tokens,
        top_p=top_p,
        stream=True,
        stop=stop,
    )
    for chunk in stream:
        yield chunk.choices[0].delta.content or ""
