# KMeans-Algorithm
Implementation of K-Means algorithm using core python which displays the centroid of the dataset.

## Getting Started

To clone this repository, run the following in a terminal
```bash
git clone git@github.com:SarthKale/KMeans-Algorithm.git
cd KMeans-Algorithm
```

### Run unittests

Run python unittests.

```bash
python3 -m unittest tests/test_Kmeans.py
```

## Run Application

This application takes a user_feature_map dictionary, mapping each user "uid_i" to a respective list of features associated with the user in question. This application use the k-means algorithm to return the `k` means(for centroids) for the provided user features.

Note: These user features are the result of a dimensionality reduction by PCA on some user-app interaction data. Here, we have direct access to this data.

Make sure you have python3.9 installed on your system.

```bash
python3 src/solution.py
```

## Tech Stack

* **Programming Language : Python 3.8**
* **Version Control : Git**

## Author

Sarthak Kale
