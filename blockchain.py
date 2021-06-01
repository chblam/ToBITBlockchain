import hashlib
from block import Block


class Blockchain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blockchain = []
        self.mempool = []
        self.genesis()

    def genesis(self):
        h = hashlib.sha512()
        h.update("Genesis Block".encode('utf-8'))
        genesis_block = Block("Genesis Block", h)
        genesis_block.mine(self.difficulty)
        self.blockchain.append(genesis_block)

    def proof_of_work(self, block):
        h = hashlib.sha512()
        h.update(str(block).encode('utf-8'))
        return block.hash.hexdigest() == h.hexdigest() and \
               int(h.hexdigest(), 16) < 2 ** (512 - self.difficulty) and \
               block.prev_hash == self.blockchain[-1].hash

    def add_to_blockchain(self, block):
        if self.proof_of_work(block):
            self.blockchain.append(block)

    def add_to_mempool(self, data):
        self.mempool.append(data)

    def mine(self):
        if len(self.mempool) > 0:
            data = self.mempool.pop()
            b = Block(data, self.blockchain[-1].hash)
            b.mine(self.difficulty)
            self.add_to_blockchain(b)
            print("*"*148)
            print("Block #" + str(self.blockchain.__len__()-1))
            print("*"*148)
            print("Difficulty: \t\t" + str(self.difficulty))
            print("Time Stamp: \t\t" + b.timestamp)
            print("Nonce: \t\t\t\t" + str(b.nonce))
            print("Block Data: \t\t" + b.data)
            print("Previous Hash: \t\t" + b.prev_hash.hexdigest())
            print("Hash: \t\t\t\t" + b.hash.hexdigest())
            print("*"*148)

