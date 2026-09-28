#!/usr/bin/env python3
"""Genera le pagine del sito ZeroKM da _pagine/ + _dati.json.

Uso:  python3 _build.py
Le cartelle e i file che iniziano con "_" non vengono pubblicati da GitHub Pages.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
DATI = json.loads((ROOT / "_dati.json").read_text(encoding="utf-8"))
BASE = (ROOT / "_parti" / "base.html").read_text(encoding="utf-8")

LOGO = (ROOT / "assets" / "zerokm-logo.svg").read_text(encoding="utf-8")
LOGO = re.sub(r'role="img" aria-label="ZeroKM"', 'aria-hidden="true" focusable="false"', LOGO)


def sostituisci(testo, valori):
    for k, v in valori.items():
        testo = testo.replace("{{" + k + "}}", str(v))
    return testo


for sorgente in sorted((ROOT / "_pagine").glob("*.html")):
    raw = sorgente.read_text(encoding="utf-8")
    meta_blocco, corpo = raw.split("\n---\n", 1)
    meta = json.loads(meta_blocco)
    valori = {**DATI, **meta, "CORPO": corpo, "LOGO": LOGO.strip(), "LOGO2": LOGO.strip().replace("zkm-c", "zkm-p")}
    testa = ""
    m = re.search(r"<!--testa-->(.*?)<!--/testa-->", corpo, re.S)
    if m:
        testa = m.group(1).strip()
        corpo = corpo[: m.start()] + corpo[m.end():]
    valori["CORPO"] = corpo.strip()
    valori["TESTA"] = testa
    valori.setdefault("ROBOTS", "index, follow")
    pagina = sostituisci(BASE, valori)
    pagina = sostituisci(pagina, valori)  # segnaposto annidati nel corpo
    rimasti = re.findall(r"\{\{[A-Z_]+\}\}", pagina)
    if rimasti:
        raise SystemExit(f"{sorgente.name}: segnaposto non risolti {set(rimasti)}")
    dest = ROOT / meta["FILE"]
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(pagina, encoding="utf-8")
    print("scritto", dest.relative_to(ROOT))
