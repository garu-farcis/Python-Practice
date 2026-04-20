"""Tuples

Tuple with Most Frequent Element
Given a list of tuples:
data = [(1, 2, 2), (3, 2, 4), (1, 2, 3), (2, 2, 2), (5, 6, 2)]
Find the tuple that contains the most frequent element across all tuples (count occurrences across the entire list of tuples).
Sort List of Tuples by Multiple Criteria
Given:
students = [('Alice', 85, 92), ('Bob', 92, 85), ('Charlie', 85, 88), ('David', 78, 95)]
Sort the list first by score1 (descending), then by score2 (descending) if the first scores are equal."""
data = [(1, 2, 2), (3, 2, 4), (1, 2, 3), (2, 2, 2), (5, 6, 2)]
L =sorted(data)
print(L)

flat_t = [j for m in data for j in m]
print(flat_t)
freq={}
for item in data:
    for i in item:
        freq[i]=freq.get(i,0)+1

ans = max(freq, key=freq.get)
print(ans)

students = [('Alice', 85, 92), ('Bob', 92, 85), ('Charlie', 85, 88), ('David', 78, 95)]
sorted_students = sorted(students, key=lambda x: (x[1], x[2]), reverse=True)
print(sorted_students)
