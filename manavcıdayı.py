armut=60
mandalina=60
limon=60
elma=60

print(" armut almak için 1 \n mandalina almak için 2 \n limon almak için 3 \n elma almak için 4 ")

def yok():
    print("Yetreli stok yoktur")

sipariş=int(input("Sipariş numarasini giriniz"))
miktar=int(input("Almak istediğiniz miktari giriniz"))
if  sipariş==1:
    if miktar<armut:
        armut-=miktar
    else:
        yok()


elif sipariş==2:
    if miktar<mandalina :
        mandalina-=miktar
    else:
        yok()

elif sipariş==3:
    if miktar<limon :
        limon-=miktar
    else:
        yok()

elif sipariş==4:
    if miktar<elma :
        elma-=miktar
    else:
        yok()

print("Kalan armut=",armut)
print("Kalan mandalina=",mandalina)
print("Kalan limon=",limon)
print("Kalan elma=",elma)


