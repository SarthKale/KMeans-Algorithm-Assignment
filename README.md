# KMeans-Algorithm-Assignment
Implementation of K-Means algorithm using python which displays the centroids for the dataset.

## Requirements

* Python3

## Getting Started

To clone this repository, run the following in a terminal
```bash
git clone https://github.com/SarthKale/KMeans-Algorithm-Assignment.git
cd KMeans-Algorithm-Assignment 
```

### Run unittests

```bash
python3 -m unittest tests/test_kmeans_algorithm_assignment.py
```

## Run Application

This application takes a `user_feature_map` python dictionary, mapping each user `"uid_i"` to a respective list of features associated with the user in question. This application uses the k-means algorithm to return the `k` means(or centroids) for the provided user features.

Note: These user features are the result of a dimensionality reduction by Principal Component Analysis on some user-app interaction data. Here, we have direct access to this data.

```bash
python3 src/kmeans_algorithm_assignment.py <input> <k_value>
```

**Example**
```bash
python3 src/kmeans_algorithm_assignment.py ./data/in.json 1
```

## Tech Stack

* Programming Language : Python3
* Python Code Formatter : autopep8

## Author

Sarthak Kale
