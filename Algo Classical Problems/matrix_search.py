"""
Given a matrix of size (n x m) sorted by row and column, search for a specific value
"""

def matrix_search(matrix, target):
    """
    This search is a varient of the binary search

    O(n + m) time
    O(1) space
    """ 
    # start the row at the beginning
    row = 0

    # start the col at the end
    first_row = matrix[0]
    col = len(first_row) - 1

    max_rows = len(matrix) - 1

    while row <= max_rows and col >= 0:

        if target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
        else:
            return True

    return False

    
