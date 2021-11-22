

def Tukar(array, index, baris, kolom):
    temp = 0
    for i in range(kolom):
        temp = array[baris-1][i]
        array[baris-1][i] = array[index][i]
        array[index][i] = temp

def pivot(array,index,baris,kolom):
    Elemen_pvt1=0
    Elemen_pvt2=0
    for i in range(baris):
        if array[index][i]==0:
            Elemen_pvt1+=1
            break
    for j in range(baris):
        if array [baris-1][i]==0:
            Elemen_pvt2 += 1
            break

    if Elemen_pvt1>Elemen_pvt2:
        return True
    else:
        return False

    




Row = int(input('Masukan Jumlah Baris ='))
Coloumn = int(input('Masukan Jumlah Kolom ='))

matriks = []
for i in range(Row):
    matriks.append([])
    for j in range(Coloumn):
        matriks[i].append(
            int(input('Masukan Elemen array['+str(i)+']['+str(j)+'] =')))


for i in range(Row):

    for j in range(Coloumn):

        print(matriks[i][j], end=" ")
    print()
print()

x=0
y = 0

for i in range((Row)):
    
    for index_kons in range(Coloumn):
        if matriks[i][index_kons]!=0:
            
            kons=matriks[i][index_kons]
            break

    for j in range(Coloumn):
        matriks[i][j]/=kons
        
    for k in range((i+1),Row) : 
        
        if (k<Row-1 and matriks [k+1][index_kons-1]!=0) or matriks [k][Coloumn-1]==0:
            for r in range (Row):
                temp=matriks[k][r]
                matriks[k][r]=matriks[Row-1][r]
                matriks[Row-1][r]=temp
        if matriks[k][index_kons] == 0:
            continue
        kons2=matriks[k][index_kons]
        for l in range(index_kons,Coloumn):
            matriks[k][l]=matriks[k][l]-(kons2*matriks[i][l])
    
x=[0]*Row
x[Row-1]=matriks[Row-1][Coloumn-1]/matriks[Row-1][Coloumn-2]


for i in range(Row-2,-1,-1):
    x[i]=matriks[i][Row]
    for j in range(i+1,Row):
        x[i]=x[i]-matriks[i][j]*x[j]
        
    x[i]=x[i]/matriks[i][i]
    

for i in range(Row):
    print(x[i])




            
for i in range(Row):

    for j in range(Coloumn):

        print(float(matriks[i][j]), end=" ")
    print()
