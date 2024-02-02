import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def grafico_elbow_silhouette(
    X, random_state=42, intervalo=(2, 11)
):

    elbow = {}
    silhouette = []

    k_range = range(*intervalo)


    for i in k_range:
        kmeans = KMeans(n_clusters=i, n_init=10, random_state=random_state)
        kmeans.fit(X)
        elbow[i] = kmeans.inertia_

        labels = kmeans.labels_
        silhouette.append(silhouette_score(X, labels))

    fig, axs = plt.subplots(ncols=2, figsize=(13,5), tight_layout=True)


    sns.lineplot(x=list(elbow.keys()), y=list(elbow.values()), ax=axs[0])
    axs[0].set_xlabel('K')
    axs[0].set_ylabel('Inertia')
    axs[0].set_title('Elbow Method')

    sns.lineplot(x=list(k_range), y=silhouette, ax=axs[1])
    axs[1].set_xlabel('K')
    axs[1].set_ylabel('Silhouette Score')
    axs[1].set_title('Silhouette Method')

    plt.show()


from matplotlib.colors import ListedColormap

def visualizar_grafico_3d(
    dataframe,
    colunas,
    quantidade_de_cores,
    centroides,
    mostrar_centroides=True,
    mostrar_pontos=True,
    coluna_clusters=None,
):
  fig = plt.figure(figsize=(12,7))
  ax = fig.add_subplot(111, projection='3d')

  colors = plt.cm.tab10.colors[:quantidade_de_cores]
  colors = ListedColormap(colors)

  x = dataframe[colunas[0]]
  y = dataframe[colunas[1]]
  z = dataframe[colunas[2]]

  grafico_centroides = mostrar_centroides
  grafico_pontos = mostrar_pontos

  for i, centroide in enumerate(centroides):
    if grafico_centroides:
      ax.scatter(*centroide, s=500, alpha=0.6)
      ax.text(
      *centroide, i, fontsize=20, horizontalalignment='center',
      verticalalignment='center'
      )

    if grafico_pontos:
      s = ax.scatter(x, y, z, c=coluna_clusters, cmap=colors)
      ax.legend(*s.legend_elements(), bbox_to_anchor=(1.2,1))

  ax.set_xlabel('Age')
  ax.set_ylabel('Annual Income (k$)')
  ax.set_zlabel('Spending Score (1-100)')
  ax.set_title('Clusters')

  plt.show()