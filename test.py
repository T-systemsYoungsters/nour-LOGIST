def collatz_sequence(n):
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence

# Beispielaufruf mit Startzahl 6
startzahl = 6
result = collatz_sequence(startzahl)

print(f"Collatz-Folge für Startzahl {startzahl}: {result}")