"""Async fetcher"""
import sys
import time
import asyncio
import aiohttp
import requests


def parse_flags() -> tuple:
    """Parsing flags from cmd"""
    if len(sys.argv) < 3:
        print("Not enough arguments")
        sys.exit(1)
    elif sys.argv[1] == "-c":
        try:
            return int(sys.argv[2]), str(sys.argv[3])
        except ValueError:
            print("Wrong arguments")
            sys.exit(1)
    else:
        try:
            return int(sys.argv[1]), str(sys.argv[2])
        except ValueError:
            print("Wrong arguments")
            sys.exit(1)


async def handle_url(url: str, session: aiohttp.ClientSession):
    """Function to handle each url"""
    async with session.get(url, ssl=False) as response:
        if response.status == 200:
            print("Success")
            print(url)
        else:
            print("Error")
            print(url)


async def main():
    """Main function"""
    url_count, file = parse_flags()

    async with aiohttp.ClientSession() as session:
        start = time.time()
        with open(file, "r", encoding="UTF-8") as f:
            urls = [f.readline().strip() for _ in range(url_count)]
        tasks = [handle_url(url, session) for url in urls]
        await asyncio.gather(*tasks)
        end = time.time()
        print(f"Time: {end - start}")

if __name__ == "__main__":
    asyncio.run(main())
