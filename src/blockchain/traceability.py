import hashlib

def create_block(data):
    return hashlib.sha256(data.encode()).hexdigest()

print(create_block("Gene Scope AI Blockchain Initialization"))
