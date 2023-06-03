import random
from Crypto.Util import number
import hashlib

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

# Function to verify the witness for a given element's membership
def verify_witness(A, witness, element, N):
    # Check if witness^element mod N equals A
    return pow(witness, element, N) == A

def main():
    N = int(input("Enter the rigid integer value: "))
    A = int(input("Enter the accumulator value: "))
    witness = int(input("Enter the membership witness: "))
    id = input("Enter email id of member: ")

    # Find the prime corresponding to the given email ID
    element = hash_to_prime(id)

    # Verify membership
    if verify_witness(A, witness, element, N):
        print("\nMembership verified.")
    else:
        print("\nMembership not verified.")

if __name__ == "__main__":
    main()
