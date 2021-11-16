#include "SaveOutput.h"
#include <iostream>
using namespace std;

    //nama untuk nama file
    //str untuk string yang akan disimpan
    void SaveOutput::SaveString(string nama, string str){
        //Buka File/Jika Tidak Create
        ofstream file(nama, ofstream::app);
        //Jika File Terbuka
        if(file.is_open()){
            //Masukkan str ke file
            file << str << endl;
        }
    }

    //a untuk matriks dua dimensi
    //b untuk matriks satu dimensi (hasil/solusi)
    //m untuk batas perulangan
    //n untuk batas perulangan
    void SaveOutput::SaveFile(string nama, float a[][N], float b[], int m, int n){
        //Buka File/Jika Tidak Create
        ofstream file(nama, ofstream::app);
        //Jika File Terbuka
        if(file.is_open()){
            if(a != NULL){
                for(int i = 0; i < m; i++){
                    for(int j = 0; j < n; j++){
                        //Masukkan a[i][j] ke file
                        file << a[i][j] << "\t";
                    }
                    //Berikan Enter Pada file
                    file << endl;
                }
            }
            if(b != NULL){
                for(int i = 0; i < n; i++){
                    //Masukkan b[i] ke file
                    file << "X[" << i+1 << "] = " << b[i] << endl;
                }
            }
        }
    }

    void SaveOutput::SaveFileInverse(string nama, float a[][N], int m, int n){
        //Buka File/Jika Tidak Create
        ofstream file(nama, ofstream::app);
        //Jika File Terbuka
        if(file.is_open()){
            if(a != NULL){
                for(int i = 0; i < m; i++){
                    for(int j = m; j < n; j++){
                        //Masukkan a[i][j] ke file
                        file << a[i][j] << "\t";
                    }
                    //Berikan Enter Pada file
                    file << endl;
                }
            }
        }
    }