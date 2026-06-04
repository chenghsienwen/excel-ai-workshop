#!/usr/bin/env python3
"""
Encrypt/decrypt the Slidev theme tgz for safe storage in a public repo.

The key never touches the repo — store it as a GitHub Actions secret (THEME_FERNET_KEY).

Usage:
    # Generate a key (run once, save the output as the THEME_FERNET_KEY secret):
    python crypt_theme.py --keygen

    # Encrypt: slidev-theme-viewsonic-proav-0.1.0.tgz → slidev-theme-viewsonic-proav-0.1.0.tgz.enc
    python crypt_theme.py --encrypt

    # Decrypt: slidev-theme-viewsonic-proav-0.1.0.tgz.enc → slidev-theme-viewsonic-proav-0.1.0.tgz
    python crypt_theme.py --decrypt
"""

import argparse
import os
from pathlib import Path

try:
    from cryptography.fernet import Fernet
except ImportError:
    raise SystemExit("Run: pip install cryptography")

ROOT = Path(__file__).parent
TGZ = ROOT / "slidev-theme-viewsonic-proav-0.1.0.tgz"
ENC = ROOT / "slidev-theme-viewsonic-proav-0.1.0.tgz.enc"


def _fernet() -> Fernet:
    key = os.environ.get("THEME_FERNET_KEY")
    if not key:
        raise SystemExit("THEME_FERNET_KEY environment variable is not set.")
    return Fernet(key.encode())


def encrypt():
    if not TGZ.exists():
        raise SystemExit(f"Missing: {TGZ}")
    token = _fernet().encrypt(TGZ.read_bytes())
    ENC.write_bytes(token)
    print(f"Encrypted → {ENC.name}")


def decrypt():
    if not ENC.exists():
        raise SystemExit(f"Missing: {ENC}")
    data = _fernet().decrypt(ENC.read_bytes())
    TGZ.write_bytes(data)
    print(f"Decrypted → {TGZ.name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--keygen", action="store_true", help="Print a new Fernet key")
    group.add_argument("--encrypt", action="store_true", help="tgz → tgz.enc")
    group.add_argument("--decrypt", action="store_true", help="tgz.enc → tgz")
    args = parser.parse_args()

    if args.keygen:
        print(Fernet.generate_key().decode())
    elif args.encrypt:
        encrypt()
    else:
        decrypt()
