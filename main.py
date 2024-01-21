from fastapi import FastAPI
from fastapi import Depends

from typing_extensions import Annotated

from swibots import BotApp

from type import MeResponse
from type import UserInput
from type import UserResponse
from type import SendMessageInput

import asyncio
from uvicorn import Config
from uvicorn import Server

# Load env
from os import environ
from dotenv import load_dotenv
load_dotenv()

# Initialize custom loop
# For both Uvicorn and Swibots
loop = asyncio.new_event_loop()

# Initialize FastAPI & Swibots
app = FastAPI()
swibots = BotApp(environ.get("BOT_TOKEN"),
                loop=loop)

@app.get("/")
async def about_me() -> MeResponse:
    about = await swibots.get_me()
    return about.to_json()

@app.get("/get_user")
async def get_user(user: Annotated[UserInput, Depends()]) -> UserResponse:
    about = await swibots.get_user(**user.model_dump())
    return about.to_json()

@app.get("/manoedinata")
async def about_manoedinata() -> UserResponse:
    about = await get_user(user=UserInput(username="manoedinata"))
    return about

@app.post("/send_message")
async def send_message(message: SendMessageInput):
    send = await swibots.send_message(**message.model_dump())
    return send.to_json()

if __name__ == "__main__":
    # Uvicorn
    config = Config(app=app, loop=loop)
    server = Server(config)
    loop.run_until_complete(server.serve())
