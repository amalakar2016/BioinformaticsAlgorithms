#!/usr/bin/env python
###Given a string , this program will generate all substrings of length k/kmers  from that string######
def composition(text,k):
    n=len(text)
    for i in xrange(n-k+1):
        kmer_compos=text[i:i+k]
        print kmer_compos
#composition('ATTGGTGACACAGAGATCACTGGCCTGGTGCGCTTTCTGGTGATCACATTCATAATTGAGGATTACTTGTCCTCTCTTGAGAGTCGCAGCACACCACTTTTAGCCATGGGTCGTCTATAGTTCTTAGAGGCGGTTCTCCGCTTGACTAGTTGGATGCTAGAGCTTAAACACCGCGACGCTGTATTACAAGGGCGAAGACTTCCCCATTGTCTGATTGACCAGCTCTCGGAATTCCACGGGAAGGCCACCGATTGTTTGAGGAGGCGGGGAGGAGCAGTCAGATGGGGCCTCAATCGAAGGGGACCACGCAACCCCCGTCGTGTAGAGGTCCTCTAGATGCCGCCCGCAGGCGACGTAGCGATTCTCGAAATGCGACTCAAAGTAGAGAATAACTGCCGAAATCTCACAACGAATGGGGTGGCACCTGCTGCCTTCCGTTGGAGTGCGTTCACCAACTATTGTAAATAATGCTGCCGTAACATGTAGAGGAACAGCAGCCCTAGGGGCAAACGTTACGCAGTACATTTCTTCTCCGGTGCAAACCGCTCGAGGAATCGCACTTATTACTTTGCGTAATCCAACTTTGCGCAGAAACGCCTGTCAATTCCCACTGAATAGATCTAATGTACCCGGTGAGTACTAGAGGTCAGCGTTTCAAAAAGGGAGGCTCAGAAGTCGGGGTATTCACGCGCATTTTTTCGACGGTGCGTGATTGATCATGTCCTATGACTCATAGTAATAAACCTTTCCAACTTCAGTGTTGTCCACAAGGCGGACTTTTATCGAAGTGAGGAGCAAAATAATATCTACGTTAATCTTTAGGACTGCCCTGAAGTGTAGGCGCCCATATGAAAACGCCGCGGGGCGTTAAGAGGAGTGATGGTATGATTCTTCCCCCGCGTAACTCCAACACCAAGATTGTCCGGATCGTTGACCGGAAACGACCCCGTGCATCGCGACCGGGTTATCACGACACGACCCCGCAAATAGACTATGCCCGGCACCTACGAGTATGTATCTTTCCAGTCATATCAATATGACACGTGTAGGCGTGGAAGTAAAGAAGGATGTACAACCGATCTGTCCTCTAGATATAGCCAAGTGCGCGTCCGGGGCGGTCGTTAATCAAAAGCTCGTCCTGAACTTTCACGAACACGCATTATCTCCTGGCGCGAGCACCCCCGCGGGTGCGGCTCCGGGATCAATCGATCATATCCTTAGAATCGAACGCATTGGATTTCATGTGACAAGGAGTTAGGTTCTGGGAAGAGCTACATCCTTCACGTCCTTTCCTCTAAACCTAGTGCACGCTGTTAACGAACTGGAATGAACGCCTCAGTTTTTTAGCATAGGTAGCATCTTACAGGTTACCACGTCATTCCGTTGCCTCACCGGCACCCGCCTGCTCCGTATGTTGCCTACTCGATTGCACGCCGTGGTTCTTAAAAGACTTCGCAGGCCAGACCTCGGGCCCGTAATATACAAGGTCCTCGTGACTAGACAAACTCCCTGATCAAGAGTCATCTTGCGCATGAGTACGACGTTTCTTTAGTACTAATTACTTGGCTCCCGCCACCGGCTTCTCGTTTCACTTTGAGGACGGTGCAGAGGGAATATCCGTGCTCACAGTGTTCCTGGTAGCCCTCATGAGTTGCTTGCAAGCGACGTATTCAAGCTTTTAGACGTCCAACATTGGGATCCTCCATGACCATAAATGCTCCGGAATTTTAGAAGCCCGAACAACGGGGAGGTACAGACGATTTATAGCAACTCGTTAAGGAGTTGACGAACTATCTACGGTGCCGGCTGAGCTTGTTTCACTAGACTTCTTGAGGGCGTGCGTACGAGTCTAGAGATCCCGCTAGAACTAATCGCTACTCTTGCTCCCCTTTCCTCTTGTACGTCGTTGTGGTAATCTACAACGCCTGGTATCTGTCGTGGTGGTACCTGAGTGCACAAGCCACAGAGGAAACGCATGGGCCTGGAGCGCCGATGTGTGATCAGGTTGACCAACTCCAAGACCATAGTACCTCAAGAGCGATATAATTTTTTAGAACTCCGACCCTCCGTACAAGGGCACAAGTCGCGATCTCAGTCCGACCATCGACATATAACAATACTATTTCTTTCTTGTGGAACACCTACTGCCCACTTGGAAACTAGCCATAAGATGTGCCGGGATGTCTTTCGTCTACAACAGAAAACCGTCCCTAGTCATTAGCTTATCGCCATCGCAGGGCTACCAAGTCTATTCGGAGGGGATTTGGGAGAGGCGCGTCGGATTTCAATAGAGTGTACATTTGGGAACCCCAGCGTGGGTGGACGTCCGACCGCACGGTCTTGCTGATTTGCTCCGGCAACTGGTATGTTGATCCCAGTCGGGCAAGGCAGAGACGTATTTCCCGTCTGGATTGCAATTTAGGGTTTACTCCGCGACGCACATCTTGCCTCTTACCTCTCGTTCGTATGTGGATACACCTCCAGAGTATCCGCAAGCTTTCGCACGTCACCGCTATTAGAGTGCGCCTGATACACGGCAACGTGACATTTGTGGCCACCGTATTGCCTGAGAAGCTCCGGACCAGATGGCGCGGAAGCACGCGTGTATCGTCGTATCACTCGTACTAATGATTAGCCGCGGCATATTGATATTCCATATTGGTATGGCATTTATTACTCGCTACGAGACTACGACTGTCAAGATCCGAAACCACTAGGCGACTCCACGATAACGGGCCTAACCGTGAATGAGATAGTCTTCACGCAGTCAGTGAGATAGGAAGAAACGAGCGTTATACAAGTAAGTGCACCGGGCGCACGCACTCCTGTGCACGCCGCACATTGGGGTAATAAATAGCATCACGTTCTCGTTTACAGTGTCGTAGAGTAAGGCACACCAATGCAGACCCATATAAATCAACTGTAGGTCCGCTTTCTGGGTGCTCAACCAATGCGCGTACTTTCATGCCACCGCATTCGGTACAGTCCGTACTGCGCCCTATACGGAATGGTAAGCGTGCTCGGATTCTATGTAATTTGAGGAGTCGCTAACCAACAGTGTGGGGTATGTCTTCGGGCGCACACATTATCGCTGGTATCTGTTGGCAGCGAGGGTGAGTCACTGGCTTAGTTCGGACTGGGGCCTACGTACAGTTCGTCATCTAATTTTGACTAAGCAACTTAGATTACTTTCGTGCTCTAAACGTCCTGAGCTACTAAGGTGCCCAATACATCCATTCTCTTTGGACTCACACTTCGCACTGCCTTGGTTGTTAGCCCTTAATAAATTGGACGTGCGATATTGGACCCCCATGGACAGTATAAAAGGTGCGCTGGGTTGCTCGGCAAACAATATTGGGAATTCCCCCCAGCAGGGCATAGACACGCGCAGTTCGCCGAGGATGTCCCACGGTCGCCGTTACTATTCAACACCCCCTAGACGTCACAGTAGCTAGAGGATACCATCGGCTCAAACCGGTGTGACGGTAAGGCCTCATGCTTCCAGGTTAGTGCCATCCCGCACTCGGTAGCGAGCTTCGGATCTATCGTGTGCATATGACTACACACGTCGATAACACTGGTAACCGAAATAGTAAGCGCGTAATTAGGGGGACGTTTGAATTGCATTAGAAGGGGGCTAAAGGTTCTCAGCAGGACAAATCGTGGTTGAGAGATTGTTAGGTAAACAGCAAACGTCGGGTTACAAAAAAGAGCTAAGAGCGACGATCGCGCCGGACGTTAAGTTCAGTCACTCCCGGACCCCTGCGGTGTACAGACCATACGAAGCCGTCACCGCTTTGGTCGTGTATTTGGTCGGTCTCCGAAAGTTGCTGCTCGCAGCTAAATAAAGCATCTCAGCACTGGTCGGGGAAGCCAGTTGAACTCAGTAAGCTGCCGGACTTTCTCGTAACTGTCAGCCAATTGACCATTGGATTTCGCCTCCTAAAAGCGTGACAGGCTCCGAGATTTACCGCGCGTCACGCCCGTCTTTGAGCTACTACAATCTATAATAGACTATGGTGCTTTCCCTGGTTAAAAACGAAACTCGAGCGTGCTTCCCTAATGTAGTGCTCCACTCCTAAGAGCTTAGGCACCAGATTCCAATTGACAGGTCCTAAGTAAGCGGAAAACGATGTGATCACACCGATTCACGCACCTTTGTAACTAAAG',100)
with open('dataset_197_3.txt','r') as fh:# we must have this file otherwise this will throw up errors!
    t=''
    while True:
        if fh.readline()!='':
            t=t+fh.readline().rstrip()
        elif fh.readline()=='':#if we have reached the end of the file 
            break#get out of the loop!"break" breaks the while loop
fh.close()
#print t
composition(t.strip(''),100)

