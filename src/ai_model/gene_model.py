class CRISPRGeneEditor:
    def __init__(self, gene_sequence):
        self.gene_sequence = gene_sequence

    def edit_gene(self, target_gene, modification):
        """
        Simulate CRISPR editing by replacing part of the gene sequence.
        :param target_gene: The target gene to edit.
        :param modification: The genetic sequence to add.
        """
        print(f"Editing gene at position: {target_gene}")
        modified_gene = self.gene_sequence.replace(target_gene, modification)
        return modified_gene

# Example usage
if __name__ == "__main__":
    gene_sequence = "ATGCATGCATGC"
    target_gene = "ATGC"
    modification = "CGTA"
    
    crispr_editor = CRISPRGeneEditor(gene_sequence)
    modified_gene = crispr_editor.edit_gene(target_gene, modification)
    print(f"Modified Gene Sequence: {modified_gene}")
