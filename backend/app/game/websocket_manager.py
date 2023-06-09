from fastapi import WebSocket
from typing import List

class Connection:
    def __init__(self, websocket: WebSocket):
        self.websocket = websocket
        self.in_game: bool = False

class ConnectionManager:
    def __init__(self):
        self.connections: List[Connection] = []
        self.queue: List[Connection] = []

    async def connect(self, websocket: WebSocket):
        connection = Connection(websocket)
        await websocket.accept()
        self.connections.append(connection)
        self.queue.append(connection)
        await self.match_players()

    async def disconnect(self, connection: Connection):
        self.connections.remove(connection)
        if connection in self.queue:
            self.queue.remove(connection)
        elif connection.in_game:
            # TODO: End the game and declare the other player the winner
            pass

    async def send_personal_message(self, message: str, connection: Connection):
        await connection.websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.connections:
            await connection.websocket.send_text(message)

    async def match_players(self):
        while len(self.queue) >= 2:
            player1 = self.queue.pop(0)
            player2 = self.queue.pop(0)
            # TODO: Create a new game with player1 and player2
            player1.in_game = True
            player2.in_game = True
            await self.send_personal_message("You have been matched with another player. Game starting soon!", player1)
            await self.send_personal_message("You have been matched with another player. Game starting soon!", player2)
