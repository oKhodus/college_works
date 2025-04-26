def compute_hash(string, base=256, prime_number=101):

    # initialize the hash value to 0
    hash_value = 0

    # iterate over each character in the string
    for i in range(len(string)):
        # get the ASCII value using ord(char)
        ascii_value = ord(string[i])
        # calculate the exponent for each character
        hash_value = (hash_value * base + ascii_value) % prime_number
        # calculate the term for the current character
    return hash_value
        # update the hash value



def rabin_karp(text, pattern, base = 256, prime = 101):
    n = len(text)
    m = len(pattern)
    
 
    # hash of the pattern text (substring)

    
    # hash of a substring that has the same length as the pattern

    
    # initialize a list to store occurrences of the pattern in text
    if m > n:
        return []
    
    # pre-compute the highest power of base
    # this is needed to update the hash for the next substring

    pattern_hash = compute_hash(pattern, base, prime)
    current_hash = compute_hash(text[:m], base, prime)
    occurrences = []
    # base^(m-1) % prime
    h = pow(base, m - 1, prime)
    # loop through all possible substrings of text with pattern length
    for i in range(n - m + 1):
        if current_hash == pattern_hash:
            if text[i:i + m] == pattern:
                occurrences.append(i)
        
        # compare hash of substring and pattern
        if i < n - m:
            current_hash = (
                (current_hash - ord(text[i]) * h) * base + ord(text[i + m])
            ) % prime
            current_hash = (current_hash + prime) % prime  # ensure positive

    return occurrences
            
            # double check to confirm match

                
        # update the hash of the next substring using the previous hash
        
            
            # update the rolling hash for the next substring
            # remove first character's hash and add next character's hash-based

 
# example usage
text = "CODEWITHCODER"
pattern = input()
occurrences = rabin_karp(text, pattern)
if occurrences:
    print(f"The pattern found at indices: {occurrences}.")
else:
    print(f"The pattern is not present in the text.")