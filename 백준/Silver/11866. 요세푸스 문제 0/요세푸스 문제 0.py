def josephus_permutation(N, K):
    # Initialize the list of people
    people = list(range(1, N + 1))
    
    # This will store the Josephus permutation
    result = []
    
    # Start position for removal
    index = 0
    
    # Continue until all people are removed
    while people:
        # Find the index of the next person to remove
        index = (index + K - 1) % len(people)
        # Append the person to the result
        result.append(people.pop(index))
    
    # Format the result as required
    result_str = '<' + ', '.join(map(str, result)) + '>'
    return result_str

# Example usage:
N, K = map(int, input().split())
print(josephus_permutation(N, K))
