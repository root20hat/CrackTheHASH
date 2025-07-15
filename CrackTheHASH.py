import hashlib

def crack_password(hash_to_crack, algorithm, wordlist_path):
    with open(wordlist_path, 'r', encoding='latin-1') as file:
        for word in file:
            word = word.strip()
            encoded_word = word.encode('utf-8')

            if algorithm == "md5":
                hash_word = hashlib.md5(encoded_word).hexdigest()
            elif algorithm == "sha1":
                hash_word = hashlib.sha1(encoded_word).hexdigest()
            elif algorithm == "sha256":
                hash_word = hashlib.sha256(encoded_word).hexdigest()
            else:
                print("Unsupported algorithm.")
                return

            if hash_word == hash_to_crack:
                print(f"[✔] Password found: {word}")
                return

    print("[✖] Password not found in the wordlist.")

# Example usage:
if __name__ == "__main__":
    hash_input = input("Enter the hash: ")
    algo = input("Enter hashing algorithm (md5/sha1/sha256): ").lower()
    wordlist = input("Enter path to wordlist: ") or "wordlist.txt"

    crack_password(hash_input, algo, wordlist)
