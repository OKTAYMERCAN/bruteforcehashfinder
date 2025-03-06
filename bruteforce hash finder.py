import hashlib
import itertools
import string
import sys
import time

def hash_crack_update(input_hash, max_length=128):
    """
    Cracks the input hash by trying all possible combinations and prints each step.

    Args:
        input_hash: The hash to crack.
        max_length: The maximum length of the password to try.

    Returns:
        The matching text (if found), otherwise None.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    algorithms = ["md5", "sha1", "sha256", "sha512"]

    start_time = time.time()

    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            text = "".join(combination)
            print(f"Generated text: {text} \n")

            for algorithm in algorithms:
                hash_object = hashlib.new(algorithm)
                hash_object.update(text.encode('utf-8'))
                generated_hash = hash_object.hexdigest()

                print(f"  Algorithm: {algorithm}, Hash: {generated_hash} \n")

                if generated_hash == input_hash:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    return f"Matching text: {text} \n (Algorithm: {algorithm}) \n Elapsed time: {elapsed_time:.2f} seconds"
                sys.stdout.flush()

    end_time = time.time()
    elapsed_time = end_time - start_time
    return f"Match not found. Elapsed time: {elapsed_time:.2f} seconds"

# Get hash input from the user
input_hash = input("Enter hash: ")

# Crack the hash
result = hash_crack_update(input_hash)

# Print the result
print(result)
