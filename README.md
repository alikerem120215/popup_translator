# 🇹🇷 ➔ 🇬🇧 macOS Minimalist Pop-up Çeviri Uygulaması

Panodaki (`pbpaste`) metni otomatik algılayıp Türkçe-İngilizce çevirisini fare imlecinin yanında küçük, modern bir pop-up pencerede gösteren minimalist macOS uygulaması.

---

## 🌟 Özellikler
- **Parmak Boyutunda Tasarım:** Ekranı kaplamayan, modern Dark Mode (Catppuccin Mocha) arayüz.
- **Otomatik Pano Okuma:** `Cmd + C` ile kopyaladığınız metni anında algılar.
- **Otomatik Kopyalama:** Çevrilen İngilizce metni otomatik olarak panonuza geri kopyalar.
- **Kolay Kapatma:** `ESC` tuşuna basarak veya pencereye tıklayarak anında kapanır.
- **En Üstte Kalma (`Topmost`):** Her zaman aktif uygulamanın üstünde görünür.
- **Otomatik Dili Algılama:** Metin Türkçeyse İngilizceye, İngilizceyse Türkçeye akıllı dönüşüm sağlar.

---

## 🚀 Hızlı Kurulum

Terminal'de proje klasörüne gidip kurulum betiğini çalıştırın:

```bash
cd /Users/alikeremguvenc/Documents/Kodus/popup_translator
./install.sh
```

---

## ⌨️ macOS Kestirmeler (Shortcuts) ile Sistem Genelinde Kısayol Atama

Betiği sistem genelinde **Option + Space** veya **Option + T** ile tetiklemek için aşağıdaki adımları uygulayın:

### 1. Kestirmeler Uygulamasını Açın
- `Cmd + Space` ile Spotlight'ı açın, **Kestirmeler** (*Shortcuts*) yazıp çalıştırın.

### 2. Yeni Kestirme Oluşturun
- Sağ üstteki **`+`** butonuna tıklayın.
- Sol üstteki isme **"Hızlı Çeviri"** yazın.

### 3. Shell Script Eylemini Ekleyin
- Sağ paneldeki arama çubuğuna **"Kabuk Betiğini Çalıştır"** (*Run Shell Script*) yazın ve çift tıklayın.
- Kod kutusuna şu komutu yapıştırın:
  ```bash
  /Users/alikeremguvenc/.popup_translator/run_translator.sh
  ```
  *(Not: macOS Güvenliği `Documents` klasörüne Kestirmeler erişimini engelleyebildiği için script `~/.popup_translator` dizinine taşınmıştır.)*

### 4. Klavye Kısayolunu Bağlayın (`Option + Space` veya `Option + T`)
- Sağ paneldeki **İzleme / Ayrıntılar** (`i` simgesi) sekmesini açın.
- **"Klavye Kısayolu Ekle"** (*Add Keyboard Shortcut*) seçeneğine tıklayın.
- Klavyenizde **`Option + Space`** veya **`Option + T`** tuş kombinasyonuna basın.

---

## 🎯 Kullanım Rehberi

1. Herhangi bir metni seçip **`Cmd + C`** ile kopyalayın.
2. **`Option + Space`** (veya **`Option + T`**) tuşlarına basın.
3. Fare imlecinizin yanında minimalist pop-up açılır ve çeviriyi gösterir.
4. Çevrilen metin panonuza kopyalanmış durumdadır; **`Cmd + V`** ile doğrudan yapıştırabilirsiniz.
5. **`ESC`** tuşuna basarak veya pop-up'a tıklayarak pencereyi kapatabilirsiniz.
