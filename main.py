from src.preprocess import load_data, preprocess_data
from src.clustering import perform_clustering
from src.visualize import plot_clusters

FILEPATH = "jewelry_data.csv"
NUMERICAL_FEATURES = ['weight', 'price', 'sales']
CATEGORICAL_FEATURES = ['type', 'material']
N_CLUSTERS = 3

def main():
    # Load and preprocess data
    data = load_data(FILEPATH)
    processed_data = preprocess_data(data, NUMERICAL_FEATURES, CATEGORICAL_FEATURES)
    
    # Perform clustering
    model, clusters = perform_clustering(processed_data, N_CLUSTERS)
    
    # Visualize results
    plot_clusters(processed_data, clusters, NUMERICAL_FEATURES[0], NUMERICAL_FEATURES[1])

if __name__ == "__main__":
    main()
