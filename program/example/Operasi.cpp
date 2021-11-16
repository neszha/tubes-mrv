#include "Operasi.h"
#include <iostream>
using namespace std;

    float Operasi::OperasiBarisElementer(float a[][N], float b[], int m, int n, int ganti, int* swap){

        //Ganti Elemen B ke A
        if(ganti > -1){
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    if(j == ganti)
                        a[i][j] = b[i];
                }
            }
        }

        //Perulangan Pada Kolom
        for(int j = 0; j < n; j++){
            //Peroleh Index untuk Pengecekan
            int maxId = j;
            //Peroleh Nilai untuk Pengecekan
            float maxValue = a[maxId][j];
            //Perulangan Pada Baris
            for(int i = j+1; i < ((m > 0 ? m : n)); i++){
                //Cek Nilai Lebih Besar Dengan Nilai Mutlak
                if((a[i][j] > 0 ? a[i][j] : -1*a[i][j]) > maxValue){
                    maxId = i;
                    maxValue = a[i][j];
                }
            }

            //Kembalikan jika 0 Pada Diagonal Utama
            if(!a[j][maxId]) return j;

            if(maxId != j) TukarBaris(a, n, j, maxId, (swap == NULL ? NULL : &(*swap)));
            
            //Eliminasi Baris //Bentuk Segitiga Atas
            for(int i = j+1; i < n; i++){
                float x = a[j][j];
                float y = a[i][j];
                //Bentuk Segitiga Atas
                for(int k = 0; k < (m > 0 ? n+1 : n); k++){
                    //Peroleh 0
                    a[i][k] -= a[j][k] * y/x;
                }
            }
        }
        return -1;
    }

    float Operasi::OBE_Inverse(float a[][N], int n){
        //Perulangan Pada Kolom
        for(int j = 0; j < n; j++){
            //Peroleh Index Untuk Pengecekan
            int maxId = j;
            //Peroleh Nilai Untuk Pengecekan
            float maxValue = a[maxId][j];
            //Perulangan Pada Baris
            for(int i = j+1; i < n; i++){
                //Cek Nilai Lebih Besar Dengan Nilai Mutlak
                if((a[i][j] > 0 ? a[i][j] : -1*a[i][j]) > maxValue){
                    maxValue = a[i][j];
                    maxId = i;
                }
            }

            //Pertukarkan Baris
            if(maxId != j) TukarBaris(a, n*2, j, maxId, NULL);

            //Eliminasi Baris
            for(int i = j+1; i < n; i++){
                float x1 = a[j][j];
                float x2 = a[i][j];
                //Peroleh 0
                for(int k = 0; k < n*2; k++){
                    a[i][k] -= a[j][k] * x2/x1;
                }
            }
        }
        return -1;
    }

    //Pertukarkan Baris Dimana |y1| < |y2|
    //Dimana y1 dan y2 adalah baris pada diagonal utama
    void Operasi::TukarBaris(float a[][N], int n, int y1, int y2, int* swap){
        //Penukaran Baris
        for(int i = 0; i < n+1; i++){
            float temp = a[y1][i];
            a[y1][i] = a[y2][i];
            a[y2][i] = temp;
        }
        //Hitung Jumlah Penukaran Untuk Determinan
        if(swap != NULL)
            *swap += 1;
    }

    float Operasi::GetDeterminant(float a[][N], int n, int t){
        //Deklarasi Variable Det
        float det = 1;
        //Kalikan Semua Nilai Pada Diagonal Utama
        for(int i = 0; i < n; i++){
            det *= a[i][i];
        }
        
        if(t % 2 == 1) det *= -1;

        return det;
    }

    void Operasi::BackwardPhase(float a[][N], int m, int n){
        //Perulangan Pada Kolom
        for(int j = n-1; j >= 0; j--){
            //Perulangan Pada Baris dari j-1 hingga Baris 0
            for(int i = j-1; i >= 0; i--){
                float x = a[j][j];
                float y = a[i][j];
                //Perulangan Untuk Memperoleh Baris Eselon Tereduksi 
                for(int k = (m > 0 ? m : n+1); k >= i; k--){
                        a[i][k] -= a[j][k] * y/x;
                }
            }
        }
    }