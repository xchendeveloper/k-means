import csv
import sys
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# image width
max_x = 0

# image height
max_y = 0

# color array
color_array = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']


def __get_data(file_path):
    result = []
    global max_x, max_y
    with open(file_path, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            col = 0
            max_y = reader.line_num - 1
            for cell in row:
                item = [col, reader.line_num - 1, float(cell) * 1e100]
                max_x = col
                col += 1
                result.append(item)
    return result


def drawKMeans(file_path, n_clusters, colors=color_array):
    """
    :param file_path: csv file's path
    :param n_clusters: cluster count
    :param colors: custom color
    :return:
    """

    data = __get_data(file_path);
    estimator = KMeans(n_clusters=n_clusters)
    res = estimator.fit(data)
    lable_pred = estimator.labels_
    centroids = estimator.cluster_centers_
    inertia = estimator.inertia_
    # print res
    print(lable_pred)
    print(centroids)
    print(inertia)

    array_x = [[] for i in range(n_clusters)]
    array_y = [[] for i in range(n_clusters)]

    for i in range(len(data)):
        array_x[lable_pred[i]].append([data[i][0]])
        array_y[lable_pred[i]].append([data[i][1]])

    for j in range(len(array_x)):
        plt.plot(array_x[j], array_y[j], colors[j])

    plt.axis([0, max_x, 0, max_y])
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("[ERROR] need more params. \n Please input like this : python draw_k_means.py 'resource/data.csv' 3 ")
    else:
        file_path = sys.argv[1]
        n_clusters = int(sys.argv[2])
        drawKMeans(file_path, n_clusters)
