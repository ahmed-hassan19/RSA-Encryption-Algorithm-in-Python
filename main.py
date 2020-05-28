from utils import *
import random

primes = [i for i in range(100, 500) if is_prime(i)]
p = random.choice(primes)
q = random.choice(primes)
message = input('Enter the text to be encrypted: ')

n = p*q
k = (p-1)*(q-1) 

for e in range(2, k):
    if gcd(e, k) == 1:
        break

public_key = (n, e)

_, b, _ = extended_gcd(e, k)
if b < 0:
    b = b + k
private_key = (n, b)

encrypted = encrypt(public_key, message)
print(f'Encrypted message: {"".join(str(s) for s in encrypted)}')

decrypted = decrypt(private_key, encrypted)
print(f'Decrypted message: {"".join(str(s) for s in decrypted)}')