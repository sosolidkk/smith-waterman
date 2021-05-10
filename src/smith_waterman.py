from random import choice

from src.cell import MatrixCell


class SmithWaterman:
    def init_matrix(self, first_sequence, second_sequence, gap):
        key = 0
        matrix = []
        first_sequence = first_sequence[::-1]

        for i in range(len(first_sequence) + 2):
            if i == len(first_sequence):
                matrix.append([MatrixCell(key, "-")])
                key += 1
                for j in range(len(second_sequence) + 2):
                    if j == 0:
                        continue
                    else:
                        matrix[i].append(MatrixCell(key, ((j - 1) * gap)))
                        key += 1
            elif i == len(first_sequence) + 1:
                matrix.append([MatrixCell(key, "")])
                key += 1
                for j in range(len(second_sequence) + 2):
                    if j == 0:
                        continue
                    elif j == 1:
                        matrix[i].append(MatrixCell(key, "-"))
                        key += 1
                    else:
                        matrix[i].append(MatrixCell(key, second_sequence[j - 2]))
                        key += 1

            else:
                matrix.append([MatrixCell(key, first_sequence[i])])
                key += 1
                for j in range(len(second_sequence) + 2):
                    if j == 0:
                        continue
                    elif j == 1:
                        matrix[i].append(MatrixCell(key, ((len(first_sequence) - i) * gap)))
                        key += 1
                    else:
                        matrix[i].append(MatrixCell(key, ""))
                        key += 1
        return matrix

    def find_diagonal_value(self, line, column, matrix, match, missmatch, size):
        diagonal = matrix[line + 1][column - 1].value

        if matrix[line][0].value == matrix[size + 1][column].value:
            diagonal += match
        else:
            diagonal += missmatch

        return diagonal

    def find_top_value(self, line, column, matrix, gap):
        return matrix[line + 1][column].value + gap

    def find_left_value(self, line, column, matrix, gap):
        return matrix[line][column - 1].value + gap

    def get_parent(self, matrix, current_line, current_column):
        # if len(matrix[current_line][current_column].parents) > 1:
        #     key = choice(matrix[current_line][current_column].parents)
        # else:
        #     key = matrix[current_line][current_column].parents[0]
        key = choice(matrix[current_line][current_column].parents)

        for line in range(len(matrix)):
            for column in range(len(matrix[line])):
                if matrix[line][column].key == key:
                    return matrix[line][column], line, column

    def backtrace(self, matrix, lines_count, columns_count):
        backtrace_result = []
        current_cell = matrix[0][columns_count]
        current_line = 0
        current_column = columns_count

        while True:
            backtrace_result.append((current_line, current_column))
            current_cell, current_line, current_column = self.get_parent(matrix, current_line, current_column)
            if current_cell.parents is None:
                backtrace_result.append((current_line, current_column))
                break

        obj = backtrace_result[-1]
        while obj != (lines_count - 1, 1):
            if obj[0] == lines_count - 1:
                matrix[obj[0]][obj[1]].parents = [matrix[obj[0]][obj[1] - 1]]
                obj = (obj[0], obj[1] - 1)
                backtrace_result.append(obj)

            elif obj[1] == 1:
                matrix[obj[0]][obj[1]].parents = [matrix[obj[0] + 1][obj[1]]]
                obj = (obj[0] + 1, obj[1])
                backtrace_result.append(obj)

        return backtrace_result

    def align(self, matrix, coordinates, first_sequence):
        second_sequence_row = len(first_sequence) + 1

        align_first_sequence = ""
        align_second_sequence = ""
        movement = None

        for i in range(len(coordinates)):
            if (
                matrix[coordinates[i][0]][0].value == "-"
                and matrix[second_sequence_row][coordinates[i][1]].value == "-"
            ):
                continue

            if movement is None or movement == "d":
                align_first_sequence += matrix[coordinates[i][0]][0].value
                align_second_sequence += matrix[second_sequence_row][coordinates[i][1]].value
            elif movement == "v":
                align_first_sequence += matrix[coordinates[i][0]][0].value
                align_second_sequence += "-"
            elif movement == "h":
                align_first_sequence += "-"
                align_second_sequence += matrix[second_sequence_row][coordinates[i][1]].value

            if i == len(coordinates) - 1:
                break

            if (coordinates[i][0] != coordinates[i + 1][0]) and (coordinates[i][1] != coordinates[i + 1][1]):
                movement = "d"
            elif coordinates[i][0] == coordinates[i + 1][0]:
                movement = "h"
            elif coordinates[i][1] == coordinates[i + 1][1]:
                movement = "v"

        return align_first_sequence, align_second_sequence
