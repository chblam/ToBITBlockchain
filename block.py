import datetime
import hashlib


class Block:

    def __init__(self, data, prev_hash):
        self.timestamp = datetime.datetime.now().isoformat()
        self.nonce = 0
        self.data = data
        self.prev_hash = prev_hash
        self.hash = hashlib.sha512()


    def __str__(self):
        return "{}{}{}{}".format(self.timestamp, self.prev_hash.hexdigest(), self.data, self.nonce)

    def mine(self, difficulty):
        self.hash.update(str(self).encode('utf-8'))
        while int(self.hash.hexdigest(), 16) > 2 ** (512 - difficulty):
            self.nonce += 1
            # updating a hash is cumulative, the hash should be calculated in one go, so it's reset before the update
            self.hash = hashlib.sha512()
            self.hash.update(str(self).encode('utf-8'))
