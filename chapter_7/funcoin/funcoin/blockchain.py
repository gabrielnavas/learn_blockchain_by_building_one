import json

from datetime import datetime
from hashlib import sha256
import random

from time import time

import structlog
import math
import asyncio

logger = structlog.getLogger("blockchain")

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.target = "0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

        # Create the genesus block
        logger.info("Creating genesis block")
        self.chain.append(self.new_block())

    def new_block(self):
        block = self.create_block(
            height=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.last_block["hash"] if self.last_block else None,
            nonce=format(random.getrandbits(64), "x"),
            target=self.target,
            timestamp=time() 
        )

        return block
    
    def reset_pending_transactions(self):
        self.pending_transactions = []

    @staticmethod
    def create_block(
        height, transactions, previous_hash, nonce, target, timestamp=None
    ): 
        block={
            "height": height,
            "transactions": transactions,
            "previous_hash": previous_hash,
            "nonce": nonce,
            "target": target,
            "timestamp": timestamp or time()
        }

        block_string = json.dumps(block, sort_keys=True).encode()
        block_bytes = block_string.encode()
        block_sha256_hex = sha256(block_bytes).hexdigest()

        block["hash"] = block_sha256_hex
        return block

    @property
    def last_block(self):
        # Returns the last block in the chain (if there are blocks)
        return self.chain[-1] if self.chain else None

    def valid_block(self, block):
        #"1000ff" < "0000ff" -> False
        #to be Block Valid need be 0000e, and not 0000f 
        return block['hash'] < self.target
    
    def add_block(self, block):
        # TODO: add proper validation logic here
        self.chain.append(block)

    def recalculate_target(self, block_index):
        """
            Returns the number we need to get below to mine a block
        """
        # check if we need to recalculete the target
        if block_index % 10 == 0:
            exppected_timespan = 10 * 10

            #calculate the actual timespan
            last_block = self.chain[-1]
            ten_n_block = self.chain[-10]
            actual_timespan = last_block["timestamp"] - ten_n_block["timestamp"]

            # Figure out what the offset is
            ratio = actual_timespan / exppected_timespan

            # Now let's adjust the ratio to not be too
            min_value, max_value = 0.25, 4.00
            ratio = max(min_value, ratio)
            ratio = min(max_value, ratio)

            # Calculate the new target by multiplying the current one by the ratio
            target_int = int(self.target, 16)
            new_target = target_int * ratio

            new_target_floor = math.floor(new_target)
            width_zeros = 64
            self.target = "{}".format(new_target_floor).zfill(width_zeros)
        return self.target

    async def get_blocks_after_timestamp(self, timestamp):
        for index, block in enumerate(self.chain):
            if timestamp < block["timestamp"]:
                return self.chain[index:] 
        return None
    
    async def mine_new_block(self):
        index_block_try_recalculate = self.last_block["index"] + 1
        self.recalculate_target(index_block_try_recalculate)

        while True:
            new_block = self.new_block()
            if self.valid_block(new_block):
                break
            await asyncio.sleep(0)
        self.chain.append(new_block)
        self.reset_peding_transactions()
        logger.info("Found a new block:", new_block)            
    