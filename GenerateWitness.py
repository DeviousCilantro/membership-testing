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

# Function to compute the witness for a given element's membership
def compute_witness(g, elements, index, N):
    product = 1
    # Compute the product of all elements except the one at the given index
    for i, element in enumerate(elements):
        if i != index:
            product *= element
    # Compute g^product mod N
    return pow(g, product, N)

def main():
    # Read list of member email IDs
    with open('emails.txt') as f:
        member_ids = f.read().splitlines()
    
    N = int(input("Enter the rigid integer value: "))
    g = int(input("Enter the generator value: "))
    a = int(input("Enter the accumulator value: "))

    # Map email IDs to prime elements
    prime_elements = [hash_to_prime(id) for id in member_ids]

    for id in member_ids:
        # Hash the name to a prime number
        prime_element = hash_to_prime(id)
        # Find the index of the corresponding prime element in the list
        index = prime_elements.index(prime_element)
        # Calculate the membership witness for the member ID
        witness = compute_witness(g, prime_elements, index, N)
        print(f"\nCalculated membership witness for {id}: \n {witness}")

if __name__ == "__main__":
    main()
