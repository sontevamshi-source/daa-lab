# 1.Linear Search Algorithm Implementation in Python
import time

# Linear Search Function
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

# Start Time
start = time.time()

# Perform Search
result = linear_search(arr, key)

# End Time
end = time.time()

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")

# Execution Time
print("Execution Time:", end - start, "seconds")

# Complexity
print("\nTime Complexity")
print("Best Case    : O(1)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")
print("Space Complexity : O(1)")

# 2. binary search algorithm implementation in Python

import time

# Linear Search Function
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# User Input
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

key = int(input("Enter the element to search: "))

# Start Timer
start_time = time.perf_counter()

# Call Linear Search
index = linear_search(arr, key)

# End Timer
end_time = time.perf_counter()

# Display Result
if index != -1:
    print(f"\nElement {key} found at index {index}.")
else:
    print(f"\nElement {key} not found.")

# Execution Time
execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time:.10f} seconds")

# Time Complexity
print("\nTime Complexity:")
print("Best Case    : O(1)  - Element found at the first position.")
print("Average Case : O(n)  - Element found in the middle of the list.")
print("Worst Case   : O(n)  - Element found at the last position or not found.")

# Space Complexity
print("\nSpace Complexity:")
print("O(1) - Constant space.")
