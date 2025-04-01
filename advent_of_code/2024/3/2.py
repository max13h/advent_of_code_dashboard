import re

with open("input.txt") as f: s = f.read()

l = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", s)
total = 0
current_instruction = ""

def add(exp: str):
    global total
    match = re.search(r"mul\((\d+),(\d+)\)", exp)

    if match:
        num1, num2 = match.groups()
        total += int(num1) * int(num2)
    else:
        raise Exception()

for el in l:
    current_instruction = el if el in {"do()", "don't()"} else current_instruction
    if not el.startswith("mul"): continue

    if current_instruction != "don't()":
        print(f"{current_instruction}: {el} - {total}")
        add(el)

print(total)


