from Crypto.Util.number import inverse, long_to_bytes

# Provided values
p = 848445505077945374527983649411
q = 1160939713152385063689030212503
n = p * q
e = 65537
ct = 948553474947320504624302879933619818331484350431616834086273

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
pt = pow(ct, d, n)
flag = long_to_bytes(pt)
print(flag.decode())

# used factordb to get p and q and used the above script to get the flag
