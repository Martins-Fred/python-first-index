
def first_index(sequence, item):
    """Where an item first appears.

    Input:   sequence, a list or a string; item, anything.
    Output:  the position (counting from 0) of the first occurrence of item in
             sequence, or -1 if it does not occur.

        first_index(["a", "b", "a"], "a")  ->  0
        first_index(["a", "b", "a"], "z")  ->  -1
        first_index("banana", "n")         ->  2
    """
    position = -1
    for i in range(len(sequence)):
        if sequence[i] == item:
            return i
    return position


# Test my function
print(first_index(["a", "b", "a"], "a")) # 0
print(first_index(["a", "b", "a"], "z")) # -1
print(first_index("banana", "n")) # 2
print(first_index([], "a")) # -1
