chain = Blockchain()

chain.create_new_block(Block(transaction=1302))
chain.create_new_block(Block(transaction=1300))
chain.create_new_block(Block(transaction=1500))
chain.create_new_block(Block(transaction=200))

print(chain)