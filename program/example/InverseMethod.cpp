#include "InverseMethod.h"
#include "InverseClass.h"
#include "SaveOutput.h"
#include<iostream>
using namespace std;

    void InverseMethod::InverseSPLKeyboard(){
        // Deklarasi Ukuran Matrix
        int n;
        //Menerima Ukuran Matrix
        cout << "Masukkan Ukuran Matrix : ";
        cin >> n;
        //Deklarasi Matrix
        float a[n][N];
        //Deklarasi Matrix Hasil
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
        InverseSPL(a, b, n);
    }
    
    void InverseMethod::InverseSPL(float a[][N], float b[], int n){
        //Menerima nama file dari user (disertai dengan .txt). Contoh : Text.txt
        cout << "Masukkan Nama File Untuk Disimpan (Disertai dengan Ekstensi) : " << endl;
        string nama;
        cin >> nama;

        //Menuliskan Matrix pada file
        SaveOutput::SaveString(nama, "Solusi Dari Matrix : ");
        SaveOutput::SaveFile(nama, a, NULL, n, n);

        //Deklarasi Matrix Solusi
        float x[n];
        InverseClass::AddIdentitas(a, n);
        InverseClass::BentukIdentitas(a, n);
        Operasi::BackwardPhase(a, n*2, n);

        cout << "Sehingga : " << endl;
        for(int i = 0; i < n; i++){
            cout << "X[" << i+1 << "] = ";
            x[i] = GetX(a, b, n, i);
            cout << x[i] << endl;
        }

        //Cetak Solusi pada file
        SaveOutput::SaveString(nama, "Ialah : ");
        SaveOutput::SaveFile(nama, NULL, x, 0, n);
    }

    float InverseMethod::GetX(float a[][N], float b[], int n, int x){
        float temp = 0;
        for(int j = n; j < n*2; j++){
            temp += a[x][j] * b[(j-n)];
        }   
        return temp;
    }