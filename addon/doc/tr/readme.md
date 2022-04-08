# NVDA için Lambda #

* Yazan: Alberto Zanella ve the lambda-nvda team.
* [kararlı sürüm][1] indir
* [geliştirme  sürüm][2] indir

Bu proje, LAMBDA Yazılımı için bir appModule'dir. Peter Lecky'nin Comenius Üniversitesi'ndeki çalışmalarından ilham almıştır. \n
LAMBDA (Braille Cihazı ve Ses Sentezi için Matematiğe Doğrusal Erişim), görme engelli kişilerin bir braille ekranı ve/veya bir konuşma sentezleyici kullanarak matematik okumasına ve yazmasına yardımcı olan bir yazılımdır.\n
LAMBDA, bir AB Projesinin sonucudur. LAMBDA hakkında daha fazla bilgi için lütfen [https://www.lambdaproject.org/](https://www.lambdaproject.org/) adresini ziyaret edin. \n
Eklentinin mevcut sürümü, İtalyanca ve İspanyolca dilleri için braille
tablolarına sahiptir ve arayüzü, NVDA çeviri topluluğu tarafından çevrildiği
için NVDA'nın resmi dillerinin çoğunda mevcuttur. İtalyan olmayan bir LAMBDA
kullanıcısıysanız ve braille tablosunun kendi dilinize çevrilmesine katkıda
bulunmak istiyorsanız, yazarla iletişime geçmekten (aşağıya bakınız) veya
proje posta listesine abone olmaktan çekinmeyin.

**Lütfen dikkat:** Bu eklenti, Alberto Zanella tarafından gönüllü bir etkinlik olarak geliştirilmiştir. Yazar veya katkıda bulunanlar da Lambda yazılımının satışına ve/veya geliştirilmesine dahil değildir. Lambda hakkında daha fazla bilgiye veya nasıl kullanılacağına ilişkin desteğe ihtiyacınız varsa, lütfen yerel distribütörünüzle iletişime geçin. Bu eklentiyi kullanırken veya kurarken herhangi bir zorlukla karşılaşırsanız, lütfen yazarla temas kurun veya Github proje sayfasındaki "Sorunlar" bağlantısını kullanın.\n

### [Resmi Github Deposu](https://github.com/lambda-nvda/lambdaNvda/)

## Eklenti Özellikleri:

### Konuşma desteği:

* iletişim kutuları ve menüler düzgün bir şekilde raporlanır;
* Lambda matematik motorunu kullanan matematik formülleri için doğal konuşma
  desteği, yani "bileşik kök 3 ayraç bileşik kök 3 x artı 24, kapa bileşik
  kök, eksi 3 eşittir 0";
* Karakter, kelime, satır satır Okuma ve Tümünü söyleme uygulaması;
* Bir metin bloğu seçildiğinde veya genişletildiğinde (CTRL+B ve
  SHIFT+CTRL+B kullanarak) bunu belirtme;
* Standart Windows komutlarını ve Lambda'ya özgü komutları kullanarak metin
  düzenleyicide hareket ederken bunları söyler;
* Hem Genişletilmiş hem de Kısa konuşma modları desteklenir (bunu
  Lambda'daki Araçlar menüsünü kullanarak seçebilirsiniz);
* yapılandırılmış kip, hesap makinesi ve matris penceresi gibi özel iletişim
  kutuları artık doğru bir şekilde bildiriliyor ve NVDA, imleci hareket
  ettirirken veya yeni metin yazıldığında bunu doğru şekilde okuyor;
* yazarken yineleme Lambda metin işlemcisini kullanır, bu nedenle semboller
  ve işaretçiler doğru şekilde belirtilir.

### Braille desteği:

* Eklenti (kullanıcı profili dizininin içinde) kurulur ve özel bir braille
  tablosunu etkinleştirir. Bu tablo farklı diller için farklı olabilir. JAWS
  (jbt dosyası) için Lambda eklentisindekilerden özel braille tabloları
  yapılmıştır. Daha sonra semboller ve işaretler aynı nokta desenleri
  kullanılarak temsil edilir;
* Eklenti, standart bir braille yapılandırması için bir NVDA profili
  oluşturur. Bu sayede çıktı, yalnızca Lambda uygulaması etkinken özel
  braille tablosuna ayarlanır;
* iletişim kutuları ve menüler braille ile düzgün bir şekilde belirtilir;
* Editörün içeriği braille'de doğru bir şekilde oluşturulur ve kullanıcı
  braille kaydırma tuşlarını veya imleç yönlendirme tuşlarını kullanarak
  hareket edebilir;
* Eklenti 1.1.0 sürümünden başlayarak, Lambda düzenleyicisindeki metnin
  görüntülenmesinin iki yolu vardır: "Düz mod" ve "Düz olmayan Mod". "Düz
  mod" açık olduğunda, NVDA, düzenleyiciden bilgi almak ve şapka konumunu
  belirlemek için Görüntü Modelini kullanacaktır. Bu, kullanıcının beyaz
  alanlarda bile ekranda hareket etmesi gerektiğinde özellikle
  faydalıdır. "Düz Mod" "kapalı" olarak ayarlandığında, NVDA onu almak için
  Windows API kullandığından braille ekranında metin oluşturma daha
  kararlıdır. Bununla birlikte, şapka metin satırının sonundaki beyaz
  boşluklarda hareket ettirildiğinde, kullanıcı tarafından beyaz olmayan bir
  boşluk eklendiği sürece braille ekranı gerçek imleci takip etmez.

"Düz mod" varsayılan olarak etkindir. NVDA+SHIFT+F tuşlarına basarak "düz
modu" açıp kapatabilirsiniz.

Windows'ta (Özel boyutlandırma seçeneği) özel DPI kullanıyorsanız, özellikle
96 dpi'den fazla (%100'den büyük) ekran ayarlarınız varsa Düz Modu devre
dışı bırakmanızı şiddetle tavsiye ederiz.

* İletişim kutularının yapısı kolaydır, tekrarlanan bilgiler kaldırılmıştır;
* Seçim, 7 ve 8 noktalar kullanılarak doğru şekilde belirtilecek ve standart
  Windows komutlarına (SHIFT+OKLAR) veya Lambda'ya özel komutlara (CTRL+B,
  CTRL+SHIFT+B) basıldığında işaretleme düzgün bir şekilde güncellenecektir.

