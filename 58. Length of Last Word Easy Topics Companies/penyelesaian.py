def lengthOfLastWord(s):
    """
    Mengembalikan panjang kata terakhir dalam string s.
    
    Args:
        s (str): String yang terdiri dari kata-kata dan spasi
        
    Returns:
        int: Panjang kata terakhir
    """
    
    # Metode 1: Menggunakan split() - Paling sederhana
    words = s.split()
    if words:
        return len(words[-1])
    return 0

def lengthOfLastWord_v2(s):
    """
    Metode 2: Menggunakan strip() dan split()
    """
    return len(s.strip().split()[-1]) if s.strip() else 0

def lengthOfLastWord_v3(s):
    """
    Metode 3: Iterasi dari belakang (lebih efisien untuk string panjang)
    """
    # Hapus spasi di akhir string
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    
    # Hitung panjang kata terakhir
    length = 0
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    
    return length

# Test cases
def test_solutions():
    test_cases = [
        "Hello World",      # Expected: 5
        "   fly me   to   the moon  ",  # Expected: 4
        "luffy is still joyboy",  # Expected: 6
        "a",                # Expected: 1
        " ",                # Expected: 0
        "hello",            # Expected: 5
    ]
    
    print("Testing all solutions:")
    print("-" * 50)
    
    for i, test in enumerate(test_cases, 1):
        result1 = lengthOfLastWord(test)
        result2 = lengthOfLastWord_v2(test)
        result3 = lengthOfLastWord_v3(test)
        
        print(f"Test {i}: '{test}'")
        print(f"  Method 1 (split): {result1}")
        print(f"  Method 2 (strip+split): {result2}")
        print(f"  Method 3 (backward iteration): {result3}")
        print()

# Jalankan test
if __name__ == "__main__":
    test_solutions()
    
    # Contoh penggunaan sesuai soal
    print("Contoh dari soal:")
    s = "Hello World"
    result = lengthOfLastWord(s)
    print(f"Input: '{s}'")
    print(f"Output: {result}")
    print(f"Explanation: Kata terakhir adalah 'World' dengan panjang {result}.")