def stringprinter(s):
	output =""
	for i in range(len(s)):
		output = output + s[:i + 1]
	return output

print stringprinter("Car")
