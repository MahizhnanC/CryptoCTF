# Manyprime RSA Challenge Writeup

## Challenge Description

This RSA challenge titled **"Manyprime"** involves decrypting a ciphertext where the modulus `n` is the product of **over 30 small prime numbers**. The small size of these prime factors makes the RSA implementation vulnerable to factorization-based attacks.

---

## Objective

Given:

* Modulus `n`
* Public exponent `e = 65537`
* Ciphertext `ct`

Goal:
Decrypt the ciphertext and retrieve the plaintext flag.

---

## Vulnerability

In standard RSA, `n` is the product of two large primes. However, when `n` is composed of many small primes, it's possible to factor it very quickly using online databases or mathematical libraries. Once factored, the private key can be computed, breaking the encryption.

---

## Steps to Solve

### 1. Factor the modulus `n`

We use [FactorDB](https://factordb.com) to factor the given modulus. The service returns 32 small prime numbers.

### 2. Compute Euler's Totient Function `φ(n)`

If the prime factors are `p1, p2, ..., pk`, then:

```
φ(n) = (p1 - 1) * (p2 - 1) * ... * (pk - 1)
```

### 3. Compute the private exponent `d`

Using the modular inverse:

```
d = e^-1 mod φ(n)
```

### 4. Decrypt the ciphertext

```
m = ct^d mod n
```

### 5. Extract the flag from the decrypted data

The decrypted value is saved to a file and printable strings are extracted using a regular expression.

---

## Code Snippet

```python
from sympy import mod_inverse
from Crypto.Util.number import long_to_bytes
import re

# Values given
e = 65537
ct = <ciphertext>
primes = [p1, p2, ..., p32]  # List of 32 primes from FactorDB

# Compute φ(n) and n
phi = 1
n = 1
for p in primes:
    phi *= (p - 1)
    n *= p

# Compute private key and decrypt
d = mod_inverse(e, phi)
m = pow(ct, d, n)
flag_bytes = long_to_bytes(m)

# Save and extract readable strings
with open("output.bin", "wb") as f:
    f.write(flag_bytes)

with open("output.bin", "rb") as f:
    data = f.read()
    printable = re.findall(rb"[a-zA-Z0-9_{}\-!?]{5,}", data)
    for s in printable:
        print(s.decode(errors="ignore"))
```

---

## Retrieved Flag

```
crypto{700_m4ny_5m4ll_f4c70r5}
```

---

## Conclusion

This challenge demonstrates the importance of selecting strong RSA parameters. Using a modulus with many small primes significantly reduces security, making RSA encryption breakable with basic factorization tools.
