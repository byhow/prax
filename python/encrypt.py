def lexical_palindrome(password: str):
    char_map = [0] * 26
    for c in password:
        char_map[ord(c) - ord("a")] += 1

    res = ""
    mid_char = ""
    for i in range(26):
        if char_map[i] != 0:
            char = chr(i + ord("a"))
            res += char_map[i] // 2 * char
            if char_map[i] % 2 != 0:
                mid_char = char

    if mid_char:
        return res + mid_char + res[::-1]
    else:
        return res + res[::-1]


print(lexical_palindrome(password="baabaab"))
print(lexical_palindrome(password="aba"))
print(lexical_palindrome(password="babab"))
print(lexical_palindrome(password="xzxyxzx"))
