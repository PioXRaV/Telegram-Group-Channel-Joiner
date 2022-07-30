import asyncio
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest

api_id = 
api_hash = ""

groups = ["1", "2", "3", "more"]

async def main():

    async with TelegramClient("Account", api_id, api_hash) as client:

        for group in groups:

            try:

                await client(JoinChannelRequest(group))

            except FloodWaitError as error:

                print(error)
                await asyncio.sleep(delay=error.seconds)

            except Exception as error:

                print(error)

asyncio.run(main())