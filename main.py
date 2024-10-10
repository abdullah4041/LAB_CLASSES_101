from Panda import * 

panda1 = Panda("panda_01", 7, 200,"healthy")
panda2 = Panda("panda_02", 5, 150,"healthy")
panda3 = Panda("panda_03", 3, 80,"healthy")
panda4 = Panda("panda_04", 10, 350,"sick")


print(panda1.display())
print(panda2.display())
print(panda3.display())
print(panda4.display())

print(panda1.check_health())
print(panda2.check_health())
print(panda3.check_health())
print(panda4.check_health())





