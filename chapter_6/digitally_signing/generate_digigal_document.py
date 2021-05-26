import nacl.encoding
import nacl.signing


def sign(document: bytes):
    # Generate a new key-pair
    private_key = nacl.signing.SigningKey.generate()
    public_key = private_key.verify_key

    # Since it's bytes, we'll need to serialize the key to a readable format before publishing it:
    public_key_hex = public_key.encode(encoder=nacl.encoding.HexEncoder)

    # Now, let's sign a message with it
    signed = private_key.sign(b"I am a document...")

    return signed, public_key_hex