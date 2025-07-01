import sys
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

if len(sys.argv) != 2:
    print("Error: Include prompt")
    sys.exit(1)

content = sys.argv[1]

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=content
)
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
