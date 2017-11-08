# Top secret decoder
# The CIA has discovered a plot against a major city
# SIGINT has intercepted a message with the location and date of the attack 
# Unfortunately, the message is encoded. 
# Due to your awesome Python skills, you have been hired to decode the message
# A double agent has provided the encoding scheme which is as follows:
# All numbers need to be changed to spaces
# All capital letters should be changed to *
# The lowercase letter q is equal to \n
# All other lowercase letters should be ignored.

import os

os.system("clear")

print("""  
 ##  ###   #  
#     #   # # 
#     #   ### 
#     #   # # 
 ##  ###  # # 
CIA DECODER
01000011 01001001 01000001""")

cypher = "qGBH71VNT03FC874IYI00BKEqjO0A19O6W07W6S327W158PqWRN91JVS30AV8854W004EGCqJ9648pX5W1i7W6B555Az11925HqX6m313T9E35Y0V67RCC05AXCqq5R7478Hc567HKW08T6GqAD2t4p8AL2u80X3S71W6Dq3L2287Z997C3F64KjLhYq2O2976J182W8U7323JqNFB18NMAa52FDP7343Bq"

# Your code starts here
def decypher(decypted):
	for i in range(0, 10):
		decypted = decypted.replace(str(i), " ")
	for n in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		decypted = decypted.replace(n, "*")
	decypted = decypted.replace("q", "\n")
	for m in "abcdefghijklmnopqrstuvwxyz":
		decypted = decypted.replace(m, "")
	return decypted

# Your code ends here	
message = decypher(cypher)
print(message)