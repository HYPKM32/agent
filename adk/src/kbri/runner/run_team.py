import asyncio
from dotenv import load_dotenv; load_dotenv()

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from test.agents.coordinator_agent import coordinator_agent

async def main():
    session = InMemorySessionService()
    await session.create_session("test_adk_app", "user1", "sess1")

    runner = Runner(
        agent=coordinator_agent,
        app_name="test_adk_app",
        session_service=session
    )

    while True:
        user = input("User: ")
        content = types.Content(role="user", parts=[types.Part(text=user)])

        async for event in runner.run_async("user1", "sess1", content):
            if event.is_final_response():
                print("Assistant:", event.content.parts[0].text)
                break

asyncio.run(main())
