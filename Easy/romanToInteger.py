class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
        "I" : 1 ,
        "V" : 5 ,
        "X" : 10 ,
        "L" : 50 ,
        "C" : 100 ,
        "D" : 500 ,
        "M" : 1000}
        num = 0
        n = len(s)
        for i in range(n):
            if i < n - 1 and values[s[i]] < values[s[i+1]]:
                num -= values[s[i]]
            else:
                num += values[s[i]]
        return num

