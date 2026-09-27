# Blockchain Visualizer

A lightweight Python library for learning and experimenting with
blockchain concepts using Python data structures.

## Features

- Block creation
- SHA-256 hashing
- Proof-of-work style nonce generation
- Previous block hash linking
- Blockchain integrity verification
- Tamper detection
- Simple Python API

## Installation

```bash
pip install blockchain-visualizer
```

## USage

```python
from blockchain_visualizer import Blockchain

chain = Blockchain()


# it will generate PoW.json file at the root dir.
chain.create_new_block(1302)
chain.create_new_block(1300)
chain.create_new_block(1500)
chain.create_new_block(200)

print(chain)
# this will print the chain.

```