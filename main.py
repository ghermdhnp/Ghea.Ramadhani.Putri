import csv
FILENAME = 'keuangan_pribadi.csv'

def create_record(tanggal, jenis, jumlah, kategori):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, jenis, jumlah, kategori])

def read_records():
    records = []
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                records.append(row)
    except FileNotFoundError:
        pass
    return records

def update_record(index, tanggal, jenis, jumlah, kategori):
    records = read_records()
    if 0 <= index < len(records):
        records[index] = [tanggal,jenis, jumlah, kategori]
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(records)
        return True
    return False

def delete_record(index):
    records = read_records()
    if 0 <= index < len(records):
        records.pop(index)
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(records)
        return True
    return False

def main():
    while True:
        print("\n=== Manajemen Keuangan Pribadi ===")
        print("1. Tambah catatan")
        print("2. Lihat semua catatan")
        print("3. Update catatan")
        print("4. Hapus catatan")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tanggal = input("tanggal: ")
            jenis = input("Jenis (pemasukan/pengeluaran): ")
            jumlah = input("Jumlah: ")
            kategori = input("Kategori: ")
            create_record(tanggal, jenis, jumlah, kategori)
            print("Catatan berhasil ditambahkan.")
        elif pilihan == '2':
            records = read_records()
            if not records:
                print("Belum ada catatan.")
            else:
                for i, record in enumerate(records):
                    print(f"{i}. tanggal: {record[0]} Jenis: {record[1]}, Jumlah: {record[2]}, Kategori: {record[3]}")
        elif pilihan == '3':
            index = int(input("Masukkan nomor catatan yang ingin diupdate: "))
            tanggal = input("tanggal: ")
            jenis = input("Jenis baru: ")
            jumlah = input("Jumlah baru: ")
            kategori = input("Kategori baru: ")
            if update_record(index, tanggal, jenis, jumlah, kategori):
                print("Catatan berhasil diupdate.")
            else:
                print("Nomor catatan tidak valid.")
        elif pilihan == '4':
            index = int(input("Masukkan nomor catatan yang ingin dihapus: "))
            if delete_record(index):
                print("Catatan berhasil dihapus.")
            else:
                print("Nomor catatan tidak valid.")
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()
