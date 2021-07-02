"""
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution({{0, 2, 1, 0, 0}, {0, 0, 0, 3, 4}, {0, 0, 0, 0, 0}, {0, 0, 0, 0,0}, {0, 0, 0, 0, 0}})
Output:
    [7, 6, 8, 21]

Input:
Solution.solution({{0, 1, 0, 0, 0, 1}, {4, 0, 0, 3, 2, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
Output:
    [0, 3, 2, 9, 14]

-- Python cases --
Input:
solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
Output:
    [7, 6, 8, 21]

Input:
solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
Output:
    [0, 3, 2, 9, 14]

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""

from __future__ import division
import copy
from fractions import Fraction

class Matrix:
    def __init__(self, obj):
        if type(obj) == list:
            self.data = copy.deepcopy(obj)
        elif type(obj) == Matrix:
            self.data = copy.deepcopy(obj.data)

        self.mapping = None  # idx: original_idx
        self.rmapping = None  # original_idx: idx
        self.states = None

    def __str__(self):
        return "[" + "\n".join([str(row) for row in self.data]) + "]"

    def __add__(self, other):
        X = copy.deepcopy(self.data)
        if type(other) == int:
            for i in range(len(X)):
                for j in range(len(X[0])):
                    X[i][j] += other
        else:
            Y = other.data
            try:
                assert len(X) == len(Y) and len(X[0]) == len(Y[0])
                for i in range(len(X)):
                    for j in range(len(X[0])):
                        X[i][j] += Y[i][j]
            except Exception:
                raise ValueError(
                    "Invalid matrix addition. Make sure that the shapes are the same.")
        return Matrix(X)

    def __sub__(self, other):
        X = copy.deepcopy(self.data)
        if type(other) == int:
            for i in range(len(X)):
                for j in range(len(X[0])):
                    X[i][j] -= other
        else:
            Y = other.data
            try:
                assert len(X) == len(Y) and len(X[0]) == len(Y[0])
                for i in range(len(X)):
                    for j in range(len(X[0])):
                        X[i][j] -= Y[i][j]
            except Exception:
                raise ValueError(
                    "Invalid matrix addition. Make sure that the shapes are the same.")
        return Matrix(X)

    def __mul__(self, other):
        """ matrix multiplication """
        X = copy.deepcopy(self.data)

        if type(other) == int:
            for i in range(len(X)):
                for j in range(len(X[0])):
                    if X[i][j] != 0:
                        X[i][j] *= other
            return Matrix(X)

        elif type(other) == Matrix:
            Y = other.rotate_ccw().data

            assert len(X[0]) == len(Y[0])

            data = []
            for k in range(len(Y)-1, -1, -1):
                row = []
                for i in range(len(X)):
                    item = sum([X[i][j] * Y[k][j] for j in range(len(X[0]))])
                    row.append(item)
                data.append(row)
            return Matrix(data).transpose()

    def get_transition_matrix(self):
        """format matrix into a transition matrix where X[i][j] is the probability of state i becoming state j
        each row should sum to 1
        does not change the shape"""
        X = copy.deepcopy(self.data)
        absorbing_states = [i for i in range(len(X)) if sum(X[i]) == 0]  # terminal states

        for i in range(len(X)):
            if i in absorbing_states and any([X[i][j] != 0 for j in range(len(X[0]))]):
                X[i][i] = 1
            else:
                denom = sum(X[i])
                for j in range(len(X[0])):
                    X[i][j] = X[i][j] / denom if X[i][j] > 0 else 0
        return Matrix(X)

    def get_standard_form(self):
        """
        transform self.data to standard form P for absorbing markov chain
        where P consists of 4 matrices stacked like 
            [[I, O], 
            [R, Q]]

        in the standard form, row 0 to end of row i [I,O] represent outgoing probability from absorbing states
        """

        absorbing_states = [i for i in range(len(self.data)) if sum(self.data[i]) == 0]  # terminal states
        non_absorbing_states = [i for i in range(len(self.data)) if sum(self.data[i]) > 0]

        assert len(self.data) == len(absorbing_states) + len(non_absorbing_states)

        X = self.get_transition_matrix().data
        mapping = {idx: original_idx for idx, original_idx in enumerate(absorbing_states + non_absorbing_states)}
        rmapping = {original_idx: idx for idx, original_idx in mapping.items()}

        data = [[0] * len(X[0]) for _ in range(len(X))]
        for i in absorbing_states + non_absorbing_states:
            for j in absorbing_states + non_absorbing_states:
                data[i][j] = X[mapping[i]][mapping[j]]

        Y = Matrix(data)
        Y.mapping = mapping
        Y.rmapping = rmapping
        Y.states = {"absorbing": absorbing_states,
                    "non-absorbing": non_absorbing_states}
        return Y

    def transpose(self):
        return Matrix([list(col) for col in zip(*self.data)])

    def rotate_ccw(self):
        X = self.data
        return Matrix([[X[i][j] for i in range(len(X))] for j in range(len(X[0])-1, -1, -1)])

    def get_QR(self):
        if not self.mapping:
            return None

        mapping = self.rmapping  # maps current index in standard form to original index
        X = self.data
        Q = [[X[mapping[i]][mapping[j]] for j in self.states["non-absorbing"]]
             for i in self.states["non-absorbing"]]
        R = [[X[mapping[i]][mapping[j]] for j in self.states["absorbing"]]
             for i in self.states["non-absorbing"]]
        return Matrix(Q), Matrix(R)

    def exclude(self, i, j):
        """removes ith row and jth column"""
        return Matrix([row[:j] + row[j+1:] for row in (self.data[:i] + self.data[i+1:])])

    def get_determinant(self):
        X = self.data

        # base case for 2x2 matrix: ac-db
        if len(X) == 2:
            return X[0][0] * X[1][1] - X[0][1] * X[1][0]

        determinant = 0
        for i in range(len(X)):
            determinant += ((-1)**i) * X[0][i] * self.exclude(0, i).get_determinant()
        return determinant

    def get_minor(self):
        data = [[self.exclude(i, j).get_determinant() for j in range(len(self.data[0]))] for i in range(len(self.data))]
        return Matrix(data)

    def inverse(self):
        if len(self.data) == 2 and len(self.data[0]) == 2:
            X = self.data
            determinant = self.get_determinant()
            Xinv = [
                [ X[1][1], -X[0][1]],
                [-X[1][0],  X[0][0]]
            ]
            for i in range(len(Xinv)):
                for j in range(len(Xinv[0])):
                    Xinv[i][j] /= determinant
            return Matrix(Xinv)

        minors = self.get_minor().data
        cofactors = copy.deepcopy(minors)
        for i in range(len(minors)):
            x = 1 if i % 2 == 0 else -1
            for j in range(len(minors)):
                cofactors[i][j] *= x
                x *= -1

        adjugate = Matrix(cofactors).transpose()
        data = adjugate.data
        determinant = self.get_determinant()
        inverse = [[0] * len(data[0]) for _ in range(len(data))]
        for i in range(len(data)):
            for j in range(len(data[0])):
                inverse[i][j] = data[i][j] / determinant if data[i][j] != 0 else 0.0

        return Matrix(inverse)

    def compute_F(self):
        """compute the fundamental matrix of P
        F = (I - Q) ** -1"""
        Q = self.data

        I = [[0] * len(Q[0]) for _ in range(len(Q))]
        for i in range(len(I)):
            I[i][i] = 1

        return (Matrix(I) - Matrix(Q)).inverse()

    @staticmethod
    def multiply_matrices(X, Y):
        """ must be used instead of __mul__ when using python2 """
        X = copy.deepcopy(X.data)
        Y = Y.rotate_ccw().data

        assert len(X[0]) == len(Y[0])

        data = []
        for k in range(len(Y)-1, -1, -1):
            row = []
            for i in range(len(X)):
                item = sum([X[i][j] * Y[k][j] for j in range(len(X[0]))])
                row.append(item)
            data.append(row)
        return Matrix(data).transpose()


def solution(m):
    if len(m[0]) == 1:
        return [1, 1]

    if sum(m[0]) == 0:
        zeros = sum([int(sum(m[i]) == 0) for i in range(1, len(m))])
        ret = [0] * zeros
        ret.insert(0, 1)
        ret.append(1)
        return ret

    if len(set(m[0])) == 1 and all([sum(row) == 0 for row in m[1:]]):
        ret = [1] * (len(m) - 1)
        ret.append(sum(ret))
        return ret

    zeros = sum([int(sum(m[i]) == 0) for i in range(1, len(m))])
    for j in range(len(m[0])):
        if m[0][j] == sum(m[0]):
            if j == 0:
                ret = [0] * zeros
                ret.insert(0, 1)
                ret.append(1)
                return ret
            else:
                ret = [0] * zeros
                ret[j-1] = 1
                ret.append(1)
                return ret

    M = Matrix(m)
    P = M.get_standard_form()
    Q, R = P.get_QR()
    F = Q.compute_F()  # verified with numpy
    FR = Matrix.multiply_matrices(F, R).data

    n = len(P.states["absorbing"])

    # probability of absorbing states as fraction
    p_terminal = [Fraction.from_float(FR[P.rmapping[0] - n][j]).limit_denominator() for j in range(n)]

    # split numerator and denominator
    fractions = [[frac.numerator, frac.denominator] for frac in p_terminal]

    # simplify fractions
    lim = 1
    for _, denom in fractions:
        lim *= denom

    for i in range(1, lim+1):
        if all([i % denom == 0 for _, denom in fractions]):
            ret = [num * (i // denom) for num, denom in fractions]
            ret.append(i)

            assert ret[-1] == sum(ret[:-1]), str(P.states) + '\n' + str(M)
            return ret

def test():
    X = Matrix([[1, 2, 3], [4, 5, 6]])
    Y = Matrix([[1, -2], [-1, 3], [2, 0]])
    Z = Matrix([[1, -1, 0], [1, 0, 1]])

    assert (X + 1).data == [[2, 3, 4], [5, 6, 7]]
    assert (X + Z).data == [[2, 1, 3], [5, 5, 7]]
    assert (X - 1).data == [[0, 1, 2], [3, 4, 5]]
    assert (X - Z).data == [[0, 3, 3], [3, 5, 5]]
    assert X.transpose().data == [[1, 4], [2, 5], [3, 6]]
    assert Matrix.multiply_matrices(X, Y).data == [[5, 4], [11, 7]]

    data = [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    X = Matrix(data)
    P = X.get_standard_form()
    Q, R = P.get_QR()
    assert Q.data == [[0, 2/3], [0, 0]]

    data = [
        [3, 0, 2],
        [2, 0, -2],
        [0, 1, 1]
    ]
    X = Matrix(data)
    assert X.exclude(1, 1).data == [[3, 2], [0, 1]]
    assert X.get_determinant() == 10
    assert X.get_minor().data == [[2, 2, 2], [-2, 3, 3], [0, -10, 0]]
    assert X.inverse().data == [[0.2, 0.2, 0.0],
                                [-0.2, 0.3, 1.0], 
                                [0.2, -0.3, 0.0]]

    data = [
        [0, 3, 3, 4],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [8, 1, 1, 0]
    ]
    X = Matrix(data)
    P = X.get_standard_form()
    Q, R = P.get_QR()
    assert Q.data == [[0, 0.4], [0.8, 0]]

def test_solution():
    assert solution([
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]) == [7, 6, 8, 21]

    assert solution([
        [0, 1, 0, 0, 0, 1], # s0, the initial state, goes to s1 and s5 with equal probability
        [4, 0, 0, 3, 2, 0], # s1 can become s0, s3, or s4, but with different probabilities
        [0, 0, 0, 0, 0, 0], # s2 is terminal, and unreachable (never observed in practice)
        [0, 0, 0, 0, 0, 0], # s3 is terminal
        [0, 0, 0, 0, 0, 0], # s4 is terminal
        [0, 0, 0, 0, 0, 0]  # s5 is terminal
    ]) == [0, 3, 2, 9, 14]

    assert solution([
        [0]
    ]) == [1, 1]

    assert solution([
        [1]
    ]) == [1, 1]

    assert solution([
        [0, 0],
        [0, 0]
    ]) == [1, 0, 1]

    assert solution([
        [1, 0],
        [0, 0]
    ]) == [1, 0, 1]

    assert solution([
        [0, 1],
        [0, 0]
    ]) == [1, 1]

    assert solution([
        [1, 1],
        [0, 0]
    ]) == [1, 1]

    assert solution([
        [1, 1, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]) == [1, 1]
    
    assert solution([
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]) == [1, 1, 2]
    
    assert solution([
        [0, 0, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]) == [0, 1, 1]

    assert solution([
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]) == [1, 0, 0, 1]

    assert solution([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]) == [1, 0, 0, 1]

    assert solution([
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]) == [1, 1]

    assert solution([
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]) == [0, 1, 1]

    assert solution([
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]) == [1, 0, 0, 0, 1]

    assert solution([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]) == [1, 0, 0, 0, 1]

    assert solution([
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]) == [1, 1, 1, 3]

    assert solution([
        [0, 0, 0, 99],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]) == [0, 0, 1, 1]

    assert solution([
        [0, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]) == [0, 1, 1, 3, 5]

    assert solution([
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]) == [1, 2, 3]

    assert solution([
        [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
        [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
        [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
        [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [1, 2, 3, 4, 5, 15]
    
    assert solution([
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [4, 5, 5, 4, 2, 20]
    
    assert solution([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [1, 1, 1, 1, 1, 5]
    
    assert solution([
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [2, 1, 1, 1, 1, 6]
    
    assert solution([
        [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
        [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
        [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [6, 44, 4, 11, 22, 13, 100]
    
    assert solution([
        [ 0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
        [ 0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
        [ 0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
        [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
        [ 0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
        [ 1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [1, 1, 1, 2, 5]

    assert solution([
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    assert solution([
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 99],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]



test()
test_solution()
