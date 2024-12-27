import pandas as pd

class CancerGenomicDataLoader:
    """
    A class to load and preprocess cancer genomic datasets.
    """
    def __init__(self, file_path: str):
        """
        Initialize with the path to the dataset.
        :param file_path: Path to the genomic dataset CSV file.
        """
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """
        Load genomic data from a CSV file.
        """
        try:
            self.data = pd.read_csv(self.file_path)
            print("✅ Data loaded successfully.")
        except FileNotFoundError:
            print("❌ Error: File not found.")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def filter_mutations(self, mutation_list):
        """
        Filter dataset for specific cancer-driving mutations.
        :param mutation_list: List of mutation markers to filter.
        :return: Filtered DataFrame.
        """
        if self.data is None:
            print("❌ Error: Data not loaded.")
            return None
        
        filtered_data = self.data[self.data['mutation'].isin(mutation_list)]
        print(f"✅ Filtered {len(filtered_data)} rows matching mutations: {mutation_list}")
        return filtered_data
    
    def get_summary(self):
        """
        Print summary statistics of the dataset.
        """
        if self.data is None:
            print("❌ Error: Data not loaded.")
            return
        
        print("📊 Dataset Summary:")
        print(self.data.describe())
