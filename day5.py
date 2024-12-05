import re
from collections import defaultdict
from functools import cmp_to_key

rule_patern = "([0-9]{1,2})\|([0-9]{1,2})"
update_pattern = "(?<=\s)[0-9]{1,2},.*(?=\s)"

def test_update_validity(update, rules):
    for idx, page in enumerate(update):
        if page in rules:
            for rule_number in rules[page]:
              try:
                  rule_num_idx = update.index(rule_number)
              except ValueError:
                  rule_num_idx = -1
              if rule_num_idx > -1 and rule_num_idx < idx:
                  return False
    return True

with open('day5.txt') as prompt:
    rules_and_updates = prompt.read()

rules = defaultdict(set)
for rule in re.findall(rule_patern, rules_and_updates):
    rules[int(rule[0])].add(int(rule[1]))

def page_cmp(a, b):
    if a in rules and b in rules[a]:
        return -1
    elif b in rules and a in rules[b]:
        return 1
    return 0

page_cmp_key = cmp_to_key(page_cmp)

valid_update_middle_total = 0
invalid_update_middle_total = 0

updates = [list(map(int, update)) for update in [update.split(',') for update in re.findall(update_pattern, rules_and_updates)]]
for update in updates:
    if test_update_validity(update, rules):
        valid_update_middle_total += update[len(update) // 2]
    else:
        update.sort(key=page_cmp_key)
        invalid_update_middle_total += update[len(update) // 2]

print("part 1:", valid_update_middle_total)
print("part 2:", invalid_update_middle_total)

