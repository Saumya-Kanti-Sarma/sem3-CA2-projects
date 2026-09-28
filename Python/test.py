from blockchain_visualizer import BlockChain, Block

chain = BlockChain()
chain.check_tamper()

chain.create_new_block(Block(332))