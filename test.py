from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Menangani kasus di mana daftar string kosong.
        # Jika tidak ada string, tidak ada prefix umum.
        if not strs: # atau if len(strs) == 0:
            return ""

        # Menginisialisasi 'prefix' dengan string pertama.
        # Kita berasumsi string pertama adalah kandidat awal untuk prefix umum terpanjang.
        prefix = strs[0]

        # Iterasi melalui string-string yang tersisa di daftar, mulai dari indeks 1.
        for i in range(1, len(strs)):
            current_string = strs[i]
            
            # Loop 'while' ini akan berjalan selama 'prefix' BUKAN merupakan awalan dari 'current_string'.
            # strs[i].find(prefix) akan mengembalikan 0 jika 'prefix' ditemukan di awal 'strs[i]'.
            # Jika mengembalikan nilai lain (misalnya -1 jika tidak ditemukan, atau >0 jika ditemukan di tengah),
            # itu berarti 'prefix' saat ini bukan awalan yang valid.
            while current_string.find(prefix) != 0:
                # Jika 'prefix' bukan awalan, kita perpendek 'prefix' dari belakang satu karakter.
                prefix = prefix[0 : len(prefix) - 1]
                
                # Jika 'prefix' menjadi string kosong setelah diperpendek,
                # itu berarti tidak ada prefix umum sama sekali di antara string-string yang dibandingkan sejauh ini.
                # Jadi, kita bisa langsung mengembalikan string kosong.
                if not prefix: # atau if prefix == "":
                    return ""
        
        # Setelah loop selesai, 'prefix' akan berisi prefix umum terpanjang
        # yang cocok dengan semua string dalam daftar.
        return prefix

# --- Contoh Penggunaan ---

# Inisialisasi objek Solution
sol = Solution()

# Contoh 1: Ada prefix umum
strs1 = ["flower", "flow", "flight"]
print(f"Input: {strs1}")
print(f"Longest Common Prefix: '{sol.longestCommonPrefix(strs1)}'\n") # Output: "fl"

# Contoh 2: Tidak ada prefix umum
strs2 = ["dog", "racecar", "car"]
print(f"Input: {strs2}")
print(f"Longest Common Prefix: '{sol.longestCommonPrefix(strs2)}'\n") # Output: ""

# Contoh 3: Daftar kosong
strs3 = []
print(f"Input: {strs3}")
print(f"Longest Common Prefix: '{sol.longestCommonPrefix(strs3)}'\n") # Output: ""

# Contoh 4: Hanya satu string
strs4 = ["apple"]
print(f"Input: {strs4}")
print(f"Longest Common Prefix: '{sol.longestCommonPrefix(strs4)}'\n") # Output: "apple"

# Contoh 5: Prefix umum adalah satu karakter
strs5 = ["apple", "apricot", "apex"]
print(f"Input: {strs5}")
print(f"Longest Common Prefix: '{sol.longestCommonPrefix(strs5)}'\n") # Output: "ap"

# Contoh 6: Semua string sama
strs6 = ["banana", "banana", "banana"]
print(f"Input: {strs6}")
print(f"Longest Common Prefix: '{sol.longestCommonPrefix(strs6)}'\n") # Output: "banana"