import array as arr

arr = [12, 45, 78, 23, 56, 91, 34]
arr_sorted = sorted(arr)
terkecil = arr_sorted[0]
terbesar = arr_sorted[-1]
print("Array diurutkan:", arr_sorted)
print("Elemen array terbesar:", terbesar)
print("Elemen array terkecil:",terkecil)

arr = [1, 2, 3, 2, 4, 3, 5]
arr_unique = list(set(arr))
print("Array setelah menghapus duplikat:", arr_unique)

from collections import Counter
arr = [1, 2, 3, 2, 4, 3, 2, 5]
frequency = Counter(arr)
print("Frekuensi kemunculan setiap angka dalam array ini adalah:", frequency)


arr = [1, 2, 3, 2, 4, 3, 5]

# Menghapus angka 2
arr_filtered = [x for x in arr if x != 2]

# Mengurutkan secara terbalik
arr_filtered.sort(reverse=True)

print("Array setelah menghapus angka 2 dan mengurutkannya secara terbalik adalah:", arr_filtered)


arr = [1, 2, 3, 4, 2, 3, 2, 5]
elemen_dicari = 2

# Menghitung frekuensi kemunculan elemen_dicari dalam array
jumlah = arr.count(elemen_dicari)

print(f"Elemen {elemen_dicari} muncul sebanyak {jumlah} kali dalam list ini")