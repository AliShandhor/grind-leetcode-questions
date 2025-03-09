# Hashing Appraoch - Using hash set
# Time complexity: O(n) - Space Complexity: O(n)
def longestConsecutive(numbers: list) -> int:
    numbers_set = set(numbers)
    longest_sequence_length = 0
    
    # need to check if we have a starting point first to increametn lenght and remove the sequtive numbers of starting point from the set
    for number in numbers:
        # Check if element is the starting point - item (x) does not have x - 1
        if number in numbers_set and number - 1 not in numbers_set:
            current_value_in_seq = number
            current_length = 0
            # while number in the hash set, we keep adding by 1.
            while current_value_in_seq in numbers_set:
                numbers_set.remove(current_value_in_seq)
                current_value_in_seq += 1
                current_length += 1
        longest_sequence_length = max(longest_sequence_length, current_length)
    return longest_sequence_length

# Example usage
if __name__ == "__main__":
    numbers = [1,100, 3, 200,2, 100, 200, 4]
    print(longestConsecutive(numbers)) 
