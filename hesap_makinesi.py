import os
os.system("cls")
sy1 = float(input("lütefen 1. deyeri giriniz: "))
os.system("cls")
if bool(sy1):
    sy2 = float(input("lütfen 2. deyeri giriniz: "))
    os.system("cls")
    if bool(sy2):
        print(40 * "=")
        print("toplama sonucu       :",sy1+sy2)
        print("çarpma sonucu        :",sy1*sy2)
        print("çıkatma sonucu       :",sy1-sy2)
        print("bölme sonucu         :",sy1/sy2)
        print(40 * "=")
    else:
        os.system("cls")
        print("boş bir değer girdiniz")
else:
    print("boş bir değer girdiniz")
input("çıkmak için bur tuşa basın")