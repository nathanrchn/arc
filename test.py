from json import loads
from aiohttp import ClientSession
from asyncio import run, ensure_future, gather

COLORS = [
    "\033[31m",
    "\033[32m",
    "\033[33m",
    "\033[34m",
    "\033[35m",
    "\033[36m",
    "\033[37m",
    "\033[91m",
    "\033[92m",
    "\033[93m",
    "\033[94m",
    "\033[95m",
    "\033[96m",
    "\033[97m",
]

async def fetch(session: ClientSession, i: int) -> str:
    headers = {
        "Authorization": "Bearer API_KEY",
    }
    body = {
        "model": "gpt-4-turbo-preview", # gpt-4-turbo-preview
        "feature": "please",
        "stream": True,
        "max_tokens": 4096,
        "response_format": {
            "type": "text"
        },
        "temperature": 0,
        "stop": [],
        "version": 1,
        "isDev": False,
        "tools": None,
        "messages": [
            {
                "content": "You are an expert research assistant.",
                "role": "system"
            },
            {
                "content": "Who are you in 10 words or less?",
                "role": "user"
            }
        ]
    }
    async with session.post("https://open-ai-chat-omega.vercel.app/api/open-ai-chat-stream", headers=headers, json=body) as response:
        c = ""
        async for data in response.content:
            if data != b'\n':
                data_str = data[6:-1].decode("utf-8")
                print(f"{COLORS[i % len(COLORS)]}{data_str}\033[0m", flush=True)
                try:
                    data_json = loads(data_str)
                    c += data_json["choices"][0]["delta"]["content"]
                except:
                    pass  

        return len(c)

async def main():
    async with ClientSession() as session:
        tasks = [ensure_future(fetch(session, i)) for i in range(20)]
        lengths = await gather(*tasks)
        print(lengths)

if __name__ == "__main__":
    run(main())