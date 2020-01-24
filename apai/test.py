infile = 'testfile.txt'

contents = open(infile).readlines()
pattern = 'a'
nlines = len(contents)
results = []
for i,line in enumerate(contents):
	if i != nlines-1:
		current_line = line
		next_line = contents[i+1]
		if pattern in current_line and pattern in next_line:
			results.append(current_line)
	elif i == nlines-1 and pattern in line:
		results.append(line)
print(results)
