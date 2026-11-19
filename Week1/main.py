from dotenv import load_dotenv
from google import genai
import os

# Load API key
load_dotenv()

# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# First LLM Call
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is Artificial Intelligence? Explain in simple words."
)

print("\nLLM Response:")
print(response.text)