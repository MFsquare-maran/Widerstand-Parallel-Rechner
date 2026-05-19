# Widerstand Parallel Rechner

def generate_e12_values():
    e12_basis = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
    values = []

    # Erweiterte Dekaden bis 82 MΩ
    for decade in range(1, 8):
        factor = 10 ** decade
        for base in e12_basis:
            values.append(base * factor)

    return values


def parallel_resistance(r1, r2):
    return (r1 * r2) / (r1 + r2)


def format_ohm(value):
    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f} MΩ"
    elif value >= 1_000:
        return f"{value / 1_000:.2f} kΩ"
    else:
        return f"{value:.2f} Ω"


# E12-Werte nur einmal erzeugen
e12_values = generate_e12_values()

print("======================================")
print("     Widerstand Parallel Rechner")
print("======================================")

while True:
    target = float(input("\nZielwiderstand in Ohm: "))

    best_r1 = 0
    best_r2 = 0
    best_parallel = 0
    smallest_error = float("inf")

    for r1 in e12_values:
        for r2 in e12_values:
            r_parallel = parallel_resistance(r1, r2)
            error = abs(r_parallel - target)

            if error < smallest_error:
                smallest_error = error
                best_r1 = r1
                best_r2 = r2
                best_parallel = r_parallel

    difference = best_parallel - target
    percent = (difference / target) * 100

    print("\n----------- Ergebnis -----------")
    print(f"Zielwert:      {format_ohm(target)}")
    print(f"R1:            {format_ohm(best_r1)}")
    print(f"R2:            {format_ohm(best_r2)}")
    print(f"Parallelwert:  {format_ohm(best_parallel)}")
    print(f"Abweichung:    {difference:.2f} Ω ({percent:.2f} %)")
    print("-------------------------------")