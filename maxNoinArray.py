arr = [10, 324, 45, 90, 9808]
n = len(arr)

max = arr[0]  # Initialize max to the first element of the array

for i in range(1, n):
    if arr[i] > max:
        max = arr[i]

print("Largest in given array ", max)
