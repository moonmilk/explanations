# extracted WHY and BECAUSE lines from logs with 5-12 syllables using
# cat *.txt | grep '  BECAUSE  ' | egrep '  [0-2]{5,12} ' > ~/because-5-12.txt&
# cat *.txt | grep '  WHY  ' | egrep '  [0-2]{5,12}  ' > ~/why-5-12.txt&

# break up the big log files into one for each rhythm

words = ('why','because')

for word in words:
  filename = word + "-5-12.txt"
  with open(filename, 'r') as f:
    for line in f:
      #print line
      parts = line.split('\t')
      #print parts, len(parts)
      if len(parts) == 4:
        rhythm = parts[2]
        splitfilename = 'split-' + word + "/" + rhythm + ".txt"
        with open(splitfilename, "a") as s:
          s.write(line) 
        
        