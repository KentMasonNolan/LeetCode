import sympy

p = 29
q = 23

n = p * q
phi_n = (p - 1) * (q - 1)
e = 3
d = sympy.mod_inverse(e, phi_n)

print("Private key: " + str(d))

M = 567

print("Plaintext: " + str(M))

signature_s = pow(M, d, n)
# This is M^d mod n

print("Modulus n:", n)
print("Phi(n):", phi_n)
print("Public Key e:", e)
print("Private Key d:", d)
print("Signature s:", signature_s)

M_prime = pow(signature_s, e, n)

print("Decrypted Message M':", M_prime)

print("Verification:", "Successful" if M == M_prime else "Failed")
