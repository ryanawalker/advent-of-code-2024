import re

valid_mul_pattern = "(?<=mul\()[0-9]{1,3},[0-9]{1,3}(?=\))"
do_pattern = "do\(\)"
dont_pattern = "don't\(\)"

def find_valid_mul_total(prompt):
    total = 0
    for instruction in [(int(factors[0]), int(factors[1])) for factors in [instruction.split(',') for instruction in re.findall(valid_mul_pattern, prompt)]]:
        total += instruction[0] * instruction[1]
    return total

with open('day3.txt') as prompt:
    read_prompt = prompt.read()

pt1_total = find_valid_mul_total(read_prompt)
print("part 1:", pt1_total)

pt2_total = 0
split_at_dos = re.split(do_pattern, read_prompt)
for substr in split_at_dos:
    split_at_donts = re.split(dont_pattern, substr)
    pt2_total += find_valid_mul_total(split_at_donts[0])

print("part 2:", pt2_total)
