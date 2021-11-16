#ifndef MENUCLASS_H
#define MENUCLASS_H
class MenuClass{
    public:
        void Menu();
            void Pertama();
                void Gauss();
                void GaussJordan();
                void Inverse();
                void Cramer();
            void Kedua();
                void Reduksi();
                void Ekspansi();
            void Ketiga();
                void Balikan();

        void FileMatrix();
        void MatrixHasil(float a[][100], float b[]);
};
#endif