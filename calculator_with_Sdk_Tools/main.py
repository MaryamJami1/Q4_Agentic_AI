from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel, AsyncOpenAI
import os
from dotenv import load_dotenv


load_dotenv()

gemini_key= os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=gemini_key
)

@function_tool
def add(a:int, b:int)->int:
    """add two numbers
       args:
       a is the first number
       b is the second numebr
    """
    
    return a + b + 4
        

agent = Agent(
    name= "Calculator",
    instructions= """You are a calculator agent. Always use the tool called 'add' to add two numbers when asked.
    Never guess the result yourself. Just call the add tool with proper arguments and return its result.""",
    model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    tools=[add]
)

query = input("How can i help you?")
result = Runner.run_sync(agent, query)



print(result.final_output)
