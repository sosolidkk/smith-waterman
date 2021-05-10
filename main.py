from src.cli import cli_args
from src.smith_waterman import SmithWaterman

if __name__ == "__main__":
    algorithm = SmithWaterman()
    args = vars(cli_args().parse_args())
    gap = args.get("gap")
    match = args.get("match")
    missmatch = args.get("missmatch")

    sequences = []
    file_name = "input.fasta"
    output_file_name = "output.txt"

    with open(file_name, "r") as file:
        file_data = file.readlines()

    for index, line in enumerate(file_data):
        if not line.startswith(">"):
            sequences.append(line.strip())

    first_sequence = sequences[0]
    second_sequence = sequences[1]

    matrix = algorithm.init_matrix(first_sequence, second_sequence, gap)

    # Run matrix from bottom to up
    for i in range((len(first_sequence) - 1), -1, -1):
        # Run matrix from left to right
        for j in range(len(second_sequence) + 2):
            if j == 0 or j == 1:
                continue
            else:
                diagonal_value = algorithm.find_diagonal_value(i, j, matrix, match, missmatch, len(first_sequence))
                top_value = algorithm.find_top_value(i, j, matrix, gap)
                left_value = algorithm.find_left_value(i, j, matrix, gap)
                max_value = max([diagonal_value, top_value, left_value])

                matrix[i][j].parents = []

                if diagonal_value == max_value:
                    matrix[i][j].parents.append(matrix[i + 1][j - 1].key)
                if top_value == max_value:
                    matrix[i][j].parents.append(matrix[i + 1][j].key)
                if left_value == max_value:
                    matrix[i][j].parents.append(matrix[i][j - 1].key)

                matrix[i][j].value = max_value

    backtrance_result = algorithm.backtrace(matrix, len(first_sequence) + 1, len(matrix[0]) - 1)
    backtrance_result.reverse()

    new_first_sequence, new_second_sequence = algorithm.align(matrix, backtrance_result, first_sequence)
    score = matrix[backtrance_result[-1][0]][backtrance_result[-1][1]].value

    with open(output_file_name, "w") as file:
        file.write(f"{new_first_sequence}\n")
        file.write(f"{new_second_sequence}\n")
        file.write(f"Score={score}\n")
    print("File `output.txt` with results was saved successful!")
