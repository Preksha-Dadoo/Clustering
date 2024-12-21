import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(data, clusters, x_feature, y_feature):
    """Scatter plot of clusters."""
    sns.scatterplot(x=data[x_feature], y=data[y_feature], hue=clusters, palette='viridis')
    plt.title("Cluster Visualization")
    plt.show()
