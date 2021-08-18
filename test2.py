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
    print(inital_centroid_users)
    old_centroid_values = list(
        map(lambda x: user_feature_map[x], inital_centroid_users))
    print(old_centroid_values)
    if k < 1 or k > len(user_feature_map):
        return []
    new_centroids = []
    count = 0
    while new_centroids != old_centroid_values or count < 10:
        cluster_list = []
        for point in user_feature_map:
            min_distance = -1
            for key in old_centroid_values:
                dist = calculate_distance(
                    key, user_feature_map[point])
                if min_distance == -1:
                    min_distance = dist
                    cluster_list.append(key)
                elif min_distance > dist:
                    min_distance = dist
                    cluster_list[-1] = key
        # calculating new mean
        for x in old_centroid_values:
            tmp = []
            for i in range(len(cluster_list)):
                if x == cluster_list[i]:
                    s = "uid_" + str(i)
                    tmp.append(user_feature_map[s])
            lst = []
            for i in range(num_features_per_user):
                total = 0
                for j in tmp:
                    total += j[i]
                lst.append(total/len(tmp))
            new_centroids.append(lst)
        print("New Centroid : ", new_centroids)
        if old_centroid_values != new_centroids:
            old_centroid_values.clear()
            old_centroid_values = new_centroids.copy()
            new_centroids.clear()
        print("Count :", count)
        count += 1
    for centroid in new_centroids:
        centroid = list(map(lambda x: round(x, 4), centroid)).copy()
    print("New Centroid : ", list(
        map(list, (set(map(lambda x: tuple(sorted(x)), new_centroids))))))
    return new_centroids


def calculate_distance(mean, point):
    if len(mean) != len(point):
        return 0
    total = 0
    for i in range(len(mean)):
        total += abs(mean[i] - point[i])
    return total


dt = {"uid_0": [-1.479359467505669, -1.895497044385029, -2.0461402601759096, -1.7109256402185178],
      'uid_1': [-1.8284426855307128, -1.714098142408679, -0.9893682669649455, -1.5766569391907947],
      "uid_2": [-1.8398933218386004, -1.7896757009107565, -1.1370177175666063, -1.0218512556903283],
      "uid_3": [-1.23224975874512, -1.8447858273094768, -1.8496517744301924, -2.4720755654344186],
      "uid_4": [-1.7714737791268318, -1.2725603446513774, -1.5512094954034525, -1.2589442628984848]}
get_k_means(dt, 4, 1)


# Task : k = 3 me issue h
