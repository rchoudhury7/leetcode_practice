def longest_substring_without_repeat(test_string):
    max_len = -1
    left = 0
    right = 1
    seen_chars = dict()
    s = test_string

    while(right < len(s)):
        if s[right] in seen_chars:
            left = seen_chars[s[right]]
            seen_chars[s[right]] = right
        else:
            seen_chars[s[right]] = right

        if right - left > max_len:
            max_len = right - left
        right += 1

    return max_len

if __name__ == '__main__':
    test = longest_substring_without_repeat
    assert(test("abcabcbb") == 3)
    assert(test("bbbb") == 1)
    assert(test("pwwkew") == 3)
    assert(test("au") == 2)
