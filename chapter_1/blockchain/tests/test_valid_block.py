import unittest

from blockchain.blockchain import Blockchain
from datetime import datetime

class TestValidBlock(unittest.TestCase):
    def test_valid_block_starts_with_four_zeros(self):
        block = {
            'index': 55,
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': [],
            'previous_hash': None,
            'hash': '0000a5123'
        }
        self.assertTrue(Blockchain.valid_block(block))

    def test_is_false_not_starts_with_four_zeros(self):
        block = {
            'index': 55,
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': [],
            'previous_hash': None,
            'hash': '1000a5123'
        }
        self.assertFalse(Blockchain.valid_block(block))
