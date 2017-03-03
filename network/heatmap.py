import matplotlib.pyplot as plt
def plot_heatmap(connections_matrix):
    plt.imshow(connections_matrix, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.show()