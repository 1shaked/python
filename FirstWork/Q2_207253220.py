import numpy as np
def solve(A:list, type):
    a = np.array(A, dtype=type) 
    return np.sort(a, order='height')

if __name__ == '__main__':
    data_type = [('name', 'S15'), ('class', int), ('height', float)]
    students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]

    print(solve(students_details, data_type))