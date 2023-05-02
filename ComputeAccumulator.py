import hashlib
import random
from Crypto.Util import number

# Function to generate a safe prime of the given bit length
def generate_safe_prime(bits):
    while True:
        # Generate a prime number q with (bits - 1) length
        q = number.getPrime(bits - 1)
        # Calculate p = 2q + 1
        p = 2 * q + 1
        # Check if p is prime, if so return it
        if number.isPrime(p):
            return p

# Function to hash input data to a prime number
def hash_to_prime(data):
    # Create a new SHA-256 hash object
    h = hashlib.sha256()
    # Update the hash object with the input data
    h.update(data.encode())
    # Convert the hash digest to an integer candidate
    candidate = int(h.hexdigest(), 16)
    # Keep incrementing the candidate until a prime number is found
    while not number.isPrime(candidate):
        candidate += 1
    return candidate

# Function to accumulate elements using the base and modulus N
def accumulate_elements(g, elements, N):
    product = 1
    # Compute the product of all elements
    for element in elements:
        product *= element
    # Compute g^product mod N
    return pow(g, product, N)

def main():
    bits = 256
    print("Generating safe primes... \n")
    p = generate_safe_prime(bits)
    q = generate_safe_prime(bits)
    print(f"Generated safe primes: \n {p} \n {q} \n")
    N = p * q
    print(f"Computed the rigid integer value (product of safe primes): \n {N} \n")
    g = random.randint(2, N-1)
    print(f"Selected base value: \n {g} \n")

    # Read list of member ids
    with open('emails.txt') as f:
        member_ids = f.read().splitlines()
    
    # Map email IDs to prime elements
    prime_elements = [hash_to_prime(id) for id in member_ids]

    # Compute the accumulated value for all prime elements
    A = accumulate_elements(g, prime_elements, N)

    print(f"Computed accumulator value: {A} \n")

if __name__ == "__main__":
    main()
