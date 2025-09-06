from cryptography.fernet import Fernet
import tkinter as tk
try:
    with open('key.key', 'rb') as file:
        key = file.read()
except FileNotFoundError:
    key=Fernet.generate_key()
    with open('key.key', 'wb') as file:
        file.write(key)

f = Fernet(key)

while True:
    print("\n Seçenekler")
    print("1. Mesajı şifrele")
    print("2. Mesajı Çöz")
    print("3. Çıkış")
    choice=input("Seçininiz : ")
    if choice=="1":##Mesajı şifrelemek için olan kısım
        message=input("Şifrelenecek veriyi giriniz : ")
        message_bytes=message.encode('utf-8')
        encrypted_message = f.encrypt(message_bytes)
        print(f"Şifrelenmiş: {encrypted_message}")
    elif choice == "2":## Şifrelenmiş veriyi çözmek için olan kısım
        encrypted_message = input("Şifrelenmiş mesajı girin : ")
        try:
            decrypted_bytes = f.decrypt(encrypted_message.encode('utf-8'))
            token = decrypted_bytes.decode('utf-8')
            print(f"Şifrelenmemiş : {token}")
        except:
            print("Hata : Geçersiz şifre veya key!")

    elif choice=="3":##Programdan çıkış
        print("Programdan çıkılıyor.")
        break
    else:
        print("Geçersiz seçim, tekrar deneyiniz.")
