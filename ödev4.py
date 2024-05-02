import sqlite3

def benzerlik_orani(metin1, metin2):
    # Adım 1: Metinleri karakterlerine ayır
    karakterler1 = list(metin1)
    karakterler2 = list(metin2)
    
    # Adım 2: Her bir metnin ASCII değerlerini topla
    toplam1 = sum(ord(karakter) for karakter in karakterler1)
    toplam2 = sum(ord(karakter) for karakter in karakterler2)
    
    # Adım 3: Toplam ASCII değerlerini karşılaştır
    # Benzerlik oranını hesapla: 1 - (fark / maksimum toplam)
    benzerlik_orani = 1 - abs(toplam1 - toplam2) / max(toplam1, toplam2)
    
    return benzerlik_orani

# Test metinleri
metin1 = "Bu bir metin örneğidir."
metin2 = "Bu da bir örnek metindir."

# Benzerlik oranını hesapla
benzerlik = benzerlik_orani(metin1, metin2)
print("Metinlerin benzerlik oranı:", benzerlik)

# Veritabanı bağlantısını kur
baglanti = sqlite3.connect('benzerlik_veritabani.db')
imlec = baglanti.cursor()

# Tabloyu oluştur (eğer daha önce oluşturulmadıysa)
imlec.execute('''CREATE TABLE IF NOT EXISTS BenzerlikDurumu
             (metin1 TEXT, metin2 TEXT, benzerlik_orani REAL)''')

# Benzerlik durumunu veritabanına ekle
imlec.execute("INSERT INTO BenzerlikDurumu (metin1, metin2, benzerlik_orani) VALUES (?, ?, ?)",
              (metin1, metin2, benzerlik))

# Değişiklikleri kaydet
baglanti.commit()

# Bağlantıyı kapat
baglanti.close()
