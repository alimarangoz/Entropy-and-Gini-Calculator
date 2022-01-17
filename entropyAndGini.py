from __future__ import division
from math import log

# P represents as Positive (Yes, OK, Qualified exc.)
# N represents as Negative(No, Not OK, Not Qualified exc.)

def EntropyNew(p, n):

    return - (p/(n+p)) * log((p/(n+p)), 2) - (n/(p+n))*log((n/(p+n)), 2)

print("Entropy:", EntropyNew(9, 5), "\n")

print("Gain:", 0.98 - (3/7)*0.91 - (4/7), "\n")

def Gini(p, n):
    return 1 - ((p/(p+n)) * (p/(p+n)) + (n/(p+n)) * (n/(p+n)))

bigNumber = 7
littleNumber = 20-bigNumber

print("Gini:", Gini(3, 4))
print("Result:", bigNumber/20*Gini(3, 4)+littleNumber/20*Gini(7, 6))





