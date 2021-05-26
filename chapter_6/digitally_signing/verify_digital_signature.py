import nacl.encoding
import nacl.signing

def verify(public_key: bytes, signed_message: bytes):
    # We generate the verify_key
    verify_key = nacl.signing.VerifyKey(public_key, encoder=nacl.encoding.HexEncoder)

    # Now we attempt to verify the message
    # Any invalidation will result in an Exception being thrown
    return verify_key.verify(signed_message)