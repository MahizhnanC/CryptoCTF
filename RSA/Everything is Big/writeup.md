#  CTF Writeup: RSA with Small Private Exponent (Wiener's Attack)

##  Challenge Overview

We are given a custom RSA encryption setup where:
- `d` (the private exponent) is a **small 256-bit prime**
- `e` is calculated as the **modular inverse of `d`** modulo φ(n)
- The ciphertext `c` is generated as usual: `c = m^e mod n`

The public key (`n`, `e`) and ciphertext `c` are given. Our goal is to recover the plaintext (which is a flag).

---

##  RSA Recap

In typical RSA:
- `n = p * q` is the modulus
- `φ(n) = (p-1)(q-1)`
- `e` is usually a small public exponent (e.g., 65537)
- `d ≡ e⁻¹ mod φ(n)` is the private exponent

In this challenge:
- `d` is small (256 bits)
- `e` is huge (≈ same size as `n`)

This makes the system vulnerable to **Wiener’s Attack**.

---

##  Vulnerability

Wiener's attack can recover `d` when it is **too small**, specifically if:

d < N^0.25

Since:
- `N` is 2048 bits → N^0.25 = 2^512
- `d` is 256 bits → definitely satisfies the condition 

---

##  Exploitation Steps

### 1. Use Continued Fractions

Use the continued fraction expansion of `e / n` to find convergents `k/d` that may satisfy the RSA equation:
ed ≡ 1 mod φ(n)

### 2. Try Each Convergent

For each `k/d`, check if:
φ(n) = (ed - 1) / k
...is an integer, and try to solve the RSA quadratic equation:
x^2 - (n - φ(n) + 1)x + n = 0

If the discriminant is a perfect square → we've found the right `d`.

---


