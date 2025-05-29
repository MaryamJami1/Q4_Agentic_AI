from agents import Agent, Runner, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
open_router_key = os.getenv("OPENROUTER_API_KEY")

client = AsyncOpenAI(
    api_key=open_router_key,
    base_url="https://openrouter.ai/api/v1"
)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=OpenAIChatCompletionsModel(model="google/gemini-2.0-flash-exp:free", openai_client=client)
)
query = input("How is assist you today? ")

result = Runner.run_sync(agent, query)      
print(result.final_output)
