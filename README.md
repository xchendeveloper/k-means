# k-means
use k-means draw thermodynamic chart

Using thermodynamics cameras to take photos, each data in the data.csv file represents the temperature of each pixel in the photo.
Sklearn's KMeans algorithm is used to process the temperature data in data.csv and get the final convergent picture.

## how to use ?
```
python ./draw_k_means.py file_path cluster_count

eg.
python ./draw_k_means.py 'data.csv' 3
```
![how to use](https://github.com/xchendeveloper/k-means/blob/master/result.png)

Now support 8 clusters at most. If you need more clusters, you can customize them.

## how to customize more ?
```
from draw_k_means import drawKMeans

drawKMeans("data.csv", 9,['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','#F09876'])
```


