"=========== Meta ============
"StrID : 102
"Title : Python defaultdict Maceraları
"Slug  : python-defaultdict-maceralari-2
"Cats  : Python
"Tags  : defaultdict, python
"=============================
"EditType   : post
"EditFormat : Markdown
"BlogAddr   : http://makkalot.com/
"========== Content ==========
Python'da hash(dictionary)'lerle çalışırken bir değer dict içinde değilse ona
önceden tanımlı bir değer vermemiz gerekebilir. Örneğin bir yazı içeresinde
geçen sözcüklerin kaç defa tekrarlandığını bulmak istiyorsak, şöyle birşey
yaparız :

<pre lang="python">
d = {"one":1, "two":2}

if not d.has_key("three"):
    d["three"] = 0

d["three"] +=1 

</pre>

Bunun yerine şöyle birşey yapabiliyor olsak daha güzel olurdu :

<pre lang="python">
    d["three"] += 1
</pre>

İşte bu tür bir kullanımı mümkün kılan defaultdict var :

<pre lang="python">
from collections import defaultdict
</pre>


Önceki örneği defaultdict ile yaparsak şöyle birşey olur :

<pre lang="python">
d = defaultdict(int, one=1, two=2)
d["three"] += 1

print d
defaultdict(<type 'int'>, {'three': 1, 'two': 2, 'one': 1})
</pre>

defaultdict aynen normal bir dictionary gibi davranıyor. Fakat, ondan farklı
olarak bir değeri alırken eğer o değer dictionary içeresinde yoksa, ona baştan
verdiğimiz fonksyonu çağırıp ondan dönen değeri set ediyor.

Nasıl mı ? Örnek verecek olursak :

<pre lang="python">
In [8]: d = defaultdict(lambda:"<missing_value>", {"name":"ali", "age":22})

In [9]: d
Out[9]: defaultdict(<function <lambda> at 0x93658ec>, {'age': 22, 'name': 'ali'})

In [10]: d["age"]
Out[10]: 22

In [11]: d["surname"]
Out[11]: '<missing_value>'
</pre>

Burada defaultdict'e ilk parametre olarak lambda verdik ve içeresinde olmayan bir değer istendiğinde bize "missing_value" değerini döndürdü.

defaultdict'in koduna bakmadım, ama büyük ihtimalle şöyle birşey [yapıyordur](http://code.activestate.com/recipes/523034/).


Bir müşteri için çalıştığım bir projede bir ayar dosyasını(json) okuyup normal bir objeymiş gibi erişmek istiyordum. Örnek olarak :

<pre lang="python">

conf_dict = {
    "logf":"/home/some/path",
    "dbsettings":{
        "port":5001,
        "address":"localhost"
        }
    }
</pre>

Gibi bir Python dictionary olsun ve biz buna normal bir objeymiş gibi erişebillim, şöyleki :

<pre lang="python">
conf_dict.logf
conf_dict.dbsettings.port = 5002
</pre>

Bu tür bir kullanımı mümkün kılmak için defaultdict kullanıp \_\_setattr\_\_ ve \_\_getattr\_\_ fonksyonlarını ezdim(override) :

<pre lang="python">
class DefDict(defaultdict):
    def __setattr__(self, name, value):
        self[name] = value
    def __getattr__(self, name):
        return self[name]
    def __repr__(self):
        def _dicts(d):
            if getattr(d,"iteritems",None):
                return {k: _dicts(v) for k,v in d.iteritems()}
            else:
                return d
        return str(_dicts(self))
</pre>


Sadece bu şekilde kullanırsak pek işimize yaramayacak çünkü iç içe girmiş
yapılara erişim sağalayamacak. Yani bir değer bulunamadığında tekrar DefDict
objesi döndürmemiz gerekir. Şöyle:

<pre lang="python">
def attrdict(*args, **kw):
    return DefDict(attrdict, *args, **kw)
</pre>

Fonksyon recursive, yani her değer bulamayışında bulamadığı değere DefDict
objesi atayacak.(Başta bakınca biraz karışık görünüyor, ama biraz zaman verin
gözünüz alışacaktır.)

Şimdi bu yapıyı bu şekilde kullanabiliriz :

<pre lang="python">
if __name__ == "__main__":
    d = attrdict()
    d.name = "Brave"
    d.last_name = "Heart"
    print d
    d.friends.best = "Linux"
    print d
    #Output:
    defaultdict(<type 'int'>, {'book_1': 12, 'book_2': 111})
    {'last_name': 'Heart', 'name': 'Brave'}
    {'last_name': 'Heart', 'friends': {'best': 'Linux'}, 'name': 'Brave'}
</pre>

Gerçekten kullanım olarak çok kolaylık sağlıyor, ayrıca isterseniz normal
dictionary gibi de kullanmaya devam edebilirsiniz.

Bu tür bir yapının şöyle bir de dezavantajı var. Her bulamadığı değer için
yeni bir DefDict yapısı oluşturduğu için, siz bulunamayan bu değere atama
yapmasanız da o alt tarafta oluşturuluyor :

<pre lang="python">

if d.enemies.worst:
    print "The enemy is :",d.enemies.worst


#The problem ?
print "Problem : ",d

#Output:
Problem :  {'last_name': 'Heart', 'friends': {'best': 'Linux'}, 'name': 'Brave', 'enemies': {'worst': {}}}
</pre>

Bu sorunu çözmeyi başaramadım, bulan varsa lütfen yorumlara yazsın.
