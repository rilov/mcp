from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

from langsmith import traceable
from langsmith.client import Client


import asyncio
import os
from langchain_openai import ChatOpenAI



os.environ["OPENAI_API_KEY"] = "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"
#os.environ["LANGCHAIN_TRACING_V2"] = "true"
#os.environ["LANGCHAIN_API_KEY"]="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"

model = ChatOpenAI(model="gpt-4o",base_url="http://127.0.0.1:5000")

server_params = StdioServerParameters(
    command="python",
    args=["mcpweatherserver.py"]
)

async def run_agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools=await load_mcp_tools(session)
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke(
                {"messages":"what's the weather forcast in Toronto?"},
            )
            return agent_response["messages"][3]
        
if __name__ == "__main__":
    result = asyncio.run(run_agent())
    print(result)
        