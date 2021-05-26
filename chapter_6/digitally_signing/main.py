from generate_digigal_document import sign
from verify_digital_signature import verify

document = b"I am a document..."

signed, public_key_hex = sign(document)
result = verify(public_key_hex, signed)

print(result)