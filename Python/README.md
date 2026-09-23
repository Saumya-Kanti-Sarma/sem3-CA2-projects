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

chain.create_new_block(Block(transaction=1302))
chain.create_new_block(Block(transaction=1300))
chain.create_new_block(Block(transaction=1500))
chain.create_new_block(Block(transaction=200))

print(chain)

```