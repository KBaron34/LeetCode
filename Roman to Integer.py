def romanToInt(self, s: str) -> int:
    result = 0
    integers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(s)):
        if i + 1 < len(s) and integers[s[i]] < integers[s[i+1]]:
            result -= integers[s[i]]
        else:
            result += integers[s[i]]
    return result
