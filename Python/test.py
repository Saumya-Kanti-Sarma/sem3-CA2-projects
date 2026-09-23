from blockchain_visualizer import BlockChain

chain = BlockChain()

chain.create_new_block(1302)
chain.create_new_block(1300)
chain.create_new_block(1500)
chain.create_new_block(200)

print(chain)