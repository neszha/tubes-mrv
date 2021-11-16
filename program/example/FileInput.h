#ifndef FILEINPUT_H
#define FILEINPUT_H
#include <iostream>
using namespace std;
#define N 100

class FileInput{
    public:
        static void MenerimaFile();
        static void PerolehUkuran(int* baris, int* kolom, string* batas, string* nama);
        static void BentukArray(float a[][N], int* baris, int* kolom, string* batas, string* nama);
};

#endif