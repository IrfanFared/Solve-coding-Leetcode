def is_palindrome_int(n: int) -> bool:
    """
    Mengecek apakah sebuah bilangan bulat adalah palindrom.

    Args:
        n: Bilangan bulat yang akan dicek.

    Returns:
        True jika bilangan adalah palindrom, False jika tidak.
    """
    # Menangani kasus bilangan negatif (palindrom hanya untuk non-negatif)
    if n < 0:
        return False

    # 1. Ubah bilangan bulat menjadi string
    s = str(n)

    # 2. Balik string
    # Python memungkinkan pembalikan string dengan slicing [::-1]
    s_reversed = s[::-1]

    # 3. Bandingkan string asli dengan string yang dibalik
    return s == s_reversed

# Contoh penggunaan:
print(f"121 adalah palindrom? {is_palindrome_int(121)}")        # Output: 121 adalah palindrom? True
      # Output: -121 adalah palindrom? False (menurut definisi, palindrom biasanya non-negatif)