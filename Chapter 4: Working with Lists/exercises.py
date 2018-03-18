#Exercise 4-3: Counting to Twenty
twenty = [foo for foo in range(0,21)]
print(twenty)

#Exercise 4-4: One Million - it's the same

#Exercise 4-5: Summing a Million
million = [bar for bar in range(0,1000001)]
print(min(million))
print(max(million))
print(sum(million))

#Ex.4-6: Odd Numbers
odd_list =[odd for odd in range(1,20,2)]
print(odd_list)

#Ex.4-7: Threes
threes = [3*three for three in range(1,11)]
print(threes)

#Ex.3-8: Cubes
cubes = [cube**3 for cube in range(1,11)]
print(cubes)

#Ex.3-9: Cubes in standard way
cubes1 = []
for cube1 in range(1,11):
    cubes1.append(cube1**3)
print(cubes1)