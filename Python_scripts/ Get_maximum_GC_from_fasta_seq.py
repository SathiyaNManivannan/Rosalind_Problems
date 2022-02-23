def GCpercent(DNA_sequence):
    G_count = DNA_sequence.upper().count("G")
    C_count = DNA_sequence.upper().count("C")
    GC_percent = (G_count + C_count)/len(DNA_sequence)*100
    return(GC_percent)

def FindMaxGC_fromfasta(file_path):
    fasta_lines = open(file_path, 'r').readlines()  
    
    fasta_lines = list(map(str.strip, fasta_lines))
    
    fasta_header = []
    sequence = ""
    fasta_sequence = []
    for lines in fasta_lines:
        if lines.startswith(">"):
            fasta_header.append(lines)
            fasta_sequence.append(sequence)
            sequence = ""
        else:
            sequence = sequence + lines
    fasta_sequence.append(sequence)
    fasta_sequence.pop(0)
    
    fasta_header = list(map(str.lstrip, fasta_header, list(">"*len(fasta_header))))
    
    fasta_GCcont = list(map(GCpercent, fasta_sequence))
    fasta_dict = dict(zip(fasta_header, fasta_sequence))
    GC_dict = dict(zip(fasta_header, fasta_GCcont))
    max_GC_key = max(GC_dict, key=GC_dict.get)
    max_GC = max(GC_dict.values())
    print(fasta_dict)
    print(GC_dict)
    print("{}\n{}".format(max_GC_key, max_GC))
