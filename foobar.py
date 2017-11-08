def answer(s):
    if len(s) <=200 and len(s) > 0: 
        count = 0
        #for i in range(len(s)):
        while s[:len(s)/2] == s[len(s)/2:]:
        	count += 1
        	s = s[:len(s)/2]
        	count += 1
    	print "pattern: %s" %(len(s))
    	print "count: %s" %(count)


    
s = "abccbaabccba"
print answer(s)