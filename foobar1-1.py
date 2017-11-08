# import re

# def answer(s):
# 	# change string to lower/upper massage the data format
#     if len(s) <=200 and len(s) > 0: 
#         count = 0
# 		for i in len(s):
# 			pattern = 
# 			if 

        	
#     return count

def answer(s):
	for subLen in range(1, len(s) + 1):
		if len(s) % subLen == 0:
			correct = True
			for multFactor in range(len(s) / subLen):
				if s[subLen * multFactor:subLen * (multFactor + 1)] != s[:subLen]:
					correct = False
					break
			if correct:
				return len(s) / subLen

print answer("a")
print answer("ab")
print answer("aa")
print answer("ababab")
print answer("abcabcabc")
print answer("abccbaabc")
print answer("aaaa")
print answer("aaabbaaaaaabbaaa")
print answer("ssa")


	

"""
a 1
ab 1
aa 2
ababab 3
"ababab"[0:2] == "ababab"[2:4]; Yes, count++;
"ababab"[2:4] == "ababab"[4:6]; Yes, count++;
"ababab"[4:6] == "ababab"[6:8] <-- ERROR;
ababcababc
abcabcabc 3
abccbaabc 1
aaaa 4
aaabbaaaaaabbaaa 2
ssa 1
sadtdytfubhkurtujfgcyirduthghkvfcjkhujikvbngbchdfthmbhnkutgyfhgd7yut5tfgy5rrtfgdcsdrtfggyuhjdhtfgyutfgbyufyuhtgfgbyuhbhjfgyfuhjgbfgbyuhuhjfb 1
"""