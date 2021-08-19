import random
import sys
import json


class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()


def get_k_means(user_feature_map, num_features_per_user, k):
    # Don't change the following two lines of code.
    random.seed(42)
    # Gets the inital users, to be used as centroids.
    inital_centroid_users = random.sample(
        sorted(list(user_feature_map.keys())), k)

    # Write your code here.
    if k < 1:
        return []
    # Creating the list of Centroid class objects and
    # a value point specific dataset.
    centroid_values = [Centroid(user_feature_map[value])
                       for value in inital_centroid_users]
    dataset = create_dataset(user_feature_map)
    old_centroids = centroid_values.copy()
    # Iterate over centroid values, with max iterations = 100.
    for i in range(100):
        # calculating the distance of points from centroids.
        distance = []
        for row in dataset:
            tmp = []
            for centroid in centroid_values:
                tmp.append(calculate_distance(row, centroid.location))
            distance.append(tmp)
        # Updating centroid values(location).
        if len(centroid_values) > 1:
            # Allocating clustters.
            classes = []
            for row in distance:
                classes.append(row.index(min(*row)))
            # Calculating mean values.
            centroid_values = calculate_mean(dataset, centroid_values, classes)
        else:
            # Calculating mean values.
            centroid_values = calculate_mean(dataset, centroid_values)
        if centroid_values == old_centroids and i > 10:
            # Old and new centroid values matched and
            # a total of 10 iterations is complete.
            break
        else:
            # Allocating new unmatched centroid values as old centroid values.
            old_centroids = centroid_values
    # Rounding the output values to fourth decimal.
    centroid_values = [[round(value, 3) for value in centroid.location]
                       for centroid in centroid_values]
    return centroid_values


def calculate_mean(dataset, centroids, classes=None):
    new_mean = []
    if len(centroids) == 1:
        tmp = []
        for index in range(len(dataset[0])):
            total = 0
            for row in dataset:
                total += row[index]
            tmp.append(total/len(dataset))
        centroids[0].location = tmp
        new_mean.append(*centroids)
    else:
        for centroid in centroids:
            centroid.closest_users.clear()
        for i in range(len(centroids)):
            for j in range(len(classes)):
                if i == classes[j]:
                    centroids[i].closest_users.add(tuple(dataset[j]))
        for centroid in centroids:
            tmp = []
            for index in range(len(dataset[0])):
                total = 0
                for row in centroid.closest_users:
                    total += row[index]
                tmp.append(total/len(centroid.closest_users))
            centroid.location = tmp
            new_mean.append(centroid)
    return new_mean


def create_dataset(data):
    dataset = []
    for value in data.values():
        dataset.append(value)
    return dataset


def calculate_distance(point, mean):
    # Applying Manhattan distance matric.
    if len(mean) != len(point):
        return 0
    return sum(abs(m - p) for m, p in zip(mean, point))


if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) != 3:
        print("Usage: python3 src/kmeans_algorithm_assignment.py <input> <k_value>")
        sys.exit(1)
    file_name = arguments[1]
    with open(file_name, mode="r") as file:
        data = json.load(file)
    features = len(list(data.values())[0])
    k = int(arguments[2])
    print(get_k_means(data, features, k))
