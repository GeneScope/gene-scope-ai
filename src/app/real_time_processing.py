import pandas as pd
import time

# Simulated Real-Time Data Stream
def process_real_time_data():
    for i in range(10):
        sample_data = {
            'gene_id': f'GENE_{i}',
            'gene_expression': round(50 + i * 1.2, 2),
            'mutation_rate': round(0.05 * i, 3),
            'health_status': 'Healthy' if i % 2 == 0 else 'Unhealthy'
        }
        
        df = pd.DataFrame([sample_data])
        print("Real-Time Data Processed:")
        print(df)
        time.sleep(1)  # Simulate real-time delay

if __name__ == "__main__":
    process_real_time_data()
