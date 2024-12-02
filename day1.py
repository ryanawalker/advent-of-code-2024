with open('day1.txt') as prompt:
    lines = prompt.read().splitlines()
location_list_1, location_list_2 = [], []
for line in lines:
    location_list_1.append(int(line.split(' ')[0]))
    location_list_2.append(int(line.split(' ')[3]))
location_list_1.sort()
location_list_2.sort()
total_distance, similarity_score = 0, 0
appearance_counts = {location_id: location_list_2.count(location_id) for location_id in set(location_list_2)}
for i in range(len(location_list_1)):
    total_distance += abs(max(location_list_1[i], location_list_2[i]) - min(location_list_1[i], location_list_2[i]))
    similarity_score += location_list_1[i] * appearance_counts[location_list_1[i]] if location_list_1[i] in appearance_counts else 0
print(total_distance)
print(similarity_score)
