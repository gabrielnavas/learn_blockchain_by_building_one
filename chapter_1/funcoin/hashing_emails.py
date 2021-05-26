from hashlib import sha256

def get_hash_with_secret_phrase(input_data: str, secret_phrase: str) -> str:
        combined = input_data + secret_phrase
        hash_combined = sha256(combined.encode())
        hex_hash = hash_combined.hexdigest()
        return hex_hash

secret_phrase = "bolognese"

email_body = "Hey Bob, I think you should learn about Blockchains! " \
            "I've been investing in Bitcoin and currently have" \
            "exactly 12.03 BTC in my account."

print(get_hash_with_secret_phrase(email_body, secret_phrase))
