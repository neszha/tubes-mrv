#include "InverseClass.h"
#include "SaveOutput.h"
#include<iostream>
using namespace std;

    void InverseClass::InverseKeyboard(){
        // Deklarasi Ukuran Matrix
        int n;
        //Menerima Ukuran Matrix
        cout << "Masukkan Ukuran Matrix : ";
        cin >> n;
        //Deklarasi Determinan
        //Deklarasi Matrix
        float a[n][N];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                //Menerima Inputan Untuk Matrix Aij
                cout << "Masukkan Nilai A[" << i+1 << "][" << j+1 << "] : ";
                cin >> a[i][j];
            }
        }
        Inverse(a, n);
    }

    void InverseClass::Inverse(float a[][N], int n){
        //Menerima nama file dari user (disertai dengan .txt). Contoh : Text.txt
        cout << "Masukkan Nama File Untuk Disimpan (Disertai dengan Ekstensi) : " << endl;
        string nama;
        cin >> nama;

        //Menuliskan Matrix pada file
        SaveOutput::SaveString(nama, "Inverse Dari Matrix : ");
        SaveOutput::SaveFile(nama, a, NULL, n, n);

        AddIdentitas(a, n);
        BentukIdentitas(a, n);
        Operasi::BackwardPhase(a, n*2, n);

        cout << "Inverse Matrix A ialah : " << endl;
        for(int i = 0; i < n; i++){
            for(int j = n; j < n*2; j++){
                cout << a[i][j] << "\t";
            }
            cout << endl;
        }

        //Cetak Inverse Matrix pada file
        SaveOutput::SaveString(nama, "Ialah:");
        SaveOutput::SaveFileInverse(nama, a, n, n*2);
    }

    void InverseClass::AddIdentitas(float a[][N], int n){
        //Jadikan Augmented
        //Masukan Identitas
        for(int i = 0; i < n; i++){
            for(int j = n; j < n*2; j++){
                if(j == i+n)
                    a[i][j] = 1;
                else
                    a[i][j] = 0;
            }
        }
        Operasi::OBE_Inverse(a, n);
    }

    void InverseClass::BentukIdentitas(float a[][N], int n){
        //Peroleh 1 Utama
        for(int i = 0; i < n; i++){
            float x = a[i][i];
            for(int j = 0; j < n*2; j++){
                a[i][j] /= x;
            }
        }
    }
