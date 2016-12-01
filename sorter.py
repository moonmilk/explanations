# read in all the rhymes inadvisedly stored in a multiline format
# try to find interesting ways to organize them

import sys, random, re
from collections import defaultdict



rhymes = []

def addRhyme(rhyme):
  global rhymes
  rhymes.append(rhyme)


rhyme = {}
for line in sys.stdin:
  line = line.rstrip()
  if len(line) == 0:
    # get rid of any same-word rhymes that snuck through
    whywords = rhyme['why'].split()
    becausewords = rhyme['because'].split()
    if len(whywords) > 1 and len(becausewords) > 1 and whywords[-1] != becausewords[-1]:
      addRhyme(rhyme)
    rhyme = {}
  elif "why" in rhyme:
    rhyme['because'] = line
  else:
    rhyme['why'] = line
    
    
#print rhymes

def sortByBecause():
  rhymes.sort(key=lambda r: r['because'])
  
  for rhyme in rhymes:
    print "q: " + rhyme['why'].lower() + "?"
    print "a: " + rhyme['because'].lower() + "."
    print ""
    
    
def findTopWords():
  topwords = {}
  for rhyme in rhymes:
    words = rhyme['why'].split() + rhyme['because'].split()
    for word in words:
      if word in topwords:
        topwords[word] += 1
      else:
        topwords[word] = 1
        
  for key, value in sorted(topwords.iteritems(), key=lambda (k,v): (-v,k)):
    print "%s: %s" % (key, value)

# good words found in top:
# people love/loved everything/things look heart friend/s nothing work play girl/s/boy/s/guy/s/man/men/woman/women smell school hurt hair twitter phone/game 
# sad/happy/afraid/feels/think/thinking/feeling/feelings/hurts/thought/mood
# husband/wife/boyfriend/girlfriend
# brother/sister/mother/father/mom/dad/kid/baby
# pretty/ugly/looks/body
# myself 
# weather/sun/rain/snow/wind
# fake boring stupid dumb
# house/home jail dumb trump worst pee dog/cat/pet understand  

groups = [
  "people", 
  "love loved",
  "everything things nothing",
  "look looks pretty ugly body",
  "heart",
  "friend friends",
  "work play job office",
  "girl girls boy boys guy guys man men woman women",
  "smell",
  "school homework schools college grade grades",
  "twitter",
  "phone game iphone email web video",
  "sad afraid hurt hurts",
  "happy good",
  "think thinking feel feels feeling feelings thought mood",
  "husband wife boyfriend girlfriend fiance fiancee",
  "brother sister mother father mom dad kid baby",
  "myself",
  "weather sun rain snow wind",
  "fake boring stupid dumb",
  "house home room apartment",
  "jail police cops lawyer legal arrest probation",
  "food cooking kitchen dinner lunch breakfast snack snacks lunches dinners stove oven",
  #"trump",
  "worst",
  "cat dog pet",
  "understand"
]
grouped = defaultdict(list)

def checkRhyme(rhyme, errorRate = 0.0004):
  global grouped
  global groups
  rhymewords = rhyme['why'].lower().split() + rhyme['because'].lower().split() 
  for groupwords in groups:
    for groupword in groupwords.split():
      if random.random() < errorRate:
        grouped[groupwords].append(rhyme)
        return
      elif groupword in rhymewords:
        grouped[groupwords].append(rhyme)
        return


def recase(t):
  t = t.lower()
  t = t[0].upper() + t[1:]
  t = re.sub(r'\bi\b', 'I', t)
  return t
    
def groupTheRhymes():
  for rhyme in rhymes:
    checkRhyme(rhyme)
    
  print "<html><head><title>Why am I put in these situations</title><link rel='stylesheet' type='text/css' href='explanations.css'></head><body>"
  print "<div class='titlepage'>"
  print "<h1 class='title'>Why am I put in these situations?</h1>"
  print "<h1 class='title'>Why do I suck at conversations?</h1>"
  print "<h1 class='title'>Why do we hate us if we're God's creations?</h1>"
  print "<h1 class='title'>Why can't I love you without complications?</h1>"
  print "<h1 class='subtitle'>a reference book of explanations</h1>"
  print "<div class'author'>https://github.com/moonmilk/explanations</div>"
  
  print "<div class='contents'><h2 class='contentshead'>Table of Contents</h2>"
  print "<ul class='contentslist'>"
  for group in grouped.keys():
    print "<li class='contentsitem'>" + recase(grouped[group][0]['why']) + "</li>"
  print "</ul></div>"
  print ""   

  for group in grouped.keys():
    print "\n\n"
    #print "====== " + group.upper() + " (" + str(len(grouped[group])) + ") ======"
    print "<div class='chapter'>"
    print "  <h2 class='chapterhead'>" + recase(grouped[group][0]['why']) + "?</h2>"
    print ""
    
    num = 140
    if len(grouped[group]) < num:
      num = len(grouped[group])
      
    for rhyme in random.sample(grouped[group], num):
      print "  <div class='pair'>"
      print "    <div class='why'>" + recase(rhyme['why']) + "?</div>"
      print "    <div class='because'>" + recase(rhyme['because']) + ".</div>"
      print "  </div>"
      print ""
    print "</div>"
    
  print "</body></html>"
    

groupTheRhymes()