import json

from datetime import datetime
from hashlib import sha256
import random

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # Create the genesus block
        print("Creating genesis block")
        self.chain.append(self.new_block())

    def new_block(self):
        # Generates a new block and adds it to the chain
        last_block = self.last_block
        hash_last_block = last_block.get('hash') if last_block else None
        nonce = self.generate_nonce()

        # '2021-05-21T20:08:13.451986'
        timestamp_utc_str = datetime.utcnow().isoformat()
        block = {
            'index': len(self.chain),
            'timestamp': timestamp_utc_str, 
            'transactions': self.pending_transactions,
            'nonce': nonce,
            'previous_hash': hash_last_block,
        }

        # Get the hash of this new block, and add it to the block
        block_hash = self.hash(block)
        block['hash'] = block_hash

        # Reset the list of peding transactions
        self.pending_transactions = []
        return block
    
    @staticmethod
    def generate_nonce() -> str:
        
        # number of the 64 bits=17716072995464023089
        bits64_int = random.getrandbits(64) 
        
        # number to hex=17716072995464023089='f5dc22868d860c31'
        hex_format = 'x' 
        bits64_hex = format(bits64_int, hex_format) 
        return bits64_hex

    @staticmethod
    def hash(block) -> str:
        # Hashes a Block
        block_str = json.dumps(block, sort_keys=True)
        block_bytes = block_str.encode()
        block_bytes_hash = sha256(block_bytes)
        return block_bytes_hash.hexdigest()

    @property
    def last_block(self):
        # Returns the last block in the chain (if there are blocks)
        return self.chain[-1] if self.chain else None
    
    def new_transaction(self, sender: str, recipient: str, amount:float):
        # Adds a new transaction to the list of pending transactions
        self.pending_transactions.append({
            "recipient": recipient,
            "sender": sender,
            "amount": amount,
        })

    @staticmethod
    def valid_block(block):
        return block['hash'].startswith('0000')

    # missing tests
    def proof_of_work(self):
        while True:
            new_block = self.new_block()
            if self.valid_block(new_block):
                break

        # Add the block to the chain
        self.chain.append(new_block)
        print('Found a new block:', new_block)
        