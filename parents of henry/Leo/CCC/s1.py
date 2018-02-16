#!/usr/bin/env python3

villageNum = int(input())
villageLocation = []
villageNeighbourhood = []

for i in range (0,villageNum):
    villageLocation.append(int(input()))

villageLocation = sorted(villageLocation)

for i in range (1,villageNum-1):
    villageNeighbourhood.append((villageLocation[i] - villageLocation[i-1])/2 + (villageLocation[i+1] - villageLocation[i])/2)

villageNeighbourhood = sorted(villageNeighbourhood)

print(villageNeighbourhood[0])
