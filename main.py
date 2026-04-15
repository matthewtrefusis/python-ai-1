import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions, call_function

load_dotenv()

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

# model = "gemma-3-27b-it"
model = "gemini-2.5-flash"
contents = args.user_prompt

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("Invalid API KEY")

client = genai.Client(api_key=api_key)

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

response = client.models.generate_content(
        model=model, 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
            temperature=0
            )
        )
if response.usage_metadata == None:
    raise RuntimeError("Failed API Request")

if response.function_calls:
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
        function_call_result = call_function(function_call)
        if not function_call_result.parts:
            raise RuntimeError("Function call result has no parts")

        function_response = function_call_result.parts[0].function_response
        if function_response is None:
            raise RuntimeError("Function response is None")

        if function_response.response is None:
            raise RuntimeError("Function response.response is None")

        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

prompt_tokens = response.usage_metadata.prompt_token_count
candidate_tokens = response.usage_metadata.prompt_token_count

if args.verbose == True:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {candidate_tokens}")

print("Response:")
print(response.text)
