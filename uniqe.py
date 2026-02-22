def count_unique_chars(s):
    result = {}
    for char in s:            
        if char in result:    
            result[char]+=1
        else:                 
            result[char]=1
    return result
print(count_unique_chars('aabbbsb'))