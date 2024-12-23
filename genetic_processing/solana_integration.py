from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.transaction import Transaction
from solana.system_program import create_account, transfer

# Connect to Solana devnet
client = Client("https://api.devnet.solana.com")

# Generate a keypair (public and private key) for the user
keypair = Keypair.generate()

# Function to store genetic data (we'll store it as metadata)
def store_genetic_data(user_keypair, data):
    # This would involve storing data in an account on the Solana blockchain
    # For simplicity, we are using a system account and attaching metadata (like genetic results)
    
    # Account to store the genetic data
    account_pubkey = user_keypair.public_key
    print(f"Storing data for account: {account_pubkey}")
    
    # Create a simple transaction (not using smart contracts for now)
    transaction = Transaction()
    
    # Add a dummy transfer operation to simulate a transaction
    transaction.add(
        transfer(
            from_pubkey=user_keypair.public_key,
            to_pubkey=account_pubkey,
            lamports=1000,  # Transfer 1000 lamports (Solana's native currency)
        )
    )
    
    # Send the transaction
    response = client.send_transaction(transaction, user_keypair)
    print(f"Transaction sent: {response}")

    # Ideally, here we would store the genetic data in metadata format or linked to an account on-chain.

# Function to retrieve genetic data (metadata)
def retrieve_genetic_data(account_pubkey):
    # In reality, we'd fetch metadata associated with this account
    print(f"Retrieving genetic data for account: {account_pubkey}")
    # Here we simulate it with dummy data
    return "Gene editing result: CRISPR-Cas9 applied to sample XYZ."

# Example of storing genetic data
store_genetic_data(keypair, "Gene editing result for sample XYZ: CRISPR-Cas9 successful!")

# Example of retrieving genetic data
genetic_data = retrieve_genetic_data(keypair.public_key)
print(f"Genetic Data: {genetic_data}")
