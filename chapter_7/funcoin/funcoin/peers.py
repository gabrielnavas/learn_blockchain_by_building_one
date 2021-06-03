import asyncio

import structlog
from funcoin.messages import (
    create_peers_message,
    create_block_message,
    create_transaction_message,
    create_ping_message,
)
from funcoin.transactions import validate_transaction

logger = structlog.getLogger(__name__)

class P2PError(Exception):
    pass

class P2PProtocol:
    def __init__(self, server):
        self.server = server
        self.blockchain = server.blockchain
        self.connection_pool = server.connection_pool

    @staticmethod
    async def send_message(writer, message):
        writer.write(message.encode() + b"\n")

    async def handle_message(self, message, writer):
        # Handles an incoming message passed by the server
        # Handles this message of to a more specific method:
        # handle_<method_name>()
        """
        That is, all messages sent in our p2p network share this structure. The
        meta key contains information about the peer sending the message (even
        if that peer is us), while the message key contains the name and payload of
        the message being sent.

        struct basic from message
        {
            "name": <message name: str>,
            "payload": <message payload: object>
            "meta": {
                "address": {
                "ip": <external ip: str>,
                "port": <external port: int>
                },
                "client": "funcoin 0.1"
            },
        }
        """
        pass

    async def handle_ping(self, message, writer):
        # Handles in incoming "ping" message
        pass

    async def handle_block(self, message, writer):
        # Handles in incoming "block" message
        pass

    async def handle_transaction(self, message, writer):
        # Handles in incoming "transaction" message
        pass

    async def handle_peers(self, message, writer):
        # Handles in incoming "peers" message
        pass
    