import json

from .Block import Block
from .utils.Generatehash import check_hash


class BlockChain:

    def __init__(self, pow_file="PoW.json"):
        self.chain = []
        self.pow_file = pow_file

        print("Generating index: 0 Block")

        genesis_block = Block(
            index=0,
            transaction=0
        )

        self.chain.append(genesis_block)
        self.save_pow()

    def last_block(self):
        return self.chain[-1]

    def check_tamper(self):

        for i, block in enumerate(self.chain):

            # Check the block's own hash
            if not check_hash(block):
                return f"Tamper detected in block no {i}"

            # Check the connection with previous block
            if i > 0:
                previous_block = self.chain[i - 1]

                if block.previous_hash != previous_block.hash:
                    return f"Broken chain detected at block no {i}"

        return True

    def create_new_block(self, transaction):

        # Make sure the existing blockchain is valid
        if self.check_tamper() is not True:
            print(self.check_tamper())
            return False

        index = len(self.chain)

        previous_block = self.last_block()

        print(f"Generating index: {index} Block")

        new_block = Block(
            index=index,
            transaction=transaction,
            previous_hash=previous_block.hash
        )

        self.chain.append(new_block)

        self.save_pow()

        return new_block

    def save_pow(self):

        data = []

        for block in self.chain:
            data.append(block.get_block_data())

        with open(self.pow_file, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4
            )

    def __str__(self):

        output = ""

        for block in self.chain:
            output += str(block)
            output += "\n---------------------\n"

        return output


if __name__ == "__main__":

    chain = BlockChain()

    print("Genesis Block:")
    print(chain.last_block())

    print("\nCreating new block...")
    chain.create_new_block(201)

    print(chain)

    print("Blockchain valid:", chain.check_tamper())