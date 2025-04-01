import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r") as f:
    lines = f.readlines()

##### PART 1
### My version
# column1 = []
# column2 = []
# for line in lines:
#     numbers = list(map(int, line.split()))
#     column1.append(numbers[0])
#     column2.append(numbers[1])

# column1.sort()
# column2.sort()
# total = 0

# for index, number_col1 in enumerate(column1):
#     number_col2 = column2[index]

#     total += abs(number_col1 - number_col2)

# print(f"Total: {total}")

### AI version
# column1, column2 = zip(*[map(int, line.split()) for line in lines])
# total = sum(abs(a - b) for a, b in zip(sorted(column1), sorted(column2)))
# print(f"Total: {total}")


### PART 2
from collections import Counter

column1, column2_unsorted = zip(*[map(int, line.split()) for line in lines])
column2 = sorted(column2_unsorted)
total = 0

column2_count = Counter(column2)

for num_col1 in column1:
    appear_in_col2_total = column2_count[num_col1]
    total += num_col1 * appear_in_col2_total

print(f"End total: {total}")

