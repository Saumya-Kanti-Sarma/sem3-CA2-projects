import hashlib

def generate_hash(index, transaction, previous_hash, timestamp, hash_standard="00ec0"):
        nonce = 0
        initial_hash_letters = ""
        hash_digest = ""
        while initial_hash_letters != hash_standard:
                block_data = "-".join([str(index), str(transaction), str(previous_hash), str(timestamp), str(nonce)])
                hash_object = hashlib.sha256()
                hash_object.update(block_data.encode('utf-8'))

                hash_digest = hash_object.hexdigest()
                initial_hash_letters = hash_digest[:len(hash_standard)]
                # print(initial_hash_letters)
                nonce +=1
        return hash_digest


if __name__ == "__main__":
  print(generate_hash(1,100,000000000000,92749228.523842))
