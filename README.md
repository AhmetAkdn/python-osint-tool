Bu proje, Python ile geliştirdiğim **basit bir OSINT aracı**.  
Yani bir domain ya da IP giriyorsun ve sana onun hakkında bilgiler topluyor.  

   Neler yapıyor?
- Domain → IP’ye çeviriyor
- IP üzerinden ülke, şehir, internet sağlayıcı gibi bilgiler gösteriyor
- Domain WHOIS bilgilerini alıyor (registrar, name server, oluşturulma ve bitiş tarihleri)
- URL girersen otomatik domaini ayıklıyor
- Basit ve kullanımı kolay bir komut satırı arayüzü var

   Nasıl kullanılır?
1. Python 3 yüklü olduğundan emin ol.
2. Gerekli kütüphaneleri kur:
```bash
pip install python-whois requests

```powershell
python osint.py

Uyarı ⚠️

Bu aracı sadece eğitim amaçlı ve kendi sistemlerini test etmek için kullan.
İzinsiz sistemlerde denemeler yapmak yasal sorunlara yol açabilir.

