"""Program 6.8: Find Mean, Variance and Standard Deviation of List Numbers
1. import math
2. def statistics(list_items):
3. mean = sum(list_items)/len(list_items)
4. print(f"Mean is {mean}")
5. variance = 0
6. for item in list_items:
7. variance += (item-mean)**2
8. variance /= len(list_items)
9. print(f"Variance is {variance}")
10. standard_deviation = math.sqrt(variance)
11. print(f"Standard Deviation is {standard_deviation}")
12. def main():
13. statistics([1, 2, 3, 4])
14. if __name__ == "__main__":
15. main()




Program 6.4: Write Python Program to Sort Numbers in a List in Ascending Order
Using Bubble Sort by Passing the List as an Argument to the Function Call
1. def bubble_sort(list_items):
2. for i in range(len(list_items)):
3. for j in range(len(list_items)-i-1):
4. if list_items[j] > list_items[j+1]:
5. temp = list_items[j]
6. list_items[j] = list_items[j+1]
7. list_items[j+1] = temp
8. print(f"The sorted list using Bubble Sort is {list_items}")
9. def main():
10. items_to_sort = [5, 4, 3, 2, 1]
11. bubble_sort(items_to_sort)
12. if __name__ == "__main__":
13. main()"""