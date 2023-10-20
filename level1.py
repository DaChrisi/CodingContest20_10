def main():
    input_filename = "input.txt"
    output_filename = "output.txt"

    try:
        with open(input_filename, "r") as file:
            lines = file.readlines()

        num_lines = int(lines[0])
        puzzle_lines = lines[1:]

        # Entferne führende/trailing Leerzeichen und Zeilenumbrüche
        puzzle_lines = [line.strip() for line in puzzle_lines]

        # Erstelle ein Dictionary, um die Anzahl jeder Zeile zu zählen
        line_count = {}
        for line in puzzle_lines:
            if line in line_count:
                line_count[line] += 1
            else:
                line_count[line] = 1

        # Öffne die Ausgabedatei im Schreibmodus
        with open(output_filename, "w") as output_file:
            for line, count in line_count.items():
                output_file.write(f"{count} {line}\n")

        print(f"Die Ergebnisse wurden in '{output_filename}' gespeichert.")

    except FileNotFoundError:
        print(f"Die Datei '{input_filename}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Verarbeiten der Datei: {str(e)}")

if __name__ == "__main__":
    main()
