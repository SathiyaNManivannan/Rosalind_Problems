def revComplement(DNA_sequence):
    Comp = str(DNA_sequence).upper().replace("A", "t")
    Comp = Comp.replace("G", "c")
    Comp = Comp.replace("T", "a")
    Comp = Comp.replace("C", "g")
    revComp = Comp.upper()[::-1]
    print(revComp)
