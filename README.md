# Python ile kütüphanesiz yapay sinir ağı kodlama

Projede kullanılan veri tabanı : https://www.kaggle.com/rishidamarla/cancer-patients-data

Kod sayfalarını isimlendirme ara katmanda kullanılan nöron sayısına göre yapılmıştır.
5 ara katman nöronu için 5N, 10 ara katman için 10N şeklindedir.

Örnek yapay sinir ağı modeli aşağıdaki gibidir.

![ANN](https://user-images.githubusercontent.com/70907491/106336721-93451680-62a0-11eb-926f-490e858dd79a.PNG)


# Nasıl çalışır?


1- Başlangıçda forEğitim.py ve forTest.py kodlarındaki gibi veriyi içe aktarma, işleme ve normalize etmek
2- Ratgele ağırlık ve bias değerleri oluşturulmalı. Bu kısım veri setine ve kullanılan ara katmanlara göre farklılık gösterir.
3- İstenilen epoch sonucu çalıştırıldıktan sonra ekrandaki ağırlık değerleri ile test.py kodları çalıştırılmalı



Ağın eğitimi tamamlandıktan sonra test edilen ağırlık ve biaslara göre ağ %94 doğruluk ile tahmin yapmaktadır.

![image](https://user-images.githubusercontent.com/70907491/106336967-10708b80-62a1-11eb-941e-333b05e585f8.png)
