# kilometrozero.eu — sito di ZeroKM

Sito statico dell'app ZeroKM, pubblicato con GitHub Pages sul dominio `kilometrozero.eu`.

## Modificare il sito

1. I testi delle pagine sono in `_pagine/` (uno per pagina).
2. Testata, piede e meta SEO comuni sono in `_parti/base.html`.
3. Ragione sociale, sede, P.IVA ed email sono in `_dati.json`.
4. Rigenera le pagine con `python3 _build.py`, poi fai commit e push.

GitHub Pages ignora i file e le cartelle che iniziano con `_`, quindi le sorgenti non vengono pubblicate.

Pagine: `/` (filosofia e come funziona), `/supporto/`, `/privacy/`, `/termini/`, `404.html`.
I font (Bricolage Grotesque, Atkinson Hyperlegible, licenza OFL) sono serviti dal sito stesso: nessuna richiesta a Google Fonts.
