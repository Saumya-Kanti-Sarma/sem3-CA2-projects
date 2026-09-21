import hashlib
import json
from datetime import datetime
from utils.Generatehash import generate_hash

class Block:
    def __init__(self, index, transaction, previous_hash="00000000000000000000000"):
        self.index = index
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.timestamp = datetime.now().timestamp()

        hash_digest, nonce = generate_hash(
            index=self.index,
            transaction=self.transaction,
            previous_hash=self.previous_hash,
            timestamp=self.timestamp,
        )

        self.nonce = nonce
        self.hash = hash_digest

    def __str__(self):
        x =  f"index: {self.index},\ntimestamp: {self.timestamp},\ntransaction: {self.transaction},\nprevious_hash: {self.previous_hash},\nhash: {self.hash},\nnonce: {self.nonce} "
        return x


if __name__ == "__main__":
  b1 = Block(
    index=1,
    transaction=100,
  )
  print(b1)

