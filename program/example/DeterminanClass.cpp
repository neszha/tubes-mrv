#include<iostream>
#include "DeterminanClass.h"
#include "SaveOutput.h"
using namespace std;

    #pragma region ReduksiBaris
    void DeterminanClass::ReduksiDeterminanKeyboard(){
        // Deklarasi Ukuran Matrix
        int n;
        //Menerima Ukuran Matrix
        cout << "Masukkan Ukuran Matrix : ";
        cin >> n;
        //Deklarasi Matrix
        float a[n][N];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                //Menerima Inputan Untuk Matrix Aij
                cout << "Masukkan Nilai A[" << i+1 << "][" << j+1 << "] : ";
                cin >> a[i][j];
            }
        }
        ReduksiDeterminan(a, n);
    }

    void DeterminanClass::ReduksiDeterminan(float a[][N], int n){
        //Menerima nama file dari user (disertai dengan .txt). Contoh : Text.txt
        cout << "Masukkan Nama File Untuk Disimpan (Disertai dengan Ekstensi) : " << endl;
        string nama;
        cin >> nama;

        //Menuliskan Matrix pada file
        SaveOutput::SaveString(nama, "Determinan Dari Matrix : ");
        SaveOutput::SaveFile(nama, a, NULL, n, n);

        //Penentu Jumlah Penukaran
        int swap = 0;
        Operasi::OperasiBarisElementer(a, NULL, 0, n, -1, &swap);
        //Deklarasi Determinan
        float det = Operasi::GetDeterminant(a, n, swap);
        cout << "Determinan Dari Matrix  A = " << det << endl;

        //Cetak Determinan pada file
        SaveOutput::SaveString(nama, "Ialah : ");
        SaveOutput::SaveString(nama, to_string(det));
    }
    #pragma endregion
    
    #pragma region Ekspansi Kofaktor
    void DeterminanClass::EkspansiKofaktorKeyboard(){
        // Deklarasi Ukuran Matrix
        int n;
        //Menerima Ukuran Matrix
        cout << "Masukkan Ukuran Matrix : ";
        cin >> n;
        
        //Deklarasi Matrix
        float a[n][N];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                //Menerima Inputan Untuk Matrix Aij
                cout << "Masukkan Nilai A[" << i+1 << "][" << j+1 << "] : ";
                cin >> a[i][j];
            }
        }
        EkspansiKofaktor(a, n);
    }

    void DeterminanClass::EkspansiKofaktor(float a[][N], int n){
        //Menerima nama file dari user (disertai dengan .txt). Contoh : Text.txt
        cout << "Masukkan Nama File Untuk Disimpan (Disertai dengan Ekstensi) : " << endl;
        string nama;
        cin >> nama;

        //Menuliskan Matrix pada file
        SaveOutput::SaveString(nama, "Determinan Dari Matrix : ");
        SaveOutput::SaveFile(nama, a, NULL, n, n);

        //Deklarasi Determinan
        float det = Ekspansi(a, n);
        cout << "Determinan Dari Matrix A = " << det;

        //Cetak Determinan pada file
        SaveOutput::SaveString(nama, "Ialah : ");
        SaveOutput::SaveString(nama, to_string(det));
    }

    float DeterminanClass::Ekspansi(float a[][N], int n){
        float Det = 0;

        if(n == 1) return a[0][0]; //Return satu jika satu elemen saja

        //Deklarasi Kofaktor
        float CoFac[n][N];
        
        //Peroleh Kofaktor
        for(int i = 0; i < n; i++){
            //Peroleh Kofaktor
            Kofaktor(a, CoFac, 0, i, n);
            //Peroleh Determinan
            if(i%2==0) Det += a[0][i] * Ekspansi(CoFac, n-1);
            else Det += -1 * a[0][i] * Ekspansi(CoFac, n-1);
        }

        //Kembalikan Nilai Determinan
        return Det;
    }

    void DeterminanClass::Kofaktor(float a[][N], float CoFac[][N], int b, int k, int n){
        int l = 0, m = 0; //Index Dalam Pembuatan Minor
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(i != b && j != k){ //Bentuk Minor
                    //Mengambil Nilai Dari Matrix A ke Minor
                    CoFac[l][m++] = a[i][j];
                    //Reset Pengulangan Pada Index Minor
                    if(m == n-1){
                        m = 0;
                        l++;
                    }
                }
            }
        }
    }
    #pragma endregion