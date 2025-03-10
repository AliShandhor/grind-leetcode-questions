def two_sum(nums, target):
    num_map = {}  # Dictionary to store number and its index
    for i in range(len(nums)):  # Using a regular for loop
        complement = target - nums[i]
        if complement in num_map:
            return [num_map[complement], i]  # Return indices of the two numbers
        num_map[nums[i]] = i  # Store the index of the current number
    return []  # Return empty list if no solution