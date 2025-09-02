def find_maximum(numbers):
    """Return the largest number from a list without using max()."""
    if not numbers:  # check if list is empty
        return None
    
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


# Example usage:
print(find_maximum([3, 7, 2, 9, 5]))   # Output: 9
print(find_maximum([-10, -3, -50, -2])) # Output: -2

