import os
#----------------------Input
letter = '5'
file_name = 'input.in'
output_file_path = '.\ergebnis.txt'

#----------------------Programm
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, file_name)

with open(file_path, 'r') as file:
    content = file.read()
    count = content.count(letter)

with open(output_file_path, 'w') as output_file:
    output_file.write(str(count))

print(f"Der Buchstabe '{letter}' kommt {count} Mal in der Datei vor.")
