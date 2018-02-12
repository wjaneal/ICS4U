#Gears Program

gears = [18,20,30,40,54,72, 80, 100, 120, 144, 150]
ratios = []
for i in range(0, len(gears)):
    for j in range(i, len(gears)):
        ratio = 1.0*gears[i]/gears[j]
        if ratio not in ratios:
	    ratios.append(ratio)
print(ratios)


