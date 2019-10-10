import time
import httpx
import asyncio
import enum


URL = "https://api.telegram.org/bot"


"""Queue holds requests in format (verb: HttpVerbs, (call: String, params: Dict))"""
queue = []


class HttpVerbs(enum.Enum):
    GET = 1
    POST = 2
    PUT = 3
    PATCH = 4
    DELETE = 5
    HEAD = 6
    CONNECT = 7
    OPTIONS = 8
    TRACE = 9


def add_call_to_queue(verb, function):
    queue.append((verb, function))


async def worker():
    start = time.time()

    async with httpx.AsyncClient() as client:
        while True:
            if not queue:
                stop = time.time()
                print(stop-start)
                break
            await make_request(queue.pop(), client)


async def make_request(request, client):
    if request[0] == HttpVerbs.GET:
        return await client.get(URL + request[1][0], params=request[1][1])
    if request[0] == HttpVerbs.POST:
        return await client.post(URL + request[1][0], params=request[1][1])


def main():
    global URL
    URL += str(open('credentials')) + "/"

    for i in range(50):
        add_call_to_queue(HttpVerbs.GET, "getUpdates")
    asyncio.run(worker())


if __name__ == "__main__":
    main()
