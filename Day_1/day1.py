# Day 1: Historian Hysteria

file_path = 'input.txt'


with open(file_path, 'r') as file:
    lines = file.readlines()

left_list = []
right_list = []


for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()

# total distance
total_dis = sum(abs(l - r) for l, r in zip(left_list, right_list))

print(total_dis)
