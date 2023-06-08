jenis_komponen = ["Control horn", "Push Wire Rod", "Brushless Motor", "Linkage stopper", "ESC (SW50A)", "Receiver (LA1OB RX)", "Carbon Fiber Rod" , "Servo 9g", "RC LIPO Battery", "Propeller", "FLYSKY - 16x Remote Control", "MPFF FORM 5x1000x900mm"]
harga_komponen = [3,2,17.79,12,67,61,25.30,5.20,57.56,5.50,16,23]
jumlah = [0,1,2,3,4,5,6,7,8,9,10,11]

print("   SELAMAT DATANG")
print("         KE   ")
print("KEDAI BARANGAN RC JET")

print("Harga control horn = RM3 (10 set), Push rod wire = RM2 (10 set), Brushless motor = RM17.29, Linkage stopper = RM12 (10 set), ESC (SW50A) = RM67, Receiver (LA1OB RX) = RM61, Carbon Fiber Rod 3mm = RM25.30 (16 set), Servo 9g = RM5.20, RC LIPO Battery = RM57.56, Propeller = RM5.50, FLYSKY - 16x Remote Control = RM16, MPPF FORM 5x1000x900mm = RM23")
a=int(input("Masukkan tempahan control horn = "))
b=int(input("Masukkan tempahan push rod wire = "))
c=int(input("Masukkan tempahan brushless motor = "))
d=int(input("Masukkan tempahan linkage stopper = "))
e=int(input("Masukkan tempahan ESC (SW50A) = "))
f=int(input("Masukkan tempahan bagi Receiver = "))
g=int(input("Masukkan tempahan bagi Carbon Fiber Rod = "))
h=int(input("Masukkan tempahan bagi Servo = "))
i=int(input("Masukkan tempahan bagi Lipo Battery = "))
j=int(input("Masukkan tempahan bagi Propeller = "))
k=int(input("Masukkan tempahan bagi FLYSKY remote control = "))
l=int(input("Masukkan tempahan bagi MPFF FORM = "))

tempahan = [a,b,c,d,e,f,g,h,i,j,k,l]

def jumlah_harga() :
    for i in range(4) :
        jumlah[i] = harga_komponen[i]*tempahan[i]
    return (jumlah)

def cetak() :
    print("\n\n Tempahan anda ialah = ")
    print(a, "komponen", jenis_komponen[0])
    print(b, "komponen", jenis_komponen[1])
    print(c, "komponen", jenis_komponen[2])
    print(d, "komponen", jenis_komponen[3])
    print(e, "komponen", jenis_komponen[4])
    print(f, "komponen", jenis_komponen[5])
    print(g, "komponen", jenis_komponen[6])
    print(h, "komponen", jenis_komponen[7])
    print(i, "komponen", jenis_komponen[8])
    print(j, "komponen", jenis_komponen[9])
    print(k, "komponen", jenis_komponen[10])
    print(l, "komponen", jenis_komponen[11])


    print("\n jumlah harga untuk tempahan ini ialah RM", sum (jumlah))

    print("TERIMA KASIH KERANA MEMBELI DI KEDAI KAMI")
jumlah_harga()
cetak()