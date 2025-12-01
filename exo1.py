def test_distinct(sequence):
    return len(sequence) == len(set(sequence))

print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))
