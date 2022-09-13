print ("enter basic salary")
basic =float(input())

hra = basic*35/100
da = basic*70/100
ta = basic*20/100
pf = basic*13/100
tax = basic*18/100

gross = basic + da + ta + hra - pf - tax

print("Basic Salary  : ",basic)
print("HRA             : ",hra)
print("TA               : ",ta)
print("DA               : ",da)
print("PF                : ",pf)
print("TAX             : ",tax)
print("Gross Salary : ",gross)
