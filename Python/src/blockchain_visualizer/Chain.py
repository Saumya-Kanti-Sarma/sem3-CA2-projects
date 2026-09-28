import json
import os

try:
    from .Block import Block
    from .Stack import Stack
    from .Queue import Queue
    from .utils.Generatehash import check_hash
except ImportError:
    from Block import Block
    from Stack import Stack
    from Queue import Queue
    from utils.Generatehash import check_hash


class BlockChain:
    def __init__(self, pow_file="PoW.json"):
        self.pow_file = pow_file
        self.chain = Stack()

        if os.path.exists(self.pow_file):
            self._load_chain()
            print(f"Loaded existing blockchain with {self.chain.size()} block(s) from '{self.pow_file}'.")
        else:
            print("PoW.json not found. Creating genesis block...")
            genesis_block = Block(index=0, transaction=0)
            self.chain.push(genesis_block)
            self._save_pow_full()

    def _load_chain(self):
        with open(self.pow_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for entry in data:
            block = Block.__new__(Block)
            block.index = entry["index"]
            block.transaction = entry["transaction"]
            block.previous_hash = entry["previous_hash"]
            block.timestamp = entry["timestamp"]
            block.nonce = entry["nonce"]
            block.hash = entry["hash"]
            self.chain.push(block)

    def _append_block_to_pow(self, block):
        with open(self.pow_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        data.append(block.get_block_data())
        with open(self.pow_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def _save_pow_full(self):
        data = [block.get_block_data() for block in self.chain]
        with open(self.pow_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def last_block(self):
        return self.chain.peek()

    def check_tamper(self):
        if not os.path.exists(self.pow_file):
            return "PoW.json not found — cannot validate chain."
        with open(self.pow_file, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        validation_queue = Queue()
        for entry in raw_data:
            block = Block.__new__(Block)
            block.index = entry["index"]
            block.transaction = entry["transaction"]
            block.previous_hash = entry["previous_hash"]
            block.timestamp = entry["timestamp"]
            block.nonce = entry["nonce"]
            block.hash = entry["hash"]
            validation_queue.enqueue(block)
        previous_block = None
        while not validation_queue.is_empty():
            block = validation_queue.dequeue()

            if not check_hash(block):
                return f"Tamper detected in block no {block.index}"
            if previous_block is not None:
                if block.previous_hash != previous_block.hash:
                    return f"Broken chain detected at block no {block.index}"

            previous_block = block

        return True

    def create_new_block(self, transaction):
        tamper_result = self.check_tamper()
        if tamper_result is not True:
            print(tamper_result)
            return False

        index = self.chain.size()
        previous_block = self.last_block()
        print(f"Generating index: {index} Block")

        new_block = Block(
            index=index,
            transaction=transaction,
            previous_hash=previous_block.hash,
        )
        self.chain.push(new_block)
        self._append_block_to_pow(new_block)

        return new_block

    def __str__(self):
        output = ""
        for block in self.chain:
            output += str(block)
            output += "\n---------------------\n"
        return output


if __name__ == "__main__":

    chain = BlockChain()
    print("\nGenesis Block:")
    print(chain.last_block())
    print("\nCreating block 1...")
    chain.create_new_block(201)
    print("\nCreating block 2...")
    chain.create_new_block(350)
    print("\n--- Full Chain ---")
    print(chain)

    print("Blockchain valid:", chain.check_tamper())
