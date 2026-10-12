name = input()
sn,n,o = name.split()
sn_2,n_2,o_2 = [x.capitalize() for x in (sn,n,o)]
print(sn_2,n_2[0] + '.',o_2[0] + '.')