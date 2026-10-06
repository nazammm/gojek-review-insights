"""Complaint themes for Indonesian Gojek reviews.

Each theme is a regular expression over lower-cased review text. The word lists
come from the most frequent words and word pairs in 1-2 star reviews, including
common spellings and slang ("gabisa", "dapet", "eror"). A review can match
several themes.
"""

import re

import pandas as pd

THEMES: dict[str, str] = {
    "Prices and fees": (
        r"\b(?:mahal|kemahalan|biaya|ongkir|ongkos|tarif|harga|potongan|biaya aplikasi|"
        r"biaya layanan|biaya jasa|naik terus|makin mahal)\b"
    ),
    "Promos and vouchers": (
        r"\b(?:promo|voucher|vocher|voucer|diskon|cashback|kupon|gopay plus|goclub|langganan)\b"
    ),
    "Finding a driver": (
        r"\b(?:dapat driver|dapet driver|cari driver|nyari driver|susah driver|tidak ada driver|"
        r"gak ada driver|ga ada driver|gada driver|gada yg mau|ga ada yg mau|gak ada yang mau|"
        r"tidak ada yang mau|ga dapet|gak dapet|nunggu|menunggu|kelamaan|lama banget|jauh banget)\b"
    ),
    "Driver conduct": (
        r"\b(?:kasar|tidak sopan|gak sopan|ga sopan|ugal|nyasar|marah|bohong|minta bintang|"
        r"fake gps|tuyul|nipu|menipu|salah alamat|cancel sepihak|dicancel|di cancel)\b"
    ),
    "GoPay and balance": (
        r"\b(?:gopay|saldo|top up|topup|isi ulang|transfer|tranfer|rekening|bank|uang saya|"
        r"uang hilang|refund|"
        r"gopaylater|gopay later|paylater|pay later)\b"
    ),
    "Account and login": (
        r"\b(?:akun|login|log in|otp|kode verifikasi|verifikasi|blokir|diblokir|di blokir|"
        r"email|nomor hp|ganti nomor|logout|akon|terhapus|ke hapus|kehapus)\b"
    ),
    "App bugs and speed": (
        r"\b(?:error|eror|bug|crash|force close|keluar sendiri|lemot|lelet|lambat|loading|ngelag|lag|"
        r"server|sibuk|susah dibuka|susah di buka|gak bisa buka|ga bisa buka|tidak bisa buka|"
        r"hang|tidak bisa dibuka|gabisa dibuka|ga bisa dibuka|gak bisa dibuka|gagal|update|"
        r"diupdate|di update|apk nya)\b"
    ),
    "Maps and addresses": (
        r"\b(?:alamat|lokasi|titik|maps|map|peta|gps|arah|rute|jemput|penjemputan)\b"
    ),
    "GoFood orders": (
        r"\b(?:gofood|go food|makanan|resto|restoran|merchant|pesanan salah|pesanan kurang|"
        r"makanannya)\b"
    ),
    "Customer service": (
        r"\b(?:cs|customer service|customer care|layanan pelanggan|pusat bantuan|bantuan|"
        r"laporan|lapor|komplain|complain|pengaduan|respon|direspon)\b"
    ),
}

_COMPILED = {name: re.compile(pattern) for name, pattern in THEMES.items()}


def tag_themes(text: pd.Series) -> pd.DataFrame:
    """Return one boolean column per theme for a series of review texts."""
    lowered = text.fillna("").str.lower()
    return pd.DataFrame(
        {name: lowered.str.contains(rx) for name, rx in _COMPILED.items()},
        index=text.index,
    )
