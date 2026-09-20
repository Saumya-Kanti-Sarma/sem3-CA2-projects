import hashlib
import json
from datetime import datetime
from utils.Generatehash import generate_hash

class Block:
    def __init__(self, index, transaction, previous_hash=00000000000000000000000, nonce=0):
        self.index = index
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.timestamp = datetime.now().timestamp()
        self.nonce = nonce
        self.hash = generate_hash(index=self.index, transaction=self.transaction, previous_hash=self.previous_hash,timestamp=self.timestamp,nonce=self.nonce)

    def __str__(self):
        x =  f"index: {self.index},\ntimestamp: {self.timestamp},\n transaction: {self.transaction},\n previous_hash: {self.previous_hash},\n hash: {self.hash},\nnonce: {self.nonce} "
        return x


if __name__ == "__main__":
  b1 = Block(
    index=1,
    transaction=100,
    nonce=12042,
    previous_hash=6420843399322
  )
  print(b1)

