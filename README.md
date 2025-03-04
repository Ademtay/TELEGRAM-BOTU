# GitHub Telegram Botu

Bu Telegram botu, GitHub hesabınızı Telegram üzerinden takip etmenizi sağlar.

## Özellikler

- GitHub repolarınızı listeleme
- Son aktivitelerinizi görüntüleme
- Kolay kullanımlı komutlar

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. `.env` dosyası oluşturun ve aşağıdaki değişkenleri ekleyin:
```
TELEGRAM_TOKEN=your_telegram_bot_token
GITHUB_TOKEN=your_github_personal_access_token
```

### Telegram Bot Token'ı Alma
1. Telegram'da [@BotFather](https://t.me/botfather) ile konuşun
2. `/newbot` komutunu kullanın
3. Bot için bir isim ve kullanıcı adı belirleyin
4. BotFather size bir token verecek, bunu `.env` dosyasına ekleyin

### GitHub Token'ı Alma
1. GitHub hesabınıza giriş yapın
2. Settings > Developer settings > Personal access tokens > Tokens (classic)
3. "Generate new token" seçeneğine tıklayın
4. Token'a gerekli izinleri verin (repo, user)
5. Oluşturulan token'ı `.env` dosyasına ekleyin

## Kullanım

Botu başlatmak için:
```bash
python github_bot.py
```

### Komutlar

- `/start` - Botu başlatır
- `/help` - Yardım menüsünü gösterir
- `/repos` - GitHub repolarınızı listeler
- `/activity` - Son aktivitelerinizi gösterir

## Güvenlik

- `.env` dosyasını asla GitHub'a pushlamayın
- Token'larınızı güvenli bir şekilde saklayın
- GitHub token'ınızı sadece gerekli izinlerle oluşturun 