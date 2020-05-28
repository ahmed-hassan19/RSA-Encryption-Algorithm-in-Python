def is_prime(x):
    '''
    Takes an integer x and returns True if x is a prime number
    and Flase if x is not a prime number.
    '''
    for i in range(2, x-1):
        if x % i == 0:
            return False
    else:
        return True

def gcd(a, b):
    '''
    Computes the Greates Common Divisor (gcd) between integers a, b.
    '''
    if b == 0:
        return a 
    else: 
        return gcd(b, a%b) 

def extended_gcd(x, y):
    '''
    Extended Euclidean algortihm between integers x, y to find
    the modular multiplicative inverse d of x under modulo y. 
    '''
    if y == 0:   
        return x, 1, 0
             
    d, a, b = extended_gcd(y, x % y)  
     
    return d, b, a - (x // y) * b

def encrypt(public_key, message):
    '''
    Encryptes a string message using a public_key as a tuple of (n, e).
    '''
    encrypted = []
    for character in message:
        int_message = ord(character)
        n, e = public_key
        c = pow(int_message, e) % n 
        encrypted.append(c)
    return encrypted

def decrypt(private_key, encrypted):
    '''
    Decryptes a string message using a private_key as a tuple of (n, d).
    '''
    decrypted = []
    for character in encrypted:
        n, d = private_key
        int_message = pow(character, d) % n
        message = chr(int_message)
        decrypted.append(message)
    return decrypted