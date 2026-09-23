import time
from .utils.Generatehash import generate_hash
class Block:
    def __init__(
        self,
        index=0,
        transaction=0,
        previous_hash="00000000000000000000000"
    ):
        self.index = index
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        print(f"Mining index: {self.index} Block...")

        hash_digest, nonce = generate_hash(
            index=self.index,
            transaction=self.transaction,
            previous_hash=self.previous_hash,
            timestamp=self.timestamp,
        )
        self.nonce = nonce
        self.hash = hash_digest

    def get_block_data(self):
        return {
            "index": self.index,
            "transaction": self.transaction,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
            "hash": self.hash,
        }
    def __str__(self):
        return (
            f"Index: {self.index}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Transaction: {self.transaction}\n"
            f"Previous Hash: {self.previous_hash}\n"
            f"Hash: {self.hash}\n"
            f"Nonce: {self.nonce}"
        )

if __name__ == "__main__":
    b1 = Block(index=1,transaction=100)
    print(b1)