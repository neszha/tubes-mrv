#include "MenuClass.h"
#include "CramerClass.h"
#include "DeterminanClass.h"
#include "SPLClass.h"
#include "InverseClass.h"
#include "InverseMethod.h"
#include "FileInput.h"
#include <iostream>
using namespace std;

    #pragma region Deklarasi Umum
    //Deklarasi penghitung banyaknya baris dan kolom
    int baris = 0, kolom = 0;
    //Tentukan batas yang berupa space (' ')
    string batas(1, ' ');
    //Deklarasi nama file
    string nama;
    #pragma endregion

    void MenuClass::Menu(){
        cout << "Pilih Aksi : " << endl;
        cout << "1. Sistem Persamaan Linier n Variable" << endl; //Completed
        cout << "2. Menghitung Determinan" << endl; //Completed
        cout << "3. Menentukan Matriks Balikan" << endl; //Completed
        cout << "4. Keluar" << endl;
        cout << "Masukkan Pilihan : ";
        int i;
        cin >> i;
        switch(i){
            case 1:
                Pertama();
            break;
            case 2:
                Kedua();
            break;
            case 3:
                Ketiga();
            break;
        }
    }
    void MenuClass::Pertama(){
        cout << "Pilih Metode : " << endl;
        cout << "1. Eliminasi Gauss" << endl; //Completed
        cout << "2. Eliminasi Gauss-Jordan" << endl; //Completed
        cout << "3. Metode Matriks Balikan" << endl; //Completed
        cout << "4. Kaidah Cramer" << endl; //Completed
        cout << "5. Kembali Ke Menu Sebelumnya" << endl; //Completed
        cout << "Masukkan Pilihan : ";
        int i;
        cin >> i;
        switch(i){
            case 1:
                Gauss();
            break;
            case 2:
                GaussJordan();
            break;
            case 3:
                Inverse();
            break;
            case 4:
                Cramer();
            break;
            case 5:
                Menu();
            break;
        }
    }
    void MenuClass::Kedua(){
        cout << "Pilih Metode : " << endl;
        cout << "1. Reduksi Baris" << endl; //Completed
        cout << "2. Ekspansi Kofaktor" << endl; //Completed
        cout << "3. Kembali Ke Menu Sebelumnya" << endl; //Completed
        cout << "Masukkan Pilihan : ";
        int i;
        cin >> i;
        switch(i){
            case 1:
                Reduksi();
            break;
            case 2:
                Ekspansi();
            break;
            case 3:
                Menu();
            break;
        }
    }
    void MenuClass::Ketiga(){
        Balikan();
    }

    void MenuClass::FileMatrix(){
        //Menerima nama file dari user (disertai dengan .txt). Contoh : Text.txt
        cout << "Masukkan Nama File (Disertai dengan Ekstensi) : " << endl;
        cin >> nama;
        //Panggil prosedur untuk memperoleh ukuran matrix
        FileInput::PerolehUkuran(&baris, &kolom, &batas, &nama);
    }
    void MenuClass::MatrixHasil(float a[][N], float b[]){
        //Memberikan nilai pada matriks a pada baris i kolom terakhir pada array b
        for(int i = 0; i < baris; i++){
            b[i] = a[i][kolom-1];
        }
    }

    void MenuClass::Gauss(){
        cout << "1. Input Dari Keyboard" << endl;
        cout << "2. Input Dari File" << endl;
        cout << "Masukkan Pilihan : ";
        int i;
        cin >> i;
        //Deklarasikan Class SPLClass dengan nama gauss
        SPLClass gauss;
        switch(i){
            case 1:
                //Memanggil Sub Program SPLGaussKeyboard pada Class SPLClass
                gauss.SPLGaussKeyboard();
            break;
            case 2:
                FileMatrix();
                //Deklarasi matriks a dengan ukuran baris x N
                float a[baris][N];
                //Panggil prosedur untuk membentuk array dengan ukuran baris x kolom
                FileInput::BentukArray(a, &baris, &kolom, &batas, &nama);
                //Panggil prosedur Gauss
                gauss.SPLGauss(a, baris, kolom-1);
            break;
        }
    }
    void MenuClass::GaussJordan(){
        cout << "1. Input Dari Keyboard" << endl;
        cout << "2. Input Dari File" << endl;
        cout << "Masukkan Pilihan : ";
        int i;
        cin >> i;
        //Deklarasikan Class SPLClass dengan nama jordan
        SPLClass jordan;
        switch(i){
            case 1:
                //Memanggil Sub Program SPLGaussJordanKeyboard pada Class SPLClass
                jordan.SPLGaussJordanKeyboard();
            break;
            case 2:
                FileMatrix();
                //Deklarasi matriks a dengan ukuran baris x N
                float a[baris][N];
                //Panggil prosedur untuk membentuk array dengan ukuran baris x kolom
                FileInput::BentukArray(a, &baris, &kolom, &batas, &nama);
                //Panggil prosedur GaussJordan
                jordan.SPLGaussJordan(a, baris, kolom-1);
            break;
        }
    }
    void MenuClass::Inverse(){
        cout << "1. Input Dari Keyboard" << endl;
        cout << "2. Input Dari File" << endl;
        cout << "Masukkan Pilihan : ";
        int i;
        cin >> i;
        //Deklarasikan Class InverseMethod dengan nama method
        InverseMethod method;
        switch(i){
            case 1:
                //Memanggil Sub Program InverseSPLKeyboard pada Class InverseMethod
                method.InverseSPLKeyboard();
            break;
            case 2:
                FileMatrix();
                //Deklarasi matriks a dengan ukuran baris x N
                float a[baris][N];
                //Deklarasi hasil matrks
                float b[baris];
                //Panggil prosedur untuk membentuk array dengan ukuran baris x kolom
                FileInput::BentukArray(a, &baris, &kolom, &batas, &nama);
                //Panggil prosedur untuk membentuk matriks hasil
                MatrixHasil(a, b);
                //Panggil prosedur Inverse
                method.InverseSPL(a, b, baris);
            break;
        }
    }
    void MenuClass::Cramer(){
        cout << "1. Input Dari Keyboard" << endl;
        cout << "2. Input Dari File" << endl;
        cout << "Masukkan Pilihan : ";
        int i;
        cin >> i;
        //Deklarasikan Class CramerClass dengan nama cramer
        CramerClass cramer;
        switch(i){
            case 1:
                //Memanggil Sub Program CramerKeyboard pada Class CramerClass
                cramer.CramerKeyboard();
            break;
            case 2:
                FileMatrix();
                //Deklarasi matriks a dengan ukuran baris x N
                float a[baris][N];
                //Deklarasi hasil matrks
                float b[baris];
                //Panggil prosedur untuk membentuk array dengan ukuran baris x kolom
                FileInput::BentukArray(a, &baris, &kolom, &batas, &nama);
                //Panggil prosedur untuk membentuk matriks hasil
                MatrixHasil(a, b);
                //Panggil prosedur Cramer
                cramer.Cramer(a, b, baris);
            break;
        }
    }

    void MenuClass::Reduksi(){
        cout << "1. Input Dari Keyboard" << endl;
        cout << "2. Input Dari File" << endl;
        cout << "Masukkan Pilihan : ";
        int i;
        cin >> i;
        //Deklarasikan Class DeterminanClass dengan nama det
        DeterminanClass det;
        switch(i){
            case 1:
                //Memanggil Sub Program ReduksiDeterminanKeyboard pada Class DeterminanClass
                det.ReduksiDeterminanKeyboard();
            break;
            case 2:
                FileMatrix();
                //Deklarasi matriks a dengan ukuran baris x N
                float a[baris][N];
                //Panggil prosedur untuk membentuk array dengan ukuran baris x kolom
                FileInput::BentukArray(a, &baris, &kolom, &batas, &nama);
                //Panggil prosedur ReduksiDeterminan
                det.ReduksiDeterminan(a, baris);
            break;
        }
    }
    void MenuClass::Ekspansi(){
        cout << "1. Input Dari Keyboard" << endl;
        cout << "2. Input Dari File" << endl;
        cout << "Masukkan Pilihan : ";
        int i;
        cin >> i;
        //Deklarasikan Class DeterminanClass dengan nama det
        DeterminanClass det;
        switch(i){
            case 1:
                //Memanggil Sub Program EkspansiKofaktorKeyboard pada Class DeterminanClass
                det.EkspansiKofaktorKeyboard();
            break;
            case 2:
                FileMatrix();
                //Deklarasi matriks a dengan ukuran baris x N
                float a[baris][N];
                //Panggil prosedur untuk membentuk array dengan ukuran baris x kolom
                FileInput::BentukArray(a, &baris, &kolom, &batas, &nama);
                //Panggil prosedur EkspansiKofaktor
                det.EkspansiKofaktor(a, baris);
            break;
        }
    }

    void MenuClass::Balikan(){
        cout << "1. Input Dari Keyboard" << endl;
        cout << "2. Input Dari File" << endl;
        cout << "Masukkan Pilihan : ";
        int i;
        cin >> i;
        //Deklarasikan Class InverseClass dengan nama inverse
        InverseClass inverse;
        switch(i){
            case 1:
                //Memanggil Sub Program InverseKeyboard pada Class InverseClass
                inverse.InverseKeyboard();
            break;
            case 2:
                FileMatrix();
                //Deklarasi matriks a dengan ukuran baris x N
                float a[baris][N];
                //Panggil prosedur untuk membentuk array dengan ukuran baris x kolom
                FileInput::BentukArray(a, &baris, &kolom, &batas, &nama);
                inverse.Inverse(a, baris);
            break;
        }
    }
