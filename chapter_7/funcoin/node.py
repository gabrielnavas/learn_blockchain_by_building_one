import asyncio

from funcoin.blockchain import Blockchain
from funcoin.connections import ConnectionPool
from funcoin.peers import P2PProtocol
from funcoin.server import Server

blockchain = Blockchain()
connection_pool = ConnectionPool()

# Instantiate the server with some config
server = Server(blockchain, connection_pool, P2PProtocol)


async def main():
    # Start the server
    await server.listen()

# Start the server
asyncio.run(main())