#!/usr/bin/python
import re
import sys
 
DNA = sys.stdin.read().strip()
text ="""UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""
map = {key: value for key,value in re.findall('([ACGU]{3}) (Stop|[^BJOUXZ]{1})', text)}
prot = ""
for i in range(len(DNA)/3):
    sym = map[DNA[3*i:3*i+3]]
    if sym == "Stop":
        break
    else:
        prot += map[DNA[3*i:3*i+3]]
print prot

