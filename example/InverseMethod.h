#ifndef INVERSEMETHOD_H
#define INVERSEMETHOD_H
#include "Operasi.h"

class InverseMethod{
    private:
        float GetX(float a[][N], float b[], int n, int x);
    public:
        void InverseSPLKeyboard();
        void InverseSPL(float a[][N], float b[], int n);
};
#endif