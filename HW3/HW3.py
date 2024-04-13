from itertools import combinations

def find_combinations(items, max_weight):
    valid_combinations = []
    for i in range(1, len(items) + 1):
        for combo_indices in combinations(range(len(items)), i):
            combo_weight = sum(items[index][1] for index in combo_indices)
            if combo_weight <= max_weight:
                valid_combinations.append([items[index] for index in combo_indices])
    return valid_combinations

items = [
    ('палатка', 2),
    ('спальный мешок', 1),
    ('еда', 3),
    ('вода', 2),
    ('карта', 0.5),
    ('фонарик', 0.3)
]

max_weight = 5

valid_combinations = find_combinations(items, max_weight)

for combination in valid_combinations:
    print(combination)
