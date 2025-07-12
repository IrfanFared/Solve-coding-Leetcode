def roman_to_int(s: str) -> int:
    """
    Mengonversi angka Romawi ke bilangan bulat.

    Args:
        s: String yang merepresentasikan angka Romawi.

    Returns:
        Representasi bilangan bulat dari angka Romawi.
    """
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

    # Iterasi melalui string angka Romawi
    for i in range(n):
        current_value = roman_map[s[i]]

        # Memeriksa kasus pengurangan (subtractive cases)
        # Jika nilai saat ini lebih kecil dari nilai berikutnya, kurangkan.
        # Contoh: IV = 5 - 1 = 4, IX = 10 - 1 = 9
        if i + 1 < n and current_value < roman_map[s[i+1]]:
            total -= current_value
        else:
            # Jika tidak, tambahkan nilai saat ini ke total.
            total += current_value
    return total

print(roman_to_int("IV"))