# Time Complexity:  O(rows * columns)
# Space Complexity:  O(1)
class SpiralOrder(object):

    def spiralOrder(self, matrix):

        if (matrix == None or len(matrix) == 0):
            return []

        maxRows = len(matrix)
        maxCols = len(matrix[0])
        result = [0 for i in range(maxRows * maxCols)]

        top = 0
        bottom = maxRows - 1
        left = 0
        right = maxCols - 1
        count = 0

        while (top <= bottom and left <= right):
            for col in range(left, right + 1):
                result[count] = matrix[top][col]
                count += 1
            top += 1

            for row in range(top, bottom + 1):
                result[count] = matrix[row][right]
                count += 1
            right -= 1

            if (top <= bottom):
                for col in range(right, left - 1, -1):
                    result[count] = matrix[bottom][col]
                    count += 1
                bottom -= 1

            if (left <= right):
                for row in range(bottom, top - 1, -1):
                    result[count] = matrix[row][left]
                    count += 1
                left += 1

        return result
