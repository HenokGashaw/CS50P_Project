def teach_scale(selected_scale):
    """Calls the corresponding function to teach the selected scale."""
    scale_functions = {
        "Selamta": teach_selamta,
        "Tizita": teach_tizita,
        "Tizita Minor": teach_tizita_minor,
        "Chernet": teach_chernet,
        "Ambasel": teach_ambasel,
        "Bati": teach_bati,
        "Bati Minor": teach_bati_minor
    }
    scale_functions[selected_scale]()

def teach_selamta():
    """Teaches the 'Selamta' scale, its notes, and the gaps between them."""
    print("\nSelamta Scale")
    print("===============")
    print("Notes: C, D, F, G, A, C")
    print("Gaps between notes (in semitones): 1, 1.5, 1, 1, 1.5")
    print("\nThe Selamta scale is unique for its melodic flow, often used in hymns to express greetings and blessings.")
    print("Stay tuned for more details about its musical applications!\n")

def teach_tizita():
    """Teaches the 'Tizita' scale."""
    print("\nTizita Scale")
    print("===============")
    print("Notes: C, D, E, G, A, C")
    print("Gaps between notes (in semitones): 1, 1, 1.5, 1, 1.5")
    print("\nTizita is a nostalgic scale, often evoking feelings of longing and remembrance.\n")

def teach_tizita_minor():
    """Teaches the 'Tizita Minor' scale."""
    print("\nTizita Minor Scale")
    print("===============")
    print("Notes: C, D, Eb, G, Ab, C")
    print("Gaps between notes (in semitones): 1, 0.5, 2, 0.5, 2")
    print("\nTizita Minor adds a somber and introspective touch to the nostalgic Tizita scale.\n")

def teach_chernet():
    """Teaches the 'Chernet' scale."""
    print("\nChernet Scale")
    print("===============")
    print("Notes: C, Db, F, Gb, A, C")
    print("Gaps between notes (in semitones): 0.5, 2, 0.5, 1.5, 1.5")
    print("\nChernet is characterized by its intricate and reflective melodies.\n")

def teach_ambasel():
    """Teaches the 'Ambasel' scale."""
    print("\nAmbasel Scale")
    print("===============")
    print("Notes: C, Db, F, G, Ab, C")
    print("Gaps between notes (in semitones): 0.5, 2, 1, 0.5, 2")
    print("\nAmbasel is lively and versatile, often used in celebratory hymns.\n")

def teach_bati():
    """Teaches the 'Bati' scale."""
    print("\nBati Scale")
    print("===============")
    print("Notes: C, E, F, G, B, C")
    print("Gaps between notes (in semitones): 2, 0.5, 1, 2, 0.5")
    print("\nBati is distinctive and expressive, conveying a sense of joy and clarity.\n")

def teach_bati_minor():
    """Teaches the 'Bati Minor' scale."""
    print("\nBati Minor Scale")
    print("===============")
    print("Notes: C, Eb, F, G, Bb, C")
    print("Gaps between notes (in semitones): 1.5, 1, 1, 1.5, 1")
    print("\nBati Minor introduces a subtle depth to the cheerful Bati scale.\n")