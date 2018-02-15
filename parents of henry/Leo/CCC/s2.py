#!/usr/bin/env python3
import sys

def noRotate(matrix):
#    return True
    for x in (0,N-1):
        for y in (0,N-2):
            if matrix[x][y] > matrix[x][y+1]:
                return False

    for y in (0,N-1):
        for x in (0,N-2):
            if matrix[x][y] >matrix[x+1][y]:
                return False
    return True

def oneRotate(matrix):
    for y in (0,N-2):
        for x in (0,N-1):
            if matrix[x][y] >matrix[x][y+1]:
                return False

    for x in (0,N-2):
        for y in (0,N-1):
            if matrix[x][y] > matrix[x+1][y]:
                return True
    return False

def threeRotate(matrix):
    for y in (0,N-2):
        for x in (0,N-1):
            if matrix[x][y] <matrix[x][y+1]:
                pass

    for x in (0,N-2):
        for y in (0,N-1):
            if matrix[x][y] < matrix[x+1][y]:
                return True
    return False


def twoRotate(matrix):
    for x in (0,N-2):
        for y in (0,N-2):
            if matrix[x][y] > matrix[x + 1][y]:
                pass

    for y in (0, N - 2):
        for x in (0, N - 1):
            if matrix[x][y] > matrix[x][y+1]:
                return True
        return False

N = int(input())
matrix = []

for i in range (N):
    rawData = input().split(" ")
    matrixRow = []
    for b in range (N):
        matrixRow.append(int(rawData[b]))
    matrix.append(matrixRow)

#matrix = sorted(matrix)

if noRotate(matrix):
    for i in range (N):
        for b in range (N):
            print(matrix[i][b], end=' ')
        print()
    sys.exit()

if oneRotate(matrix):
    for x in range (N):
        for y in range (N):
            print(matrix[-y-1][x],end=' ')
        print()
    sys.exit()

if threeRotate(matrix):
    for x in range (N):
        for y in range (N):
            print(matrix[y][-x-1],end=' ')
        print()
    sys.exit()

if twoRotate(matrix):
    for x in range (N):
        for y in range (N):
            print(matrix[-x-1][-y-1],end=' ')
        print()
    sys.exit()