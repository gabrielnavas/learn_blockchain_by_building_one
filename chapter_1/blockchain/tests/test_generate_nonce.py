import unittest

from blockchain.blockchain import Blockchain

class TestGenerateNonce(unittest.TestCase):
    def test_generate_nonce_in_hex_16Bytes(self):
        nonce = Blockchain.generate_nonce()
        self.assertEqual(len(nonce), 16)