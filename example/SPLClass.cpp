#include<iostream>
#include "Operasi.h"
#include "SPLClass.h"
#include "SaveOutput.h"
using namespace std;

    #pragma region GaussElimination
    void SPLClass::SPLGaussKeyboard(){
        //Deklarasi Persamaan
        int m, n;
        cout << "Masukkan Jumlah Persamaan : ";
        cin >> m;
        cout << "Masukkan Jumlah Variable : ";
        cin >> n;
        //Deklarasi Variable Persamaan
        float a[m][N];
        //Deklarasi Variable Hasil Persamaan
        for(int i = 0; i < m; i++){
            // Menerima Inputan Untuk Persamaan Ke-i
            cout << "Masukkan Persamaan " << i+1 << " : " << endl;
            for(int j = 0; j < n; j++){
                //Menerima Inputan Untuk Variable Ke-i
                cout << "Masukkan Variable x" << j+1 << " : ";
                cin >> a[i][j];
            }
            cout << "Masukkan Hasil Dari Persamaan : ";
            cin >> a[i][n];
        }
        SPLGauss(a, m, n);
    }

    void SPLClass::SPLGauss(float a[][N], int m, int n){
        //Menerima nama file dari user (disertai dengan .txt). Contoh : Text.txt
        cout << "Masukkan Nama File Untuk Disimpan (Disertai dengan Ekstensi) : " << endl;
        string nama;
        cin >> nama;
        
        //Menuliskan Matrix pada file
        SaveOutput::SaveString(nama, "Solusi Dari Matrix : ");
        SaveOutput::SaveFile(nama, a, NULL, n, n);
        SaveOutput::SaveString(nama, "Ialah : ");

        //Deklarasi Matrix Solusi
        float x[n];
        int cek = Operasi::OperasiBarisElementer(a, NULL, m, n, -1, NULL);

        if(cek != -1){
            cout << "Berkemungkinan Tidak Bersolusi" << endl;
            if(a[cek][n]){
                cout << "Tidak Bisa Di proses" << endl;
                SaveOutput::SaveString(nama, "Matrix Tidak Bisa Di proses");
            }else{
                cout << "Memiliki Solusi Banyak" << endl;
                SaveOutput::SaveString(nama, "Matrix Memiliki Solusi Banyak");
            }
            return;
        }

        BackwardSubtitution(a, x, m, n);
        
        //Cetak Solusi pada file
        SaveOutput::SaveFile(nama, NULL, x, 0, n);
    }

    void SPLClass::BackwardSubtitution(float a[][N], float x[], int m, int n){
        for(int i = m-1; i >= 0; i--){
            //Peroleh Nilai Paling Akhir
            x[i] = a[i][n];
            for(int j = i+1; j < n ;j++){
                x[i] -= a[i][j]*x[j];
            }

            //Peroleh Nilai Akhir/Solusi
            x[i] /= a[i][i];
        }
        cout << "Solusi Dari Persamaan Tersebut Ialah : " << endl;
        for(int i = 0 ; i < n; i++){
            cout << "X[" << i+1 << "] = " << x[i] << endl;
        }
    }
    #pragma endregion

    #pragma region GaussJordanElimination
    void SPLClass::SPLGaussJordanKeyboard(){
        //Deklarasi Persamaan
        int m, n;
        cout << "Masukkan Jumlah Persamaan : ";
        cin >> m;
        cout << "Masukkan Jumlah Variable : ";
        cin >> n;
        //Deklarasi Variable Persamaan
        float a[m][N];
        //Deklarasi Variable Hasil Persamaan
        for(int i = 0; i < m; i++){
            // Menerima Inputan Untuk Persamaan Ke-i
            cout << "Masukkan Persamaan " << i+1 << " : " << endl;
            for(int j = 0; j < n; j++){
                //Menerima Inputan Untuk Variable Ke-i
                cout << "Masukkan Variable x" << j+1 << " : ";
                cin >> a[i][j];
            }
            cout << "Masukkan Hasil Dari Persamaan : ";
            cin >> a[i][n];
        }

        SPLGaussJordan(a, m, n);
    }

    void SPLClass::SPLGaussJordan(float a[][N], int m, int n){
        //Menerima nama file dari user (disertai dengan .txt). Contoh : Text.txt
        cout << "Masukkan Nama File Untuk Disimpan (Disertai dengan Ekstensi) : " << endl;
        string nama;
        cin >> nama;

        //Menuliskan Matrix pada file
        SaveOutput::SaveString(nama, "Solusi Dari Matrix : ");
        SaveOutput::SaveFile(nama, a, NULL, n, n);
        SaveOutput::SaveString(nama, "Ialah : ");

        //Deklarasi Banyak Variable
        float x[n];

        int cek = Operasi::OperasiBarisElementer(a, NULL, m, n, -1, NULL);

        if(cek != -1){
            cout << "Berkemungkinan Tidak Bersolusi" << endl;
            if(a[cek][n]){
                cout << "Tidak Bisa Di proses" << endl;
                SaveOutput::SaveString(nama, "Matrix Tidak Bisa Di proses");
            }else{
                cout << "Memiliki Solusi Banyak" << endl;
                SaveOutput::SaveString(nama, "Matrix Memiliki Solusi Banyak");
            }
            return;
        }

        Operasi::BackwardPhase(a, 0, n);

        cout << "Solusi Dari Persamaan Tersebut Ialah : " << endl;
        for(int i = 0; i < m; i++){
            x[i] = a[i][n]/a[i][i];
            cout << "X[" << i+1 << "] = " << x[i] << endl;
        }
        //Cetak Solusi pada file
        SaveOutput::SaveFile(nama, NULL, x, 0, n);
    }

    #pragma endregion