import hashlib


# read dolar.jpg
file = open('imgs/dolar.jpg', 'rb')
bytes_from_file = file.read()
file.close()

hash = hashlib.sha256(bytes_from_file)

# str type
dolar_hex_hash = hash.hexdigest()

# bytes type
dolar_digest_hash = hash.digest()

print(f'hash digest bytes{dolar_digest_hash}')
print(f'The hash of my file is: {dolar_hex_hash}')



# read renminbi.jpg
file = open('imgs/renminbi.jpg', 'rb')
bytes_from_file = file.read()
file.close()

hash = hashlib.sha256(bytes_from_file)

# str type
renminbi_hex_hash = hash.hexdigest()

# bytes type
renminbi_digest_bytes = hash.digest()

print(type(renminbi_digest_bytes)) 
print(f'hash digest bytes{renminbi_hex_hash}')
print(f'The hash of my file is: {renminbi_digest_bytes}')


# dolar hash == renminbi hash is equals? False
print(dolar_hex_hash == renminbi_hex_hash)
