import array as arr

# arr = [1, 2, 3, 2, 4, 3, 5]
# hasil_array = []
# for element in arr:
#     if element not in hasil_array:
#         hasil_array.append(element)

# print(hasil_array)        

arr = [1, 2, 3, 4, 2, 3, 2, 5]
elemen_dicari = 2
banyak_elemen_dicari = arr.count(elemen_dicari)
print(f"Elemen {elemen_dicari} muncul sebanyak {banyak_elemen_dicari} kali dalam list ini")