def decomposicao(S, piv, p, r):
    i = p
    j = r

    while i <= j:
        if S[i] < piv:
            i += 1
        elif S[j] > piv:
            j -= 1
        else:
            S[i], S[j] = S[j], S[i]
            i += 1
            j -= 1

    q1 = j
    q2 = i

    return q1, q2

S = [2, 8, 5, 1, 7, 6]
piv = 5
p = 0
r = len(S) - 1

q1, q2 = decomposicao(S, piv, p, r)

print("Vetor S:", S)
print("Q1:", q1)
print("Q2:", q2)