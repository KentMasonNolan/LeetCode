import sympy

p = 16381
q = 27449

n = p * q
phi_n = (p - 1) * (q - 1)
e = 65537
d = sympy.mod_inverse(e, phi_n)

print("Private key: " + str(d))

M = 500600700

print("Plaintext: " + str(M))

cipher = pow(M, e, n)
# This is M^e mod n

print("Cipher text: " + str(cipher))

plaintext = pow(cipher, d, n)
# This is ciphertext^d mod n

print("Decyrpyed text: " + str(plaintext))


# C = sympy.Mod(M, n)
#
# print(C)

