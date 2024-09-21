**WHAT IS MODULAR ARITHMATICS**

Modular arithmetic deals with the remainder when one number is divided by another. The modulus of a to B (often written as mod(B, a)) is the remainder when a is divided by B.

-mod(11, 2) = 1, as 11 = 2(5) + 1, where 1 is the remainder
-mod(11, 4) = 3, as 11 = 4(2) + 3, where 3 is the remainder

If remainder = mod(B, a)
B =  a*N + remainder
N is the qoutient of B and a -> B//a
_____________________________________________________________

**THE USE OF MODULAR ARITHMATICS IN PRODUCT MAPPING (one to one correspondence)**

1.Product Mapping

Set A = [a1, a2, a3...aM] with size p
Set B = [b1, b2, b3...aM] with size q

Set C is the Product Map of Set A to Set B
Set C will have  size p*q

Set C = ([A0, B0], [A0, B1], [A0, B2]...[A(p - 1), B(q - 1)])

**Alternate expression below for set C**

A0 -> B[0], B[1], ...B[q - 1]
A1 -> B[0], B[1], ...B[q - 1]
.
.
A[p - 1] -> B[0], B[1], ...B[q - 1]


2.Computing the index of set A and set B, where index of set C is the dependant(known) variable.

An = Set A index
Bn = Set B index
Cn = Set C index
p = Set A size
q = Set B size 

Index Cn is modulated by the index An multipllied by the size of set B (q) , index Bn is the remainder.

Given the modular form Cn = q(An) + Bn

>>Bn = Mod(Cn, q)

>>An = Cn//q OR [(Cn - Mod(Cn, q))]/q






