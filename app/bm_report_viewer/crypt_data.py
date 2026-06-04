#!/usr/bin/env python3
"""
Encrypt/decrypt CSV files for safe storage in a public repo.

The key never touches the repo — store it as a GitHub Actions secret (FERNET_KEY).

Usage:
    # Generate a key (run once, save the output as the FERNET_KEY secret):
    python crypt_data.py --keygen

    # Encrypt: reads input/*.csv  →  writes input_enc/*.enc
    python crypt_data.py --encrypt

    # Decrypt: reads input_enc/*.enc  →  writes input/*.csv
    python crypt_data.py --decrypt
"""

import argparse
import os
from pathlib import Path

try:
    from cryptography.fernet import Fernet
except ImportError:
    raise SystemExit("Run: pip install cryptography")

APP_DIR = Path(__file__).parent
INPUT_DIR = APP_DIR / "input"
ENC_DIR = APP_DIR / "input_enc"

CSV_FILES = [
    "raw_report.csv",
    "layer1_report.csv",
    "layer2_report.csv",
    "layer3_segmentation.csv",
    "layer3_timeseries.csv",
]


def _fernet() -> Fernet:
    key = os.environ.get("FERNET_KEY")
    if not key:
        raise SystemExit("FERNET_KEY environment variable is not set.")
    return Fernet(key.encode())


def encrypt():
    f = _fernet()
    ENC_DIR.mkdir(exist_ok=True)
    missing = [n for n in CSV_FILES if not (INPUT_DIR / n).exists()]
    if missing:
        raise SystemExit(f"Missing in input/: {', '.join(missing)}")
    for name in CSV_FILES:
        token = f.encrypt((INPUT_DIR / name).read_bytes())
        (ENC_DIR / (name + ".enc")).write_bytes(token)
        print(f"  encrypted  {name}")
    print(f"Done — {len(CSV_FILES)} files written to input_enc/")


def decrypt():
    f = _fernet()
    INPUT_DIR.mkdir(exist_ok=True)
    missing = [n + ".enc" for n in CSV_FILES if not (ENC_DIR / (n + ".enc")).exists()]
    if missing:
        raise SystemExit(f"Missing in input_enc/: {', '.join(missing)}")
    for name in CSV_FILES:
        data = f.decrypt((ENC_DIR / (name + ".enc")).read_bytes())
        (INPUT_DIR / name).write_bytes(data)
        print(f"  decrypted  {name}")
    print(f"Done — {len(CSV_FILES)} files written to input/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--keygen", action="store_true", help="Print a new key to stdout")
    group.add_argument("--encrypt", action="store_true", help="input/*.csv → input_enc/*.enc")
    group.add_argument("--decrypt", action="store_true", help="input_enc/*.enc → input/*.csv")
    args = parser.parse_args()

    if args.keygen:
        print(Fernet.generate_key().decode())
    elif args.encrypt:
        encrypt()
    else:
        decrypt()
