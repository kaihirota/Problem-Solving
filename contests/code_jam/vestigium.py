"""
The trace of a square matrix is the sum of the values on the main diagonal (which runs from the upper left to the lower right).

An N-by-N square matrix is a Latin square if each cell contains one of N different values, and no value is repeated within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the N values are the integers between 1 and N.

1 2 3
2 3 1
3 1 2

Problem:
Given a matrix that contains only integers between 1 and N, we want to compute its trace and check whether it is a natural Latin square.
To give some additional information, instead of simply telling us whether the matrix is a natural Latin square or not, please compute the number of rows and the number of columns that contain repeated values.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each starts with a line containing a single integer N: the size of the matrix to explore. Then, N lines follow. The i-th of these lines contains N integers Mi,1, Mi,2 ..., Mi,N. Mi,j is the integer in the i-th row and j-th column of the matrix.

Output
For each test case, output one line containing Case #x: k r c, where
- x is the test case number (starting from 1),
- k is the trace of the matrix,
- r is the number of rows of the matrix that contain repeated elements,
- and c is the number of columns of the matrix that contain repeated elements.

Limits
Test set 1 (Visible Verdict)
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
2 ≤ N ≤ 100.
1 ≤ Mi,j ≤ N, for all i, j.

Sample Input:
3
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3

Output
Case #1: 4 0 0
Case #2: 9 4 4
Case #3: 8 0 2
"""

def test_case(x = [[2, 1, 3], [1, 3, 2], [1, 2, 3]], n=3):
    trace = compute_trace(x, n)
    dupe_rows, dupe_cols = check_duplicate(x, n)
    for row in x:
        print(row)
    print(f"Output: {trace} {dupe_rows} {dupe_cols}")

def compute_trace(x, n):
    return sum([x[i][i] for i in range(n)])

def check_duplicate(x, n):
    dupe_rows = 0
    dupe_cols = 0

    # rows:
    for row in x:
        # if len(set([elem for elem in row if 1 <= elem <= n])) != n:
        if len(set(row)) != n:
            dupe_rows += 1

    # columns
    for col in range(n):
        # if len(set([x[i][col] for i in range(n) if 1 <= x[i][col] <= n])) != n:
        if len(set([x[i][col] for i in range(n)])) != n:
            dupe_cols += 1

    return dupe_rows, dupe_cols


if __name__ == "__main__":
    tests = int(input())

    for test in range(1, tests+1):
        n = int(input())
        x = []
        for i in range(n):
            row = list(map(int, input().strip().split()))
            x.append(row)

        trace = compute_trace(x, n)
        dupe_rows, dupe_cols = check_duplicate(x, n)

        # print(f"Case #{test}: {trace} {dupe_rows} {dupe_cols}")
        print("Case #" + str(test) + ":" + " " + str(trace) + " " + str(dupe_rows) + " " + str(dupe_cols))
