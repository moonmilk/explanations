

import glob, re, sys
from random import choice, randrange


def rhymeInfo(logline, whybecause=None):
  info = {}
  info['id'], info['text'], info['rhythm'], info['pron'] = logline.rstrip().split('\t')
  # if the last word is "IT", make it unaccented
  if re.sub(r', IH1 T$', ', IH0 T', info['pron']):
    re.sub(r'1$', '0', info['rhythm'])
  
  # # adjust because rhythm
  # if whybecause=="because":
  #  re.sub(r'^01', '0', info['rhythm'])
   
  pron_no_words = re.sub(' , ', '', info['pron'])
  rhymematch = re.search(r'([A-Z]+\d?)*\s([A-Z]+1[^1]*)$', pron_no_words)
  if rhymematch:
    info['consonant'] = rhymematch.group(1)
    info['rhymeclass'] = rhymematch.group(2)
  return info
  
def rhymes(info1, info2):
  return info1['consonant'] != info2['consonant'] and info1['class'] == info2['class']


ccc = 0

shortenBecause = True
if shortenBecause:
  sylList = (13,12,11,10,9,8,7,6)
else:
  sylList = (13,12,11,10,9,8,7,6,5)

for syls in sylList:
  usedwhyids = []
  
  whyfilenames = glob.glob('split-uniq-why/' + ('?' * syls) + '.txt')
  becausefilenames = glob.glob('split-uniq-because/' + ('?' * syls) + '.txt')
  
  for bfn in becausefilenames:

    whatever, rhythm, whatever = re.split('\D+', bfn)

    if shortenBecause:
      rhythm = re.sub('^0', '', rhythm)
      
          
    # find potentially matching why files
    matchingre = re.sub('2', '\d', rhythm)
    matchingre = re.sub('0', '[02]', matchingre)
    matchingre = re.sub('1', '[12]', matchingre)
    matchingre = '/' + matchingre + '.txt'
    matcher = re.compile(matchingre)
    
    strictRhythms = True
    if strictRhythms:
    # go strict instead
      matchingwhyfilenames = ['split-uniq-because/' + rhythm + '.txt']
    else:
      matchingwhyfilenames = filter(matcher.search, whyfilenames)
    
    
    # load in all potentially matching why lines
    whys = {}
    
    for mwhyfn in whyfilenames:
      with open(mwhyfn) as mwhyfile:    
        for whyline in mwhyfile:
          info = rhymeInfo(whyline)
          id, rhymeclass, consonant = info['id'], info['rhymeclass'], info['consonant']
          # don't use the same whyid twice
          if not id in usedwhyids:
            if not rhymeclass in whys:
              whys[rhymeclass] = {}
            if not consonant in whys[rhymeclass]:
              whys[rhymeclass][consonant] = []
            whys[rhymeclass][consonant].append(info)
            
            ccc += 1
            #if ccc % 250 == 0:
            #  print ccc
          
          
    #print whys[whys.keys()[0]]
    
    with open(bfn) as becausefile:
      for becauseline in becausefile:
        info = rhymeInfo(becauseline, 'because')
        rhymeclass, consonant = info['rhymeclass'], info['consonant']
        if rhymeclass in whys:
          why_consonants = whys[rhymeclass].keys()
          if consonant in why_consonants:
            why_consonants.remove(consonant) 
          if len(why_consonants) > 0:
            why_consonant = choice(why_consonants)
            # keep list neat so we are guaranteed there's at least one choice in here
            why_item_index = randrange(len(whys[rhymeclass][why_consonant]))
            why_rhyme = whys[rhymeclass][why_consonant].pop(why_item_index) # pop removes the item from the list
            # if nothing left, delete the consonant array
            if len(whys[rhymeclass][why_consonant]) == 0:
              del(whys[rhymeclass][why_consonant])
            # if nothing left in rhymeclass, delete it
            if len(whys[rhymeclass]) == 0:
              del(whys[rhymeclass])
              
            # don't use the same why id again in a future round (wouldn't happen anyway in strictRhythm mode)
            usedwhyids.append(why_rhyme['id'])
            
            print why_rhyme['text'], "\n", info['text'], "\n"
            sys.stdout.flush()
            
            
            
          
          
        
  
  
  
  
