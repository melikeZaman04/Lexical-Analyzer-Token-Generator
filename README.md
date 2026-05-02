# Lexical-Analyzer-Token-Generator  
**Anahtar kelime CSV dosyası kullanarak kaynak kodu lexeme ve token’lara ayıran basit bir sözdizim çözümleyici**

##  Proje Hakkında  
Bu proje, belirli bir programlama dili (örneğin Java-benzeri) için kaynak kodunu okuyarak **lexeme** ve bunlara karşılık gelen **token** tiplerini çıkaran bir lexical analyzer (tokenizer) uygulamasıdır.  
Anahtar kelimeler (keywords) `keywords.csv` dosyasında tanımlanır. Proje bu tanımlara dayanarak “public”, “if”, “while” gibi kelimeleri tanır ve uygun token tiplerine çevirir.

##  Özellikler  
- `keywords.csv` dosyasındaki lexeme-token eşlemelerini okur  
- Veri tipleri, anahtar kelimeler, operatörler, semboller gibi temel token kategorilerini tanır  
- Kaynak kodda satır/sütun bilgisiyle birlikte token oluşturabilir (gerekiyorsa)  
- Basit ama genişletilebilir: DFA ya da otomata tabanlı genişleme yapılabilir  
- Uygulama dosya tabanlı ya da konsol-tabanlı kullanılabilir

