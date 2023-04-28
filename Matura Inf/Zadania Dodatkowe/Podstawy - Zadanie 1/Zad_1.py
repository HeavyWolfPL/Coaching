# Otwarcie pliku z sekwencjami
with open("sekwencje.txt", "r") as file:
    lines = file.readlines()
    # Odkomentuj poniższy fragment jeśli chcesz uzyskać wyniki dla pierwszych 10 sekwencji
    # temp = []
    # for i, line in enumerate(lines):
    #     if i == 10: 
    #         break
    #     temp.append(line)
    # lines = temp

#################################################
#                                               #
#################################################

# DNA - nić matrycowa


def is_dna(sequence):
    # Sprawdzenie, czy linia zawiera tylko litery A, C, T, G, co wskazuje na sekwencję DNA
    sequence = sequence.strip()
    for char in sequence:
        if char not in "ACTG":
            return False
    return True

def is_rna(sequence):
    # Sprawdzenie, czy linia zawiera tylko litery A, C, U, G, co wskazuje na sekwencję RNA
    sequence = sequence.strip()
    for char in sequence:
        if char not in "ACUG":
            return False
    return True

# Inicjalizacja list na sekwencje DNA i RNA
dna_sequences = []
rna_sequences = []

# Pętla po liniiach pliku
for line in lines:
    if is_dna(line):
        dna_sequences.append(line)
    elif is_rna(line):
        rna_sequences.append(line)



# Zapis sekwencji DNA do pliku nic_matrycowa.txt
with open("nic_matrycowa.txt", "w") as dna_file:
    for sequence in dna_sequences:
        dna_file.write(sequence)

# Zapis sekwencji RNA do pliku rna.txt
with open("rna.txt", "w") as rna_file:
    for sequence in rna_sequences:
        rna_file.write(sequence)

with open("wyniki_zad1.txt", "w") as file:
    file.write(f"Liczba znalezionych sekwencji DNA wynosi {len(dna_sequences)}\n")
    file.write(f"Liczba znalezionych sekwencji RNA wynosi {len(rna_sequences)}")



#################################################
#                                               #
#################################################


# Funkcja do zamiany sekwencji DNA na sekwencje RNA
def dna_to_rna(dna_sequence):
    rna_sequence = list(dna_sequence)
    for i, char in enumerate(rna_sequence):
        if char == "A":
            rna_sequence[i] = "T"
        elif char == "T":
            rna_sequence[i] = "A"
        elif char == "G":
            rna_sequence[i] = "C"
        elif char == "C":
            rna_sequence[i] = "G"

    rna_sequence = "".join(rna_sequence).replace("T", "U")
    return rna_sequence

# Funkcja do zamiany sekwencji RNA na sekwencje DNA
def rna_to_dna(rna_sequence):
    dna_sequence = list(rna_sequence.replace("U", "T"))
    for i, char in enumerate(dna_sequence):
        if char == "A":
            dna_sequence[i] = "T"
        elif char == "T":
            dna_sequence[i] = "A"
        elif char == "G":
            dna_sequence[i] = "C"
        elif char == "C":
            dna_sequence[i] = "G"
    
    dna_sequence = "".join(dna_sequence)
    return dna_sequence



# Odczytanie sekwencji DNA z pliku nic_matrycowa.txt
with open("nic_matrycowa.txt", "r") as dna_file:
    dna_sequences = dna_file.readlines()

# Generowanie sekwencji RNA na podstawie sekwencji DNA
for i, sequence in enumerate(dna_sequences):
    rna_sequences[i] = dna_to_rna(sequence)

# Zapis sekwencji RNA do pliku rna_nowe.txt
with open("rna_nowe.txt", "w") as rna_file:
    for sequence in rna_sequences:
        rna_file.write(sequence)



# Odczytanie sekwencji RNA z pliku rna.txt
with open("rna.txt", "r") as rna_file:
    rna_sequences = rna_file.readlines()

# Generowanie sekwencji DNA na podstawie sekwencji RNA
for i, sequence in enumerate(rna_sequences):
    dna_sequences[i] = rna_to_dna(sequence)

# Zapis sekwencji DNA do pliku dna_nowe.txt
with open("dna_nowe.txt", "w") as dna_file:
    for dna_sequence in dna_sequences:
        dna_file.write(dna_sequence)
