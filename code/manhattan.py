users = {
        "zhangsan": {"a": 4, "b": 5, "c": 7},
        "lisi": {"a": 1, "b": 4, "c": 3},
        "wanger": {"a": 2, "b": 3, "c": 5}
}


def manhattan(ratinga, ratingb):
    distance = 0
    for k in ratinga:
        if k in ratingb:
            distance += abs(ratinga[k] - ratingb[k])
    return distance


def computerNearestNeighbor(username, users):
    distance = []
    for user in users:
        if user != username:
            distance.append((user, manhattan(users[username], users[user])))
    distance.sort()
    print distance


if __name__ == "__main__":
    computerNearestNeighbor("zhangsan", users)
