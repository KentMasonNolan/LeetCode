import sympy

# Bob
p = 659
b = 160
G = 3
B = pow(G, b, p)

# Alice
a = 135
C1 = pow(G, a, p)
s = pow(B, a, p)
M = 500
C2 = (M * s) % p

# Bob's decryption
s_dec = pow(C1, b, p)

# Calculate modular inverse of s_dec
s_inv = sympy.mod_inverse(s_dec, p)

M_decrypted = (C2 * s_inv) % p

print("New values: ")
print(a)
print(b)
print(M)

print("Plaintext: " +str(M))

print("C1: " + str(C1))
print("C2: " + str(C2))

print("Decrpyted text: " + str(M_decrypted))

