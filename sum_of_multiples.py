n = int(input("Entrez un nombre n : "))
L = int(input("Entrez une limite L : "))

somme = 0
for i in range(1, L+1):
    if i % n == 0:
        somme += i

print("La somme de tous les multiples de", n, "qui sont inférieurs ou égaux à", L, "est :", somme)