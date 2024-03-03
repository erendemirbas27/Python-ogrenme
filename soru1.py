import time

kasa=1400
çekilecekpara=int(input("Kaç lira çekmek istiyorunuz"))


if çekilecekpara<5:
    print("Demir paralar çekilmez")

elif çekilecekpara>kasa:
    print("Yeterli para olmadiği için çekemezsiniz")

else:
    kasa-=çekilecekpara

print("Kalan para",kasa)

################################################3
if kasa % 2 ==0 :
    print("kalan para çifttir")
    
else :
    print("kalan para tektir")

time.sleep(10)