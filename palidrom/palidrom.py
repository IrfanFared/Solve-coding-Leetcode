def solusi(nilai: int)-> bool:
    if nilai < 0:
        return False

    nilai_toString = str(nilai)
    balik_huruf = nilai_toString[::-1]

    # Perbaikan ada di baris ini:
    return nilai_toString == balik_huruf # Bandingkan string dengan string

p = solusi(121)
print(p)