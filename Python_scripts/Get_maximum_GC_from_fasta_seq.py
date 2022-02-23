# These two python functions help identify the DNA sequence with highest GC content among a set of DNA sequences in fasta format 

# Define GCpercent function
# Algoritm
# 1. convert the DNA sequence to upper case to prevent lower_case/upper_case confusion
# 2. Find all Gs
# 3. Find all Cs
# 4. Calculate percentage as sum of all Gs and all Cs, divided by length of the sequence, times 100
# 5. return GC percent
def GCpercent(DNA_sequence):
    G_count = DNA_sequence.upper().count("G")
    C_count = DNA_sequence.upper().count("C")
    GC_percent = (G_count + C_count)/len(DNA_sequence)*100
    return(GC_percent)

# Define FindMaxGC_fromfasta
# Algorithm
# 1. open the fasta file in read format
# 2. strip line end characters
# 3. create a empty list for fasta_headers
# 4. initiate an empty sequence
# 5. initiate an empty list for fasta_sequence
# 6. Loop through the lines to identify 
#   6a. If the line starts with a > symbol indicating a header
#       6a. 1) Add the current line to list of fasta_headers
#       6a. 2) Add any sequence that has been compiled together to sequences list
#       6a. 3) reset sequence to empty ("")
#   6b. If the line does not start with > symbol
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
