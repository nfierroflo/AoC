import os

def compute_distance(list1, list2):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    distance = sum(abs(x - y) for x, y in zip(sorted_list1, sorted_list2))
    return distance

def compute_similarity_score(list1, list2):
    dic1 = {}
    dic2 = {}
    score = 0

    for i in range(len(list1)):
        dic1[list1[i]] = dic1.get(list1[i], 0) + 1
        dic2[list2[i]] = dic2.get(list2[i], 0) + 1

    for key in dic1:
        if key in dic2:
            score += dic1[key] * dic2[key] * key

    return score

def text_2_list(text):
    with open(text, 'r') as file:
        lines = file.readlines()
        #split lines with the space
        list1 = []
        list2 = []
        for line in lines:
            list1.append(int(line.split()[0]))
            list2.append(int(line.split()[1]))
        return list1, list2

if __name__ == "__main__":
    l1_test=[3,4,2,1,3,3]
    l2_test=[4,3,5,3,9,3]

    assert compute_distance(l1_test, l2_test) == 11
    assert compute_similarity_score(l1_test, l2_test) == 31

    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "input.txt")
    list1, list2 = text_2_list(input_file)

    distance = compute_distance(list1, list2)
    similarity_score = compute_similarity_score(list1, list2)
    print("Day 1")
    print(f"Part 1: {distance}")
    print(f"Part 2: {similarity_score}")


        





