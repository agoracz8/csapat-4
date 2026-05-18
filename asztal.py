asz =int(input("melyik asztalt szeretné(1-10 bent,11-20 kint?:)"))
while asz <1 or asz >20:
    print('hibás asztalszám')
    asz =int(input("melyik asztalt szeretné(1-10 bent,11-20 kint)"))
with open("aszatlfoglalas.txt","w") as fajl:
    fajl.write(str(asz))
