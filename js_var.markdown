"=========== Meta ============
"StrID : 102
"Title : Javascript Acayiplikleri - var
"Slug  : javascript-acayiplikleri-var
"Cats  : Genel, Javascript, Web
"Tags  : javascript, js
"=============================
"EditType   : post
"EditFormat : Markdown
"BlogAddr   : http://makkalot.com/
"========== Content ==========
Eskiden hep javascript ile çalışırken bir değişken kullanacağım zaman 
öncelikle _"var"_ ile tanımlamam(declaration) söyleniyordu. Nedenini pek 
anlamasam ve öğrenmeye çalışmasam da(js Java'nın aynısı ya!) genelde 
değişken tanımlarken _"var"_ kullandım. Fakat javascript Python gibi

<pre lang="javascript">
a = 12;
</pre>

dememize izin veriyor aslında. Peki neden bu şekildeki kullanımdan 
kaçınmak gerekiyor? Bütün iş javascript'te block scope kavramının 
olmamasından kaynaklanıyor. Javascript'te bunun yerine function 
scope var. Peki bu ne demek ?

Block scope olan dillerde scope içeresindeki değişkenler block 
scope'nin dışında tanımsız oluyor. Örneğin C'de

<pre lang="c">
{
    int a = 15;
}
</pre>

dediğimizde, a bu block'un dışında tanımsız olacaktır. Javascript'te bu 
tür bir kısıtlama yok :

<pre lang="javascript">
function f(){
    {
        var a = 12;
    };
    
    console.log("a : "+a);
    
};

f();

a : 12
</pre>

Görüldüğü üzere _"a"_ bir block içeresinde olmasına rağmen, block'un dışında 
da değerini hala koruyor. Burdan da anlaşıldığı gibi Javascript'te block 
yapısının görsellikten başka bir espirisi yok.

Peki function scope nasıl oluyor ?
Javascript'te fonksyon içeresinde bir değişkeni _"var"_ ile tanımladığınız 
zaman bu değişken fonksyon dışından erişelemiyor. Örneğin :

<pre lang="javascript">
loc = 11;

function f(){
    var loc = 10;
    console.log("Local "+loc);
};

f();

console.log("Global : "+loc);

Local 10
Global : 11
</pre>

Bu tür bir davranış diğer dillerde zaten ön tanımlı olarak geliyor.
C, Python, Java vs fonksyon içeresinde tanımlanan değişkenler dışarıdan erişelemiyor.

Peki neden _"var"_ kullanalım o zaman ?
En önemli nedeni, bir fonksyon içeresinde bir değişkeni var ile kullanmayıp drek 
olarak kullanırsak :

<pre lang="javascript">
a = 12
</pre>

Bu değişken artık global değişken olarak erişime açılıyor, yani function scope 
kavramının dışına çıkıyor. Örneğin :

<pre lang="javascript">
function g(){
    gv = 12;
}

g();

console.log("Outside : "+gv);

Outside : 12
</pre>

Bu şekildeki bir kullanım, oldukça sakıncalı görünüyor. En büyük nedeni 
global değişkenlerden herhangi birinin değerini yanlışlıkla değiştirme 
olasılığından geliyor. Bu tür hataların nedenini bulmak oldukça zor oluyor.


Javascriptin bu özelliği gerçekten çok ilginç, onu geliştirenler bu 
özelliği implemente ederken ne düşünüyorlardı acaba ?
