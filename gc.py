#!/Users/fktadros/anaconda3/bin/python
"""
This is my first Python program, it calculates the GC content of any given DNA sequence
"""
dna=input("DNA Sequence:") #DNA sequence
no_c=dna.count('C') # count C's in the "dna" string
no_g=dna.count('G') # count G's in the "dna" string
dna_len=len(dna) # output length of "dna"
gc_percent=(no_g+no_c)*100/dna_len # calculate GC percentage
print("GC Content of given DNA sequence: %5.3f" % gc_percent,"%") # print GC% to screen
