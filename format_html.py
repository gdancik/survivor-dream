# reads from file and writes to standard output, but adds <p> tags around non-blank lines

with open('file.txt') as f :
	for line in f.readlines() :
		if len(line.strip()) == 0 :
			print(line.strip())
		else :
			print('<p>', line.strip(), '</p>') 

