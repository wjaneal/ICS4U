#Gears Program

gears = [18,24,30,40,54,72]
ratios = []
for i in range(0, len(gears)):
    for j in range(i, len(gears)):
        ratio = 1.0*gears[j]/gears[i]
        if ratio not in ratios:
            ratios.append(ratio)
print(ratios)
compound = []
for i in range(len(ratios)):
    for j in range(i,len(ratios)):
        ratio = ratios[j]*ratios[i]
        if ratio not in compound:
            compound.append([ratios[i],ratios[j],ratio])
print(compound)


