import unittest

from datetime import datetime 

from blockchain.blockchain import Blockchain

class TestNewTransaction(unittest.TestCase):
	def test_transaction_is_zero_length(self):
		bc = Blockchain()
		jonh_hash='123!@#'
		anna_hash='321%&'
		coins=101
		bc.new_transaction(jonh_hash,anna_hash,coins)
		first_pending_transaction = bc.pending_transactions[0]
		self.assertEqual(first_pending_transaction['sender'], jonh_hash)
		self.assertEqual(first_pending_transaction['recipient'], anna_hash)
		self.assertEqual(first_pending_transaction['amount'], coins)

