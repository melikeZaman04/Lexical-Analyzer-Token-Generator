# DFA-based Lexical Analyzer (Java)

Bu proje, deterministik sonlu otomat (DFA) yaklaşımıyla basit bir lexical analyzer (tokenizer) ve Swing tabanlı bir görsel arayüz sağlar.

Özellikler
- Kelimeler / anahtar kelimeler `src/main/resources/keywords.csv` içinde tutulur.
- Kaynak koddan lexeme ve token tipleri çıkartılır ve her token için satır/sütun bilgisi hesaplanır.
- Satır yorumları (`//...`) ve blok yorumları (`/*...*/`) temizlenir.
- Basit bir ön işlemci: `#define NAME value` satırları okunur ve sonraki kodda `NAME` kelimeleri `value` ile değiştirilir.
- Sonuçlar Swing tablosunda gösterilir.

Nasıl çalıştırılır
1. Proje kök dizininde terminal açın (Windows PowerShell önerilir).
2. Bu kod Java 8 (1.8) çalışma zamanı ile uyumludur. Sisteminizde JDK 1.8 veya daha yeni bir JDK bulunmalıdır.
3. Derleme: `mvn compile` (Maven yüklü ise) veya IDE üzerinden derleyin.
4. Çalıştırma (IDE veya komut satırı):

   java -cp target\classes com.prodev1.Main

Veya IDE ile `com.prodev1.Main` sınıfını çalıştırın.

