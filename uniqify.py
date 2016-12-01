# eliminate duplicates from one of the rhythm files - only print the first occurrence

# cd split-because; for f in *.txt; do python ../uniqify.py < $f > ../split-uniq-because/$f; done
# cd split-why; for f in *.txt; do python ../uniqify.py < $f > ../split-uniq-why/$f; done


import sys 
texts = {}


for line in sys.stdin:
  id, text, rhythm, pronunciation = line.split('\t')
  if not text in texts:
    texts[text] = True
    sys.stdout.write(line)
    
    