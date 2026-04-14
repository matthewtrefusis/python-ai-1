import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

model = "gemma-3-27b-it"
contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("Invalid API KEY")

client = genai.Client(api_key=api_key)

print(f"User prompt: {contents}")

response = client.models.generate_content(
        model=model, 
        contents=contents)

if response.usage_metadata == None:
    raise RuntimeError("Failed API Request")

prompt_tokens = response.usage_metadata.prompt_token_count
candidate_tokens = response.usage_metadata.prompt_token_count

print(f"Prompt tokens: {prompt_tokens}")
print(f"Response tokens: {candidate_tokens}")

print("Response:")
print(response.text)
