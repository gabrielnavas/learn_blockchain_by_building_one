import hashlib

# hash functions expect bytes as input: the encode() method turns strings to bytes
input_bytes = b'backpack'

output = hashlib.sha256(input_bytes)

#we use hexdigest() to convert bytes to hex because it's easier to read
print(output.hexdigest())
#output: 5f00368a6ad231c3c439c4f6bc33c27014b4d35a904ff1656d74f9528636f496

other_input = b'BaCkPaCk'
other_output = hashlib.sha256(other_input)
print(other_output.hexdigest())
#output: 2770bfb06520159f9198211e7c9d40d8816a8def96efc887a10a2679a795e04f 

#false
print(other_output == output)
