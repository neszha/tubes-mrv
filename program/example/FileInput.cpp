#include "FileInput.h"
#include<fstream>
#include<iostream>
using namespace std;

    void FileInput::PerolehUkuran(int* baris, int* kolom, string* batas, string* nama){
        //Deklarasikan FileOpener (fsteram)
        fstream f;
        //Buka File Dengan nama dari pointer nama dan pembukaan hanya read only
        f.open((*nama).c_str(), ios::in);
        //Jika File Dibuka
        if(f.is_open()){
            //Deklarasikan tf untuk menampung text di dalam file
            string tf;
            //Selagi memiliki baris pada file
            while(getline(f, tf)){
                //Hitung banyaknya baris
                *baris += 1;
                //Jika baris bernilai satu  hitung banyaknya kolom
                if(*baris == 1){
                    //Deklarasi start sebagai indikator awal char pada string
                    int start = 0;
                    //Deklarasi end sebagai indikator awal dimana batas (' ') pertama kali ditemukan
                    int end = tf.find(*batas);
                    //Selagi end masih menemukan batas
                    while(end != string::npos){
                        //Hitung banyaknya kolom
                        *kolom += 1;
                        //Ubah nilai start dengan lokasi end dan ukuran dari batas
                        start = end+(*batas).length();
                        //Ubah nilai end dengan mencari batas selanjutnya setelah posisi start
                        end = tf.find(*batas, start);
                    }
                }
            }
        }
        //Tambahkan 1 pada kolom untuk
        //menghitung kolom terakhir
        *kolom += 1;
        //Tutup file
        f.close();
    }

    void FileInput::BentukArray(float a[][N], int* baris, int* kolom, string* batas, string* nama){
        //Deklarasikan FileOpener (fsteram)
        fstream file;
        //Buka File Dengan nama dari pointer nama dan pembukaan hanya read only
        file.open((*nama).c_str(), ios::in);
        //Jika File Dibuka
        if(file.is_open()){
            //Deklarasikan tf untuk menampung text di dalam file
            string tf;
            //Deklarasi index baris dan kolom untuk perulangan
            int i = 0, j = 0;
            //Selagi memiliki baris pada file
            while(getline(file, tf)){
                //Deklarasi start sebagai indikator awal char pada string
                int start = 0;
                //Deklarasi end sebagai indikator awal dimana batas (' ') pertama kali ditemukan
                int end = tf.find(*batas);
                //Selagi end masih menemukan batas
                while(end != string::npos){
                    //Masukan nilai yang ditemukan pada matriks A pada elemen a[i][j]
                    a[i][j] = stof(tf.substr(start, end - start));
                    //Ubah nilai start dengan lokasi end dan ukuran dari batas
                    start = end+(*batas).length();
                    //Ubah nilai end dengan mencari batas selanjutnya setelah posisi start
                    end = tf.find(*batas, start);
                    //Tambahkan penghitung kolom
                    j++;
                }
                //Jika end berada akhir baris
                if(end == string::npos){
                    //Masukan nilai yang ditemukan pada matriks A pada elemen a[i][j]
                    a[i][j] = stof(tf.substr(start, end - start));
                    //Ubah nilai start dengan lokasi end dan ukuran dari batas
                    start = end+(*batas).length();
                    //Ubah nilai end dengan mencari batas selanjutnya setelah posisi start
                    end = tf.find(*batas, start);
                    //Reset ukuran kolom
                    j = 0;
                }
                //Tambahkan penghitung baris
                i++;
            }
        }
        //Tutup file
        file.close();
    }

    void FileInput::MenerimaFile(){
        // FileInput input;
        //Deklarasi penghitung banyaknya baris dan kolom
        int baris = 0, kolom = 0;
        //Tentukan batas yang berupa space (' ')
        string batas(1, ' ');
        //Deklarasi nama file
        string nama;
        cout << "Masukkan Nama File (Disertai dengan Ekstensi) : " << endl;
        //Menerima nama file dari user (disertai dengan .txt). Contoh : Text.txt
        cin >> nama;
        //Panggil prosedur peroleh Ukuran untuk memperoleh Banyaknya baris dan kolom pada matriks
        FileInput::PerolehUkuran(&baris, &kolom, &batas, &nama);
        //Deklarasi matriks a dengan ukuran baris x N
        float a[baris][N];
        //Panggil prosedur untuk membentuk array dengan ukuran baris x kolom
        FileInput::BentukArray(a, &baris, &kolom, &batas, &nama);
    }