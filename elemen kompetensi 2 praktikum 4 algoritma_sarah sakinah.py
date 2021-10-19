# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 07:23:46 2021

@author: HP
"""

print("@@@@ @@@ @@@@ @@@  @ @")
print("@    @ @ @  @ @ @  @ @")
print("@    @@@ @@@@ @@@  @ @")
print("@@@@ @@@ @@   @ @  @@@")
print("   @ @ @ @ @  @ @  @ @")
print("   @ @ @ @  @ @ @  @ @")
print("@@@@ @ @ @   @@ @  @ @")
sarah=0
while sarah==0:
    k=input('masukan list angka (integer): ')
    # nilai di dalam K yang diberi spasi # 3 5 9
    genap=[]
    ganjil=[]
    for k in k.split():
        if int(k)%2==1:
            
            genap.append(int(k))
            print('list angka tidak memiliki angka genap')
            break

        if int(k)%2==0:
                print('list angka memiliki angka genap')
                break
        else:
            print('tidak terdapat bilangan genap')
