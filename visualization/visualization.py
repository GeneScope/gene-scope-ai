import matplotlib.pyplot as plt
import numpy as np

# Simulating gene expression data
genes = ['Gene1', 'Gene2', 'Gene3', 'Gene4', 'Gene5']
expression_values = np.random.random(5) * 100

# Creating a bar plot to represent gene expression
plt.bar(genes, expression_values)
plt.xlabel('Genes')
plt.ylabel('Expression Levels')
plt.title('Gene Expression Levels')
plt.show()
