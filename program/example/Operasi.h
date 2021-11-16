#ifndef OPERASI_H
#define OPERASI_H
#define N 100

class Operasi{
    public:
        static float OperasiBarisElementer(float a[][N], float b[], int m, int n, int ganti, int* swap);
        static float OBE_Inverse(float a[][N], int n);
        static void TukarBaris(float a[][N], int n, int y1, int y2, int* swap);

        static void BackwardPhase(float a[][N], int m, int n);

        static float GetDeterminant(float a[][N], int n, int t);
};
#endif