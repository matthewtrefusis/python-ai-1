import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

model = "gemma-3-27b-it"
contents = args.user_prompt

api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("Invalid API KEY")

client = genai.Client(api_key=api_key)

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

response = client.models.generate_content(
        model=model, 
        contents=messages)

if response.usage_metadata == None:
    raise RuntimeError("Failed API Request")

prompt_tokens = response.usage_metadata.prompt_token_count
candidate_tokens = response.usage_metadata.prompt_token_count

if args.verbose == True:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {candidate_tokens}")

print("Response:")
print(response.text)
