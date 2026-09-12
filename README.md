# Supermarket Together Türkçe Yama — uyumluluk sürümü

Bu fork, [@ebuword'un Türkçe yamasını](https://github.com/ebuword/Supermarket-Together-TR-Yama)
güncel **Supermarket Together** sürümünde çalışacak şekilde paketler.

## İndir

En güncel kurulum dosyasını **[Releases](../../releases/latest)** sayfasından indirin.

## Düzeltilen sorunlar

- XUnity AutoTranslator **5.6.2** sürümüne güncellendi.
- Hatalı `BepInEx\BepInEx\Translation` yolu giderildi.
- Çeviri yolları BepInEx köküne göre `Translation\{Lang}\Text` olarak düzeltildi.
- Unity UI Toolkit desteği için `EnableUIElements=True` etkinleştirildi.
- TextMeshPro çevirisi etkin tutuldu.
- Kurulumdan önce üzerine yazılacak mevcut dosyalar otomatik yedekleniyor.
- Kurulum sonunda 1.600'den fazla çeviri satırı ve kritik dosyalar doğrulanıyor.

## Kurulum

1. Oyunu ve Steam'deki oyun penceresini kapatın.
2. Releases sayfasındaki `.exe` dosyasını çalıştırın.
3. Kurucu oyun klasörünü otomatik bulamazsa şu klasörü seçin:
   `...\steamapps\common\Supermarket Together`
4. **Türkçe Yamayı Kur** düğmesine basın.
5. Oyunu açın. Oyun içindeki dil **English** olarak kalmalıdır; yama İngilizce
   metinleri çalışma zamanında Türkçeye dönüştürür.

> Ayrı bir “Türkçe” dil düğmesinin görünmemesi normaldir.

## Kaynaktan test ve derleme

Gereksinim: Windows ve Python 3.11+

```powershell
python -m unittest discover -s tests -v
.\build.ps1
```

Derlenen dosya `dist\Supermarket_Together_TR_Yama_v12.27.4-fixed.1.exe`
konumunda oluşur. GitHub Actions da her değişiklikte aynı testleri çalıştırıp
Windows kurulum paketini artifact olarak üretir.

## Sürümler

- Türkçe çeviri paketi: **12.27.4** (upstream)
- Uyumluluk paketi: **12.27.4-fixed.1**
- XUnity AutoTranslator: **5.6.2**

## Atıf ve lisanslar

Çeviri çalışması: **@ebuword**. Bu fork bağımsız bir uyumluluk güncellemesidir.
Üçüncü taraf lisansları ve ayrıntılar için [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)
dosyasına bakın.
