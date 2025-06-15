
from koneksi import buka_koneksi
from mahasiswa import Mahasiswa
from matkul import Matkul
from krs import KRS
from nilai import Nilai
import config

from pyreportjasper import PyReportJasper
from os.path import *
from os import startfile

koneksi = buka_koneksi()
if koneksi is not None:
    print("Koneksi berhasil")
else:
    exit()

print("=================")
print("ISB ATMA LUHUR")
print("==================")
while True:
    print("[1] Master")
    print("[2] Transaksi")
    print("[3] Laporan")
    print("[4] Keluar")
    pilih1 = int(input("Masukkan pilihan Anda (1-4): "))
    print()
    match pilih1:
        case 1: # Master
            while True:
                print("[1.1] Mahasiswa")
                print("[1.2] Mata Kuliah")
                print("[1.3] Kembali")
                pilih2 = int(input("Masukkan pilihan Anda (1-3): "))
                print()

                match pilih2:
                    case 1: # Mahasiswa
                        while True:
                            print("[1.1.1] Tambah Mahasiswa")
                            print("[1.1.2] Ubah Data Mahasiswa")
                            print("[1.1.3] Hapus Data Mahasiswa")
                            print("[1.1.4] Tampil Daftar Mahasiswa")
                            print("[1.1.5] Kembali")
                            pilih3 = int(input("Masukkan pilihan Anda (1-5): "))
                            print()
                            mhs = Mahasiswa()
                            match pilih3:
                                case 1: # Tambah mahasiswa
                                    mhs.nim = input("NIM: ")
                                    mhs.nm_mahasiswa = input("Nama mahasiswa: ")
                                    mhs.simpan ()
                                case 2: # Ubah data mahasiswa
                                    while True:
                                        nim = input("NIM: ")
                                        data = mhs.ambil_data(nim)
                                        if len(data) > 0:
                                            mhs.nm_mahasiswa = input (f"Nama mahasiswa: {data["nama"]} -> ")
                                            mhs.ubah (nim)
                                            break
                                        else:
                                            print(f"Data mahasiswa dengan NIM [{nim}] tidak ditemukan")
                                            ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                            if ulang:
                                                print()
                                            else:
                                                break
                                case 3: # Hapus data mahasiswa
                                    while True:
                                        nim = input("NIM: ")
                                        data = mhs.ambil_data(nim)
                                        if len(data) > 0:
                                            mhs.hapus (nim)
                                            break
                                        else:
                                            print (f"Data mahasiswa dengan NIM [{nim}] tidak ditemukan")
                                            ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                            if ulang:
                                                print()
                                            else:
                                                break
                                case 4: # Tampil daftar mahasiswa
                                    mhs.tampil()
                                case 5: # Kembali
                                    break
                                case _:
                                    print("Pilihan salah!")
                            print()

                    case 2: # Mata kuliah
                        while True:
                            print("[1.2.1] Tambah Mata Kuliah")
                            print("[1.2.2] Ubah Data Mata Kuliah")
                            print("[1.2.3] Hapus Data Mata Kuliah")
                            print("[1.2.4] Tampil Daftar Mata Kuliah")
                            print("[1.2.5] Kembali")
                            pilih3 = int(input("Masukkan pilihan Anda (1-5): "))
                            print()
                            mk = Matkul()

                            match pilih3:
                                case 1: # Tambah mata kuliah
                                    mk.kd_matkul = input("Kode mata kuliah: ")
                                    mk.nm_matkul = input("Nama mata kuliah: ")
                                    while True:
                                        mk.sks = int(input("SKS (2-4): "))
                                        if mk.sks < 2 or mk.sks >= 4:
                                            print("SKS mata kuliah salah!")
                                        else:
                                            break
                                    mk.simpan()

                                case 2: # Ubah data mata kuliah
                                    while True:
                                        kd_matkul = input("Kode mata kuliah: ")
                                        data = mk.tampil_detail(kd_matkul)
                                        if len(data) > 0:
                                            mk.nm_matkul = input(f"Nama mata kuliah: {data["nama"]} -> ")
                                            while True:
                                                mk.sks = int(input("SKS (2-4): "))
                                                if mk.sks < 2 or mk.sks >= 4:
                                                    print("SKS mata kuliah salah!")
                                                else:
                                                    break
                                            mk.ubah(kd_matkul)
                                            break
                                        else:
                                            print(f"Data mata kuliah dengan kode [{kd_matkul}] tidak ditemukan")
                                            ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                            if ulang:
                                                print()
                                            else:
                                                break

                                case 3: # Hapus data mata kuliah
                                    while True:
                                        kd_matkul = input("Kode mata kuliah: ")
                                        data = mk.tampil_detail(kd_matkul)
                                        if len(data) > 0:
                                            mk.hapus(kd_matkul)
                                            break
                                        else:
                                            print(f"Data mata kuliah dengan kode [{kd_matkul}] tidak ditemukan")
                                            ulang = input("Tekan R jika ingin mencoba lagi: ").upper() == 'R'
                                            if ulang:
                                                print()
                                            else:
                                                break
                                case 4: # Tampil daftar mata kuliah
                                    mk.tampil()
                                case 5: # Kembali
                                    break
                                case _:
                                    print("Pilihan salah!")
                    case 3: # kembali
                        break
                    case _:
                        print('Pilihan Salah')

        case 2: # Transaksi
            while True:
                print("[2.1] Entri KRS")
                print("[2.2] Update KRS")
                print("[2.3] Entri Nilai")
                print("[2.4] Kembali")
                pilih2 = int(input("Masukkan pilihan Anda (1-4): "))
                print()
                mhs = Mahasiswa()
                mk = Matkul()
                kr = KRS ()
                nil = Nilai()
                berhasil = False

                match pilih2:
                    case 1: # Entri KRS
                        while True:
                            kr.nim = input("NIM: ")
                            data = mhs.ambil_data(kr.nim)
                            if len(data) > 0:
                                print(f"Nama mahasiswa: {data["nama"]}")
                                while True:
                                    kr.kd_matkul = input("Kode mata kuliah: ")
                                    data = mk.tampil_detail(kr.kd_matkul)
                                    if len(data) > 9:
                                        print(f"Nama mata kuliah: {data['nama']}")
                                        print("SKS: data['sks']}")
                                        while True:
                                            smt = input("Semester ([0] Ganjil/[E] Genap): ")
                                            match smt.upper():
                                                case '0':
                                                    kr.semester = "Gasal"
                                                    break
                                                case 'E':
                                                    kr.semester = "Genap"
                                                    break
                                                case _:
                                                    print("Pilihan salah!")
                                        kr.thn_akademik = int(input("Tahun akademik (tahun semester gasal saja): "))
                                        kr.simpan_krs()
                                        berhasil = True
                                        break
                                    else:
                                        print(f"Data mata kuliah dengan kode [{kd_matkul}] tidak ditemukan")
                            else:
                                print(f"Data mahasiswa dengan NIM [{nim}] tidak ditemukan")
                            if berhasil:
                                print()
                                break
                    case 2: # Update KRS
                        while True:
                            nim = input("NIM: ")
                            data = mhs.ambil_data(nim)
                            if len(data) > 0:
                                print(f"Nama mahasiswa: {data["nama"]}")
                                while True:
                                    kd_matkul = input("Kode mata kuliah: ")
                                    data = mk.tampil_detail (kd_matkul)
                                    if len(data) > 0:
                                        print (f"Nama mata kuliah: {data['nama']}")
                                        print(f"SKS: {data["sks"]}")
                                        while True:
                                            smt = input("Semester ([0] Ganjil/[E] Genap): ")
                                            match smt.upper():
                                                case '0':
                                                    kr.semester = "Gasal"
                                                    break
                                                case 'E':
                                                    kr.semester = "Genap"
                                                    break
                                                case _:
                                                    print("Pilihan salah!")


                                    else:
                                        kr.thn_akademik = int(input("Tahun akademik (tahun semester gasal saja): "))
                                        kr.ubah_krs = (nim, kd_matkul)
                                        berhasil = True
                                        break
                            else:
                                print(f"Data mata kuliah dengan kode [{kd_matkul}] tidak ditemukan")
                                print(f"Data mahasiswa dengan NIM [{nim}] tidak ditemukan")
                            if berhasil:
                                print()
                                break
                    case 3: # Entri nilai
                        while True:
                            nim = input("NIM: ")
                            data = mhs.ambil_data(nim)
                            if len(data) > 0:
                                print (f"Nama mahasiswa: {data["nama"]}")
                                kd_matkul = input("Kode mata kuliah: ")
                                data = mk.tampil_detail (kd_matkul)
                                if len(data) > 0:
                                    print(f"Nama mata kuliah: {data['nama']}")
                                    print(f"SKS: {data['sks']}")
                                    nil.presensi = int(input("Presensi: "))
                                    nil.tugas = int(input("Tugas: "))
                                    nil.uts = int(input("UTS: "))
                                    nil.uas = int(input("UAS: "))
                                    nil.update_khs(nim, kd_matkul)
                                    print()
                                    break

                                else:
                                    print(f"Data mata kuliah dengan kode [{kd_matkul}] tidak ditemukan")
                            else:
                                print (f"Data mahasiswa dengan NIM [{nim}] tidak ditemukan")
                    case 4: # Kembali
                        break
                    case _:
                        print("Pilihan salah!")


        case 3: # Laporan
            while True:
                print("[3.1] Cetak KHS")
                print("[3.2] Kembali")
                pilih2 = int(input("Masukkan pilihan Anda (1-2): "))
                print()
                mhs = Mahasiswa()
                mk = Matkul()
                nil = Nilai()
                berhasil = False
                match pilih2:
                    case 1: # Cetak KHS
                        while True:
                            nim = input("NIM: ")
                            data = mhs.ambil_data(nim)

                            if len(data) > 0:
                                print (f"Nama mahasiswa: {data["nama"]}")
                                while True:
                                    smt = input("Semester ([0] Ganjil/[E] Genap): ")
                                    match smt.upper():
                                        case '0':
                                            semester = "Gasal"
                                            break
                                        case 'E':
                                            semester = "Genap"
                                            break
                                        case _:
                                            print("Pilihan salah!")

                                    thn_akademik = int(input("Tahun akademik (tahun semester gasal saja): "))
                                    # Cetak KHS ke PDF via Jasper Reports
                                    reports_dir = abspath (dirname(__file__))
                                    input_file = join (reports_dir, "khs.jasper")
                                    output_file = join (reports_dir, "khs")
                                    prj = PyReportJasper()
                                    params = {"nim": nim, "semester": semester, "thn_akademik": thn_akademik}

                                    mysql_conf = {
                                        "driver": config.driver,
                                        "username": config.username,
                                        "password": config.password,
                                        "host": config.host,
                                        "database": config.database,
                                        "port": config.port,
                                        "jdbc_driver": config.jdbc_driver,
                                        "jdbc_dir": reports_dir
                                    }
                                    print("Membuat KHS...")
                                    prj.config(input_file, output_file, parameters=params, db_connection=mysql_conf)
                                    prj.process_report()
                                    print("KHS selesai dibuat! Membuka KHS...")
                                    startfile(f" {output_file}.pdf")
                                    print()
                                    break
                            else:
                                print (f"Data mahasiswa dengan NIM [{nim}] tidak ditemukan")
                    case 2: # Kembali
                        break
                    case _:
                        print("Pilihan salah!")

        case 4: # Keluar
            exit()
        case _:
            print("Pilihan salah!")