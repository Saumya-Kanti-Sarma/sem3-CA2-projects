from .Block import Block
from .utils.Generatehash import check_hash


class BlockChain:
    def __init__(self):
        self.chain = []
        genesis_block = Block(
            index=0,
            transaction=0
        )
        self.chain.append(genesis_block)

    def last_block(self):
        return self.chain[-1]

    def check_tamper(self):
        for i, block in enumerate(self.chain):
            if not check_hash(block):
                return f"Tamper detected in block no {i}"
        return True

    def create_new_block(self, transaction):
        if self.check_tamper() is not True:
            print(self.check_tamper())
            return False

        previous_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            transaction=transaction,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)


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

    print("Creating new block...")
    chain.create_new_block(201)
    print(chain)
    print()

    print("Blockchain valid:", end="")
    print(chain.check_tamper())