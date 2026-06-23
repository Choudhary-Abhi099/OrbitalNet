import asyncio
import websockets


async def test_socket():

    uri = (
        "ws://127.0.0.1:8000/ws/simulation"
    )

    async with websockets.connect(
        uri
    ) as websocket:

        print(
            "Connected to OrbitalNet!"
        )

        await websocket.send(
            "hello"
        )

        while True:

            message = (
                await websocket.recv()
            )

            print(
                message
            )


asyncio.run(
    test_socket()
)