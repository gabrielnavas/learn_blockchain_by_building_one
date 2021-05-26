import unittest

from datetime import datetime 

from blockchain.blockchain import Blockchain

class TestBlockGenesis(unittest.TestCase):
	def test_transaction_is_zero_length(self):
		bc = Blockchain()
		genesis_block = bc.last_block
		self.assertEqual(genesis_block.get('transactions'), [])

	def test_block_genesis_is_block_zero(self):
		bc = Blockchain()
		genesis_block = bc.last_block
		self.assertEqual(genesis_block.get('index'), 0)

	def test_new_block(self):
		bc = Blockchain()
		genesis_block = bc.last_block
		self.assertTrue(genesis_block)
		self.assertTrue(datetime.fromisoformat(genesis_block.get('timestamp')))

	def test_has_one_block(self):
		bc = Blockchain()
		self.assertEqual(len(bc.chain), 1)

	def test_previous_hash_is_none(self):
		bc = Blockchain()
		self.assertEqual(bc.chain[0]['previous_hash'], None)
