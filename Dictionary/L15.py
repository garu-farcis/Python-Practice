"""Create a nested dictionary comprehension that produces:

Python
{
    1: [1],
    2: [1, 2],
    3: [1, 2, 3],
    ...
    5: [1, 2, 3, 4, 5]
}
(keys from 1 to 5, values = list of numbers from 1 to the key)."""
my_dict={k:[v for v in range(1,k+1)] for k in range(1,6) }
print(my_dict)

