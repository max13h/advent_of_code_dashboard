import re

with open("input.txt") as f: s = f.read()

l = re.findall(r"mul\(\d*,\d*\)", s)
total = 0
for el in l:
    match = re.search(r"mul\((\d+),(\d+)\)", el)

    if match:
        num1, num2 = match.groups()
        total += int(num1) * int(num2)
    else:
        raise Exception()

print(total)