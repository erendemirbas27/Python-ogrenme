user_kullanci="7adrenalin"
user_şifre="7adrenalinn"
kullaniciadi=input("Kullanici adini gir")
şifre=input("Şifrenizi girin")


if kullaniciadi==user_kullanci :
    if şifre==user_şifre:
        print("login successful")
    else:
        print("Şifre Yanliş")
else :
    print("Kullanici adi yanliş")


