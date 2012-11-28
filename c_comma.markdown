"=========== Meta ============
"StrID : 231
"Title : C ve Virgül Operatörü
"Slug  : 
"Cats  : C, Sistem Programlama
"Tags  : c, comma, system, virgül
"=============================
"EditType   : post
"EditFormat : Markdown
"BlogAddr   : http://makkalot.com/
"========== Content ==========
**C** programlama dilini günlük işlerimde pek fazla kullanmıyorum. Ama
zaman buldukça hep onunla alakalı bilgilerimi genişletmeye çalışıyorum.
Genelde C öğretilirken, sıra operatör önceliklerine gelince hatırlayamazsanız
parantez kullanın diyorlardı(hocalarımız). Fakat büyük ve profesyonel 
projelerdeki C kodlarını yazan insanlar bu kuralları çok iyi bilip
yuttukları için, bu tür bilgisizlikten doğan parantez kullanımını
göremezsiniz. Bu durumda da bizim gibi dili tam bilmeyenler kodu bazen
anlamakta güçlük çekebiliyor.

Bazı projelerde virgül operatörünün değişik kullanımlarını görüyorum.
C'de virgül operatörünün değişik anlamları olabiliyor. Örneğin bir fonksyon
çağırırken :

<pre lang="c">
important(a, b, c);
</pre>

Buradaki kullanımda virgülün pek bir anlamı yok, sadece parametreleri birbirinden
ayırmak için kullanılıyor. C'de virgül operatörü önceliği en düşük olan operatör.
Önceliği **=**'den bile düşük. Ayrıca, virgül operatörü binary bir operatör. Peki bu
ne demek? Bunun anlamı, kullanmak için 2 tane operandınızın olması gerekir demek.
(Yani 3 + 5 'teki **+** gibi). Çalışma şekli de şöyle; önceki soldaki operandın değeri
alınıp atılır, sonra sağdaki operandın değeri alınır ve geriye sağdakinin değeri döndürülür.
Örnek verecek olursak :

<pre lang="c">
int a;
a = (3 + 5, 4 * 5);
</pre>

Yukarıda verdiğimiz tanıma göre a'nın değeri 20 olacak. Peki neden parantez içine
koyduk tüm ifadeyi ? Dediğimiz gibi virgül'ün önceliği **=** operatöründen düşük.Şöyle
olsaydı :
 
<pre lang="c">
int a;
a = 3 + 5, 4 * 5;
</pre>

a'nın değeri 8 olacaktı.

Peki bu tür bir kullanımın ne yararı var bize ? Yararını pek anlayamasam da
bazen bu kullanımı makrolarda görüyorum. Örneğin aynı satırda 2 fonksyon çağırıp
2.'nin değerini geri döndürmek istersek bu şekilde kullanabiliriz. Örneğin :

<pre lang="c">
#define evalme(INPUT) (logger(INPUT), inc(INPUT))

void logger(int input){
    printf("Log Value is : %d \n",input);
}

int inc(int input){
    return ++input;
}

int main(int argc, char *argv[]){
    int a;
    a = evalme(5);
    printf("Value is : %d\n", a); 

}


//Output :
//Log Value is : 5
//Value is : 6

</pre>


Evet, virgül operatörünün neden bu şekilde kullanıldığını anlayamazsam da
nasıl kullanıldığını öğrenmiş oldum. Gerek var mı, yok bence ...
