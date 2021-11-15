#ifndef DETERMINANCLASS_H
#define DETERMINANCLASS_H
#include "Operasi.h"

class DeterminanClass{
    private:
        float Ekspansi(float a[][N], int n);
        void Kofaktor(float a[][N], float CoFac[][N], int b, int k, int n);
    public:
        void ReduksiDeterminanKeyboard();
        void ReduksiDeterminan(float a[][N], int n);

        void EkspansiKofaktorKeyboard();
        void EkspansiKofaktor(float a[][N], int n);
};
#endif