f = open("githubascii.txt")
string = ''
i = 0
CHARTOREPLACE = 'N'
STRINGREPLACEMENT = 'sphinx of black quartz, judge my vow'

for line in f:
	for char in line:
		if char == CHARTOREPLACE:
			if i > (len(STRINGREPLACEMENT)-1):
				i = 0
			string += STRINGREPLACEMENT[i]
			i+=1
		else:
			string += char

f.close()
out = open(f'replaced_with_({STRINGREPLACEMENT}).txt','w')
out.write(string)
out.close()