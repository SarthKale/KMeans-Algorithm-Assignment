import random


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
        print([])
        return []
    centroid_values = list(user_feature_map[value]
                           for value in inital_centroid_users)
    dataset = create_dataset(user_feature_map)
    old_centroids = centroid_values.copy()
    for i in range(100):
        distance = []
        for row in dataset:
            tmp = []
            for centroid in centroid_values:
                tmp.append(calculate_distance(row, centroid))
            distance.append(tmp)
        if len(centroid_values) > 1:
            classes = []
            for row in distance:
                classes.append(row.index(min(*row)))
            centroid_values = calculate_mean(dataset, centroid_values, classes)
        else:
            centroid_values = calculate_mean(dataset, centroid_values)
        if centroid_values == old_centroids and i > 10:
            break
        else:
            old_centroids = centroid_values
    centroid_values = [[round(value, 3) for value in centroid]
                       for centroid in centroid_values]
    print("\nRounded Centroids :", centroid_values)
    return centroid_values


def calculate_mean(dataset, centroids, classes=None):
    new_mean = []
    if len(centroids) == 1:
        tmp = []
        for index in range(len(dataset[0])):
            total = 0
            for row in dataset:
                total += row[index]
            tmp.append(total/len(dataset[0]))
        new_mean.append(tmp)
    else:
        collections = []
        for i in range(len(centroids)):
            tmp = []
            for j in range(len(classes)):
                if i == classes[j]:
                    tmp.append(dataset[j])
            collections.append(tmp)
        for collection in collections:
            tmp = []
            for index in range(len(dataset[0])):
                total = 0
                for row in collection:
                    total += row[index]
                tmp.append(total/len(dataset[0]))
            new_mean.append(tmp)

    print("\nNew Mean :", new_mean)
    return new_mean


def create_dataset(data):
    dataset = []
    for value in data.values():
        dataset.append(value)
    return dataset


def calculate_distance(point, mean):
    if len(mean) != len(point):
        return 0
    return sum(abs(m - p) for m, p in zip(mean, point))


dt = {"uid_0": [-1.479359467505669, -1.895497044385029, -2.0461402601759096, -1.7109256402185178],
      'uid_1': [-1.8284426855307128, -1.714098142408679, -0.9893682669649455, -1.5766569391907947],
      "uid_2": [-1.8398933218386004, -1.7896757009107565, -1.1370177175666063, -1.0218512556903283],
      "uid_3": [-1.23224975874512, -1.8447858273094768, -1.8496517744301924, -2.4720755654344186],
      "uid_4": [-1.7714737791268318, -1.2725603446513774, -1.5512094954034525, -1.2589442628984848]}

get_k_means(dt, 4, 1)