## Before starting to use this addon.

Bu eklenti, "lambda.exe" uygulamasıyla ilişkili "lambda" adlı bir NVDA
profili oluşturur. Profil, tüm braille seçeneklerini otomatik olarak
ayarlar: özel braille tablosu, odak bağlantısı ve düz mod ayarları.

Sisteminizde aynı ada sahip önceki bir profil varsa, eklenti bunu geçersiz
kılmaz ve yapılandırma profilinizi elle ayarlamanız gerekir.

Bu durumu önlemek için, korumak istediğiniz belirli ayarlarınız varsa,
"LAMBDA Profil Sihirbazını Geri Döndür"ü kullanabilirsiniz. Bu aracı
başlatmanın kısayolu (LAMBDA'ya odaklanıldığında) NVDA+alt+r'dir.

Eklentinin yüklenmesinden sonra "lambda" profilinin eski sürümlerini silmek
de kolay bir seçenek olabilir. Bunu yapmak için NVDA menüsünü açın,
"Yapılandırma profilleri" menü Öğesini seçin ve ENTER'a basın.

Konfigürasyon profilleri iletişim kutusunda, "lambda" profilini bulabilir ve
silebilirsiniz. Profil, Lambda uygulamasının bir sonraki başlatılışında
yeniden oluşturulacaktır.

"lambda" profilini silmek, eklenti herhangi bir sorunla karşılaştığında da
kolay bir çözüm olacaktır. Örneğin, braille tablosu uygun şekilde
ayarlanmamışsa, profili elle yapılandırmak yerine basitçe
silebilirsiniz. Lambda editörünü bir sonraki açışınızda eklenti yeni bir
tane profil oluşturacaktır.

Lambda editörü her başlatıldığında, bu eklenti "lambda" adında bir profilin
var olup olmadığını kontrol eder. yoksa, otomatik olarak aşağıdaki formda
bir profil oluşturur:

```
filename : userData\profiles\lambda.ini :

[braille]
	readByParagraph = False
	tetherTo = focus
	translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
	brailleFlatMode = True

```

konum :

* path-to-the-addon-brailleTable-dir : eklenti dizininin mutlak yolu +
  "\brailleTables"
* tableName : etkin NVDA diline bağlıdır. Şu anda yalnızca italyanca ve
  İspanyolca braille tabloları, sırasıyla "lambda-ita.utb" ve
  "lambda-esp.utb" mevcuttur.

## Eklenti Klavye Kısayolları:

* **NVDA+Shift+f**: Braille düz kipini açar veya kapatır;
* **NVDA+alt+r**: "LAMBDA Profil Sihirbazını Geri Döndür"ü açar;
* **NVDA+d**: satırları çoğaltır (kontrol+d'nin yerine bunu kullanın).

## Bilinen Sorunlar:

LAMBDA'da bulunan bir hata nedeniyle eklenti, boşlukları bildiren ekstra bir
mantık sağlar. Bu mantık aşağıdaki durumlarda başarısız olabilir:

* Metne "boşluk", "spazio" "Espacio" vb. sözcükler eklendiğinde, bunlar NVDA
  tarafından yerel NVDA dil çevirisi olarak bildirilebilir.
* LAMBDA konuşma motoru tarafından boş satırlar bildirilmez. Kullanıcı bunun
  yerine "boşluk" kelimesinin çevirisini duyacaktır. Bu, hem boş bir satır
  hem de yalnızca "boşluk" kelimesini içeren bir satır olabilir.

## Yaralı ipuçları:

Bu, eklentiyi daha verimli bir şekilde kullanmanıza yardımcı olacak bir dizi
ipucudur.

* Karakter karakter bildirim: Normalde matematikle çalışırken NVDA'nın
  yazdığınız şeyleri karakter karakter bildirmesini istersiniz. Bunu yapmak
  için birkaç basit adım vardır: LAMBDA'nın penceresine veya varyantlarından
  birine odaklandığınızdan emin olun (örneğin altı nokta gösterimi);
  NVDA+2'ye (numara sırasındaki iki) basın veya NVDA menüsü>Tercihler>Klavye
  ayarları'na gidin ve Yazılan karakterleri seslendir kutusunu işaretleyin;
  LAMBDA>Seçenekler>Ses parametreleri'ne gidin ve "yinele" onay kutusunun
  AÇIK olduğundan emin olun, aksi takdirde NVDA siz yazarken konuşma
  motorundan hiçbir şey almaz. Ve bittiğinde, NVDA yazılan karakterleri
  söyleyecektir, ama kaygılanmayın , sadece LAMBDA'da veya onun özel
  pencerelerinde, bu ayar geçerli olacaktır diğer uygulamaların ayarları
  olduğu gibi kalacaktır.

## Eklenti ileti grubu:

Hataları, önerileri bildirmek veya katkıda bulunmak istiyorsanız Addon
Grubuna (İngilizcedir), abone olabilirsiniz. abone olmak için şu web
sitesini kullanın: <https://groups.io/g/lambda-nvda>.

## Logu değiştir

Aşağıda, farklı eklenti sürümleri arasındaki değişikliklerin bir listesi
bulunmaktadır. Sürüm numarasının yanında, parantezler arasında geliştirme
durumu bulunur. Mevcut geliştirme sürümü, kararlı olarak işaretlenene veya
aday olarak atılana kadar değişebileceğinden dahil edilmemiştir.

### Sürüm 1.3.0 (kararlı)

* NVDA'nın daha yeni sürümü için destek (Python 3 Desteği)
* Boş bir satırda satır çoğalt komutu NVDA+d'ye basıldığında pano içeriğinin
  yapıştırılmasına neden olan bir sorun çözüldü. Şimdi NVDA+d'ye
  bastığınızda ve boş bir satırda olduğunuzda, beklendiği gibi yeni bir boş
  satır görünür.

### Sürüm 1.2.2 (kararlı)

* WX Python sürüm  4 ile uyumluluk (NVDA 2018.3 ile gelmiştir). wx.NewId()
  uyarısı artık ayıklama kayıtlarında gösterilmemektedir.
* iletişim kutularının görünümünü geliştirmek için grafik arayüzlü yardım
  uygulandı.
* Yeni diller. Çeviriler güncellendi.

### Sürüm 1.2.1a (kararlı)

Bu güncellemenin uzun vadeli bir destek sürümü olması amaçlanmıştır. Bu, en
azından Haziran 2018'e kadar bunun kadar kararlı bir sürüm yayınlanmayacağı
anlamına gelmektedir. Öğrencilere üst düzey istikrar sağlamak ve akademik
yıl boyunca değişiklikleri en aza indirmek için yapılmıştır.

* Yeni diller. Çeviriler güncellendi.

### Sürüm 1.2.1 (kararlı)

* NVDA 2017.3'ün braille'i yönetmek için kullandığı yöntemle uyumluluk
  eklendi. Geriye dönük uyumluluk korundu.
* birçok braille sorunu düzeltildi.

### Sürüm 1.2.0 (geliştirme)

1.2.1 sürümü önemli düzeltmeler içerdiğinden bu sürüm kararlı olarak
yayınlanmadı.

* Yeni yerel ayarlar. Güncellenmiş yerelleştirmeler.

### Sürüm 1.1.8 (kararlı)

* İlk kararlı sürüm.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=lambda

[2]: https://addons.nvda-project.org/files/get.php?file=lambda-dev
