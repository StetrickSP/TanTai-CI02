def counting_sort(arr):
    if not arr:
        return arr  # Handle empty input

    # Find the range of the array (minimum and maximum values)
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Step 1: Create and populate the count array
    count = [0] * range_of_elements
    for num in arr:
        count[num - min_val] += 1

    # Step 2: Update the count array with cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 3: Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):  # Traverse in reverse to maintain stability
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# Example usage
array = [5,9,-1,12,30,35,-75,10,15]
sorted_array = counting_sort(array)
print(sorted_array)  # Output: []

def counting_sort1(arr:list):
    if len(arr) <= 1:
        return
    
    max_val = max(arr)

    count = [0] * (max_val+1)
    for el in arr:
        count[el] += 1

    index = 0
    for i in range(max_val+1):
        for j in range(count[i]):
            arr[index] = i
            index += 1

