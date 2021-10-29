python="python"
print("A szó első karaktere:",python[0])
print("A szó utolso karaktere:",python[5]) #nem jó, ha változik  hossz
print("A szó utolso karaktere:",python[-1])
print("A szó utolso karaktere:",python[len(python) - 1])

print("A szó 5 ször egymás után:", (python + " ")*5)

str2, str3 = "hallgató", "Hiába hegynyi az anyag, a hallgató gyorsan halad"
print(str2 in str3)
print(python in str3)
print(python not in str3)
print(str3[6:22])
print(python+str2+str3)
print(python,str2,str3,sep="\t")

str4="HALLGATÓ"
print(str4 in str3)
print(str4 > str2)