# converter.py
# Convertisseur de devises / Währungsrechner
# Utilise des taux fixes (pas besoin d'API) / Verwendet feste Wechselkurse (keine API nötig)

# ── Taux de change (base EUR) / Wechselkurse (Basis EUR) ─────────────────
TAUX = {
    "EUR": 1.0000,
    "USD": 1.0800,
    "GBP": 0.8550,
    "JPY": 161.50,
    "CAD": 1.4700,
    "CHF": 0.9650,
    "CNY": 7.8200,
    "XAF": 655.96,    # Franc CFA (Cameroun / Kamerun)
    "NGN": 1710.00,   # Naira (Nigeria)
    "ZAR": 19.80,     # Rand (Südafrika)
}

NOMS = {
    "EUR": "Euro",
    "USD": "US-Dollar",
    "GBP": "Britisches Pfund",
    "JPY": "Japanischer Yen",
    "CAD": "Kanadischer Dollar",
    "CHF": "Schweizer Franken",
    "CNY": "Chinesischer Yuan",
    "XAF": "CFA-Franc (Kamerun/Zentralafrika)",
    "NGN": "Nigerianische Naira",
    "ZAR": "Südafrikanischer Rand",
}

def convertir(montant: float, de: str, vers: str) -> float:
    """
    Convertit un montant d'une devise vers une autre.
    Rechnet einen Betrag von einer Währung in eine andere um.
    """
    de   = de.upper()
    vers = vers.upper()

    if de not in TAUX:
        raise ValueError(f"Währung '{de}' unbekannt.")
    if vers not in TAUX:
        raise ValueError(f"Währung '{vers}' unbekannt.")

    # Passage par EUR comme devise intermédiaire
    # Umrechnung über EUR als Zwischenwährung
    montant_eur   = montant / TAUX[de]
    montant_cible = montant_eur * TAUX[vers]
    return round(montant_cible, 4)

def afficher_menu():
    """Affiche les devises disponibles / Verfügbare Währungen anzeigen"""
    print("\n Verfügbare Währungen:")
    for code, nom in NOMS.items():
        print(f"   {code}  →  {nom}")

def main():
    print("╔════════════════════════════════════╗")
    print("║       WÄHRUNGSRECHNER              ║")
    print("╚════════════════════════════════════╝")
    print("Tipp: Wechselkurse sind fest (Stand 2024)")

    continuer = True
    while continuer:
        afficher_menu()

        print("\nEingabe:")
        try:
            montant = float(input("  Betrag       : "))
            de      = input("  Von Währung  : ").strip().upper()
            vers    = input("  Nach Währung : ").strip().upper()

            resultat = convertir(montant, de, vers)

            print(f"\n   {montant:.2f} {de} = {resultat:.4f} {vers}")
            print(f"     ({NOMS.get(de, de)} → {NOMS.get(vers, vers)})")

        except ValueError as e:
            print(f"\n   Fehler: {e}")

        print("\nNochmal rechnen? (j/n): ", end="")
        antwort = input().strip().lower()
        if antwort != "j":
            continuer = False

    print("\n Auf Wiedersehen!")

if __name__ == "__main__":
    main()
