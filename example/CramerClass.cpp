#include <iostream>
#include "CramerClass.h"
#include "SaveOutput.h"
using namespace std;

    void CramerClass::CramerKeyboard(){
        // Deklarasi Ukuran Matrix
        int n;
        //Menerima Ukuran Matrix
        cout << "Masukkan Ukuran Matrix : ";
        cin >> n;
        //Deklarasi Matrix
        float a[n][N];
        float b[n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                //Menerima Inputan Untuk Matrix Aij
                cout << "Masukkan Nilai A[" << i+1 << "][" << j+1 << "] : ";
                cin >> a[i][j];
            }
            cout << "Masukkan Hasil Dari Persamaan " << i+1 << " : ";
            cin >> b[i];
        }
        Cramer(a, b, n);
    }

    void CramerClass::Cramer(float a[][N], float b[], int n){
        //Menerima nama file dari user (disertai dengan .txt). Contoh : Text.txt
        cout << "Masukkan Nama File Untuk Disimpan (Disertai dengan Ekstensi) : " << endl;
        string nama;
        cin >> nama;
        
        //Menuliskan Matrix pada file
        SaveOutput::SaveString(nama, "Solusi Dari Matrix : ");
        SaveOutput::SaveFile(nama, a, NULL, n, n);

        //Deklarasi Determinan
        float det[n+1];
        //Deklarasi Solusi
        float x[n];

        for(int i = -1; i < n; i++){
            int swap = 0;
            float temp[n][N];
            for(int j = 0; j < n; j++){
                for(int k = 0; k < n; k++){
                    temp[j][k] = a[j][k];
                }
            }
            
            Operasi::OperasiBarisElementer(temp, b, 0, n, i, &swap);
            det[i+1] = Operasi::GetDeterminant(temp, n, swap);
        }
        
        cout << "Solusi Dari Persamaan Ialah : " << endl;
        for(int i = 1; i < n+1; i++){
            x[i-1] = det[i]/det[0];
            cout << "X[" << i << "] = " << x[i-1] << endl;
        }
        
        //Cetak Solusi pada file
        SaveOutput::SaveString(nama, "Ialah : ");
        SaveOutput::SaveFile(nama, NULL, x, 0, n);
    }
