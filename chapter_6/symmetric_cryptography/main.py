from symmetric_hash import generate_hash

message = "Hello gab, Let's meet at the Kruger National Park on 2020-12-12 at 1pm"
key = "p@55w0rd"

hash = generate_hash(message, key)    
print(hash) # f4fe9553ac1cebd7248538515a38a9622d6250624ac95d1946ce7f4021ba0916