# Mahmoud.aboalenen
# @maboalenen
# RSA-implementation 
# python3 module crypto


from Crypto.Util import number
import random

# greatest common divisor
def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1

# Prime numbers (Typical lengths for p & q are 512-bits and larger 
# sample of prime two prime numbers

p = 1171 #number.getPrime(512)
q = 2099 #number.getPrime(512)

# the minimum length of n secure RSA algorithm is 1024 bits

n = p * q

# the two exponents e & d must be relatively prime to p-1 and q-1. 

fi = (p-1) * (q-1)

e = random.randrange(1, fi)


#Use Euclid's Algorithm to verify that e and fi (n) are comprime
#This function outputs the number of integers between 0 and n that are relatively prime to n 

g = gcd(e, fi)
while g != 1:
	e = random.randrange(1, fi)
	g = gcd(e, fi)
 
# start_number = key lenth to genrat the D (sample) minimum length of secure RSA algorithm is 1024 bits

start_number = 65535

#1024 start of the key length
#100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000   

# genrat e 

for e in range(start_number, fi):
    if is_coprime(e, fi) and is_coprime(e, n):
        break

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext): 
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)
print("P -> ",p)
print("Q -> ",q)
print("N -> ",n)
print("FI -> ",fi)
print("Public_key (E) -> ", e,n) 


# genrate D 

if e:
    for d in range(start_number, n):
        if ((e*d) % fi) == 1:        # Choose d  (e*d mod Φ(n) =1 )
            print("Secrit-key (D) : ")
            print(d,n)
            break

# Message encryption and decryption 

message = input("Enter a message to encrypt with public_key: ")    
encrypted_msg = encrypt((e,n), message)
print ("Your encrypted message is:")
print (''.join(map(lambda x: str(x), encrypted_msg)))
print ("Decrypting message with private_key ", (d,n) ," . . .")  
print ("Your message is:")
print (decrypt((d,n), encrypted_msg))