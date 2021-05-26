import unittest

from datetime import datetime 

from blockchain.blockchain import Blockchain

class TestHash(unittest.TestCase):
	def test_valid_hash(self):
		block = {
			'index': 66,
			'timestamp': datetime.utcnow().isoformat(),
			'transactions': [],
			'previous_hash': '123',
		}
		hex_hash_valid = Blockchain.hash(block)
		len_hex_hash_valid = 64
		self.assertEqual(type(hex_hash_valid), str)
		self.assertEqual(len(hex_hash_valid), len_hex_hash_valid)
