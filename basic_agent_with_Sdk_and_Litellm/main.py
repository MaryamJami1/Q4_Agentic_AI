# ✅ IMPORTS
import os
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.extensions.models.litellm_model import LitellmModel

# ✅ Load API key from .env
load_dotenv()
os.environ["LITELLM_API_KEY"] = os.getenv("OPENROUTER_API_KEY")


agent = Agent(
        name="SmartAgent",
        instructions="You help with general questions",
        model=LitellmModel(model="openrouter/google/gemini-2.0-flash-exp:free")  # 💡 using LiteLLM as model provider
    )

query = input("How can i help you?")

    # Agent runs with user's message
result = Runner.run_sync(agent, query)
print("\n🤖 Agent says:", result.final_output)


