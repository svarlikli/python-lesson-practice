def health_system():
    for i in range(0,1):
        liste_tc=[]
        language_selection=input("Which language will you continue with?= Eng or Tur")
        # Maalesef ingilizce bilmediğim için türkçe yazdım..
        if language_selection=="Tur":
            print("Kovid risk sorgulama programına hoşgeldiniz...")
            print("Programa kayıt olabilmeniz için lütfen Tc numaranızı giriniz...")
            tc_no=input("Lütfen Tc Numaranızı giriniz = ")
            if len(tc_no)!=11:
                print("Tc numaranız 11 haneli olmalıdır.")
                break
            elif len(tc_no)==11:
                if not tc_no.isdigit() or int(tc_no[0])==0:
                    print("Girilen tc no 11 haneli ama yanlış bir tc numarası girdiniz...")
                    break
                elif tc_no.isdigit() and int(tc_no[0])!=0:
                    for i in tc_no:
                        liste_tc.append(int(i))
                    a= 7 * sum(liste_tc[0:10:2])
                    b= sum(liste_tc[1:9:2])
                    c=(a-b)%10
                    x=sum(liste_tc[:10])
                    y=x%10
                    if c!=liste_tc[9] or y!=liste_tc[10]:
                        print("Tc numara kriterlerine uymuyor..")
                        break
                    elif c==liste_tc[9] and y==liste_tc[10]:
                        print("Doğru giriş yaptınız. Tc numaranız sisteme kayıt oldu...")
                        print("Gireceğiniz şifre 8 karakterli olmalı. ilk iki değeri harf, diğer 6 değeri rakam olacak")
                        print("Ayrıca İlk harf büyük 2. harf küçük olacak")
                        password= input("Lütfen şifrenizi giriniz= ")
                        p=password[0:2]
                        s=password[2:8]
                        if p.isdigit() or not p.capitalize() or not s.isdigit():
                            print("Şifrenizi yanlış girdiniz!!")
                            break
                        elif p.capitalize() and not p.isdigit() and s.isdigit():
                            print("Şifrenizi doğru girdiniz. Sisteme yönlendiriliyorsunuz...")
                            print("Covid Risk analiz sistemine hoşgeldiniz.")
                            sifre_tc_kayit=input("Şifreniz ve tc numaranızı görmek ister misiniz? E/H ")
                            if sifre_tc_kayit=="E":
                                sifre=p+s
                                print(f"Şifreniz={sifre}")
                                for i in liste_tc:
                                    print(i,end="")
                            elif sifre_tc_kayit=="H":
                                print("İsteğiniz doğrultusunda tc numaranız ve şifreniz ekranda gösterilmedi..")
                            isim=input("Adınızı ve soyadınızı giriniz= ")
                            yas=int(input(f"Sayın {isim} bey lütfen yaşınızı giriniz= "))
                            if yas<0 :
                                print("Lütfen negatif bir sayı girmeyiniz!!")
                            elif yas>0 and yas<18:
                                print("Bu program 18 yaşından büyükler için hizmet vermetedir..")
                                break
                            sigara_durum=input(f"Sayın {isim} bey sigara kullanıyor musunuz? E/H")
                            if yas>18 and yas<40 and sigara_durum=="H":
                                print("Risk seviyeniz düşük-düşük.")
                            elif yas>18 and yas<40 and sigara_durum=="E":
                                print("Yaş grubu olarak risk grubunda bulunmuyorsunuz.")
                                print("Sigara içtiğiniz için vücud bağışıklığınız düşük olacaktır.")
                                print("Risk seviyeniz sigara yüzünden orta-yüksek. sigarayı bırakın!!")
                            elif yas>=40 and yas<60 and sigara_durum=="H":
                                print("Riskli bir yaş aralığınız var ")
                                print("Risk seviyeniz orta-yüksek.Sigara içmemeye devam edin... ")
                            elif yas>=40 and yas<60 and sigara_durum=="E":
                                print("Riskli bir yaş aralığınız var ")
                                print("Risk seviyeniz yüksek-yüksek.Sigarayı acilen bırakın... ")
                            elif yas>=60 and yas<90 and sigara_durum=="H":
                                print("Çok Riskli bir yaş aralığınız var. aşı sırasında önceliklisiniz.. ")
                                print("Risk seviyeniz yüksek-yüksek.Kesinlikle sigara içmemeye devam edin... ")
                            elif yas>=60 and yas<99 and sigara_durum=="E":
                                print("Çok Riskli bir yaş aralığınız var. aşı sırasında önceliklisiniz.. ")
                                print("Risk seviyeniz maximun-yüksek. Lütfen acilen sigarayı bırakın")
                                print("Sigara kullandığınız için hayati tehlikeniz var..")
                                adress=input("Sağlık ekiplerinin acil müdahalesi için Lütfen ev adresinizi giriniz = ")
                                gsm=input("Lütfen gsm giriniz= " )
                                print("adres bilgileriniz ve gsm bilgileriniz kaydedildi.")
                                print(f"Ev adresiniz={adress}\n gsm numaranız={gsm}")
