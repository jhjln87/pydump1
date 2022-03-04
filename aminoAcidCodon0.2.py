# List of codons for each amino acid, they all have six items in the list so I can write less line of code
Methionine = ["AUG","AUG","AUG","AUG","AUG","AUG"]
Threonine = ["ACG","ACA","ACC","ACU","ACG","ACA"]
Asparagine = ["AAC","AAU","AAC","AAU","AAC","AAU"]
Lysine = ["AAG","AAA","AAG","AAA","AAG","AAA"]
Serinine = ["AGC","AGU","AGC","AGU","AGC","AGU"]
Arginine = ["AGG","AGA","AGG","AGA","AGG","AGA"]
Valine = ["GUU","GUC","GUA","GUG","GUU","GUC"]
Alanine = ["GCU","GCC","GCA",'GCG',"GCU","GCC"]
AsparticAcid = ["GAU","GAC","GAU","GAC","GAU","GAC"]
GlutamicAcid = ["GAA","GAG","GAA","GAG","GAA","GAG"]
Glycine = ["GGU",'GGC',"GGA","GGG","GGU","GGC"]
Phernylalanine = ["UUU","UUC","UUU","UUC","UUU","UUC"]
Leucine = ["UUA","UUG","CUU","CUC","CUA","CUG"]
Serine = ["UCU","UCC","UCA","UCG","UCU","UCC"]
Tyrosine = ["UAU","UAC","UAU","UAC","UAU","UAC"]
Cytesine = ["UGU","UGC","UGU","UGC","UGU","UGC"]
Tryptophan = ["UGG","UGG","UGG","UGG","UGG","UGG"]
Proline = ["CCU","CCC","CCA","CCG","CCU","CCC"]
Histidine = ["CAU","CAC","CAU","CAC","CAU","CAC"]
Glutamine = ["CAA","CAG","CAA","CAG","CAA","CAG"]
Arginine = ["CGG","CGA","CGC","CGU","CGG","CGA"]
Isoleucine = ["AUA","AUC","AUU","AUA","AUC","AUU"]
Stop = ["UAA","UAG","UGA","UAA","UAA","UAG"]

# So the same codon isn't projected for each amino acid'
import random

# Asking what you wanted to do
action = input("Code or decode the amino acids? (lowercase) ")

# running variable: loops until stop amino acid. 
running = True
if action == "code" or action == "c":
	sequence = ""
	while running == True: 
		number = random.randint(0,5)
		aminoAcid = input("input ONE amino acid name of the sequence (in order) ")

# Going through each amino acid because I don't know any other way' 
		if aminoAcid == "methionine" or aminoAcid == "met":
			sequence = sequence + Methionine[number]
		if aminoAcid == "threonine" or aminoAcid == "thr":
			sequence = sequence + Threonine[number]
		if aminoAcid == "asparagine" or aminoAcid == "asn":
			sequence = sequence + Asparagine[number]
		if aminoAcid == "lysine" or aminoAcid == "lys":
			sequence = sequence + Lysine[number]
		if aminoAcid == "serinine" or aminoAcid == "ser":
			sequence = sequence + Serinine[number]
		if aminoAcid == "arginine" or aminoAcid == "arg":
			sequence = sequence + Arginine[number]
		if aminoAcid == "valine" or aminoAcid == "val":
			sequence = sequence + Valine[number]
		if aminoAcid == "alanine" or aminoAcid == "ala":
			sequence = sequence + Alanine[number]
		if aminoAcid == "aspartic acid" or aminoAcid == "asparticacid" or aminoAcid == "asp":
			sequence = sequence + AsparticAcid[number]
		if aminoAcid == "glutamic acid" or aminoAcid == "glutamicacid" or aminoAcid == "glu":
			sequence = sequence + GlutamicAcid[number]
		if aminoAcid == "glycine" or aminoAcid == "gly":
			sequence = sequence + Glycine[number]
		if aminoAcid == "phernylalanine" or aminoAcid == "phe":
			sequence = sequence + Phernylalanine[number]
		if aminoAcid == "leucine" or aminoAcid == "leu":
			sequence = sequence + Leucine[number]
		if aminoAcid == "serine" or aminoAcid == "ser":
			sequence = sequence + Serine[number]
		if aminoAcid == "tyrosine" or aminoAcid == "tyr":
			sequence = sequence + Tyrosine[number]
		if aminoAcid == "cytesine" or aminoAcid == "cys":
			sequence = sequence + Cytesine[number]
		if aminoAcid == "tryptophan" or aminoAcid == "trp":
			sequence = sequence + Tryptophan[number]
		if aminoAcid == "proline" or aminoAcid == "pro":
			sequence = sequence + Proline[number]
		if aminoAcid == "histidine" or aminoAcid == "his":
			sequence = sequence + HIstidine[number]
		if aminoAcid == "glutamine" or aminoAcid == "gln":
			sequence = sequence + Glutamine[number]
		if aminoAcid == "arginine" or aminoAcid == "arg":
			sequence = sequence + Arginine[number]
		if aminoAcid == "isoleucine" or aminoAcid == "ile":
			sequence = sequencse + Isoleucine[number]
		if aminoAcid == "stop":
			running = False
			print(sequence)

# decodig the codons, work in progress
if action == "decode" or action == "d":
	print("work in progress")
	print("sorry")