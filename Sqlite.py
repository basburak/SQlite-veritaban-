import sqlite3

con=sqlite3.connect("kütüphane.db")

cursor=con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa sayısı İNT)")
    con.commit()
def veri_ekle():
    cursor.execute("insert into kitaplık Values('istanbul hatırası','ahmet ümit','everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayınevi,sayfa):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa))
    con.commit()
    
def verileri_al():
    cursor.execute("select * from kitaplık")
    liste= cursor.fetchall()
    print("kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("select İsim,Yazar from kitaplık")
    liste= cursor.fetchall()
    print("kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)

def verileri_al3(yayınevi):
    cursor.execute("select * from kitaplık where Yayınevi= ?",(yayınevi,))
    liste= cursor.fetchall()
    print("kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)

def verileriguncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("Update kitaplık set Yayınevi=? Where Yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()
    
def verileriguncelle(eski_sayfa,yeni_sayfa):
    cursor.execute("Update kitaplık set Sayfa=? Where Sayfa = ?",(yeni_sayfa,eski_sayfa))
    con.commit()
def verilerisil(yazar):
    cursor.execute("Delete from kitaplık where Yazar =?",(yazar,))
    con.commit()


isim=input("isim : ")
yazar=input("yazar : ")
yayınevi=input("yayınevi : ")
sayfa= int(input("sayfa : "))
veri_ekle2(isim,yazar,yayınevi,sayfa)




con.close()
