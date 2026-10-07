# Cetak angka ganjil saja
for i in range(20):
    if i % 2 == 0: # habis dibagi 2 
        continue  # Lewati, lanjut angka berikut
    print(i)      # Hanya muncul angka ganjil
    # genap continue = dihiraukan/tidak dimunculkan