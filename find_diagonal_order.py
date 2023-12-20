# Time Complexity: O(rows * columns)
# Space Complexity: O(1)
class FindDiagonalOrder(object):

    def findDiagonalOrder(self, matrix):

        if (matrix == None or len(matrix) == 0):
            return []

        maxRows = len(matrix)
        maxCols = len(matrix[0])
        result = [0 for i in range(maxRows * maxCols)]

        direction = 1
        count = 0
        row = 0
        col = 0

        while (count <= (maxRows * maxCols) - 1):
            result[count] = matrix[row][col]

            if (direction == 1):
                if (col == maxCols - 1):
                    row += 1
                    direction = 0
                elif (row == 0):
                    col += 1
                    direction = 0
                else:
                    row -= 1
                    col += 1

            else:
                if (row == maxRows - 1):
                    col += 1
                    direction = 1
                elif (col == 0):
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

            count += 1

        return result
