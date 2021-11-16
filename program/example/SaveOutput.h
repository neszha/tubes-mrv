#ifndef SAVEOUTPUT_H
#define SAVEOUPUT_H
#include <fstream>
#include <iostream>
using namespace std;
#define N 100
class SaveOutput{
    public:
        static void SaveString(string nama, string str);
        static void SaveFile(string nama, float a[][N], float b[], int m, int n);
        static void SaveFileInverse(string nama, float a[][N], int m, int n);
};

#endif