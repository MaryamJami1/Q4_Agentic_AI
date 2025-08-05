# step 1: required imports
import os
from dotenv import load_dotenv
from litellm import completion, exceptions

load_dotenv()

# set environment for LiteLLM
os.environ["LITELLM_API_BASE"] = "https://openrouter.ai/api/v1"
key = os.environ["LITELLM_API_KEY"] = os.getenv("OPENROUTER_API_KEY")


# step 2: user input
query = input("You: ")

# step 3
try:
    print("\n🤖 AI is replying...")
    response = completion(
        model="openrouter/mistralai/mistral-7b-instruct",  # valid model name for OpenRouter
        messages=[{"role": "user", "content": query}]
    )
    print("Mistral:", response['choices'][0]['message']['content'])

# step 4: fallback
except exceptions.BadRequestError as e:
    print("\n❌ Mistral failed, switching to Meta.")
    response = completion(
        model="openrouter/meta-llama/llama-3-8b-instruct",  
        messages=[{"role": "user", "content": query}]
    )
    print("llama-3-8b:", response['choices'][0]['message']['content'])
