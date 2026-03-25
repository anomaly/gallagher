from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP

server = MCPServerStreamableHTTP('http://localhost:8000/mcp')  
agent = Agent('openai:gpt-5', toolsets=[server])  

async def main():
    result = await agent.run('List all divisions in my command centre.')
    print(result.output)


    result = await agent.run('List all users in my command centre.')
    print(result.output)
