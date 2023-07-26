Assignment 1:

Given a string s and a number x, print the shortest substrings which start and end with the same character and have lengths greater than or equal to x. If multiple substrings exist with the same shortest length, print them all.

def short_substrings(s, x):
    result = []
    for i in range(len(s)):
        for j in range(i + x, len(s) + 1):
            substr = s[i:j]
            if substr[0] == substr[-1] and len(substr) >= x:
                if not result or len(substr) < len(result[0]):
                    result = [substr]
                elif len(substr) == len(result[0]):
                    result.append(substr)
    return result


s = "abccdbacca"
x = 3
res = short_substrings(s, x)
print(res)



Assignment 2:

Given a string s, find the ASCII value of each character iteratively. If the ASCII value is even, increment the next character by (ASCII_value % 7). If the ascii value is odd, decrement the previous character by (ASCII_value % 5). Output the newly formed string. 
Note:
If a character has already been changed once, do not change that character again. 
If the new number is an invalid ASCII value, replace it with 83. 

def mod_str(s):
    new_str = []
    modified = [False] * len(s)

    for i, char in enumerate(s):
        ascii_val = ord(char)

        if ascii_val % 2 == 0:
            next_char_val = ascii_val + (ascii_val % 7)
            if next_char_val > 127:
                next_char_val = 83
            new_str.append(chr(next_char_val))
            if i < len(s) - 1:
                modified[i + 1] = True
        else:
            if i > 0 and not modified[i - 1]: 
                prev_char_val = ascii_val - (ascii_val % 5)
                if prev_char_val < 0:
                    prev_char_val = 83
                new_str[-1] = chr(prev_char_val)
                modified[i - 1] = True
            else:
                new_str.append(char)

    return ''.join(new_str)

s = "sHQen}"
res = mod_str(s)
print("output:", res)


