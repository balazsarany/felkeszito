names = ["Ábel", "Abigél", "Ádám", "Adél", "Adrián", "Ákos", "Alex", "Alexander", "Alexandra", "Alíz", "Amira", "András", "Anna", "Ármin", "Áron", "Attila", "Balázs", "Bálint", "Barbara", "Barnabás", "Bella", "Bence", "Bende", "Bendegúz", "Benedek", "Benett", "Benjamin", "Benjámin", "Bertalan", "Bianka", "Bíborka", "Blanka", "Boglárka", "Boldizsár", "Borbála", "Boróka", "Botond", "Brájen", "Brendon", "Csaba", "Csenge", "Csongor", "Dalma", "Dániel", "Dávid", "Dénes", "Denisz", "Diána", "Dominik", "Donát", "Dóra", "Dorián", "Dorina", "Dorka", "Dorottya", "Elena", "Eliza", "Elizabet", "Emese", "Emili", "Emília", "Emma", "Enikő", "Erik", "Eszter", "Fanni", "Félix", "Ferenc", "Flóra", "Fruzsina", "Gábor", "Gellért", "Gergely", "Gergő", "Gréta", "György", "Gyula", "Hanga", "Hanna", "Hédi", "Hunor", "Imre", "István", "Izabella", "Janka", "János", "Jázmin", "Johanna", "József", "Júlia", "Kamilla", "Károly", "Kende", "Kevin", "Kiara", "Kincső", "Kinga", "Kornél", "Kristóf", "Krisztián", "Krisztofer", "Lajos", "Lara", "László", "Laura", "Léna", "Letícia", "Levente", "Lia", "Lili", "Liliána", "Lilien", "Lilla", "Linett", "Liza", "Lora", "Lotti", "Luca", "Lujza", "Maja", "Marcell", "Márk", "Martin", "Márton", "Máté", "Mátyás", "Mia", "Mihály", "Miklós", "Milán", "Milla", "Mira", "Mirella", "Mirkó", "Nándor", "Nara", "Natália", "Natasa", "Nikolasz", "Nimród", "Noé", "Noel", "Noémi", "Nolen", "Nóra", "Norbert", "Norina", "Olivér", "Olívia", "Panka", "Panna", "Patrik", "Péter", "Petra", "Rebeka", "Regina", "Réka", "Richárd", "Róbert", "Roland", "Róza", "Rozina", "Sámuel", "Sándor", "Sára", "Simon", "Soma", "Szabolcs", "Szofi", "Szofia", "Szófia", "Szonja", "Tamara", "Tamás", "Tibor", "Tímea", "Vanda", "Vanessza", "Vencel", "Vendel", "Veronika", "Viktor", "Viktória", "Vilmos", "Vince", "Virág", "Vivien", "Zalán", "Zara", "Zénó", "Zente", "Zétény", "Zita", "Zoé", "Zoltán", "Zorka", "Zselyke", "Zsófia", "Zsolt", "Zsombor"]

def listaz(nev, betu):
    nev = []
    nev.append(names)
    betu = input("Add meg a kezdobetut")
    for i in nev:
        if i.startwith(betu.apper, betu) or i.startwith(betu.lower):
            print(i)


def kivalogat(nev, betu):
    ujnev = []
    nev.append(names)
    betu = input("Add meg a kezdobetut")
    for i in nev:
        if i.startwith(betu):
            ujnev.append(i)