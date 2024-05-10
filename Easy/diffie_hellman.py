def diffie_hellman(p, g, a, b):
    # Alice computes her public key
    A = pow(g, a, p)
    # Bob computes his public key
    B = pow(g, b, p)

    # Alice computes the shared secret
    secret_key_alice = pow(B, a, p)
    # Bob computes the shared secret
    secret_key_bob = pow(A, b, p)

    return A, B, secret_key_alice, secret_key_bob


results_ex1 = diffie_hellman(251, 3, 15, 13)
results_ex2 = diffie_hellman(257, 5, 18, 19)

print("Example 1:", results_ex1)
print("Example 2:", results_ex2)


