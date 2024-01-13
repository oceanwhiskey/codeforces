def calc_E_0(a, b, p):
    E, c = 0.0, 1.0
    for i in range(n):
        E += c*(a[i] + p[i]*b[i])
        c *= (1.0-p[i])
    E = E/(1.0 - c)
    return E

def calc_E(a, b, p, n):
    E = [0.0] * n
    E[0] = calc_E_0(a, b, p)
    for i in reversed(range(1, n)):
        E[i] = a[i] + p[i]*(b[i]-E[(i+1) % n]) + E[(i+1) % n]
    return E

n = int(input())
a, b = [], []
for _ in range(n):
    a_i, b_i = map(int, input().split(' '))
    a.append(a_i)
    b.append(b_i)

b_min, i_min = b[0], 0
for i in range(1, n):
    if b[i] < b_min:
        b_min, i_min = b[i], i

p = [0.0] * n
i = i_min
sum_a = a[i_min]
p[i_min] = 0.99
for k in range(1, n):
    j = (i + n - k) % n
    if b[j] - sum_a <= b_min:
        p[j] = 0.99
    else:
        p[j] = 0.01
    sum_a += a[j]

for _ in range(n):
    change = False
    E = calc_E(a, b, p, n)
    for k in (k for k in range(n) if b[k] - a[(k + 1) % n] > b_min):
        if b[k]*(2*p[k]-1) > (2*p[k]-1)*E[(k+1)%n]:
            change = True
            p[k] = 1 - p[k]
    if not change:
        break
print(sum(E)/n)