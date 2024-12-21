# Clustering
This project demonstrates clustering techniques on a jewelry dataset using Python.

## Features
- Data Preprocessing
- K-Means Clustering
- Cluster Visualization

## How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Open in Jupyter Notebook   
   
## Project Structure
   ```bash
jewelry-clustering/
├── data/
│   └── jewelry_data.csv          # Dataset file
├── src/
│   ├── preprocess.py             # Preprocessing module
│   ├── clustering.py             # Clustering logic
│   ├── visualize.py              # Visualization functions
│   └── __init__.py               # Makes src a Python package
├── notebooks/
│   └── exploratory_analysis.ipynb # Jupyter Notebook for EDA
├── tests/
│   └── test_clustering.py        # Unit tests for clustering
├── .gitignore                    # Git ignore file
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
├── LICENSE                       # License file
├── setup.py                      # For making the project installable
└── main.py                       # Main script to run the pipeline
```

## Conclusion
This project demonstrates the impact of different clustering techniques and preprocessing methods on clustering quality. K-Means Clustering with PCA preprocessing consistently outperformed other methods, making it the most effective approach for this dataset. This analysis provides insights into how data preprocessing and choice of clustering algorithm can influence the quality and interpretability of clusters in unsupervised learning tasks.

## License
This project is distributed under the MIT License
