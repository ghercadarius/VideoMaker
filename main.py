import os
import asyncio
from sydney import SydneyClient


async def get_result(prompt):
    print("entered get_result")
    sydney = SydneyClient()
    await sydney.start_conversation()
    print("started conversation")
    response = await sydney.ask(prompt)
    print(response)
    await sydney.close_conversation()
    print("closed conversation")
    return response

if __name__ == "__main__":
    print(asyncio.run(get_result("can you tell me about the first world war?")))
