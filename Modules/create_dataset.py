import numpy as np
import pandas as pd

# Create random data
keywords = np.random.randint(1, 7, size=(1000,))
grammar = np.random.randint(0, 2, size=(1000,))
qst = np.random.randint(1, 7, size=(1000,))
# Calculate class based on keywords, grammar, and qst values
classes = np.round(8 - (keywords + grammar + qst) / 3).astype(int)

# Combine data into a DataFrame
df = pd.DataFrame({'keyword': keywords, 'grammar': grammar,
                   'qst': qst, 'class': classes})

# Save DataFrame to CSV file
df.to_csv('dataset.csv', index=False)
