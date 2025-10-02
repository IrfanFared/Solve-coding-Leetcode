class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 1. Gabungkan dan Urutkan List (Ini KUNCI untuk Median)
        merge_list = nums1 + nums2
        merge_list.sort() # Harus diurutkan!
        
        n = len(merge_list)
        
        # 2. Cek Kasus: Panjang List Ganjil atau Genap
        if n % 2 == 1:
            # Kasus Ganjil: Median adalah nilai di indeks tengah
            # Contoh: [1, 2, 3], n=3. Indeks tengah: 3 // 2 = 1. Nilai = 2.
            median_index = n // 2
            result = merge_list[median_index]
        else:
            # Kasus Genap: Median adalah rata-rata dari dua nilai tengah
            # Contoh: [1, 2, 3, 4], n=4. 
            # Indeks Tengah Kiri: 4 // 2 - 1 = 1. Nilai = 2.
            # Indeks Tengah Kanan: 4 // 2 = 2. Nilai = 3.
            
            middle_right_index = n // 2
            middle_left_index = middle_right_index - 1
            
            nilai_kiri = merge_list[middle_left_index]
            nilai_kanan = merge_list[middle_right_index]
            
            result = (nilai_kiri + nilai_kanan) / 2.0 # Pembagian float untuk hasil akurat
            
        return result

# Uji Kode
solusi = Solution()

# Kasus Ganjil: [1, 3] + [2] -> [1, 2, 3]. Median: 2.0
print(f"Hasil untuk ([1,3],[2]): {solusi.findMedianSortedArrays([1,3],[2])}") 

# Kasus Genap: [1, 2] + [3, 4] -> [1, 2, 3, 4]. Median: (2+3)/2 = 2.5
print(f"Hasil untuk ([1,2],[3,4]): {solusi.findMedianSortedArrays([1,2],[3,4])}")