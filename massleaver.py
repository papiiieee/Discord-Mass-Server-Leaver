import aiohttp
import asyncio
import tracemalloc
import requests
tracemalloc.start()
token = "MTE3ODc1MzkwNTc1NzI3ODI0OA.Gx4oV9.Ni2eSw87UEmju649x4BckyUm-qA8B3t1cp27PA"
async def mass_leave():
    headers = {'Authorization': token}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://discordapp.com/api/v6/users/@me/guilds', headers=headers) as resp:
            guilds = await resp.json()
            for guild in guilds:
                try:
                    
                    await session.delete(f'https://discordapp.com/api/v6/users/@me/guilds/{guild["id"]}', headers=headers)
                    print(f'Left {guild["name"]}')
                    await session.delete(f'https://discordapp.com/api/v6/users/@me/guilds/{guild["id"]}', headers=headers)
                    requests.delete(f'https://discordapp.com/api/v6/users/@me/guilds/{guild["id"]}', headers=headers)
                except:
                    print(f'Failed to leave {guild["name"]}')
loop = asyncio.get_event_loop()
loop.run_until_complete(mass_leave())
