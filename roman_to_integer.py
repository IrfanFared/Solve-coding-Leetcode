class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
        total = 0
        n = len(s)
        for i in range(n):
            nilai_saat_ini = roman_map[s[i]]
            if  i + 1 < n and nilai_saat_ini < roman_map[s[i+1]]:
                total = total - nilai_saat_ini
            else:
                total = total + nilai_saat_ini
        return total
    
solusi1 = Solution()
print(solusi1.romanToInt("IV"))
