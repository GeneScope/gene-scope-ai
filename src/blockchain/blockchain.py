from hashlib import sha256
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def hash_block(self, block):
        block_string = str(block)
        return sha256(block_string.encode()).hexdigest()

    def proof_of_work(self, previous_proof):
        proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = sha256(f'{proof**2 - previous_proof**2}'.encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                proof += 1
        return proof


# Simulate storing genetic data on blockchain
if __name__ == "__main__":
    blockchain = Blockchain()
    previous_proof = 100
    gene_sequence = "ATGCGTACGATGCTAG"
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash_block(blockchain.chain[-1])

    block = blockchain.create_block(proof, previous_hash)
    print(f"Stored gene data in block: {block} | Gene: {gene_sequence}")
