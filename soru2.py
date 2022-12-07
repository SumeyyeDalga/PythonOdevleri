import numpy as np     # kütüphaneler eklendi.
import numpy as plt

ornekler = "herhangi_bir_bilgisayar_dosyası" ##burada değişken ataması yapmıştır. herhangibirbilgisayardosyası nı ornekler e atamış.

X = ornekler [:0] ## ornekleri atadığı kelimenin başlangıcından indexi sıfır olan harfe kadarki yerin listesini X e atamıştır.
Y = ornekler [:1] ## ornekleri atadığı kelimenin başlangıcından indexi bir olan harfe kadarki yerin listesini  Y ye atamıştır.

mean_x = np.mean (X) # X listesindeki değerlerin ortalamasını alır.
mean_y = np.mean (Y) # Y listesindeki değerlerin ortalamasını alır.

m=len(X) # X in uzunluğunu almış.

numerator = 0   #Bölünen 
denominator = 0 #Bölen

for i in range (m):   
    numerator += (X[i]-mean_x) + (Y[i]-mean_y) # herbir x ve y değerlerinden tüm x ve y değerlerinin ortalamasını çıkarıp toplama yapılmıstır. 
    denominator += (X[i]-mean_x) ** 2   # her bir x değerinden x değerlerinin ortalamasını cıkarıp karesini almış.

m= numerator / denominator
c= mean_y - (m*mean_x)

print(f'm={m} c = {c}')   # çizelecek doğrunun denklemini oluşturma.

max_x = np.max(X)  # X in max değeri
min_x = np.min(Y)  # X in min değeri

x = np.linspace (min_x , max_x)   
y = c + m * x 

plt.plot(x,y,'g',label = 'Cizgi')
plt.plot(X,Y, 'rx', label = 'Veriler')


plt.xlabel ("İlk sütundaki veri")
plt.ylabel ("İkinci sütundaki veri")   
plt.legend()
plt.show()

