from hashlib import sha256

def generate_hash(message, key):
    hash_message = sha256((key + message).encode()).hexdigest() 
    return hash_message
