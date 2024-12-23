from solders.pubkey import Pubkey
from solders.keypair import Keypair
from solders.system_program import create_account
from solders.rpc.api import Client

# Connect to Solana Devnet
solana_client = Client("https://api.devnet.solana.com")

# Generate Keypair
keypair = Keypair()
public_key = keypair.pubkey()

# Example Data to Store
genetic_result = {
    "gene_id": "GENE001",
    "prediction": "High Risk",
    "accuracy": 0.92
}

# Prepare Transaction
transaction = create_account(
    from_pubkey=public_key,
    to_pubkey=public_key,
    lamports=1000000,
    space=500,
    owner=Pubkey.from_string("11111111111111111111111111111111")
)

# Send Transaction
response = solana_client.send_transaction(transaction, keypair)
print("Transaction Response:", response)
