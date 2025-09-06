# Text-Encryption-App
A simple Python command-line tool for encrypting and decrypting messages using Fernet symmetric encryption. Automatically generates a key (key.key) on first run. Key is stored locally and should be kept safe.

# Proje klasörüne git

# Sanal ortam oluştur
python -m venv .venv

# Sanal ortamı aktive et
.venv\Scripts\activate

# Gerekli paketleri yükle
pip install cryptography

# Programı çalıştır
python main.py
