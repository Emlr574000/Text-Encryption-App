# EncryptedFile

A simple Python command-line tool for encrypting and decrypting messages using Fernet symmetric encryption.

## Features

- Encrypt messages easily from the terminal.
- Decrypt messages with the same key.
- Automatically generates a `key.key` file on first run.
- Key is stored locally and must be kept safe. If the key is lost, encrypted messages cannot be recovered.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Emlr574000/EncryptedFile.git

cd EncryptedFile

(Optional)

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

Dependencies:
pip install cryptography


python main.py
