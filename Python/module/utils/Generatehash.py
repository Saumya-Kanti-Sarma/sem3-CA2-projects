import hashlib

def generate_hash(index, transaction, previous_hash, timestamp, nonce):
        block_data = "-".join([str(index), str(transaction), str(previous_hash), str(timestamp), str(nonce)])

        hash_object = hashlib.sha256()
        hash_object.update(block_data.encode('utf-8'))

        return hash_object.hexdigest()

if __name__ == "__main__":
  print(generate_hash(1,100,000000000000,92749228.523842,4829))
