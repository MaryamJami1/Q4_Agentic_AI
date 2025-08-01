# This code is for practice purposes only. It did not run successfully because the Gemini model does not support hosted tools."
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, WebSearchTool
import os
from dotenv import load_dotenv
import asyncio
from agents.run import RunConfig 

# Load environment variable
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/", 
    api_key=gemini_key,
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", 
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True 
)

# 
async def main():
    query = input("Ask your question? ")

    agent = Agent(
        name="Assistant", 
        instructions="You are a helpful assistant that can search the web.",
        model=model,      
        tools=[WebSearchTool()]   
    )


    result = await Runner.run(agent, query, run_config=config)

    print(result.final_output)


asyncio.run(main())
