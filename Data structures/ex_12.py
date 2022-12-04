def game(terra, power):
    #print(terra)
    #print(power)
    for i in terra:
        for j in i:
            if j <= power:
                power += j
                #print(power)
            else:
                break
    return power


print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))
print(game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 1))
print(game([[], []], 1))
print(game([], 1))