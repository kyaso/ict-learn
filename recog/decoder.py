from __future__ import absolute_import, division, print_function

scientists = ["shannon", "plato", "schottky", "nyquist", "hamming", "turing", "fourier", "wiener",  "gallager", "knuth" , "mackay","bell","kolmogorov","gauss","zuse","marconi","bernoulli","ohm","kirchhoff"]

#print Wissen[1]


#test = "rmrlrrrrmmrmllrrmrlrmrrrlrrrrlmllmlllrlrlrrlrllrrrmrmrrllrrmrlmlmmrlrmrlrrrmrrllrrlrrlmmr"
#print test


decoder = {"000" : " ", "0111" : "a" , "101110" : "b" , "11110" : "c",          			
		"00110" : "d" ,"110" : "e","10000" :"f","010100" :"g",
		"11111" :"h","0110" : "i","00111000100" : "j","00111001" :"k","10110" : "l",
		"01011" : "m","1001" : "n","1010" : "o","001111" : "p","00111000101" : "q","0010" :"r","0100":"s" ,
		"1110" :"t","10001" : "u","0011101" :"v","101111" :"w",
		"001110000" :"x","010101" :"y","0011100011" : "z"}

#print decoder["0111"]

slats = {"lll":"0010",
"llr": "1101",
"llm" : "00000",
"lrl": "1100",
"lrr":"1111",
"lrm":"00011",
"lml":"00010",
 "lmr":"01101",
"lmm":"0000111",
"rll":"1110",
"rlr":"1001",
"rlm":"01100",
"rrl":"1000",
"rrr":"1011",
"rrm":"01111",
"rml":"01110",
"rmr":"01001",
 "rmm":"000010",
"mll":"01000",
"mlr":"01011" ,
"mlm":"001101",
"mrl":"01010",
"mrr":"1010",
"mrm":"001100",
"mml":"001111",
"mmr":"001110",
"mmm":"0000110" }

#print slats["lll"]


def help(string):
	blocks = []
	word = ""
	i = 0
	for a in string:
	    word = word + a
	    #print word
	    #print i
	    if(i == 2):
		blocks.append(word)
		word = ""
		i = -1
	    i = i + 1

	#print (blocks)

	onezero=""
	for a in blocks:
		onezero = onezero + slats[a]
	#print (onezero)


	decoded=""
	#offset = 0
	#for offset < 
	wort=onezero[0]+onezero[1]+onezero[2]
	for a in onezero[3:]:
		if wort in decoder:
			decoded=decoded+decoder[wort]
			wort=""
		wort = wort+a

	#print decoded
	
	for a in scientists:
		if(a in decoded):
			print (decoded)
			return decoded

	

	return None

def decode(lmr_string):
	for offset in range(0,10):
		print("Decoder offset:" , offset)
		blocks = []
		word = ""
		j = 0
		for a in lmr_string[offset:]:
		    word = word + a
		    if(j == 2):
			blocks.append(word)
			word = ""
			j = -1
		    j = j + 1

		#print (blocks)

		onezero=""
		for a in blocks:
			onezero = onezero + slats[a]
		#print (onezero)


		decoded=""
		wort=onezero[0]+onezero[1]+onezero[2]
		for a in onezero[3:]:
			if wort in decoder:
				decoded=decoded+decoder[wort]
				wort=""
			wort = wort+a

		#print (decoded)
	
		for a in scientists:
			if(a in decoded):
				print("\nResult:\n")
				print (decoded)
				return True

	return False	
			

