def process_file(input_file, output_file):
    count = int(read_token(input_file))

    puzzel_pieces = []
    puzzel_count = []

    for _ in range(count):
        piece = read_token(input_file)

        position = -1
        for j in range(len(puzzel_pieces)):
            if is_same_piece(puzzel_pieces[j], piece):
                position = j
                break

        if position == -1:
            puzzel_pieces.append(piece)
            puzzel_count.append(1)
        else:
            puzzel_count[position] += 1

    # Write Pieces to the same directory
    for i in range(len(puzzel_count)):
        output_file.write(f"{puzzel_count[i]} {puzzel_pieces[i]}\n")

def is_same_piece(piece1, piece2):
    piece_types = piece1.split(",")
    piece_types2 = piece2.split(",")

    for _ in range(4):
        if piece_types == piece_types2:
            return True

        temp = piece_types2
        piece_types2 = [temp[1], temp[2], temp[3], temp[0]]

    return False

def read_token(input_file):
    read = -1
    token = ""

    while True:
        try:
            read = input_file.read(1)
            token += read
        except IOError as e:
            print(e)

        if token[-1] == ' ' or token[-1] == '\n' or read == '':
            return token.strip()

def main():
    try:
        input_filename = "level2_example.in"
        output_filename = "output.txt"

        with open(input_filename, "r") as input_file, open(output_filename, "w") as output_file:
            process_file(input_file, output_file)

    except IOError as e:
        print(e)

if __name__ == "__main__":
    main()
