def poly_add(A, B):
    lenA = len(A)
    lenB = len(B)
    result = [0]*max(lenA, lenB)

    for i in range(lenA):
        result[i] = A[i]

    for j in range(lenB):
        result[j] += B[j]
    return result


def poly_multiply(A, B):
    lenA = len(A)
    lenB = len(B)
    result = [0]*(lenA + lenB - 1)
    for i in range(lenA):
        for j in range(lenB):
            result[i + j] += A[i]*B[j];
    return result

def poly_to_str(A):
    s = ""
    for i in range(len(A)):
        s += str(A[i])
        if i != 0:
            s += "x^"
            s += str(i)

        if i != len(A) - 1:
            s += " + "

    return s

def poly_print(A):
    print(poly_to_str(A))

p1 = [3, 1, 11, 6]
poly_print(p1)
p2 = [1, 2, 3]
poly_print(p2)
poly_print(poly_add(p1, p2))
poly_print(poly_multiply(p1, p2))
poly_print(poly_multiply(p1, [-1]))
