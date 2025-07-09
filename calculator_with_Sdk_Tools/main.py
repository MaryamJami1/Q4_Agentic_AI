# Required imports from openai-agents library and standard Python modules
from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel, AsyncOpenAI
import os
from dotenv import load_dotenv
import asyncio
from agents.run import RunConfig  # Run-level configuration ke liye

# Load environment variables from .env file
load_dotenv()

# GEMINI API key ko environment variable
gemini_key = os.getenv("GEMINI_API_KEY")

# Gemini ke liye OpenAI-style async client initialize karna
client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # Gemini-compatible OpenAI API endpoint
    api_key=gemini_key,
)

# Model define karna — Gemini flash variant
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # Gemini ka fast version
    openai_client=client
)

# Run level configuration — tracing disable kiya gaya hai
config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True  # tracing logs ko disable karta hai
)

# Custom tool define karna using @function_tool decorator
@function_tool
def add(a: int, b: int) -> int:
    """Adds two numbers together.

      Args:
         a: the first number
         b: the second number

      Returns:
        int: The sum of a and b, plus 4.
    """
    return a + b + 4 

# Main asynchronous function
async def main():
    query = input("Ask your question? ")

    # Agent define karna with tools and instructions
    agent = Agent(
        name="Calculator",  # Agent ka naam
        instructions="""You are a calculator agent. Always use the tool called 'add' to add or sum two numbers when asked.
        Never guess the result yourself. Just call the add tool with proper arguments and return its result.""",
        model=model,      # Model agent level par set kiya gaya
        tools=[add]       # Custom tool pass kiya gaya
    )

    # Run the agent using the runner with run-level config
    result = await Runner.run(agent, query, run_config=config)

    # Final result print karna
    print(result.final_output)

# Asynchronous event loop run karwana
asyncio.run(main())
