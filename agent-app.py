import os

from agents import Agent, Runner
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
from bedrock_agentcore import BedrockAgentCoreApp
from openai import AsyncAzureOpenAI

app = BedrockAgentCoreApp()
openai_key = os.environ["AZURE_OPENAI_API_KEY"]
endpoint = os.environ["AZURE_ENDPOINT"]

client = AsyncAzureOpenAI(
    api_version="2025-01-01-preview",
    api_key=openai_key,
    azure_endpoint=endpoint
)
agent = Agent(
    name="SampleAgent",
    model=OpenAIChatCompletionsModel(model="gpt-5-nano", openai_client=client)
)

@app.entrypoint
async def invoke(payload):
    user_message = payload.get("prompt", "Hello!")
    result = await Runner.run(agent, user_message)
    return result

if __name__ == "__main__":
    app.run()