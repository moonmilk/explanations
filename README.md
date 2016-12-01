# explanations
A book of explanations: a project for nanogenmo 2016

Download the finished novel from https://github.com/moonmilk/explanations/raw/master/explanations.pdf

```
WHY BE SEDUCED BY THE PAST IT WASN'T PLEASANT 
BECAUSE SUBJECTIVITY IS OMNIPRESENT 

WHY IF MY CONVERSE SHRINK IN THE DRYER UH OH 
BECAUSE IN THE END THE ANSWER IS ALWAYS NO 

WHY I GET HOME AND MY WHOLE ROOM IS REARRANGED 
BECAUSE PERSEVERING THAT MAKE A PERSON CHANGED 

WHY IS IT SNOWING RIGHT NOW WHAT HAPPENED TO FALL 
BECAUSE IN OCTOBER IT'S ALL ABOUT BASEBALL 

WHY ARE WE TALKING ABOUT SLICED CHEESE THIS IS CHEM 
BECAUSE IN THE END YOU BECAME USELESS TO THEM 

WHY COULDN'T I HAVE BEEN BLESSED WITH GREEN OR GREY EYES 
BECAUSE IN THE END OF THE DAY GALS BEFORE GUYS 

WHY DO WHITE PEOPLE HAVE TROUBLE SPELLING JOSE 
BECAUSE IN THE END EVERYTHING WILL BE OKAY 

WHY ME AND MY SISTER UP EATING CAKE BATTER 
BECAUSE IN THE END IT DOESN'T EVEN MATTER 

WHY THIS LONG HEAD GIRL DON'T HURRY ANSWER MY CALL 
BECAUSE IN THE END THIS WILL DETERMINE IT ALL 
```

I collected hundreds of thousands of tweets that begin with WHY or BECAUSE, and saved the ones with between 5 and 12 syllables - they are saved in the files `why-5-12.txt` and `because-5-12.txt`. I'd saved them in a format that looks like this:

```
682838856970842112	BECAUSE I'M DRUNK LET ME TELL YOU SOMETHING	0111111110	B IH0 K AO1 Z  , AY1 M  , D R AH1 NG K  , L EH1 T  , M IY1  , T EH1 L  , Y UW1  , S AH1 M TH IH0 NG 
682838915875639296	BECAUSE I AM SO NOT LIVING RIGHT NOW	0111111011	B IH0 K AO1 Z  , AY1  , AE1 M  , S OW1  , N AA1 T  , L IH1 V IH0 NG  , R AY1 T  , N AW1 
```

That's the tweet ID, all the words from the tweet that also exist in the CMU Pronouncing Dictionary (CMUDict), and finally the meter and pronunciation of the tweet as determined by CMUDict. I neglected to save the original tweet text!

`splitter.py` splits the why and because files into thousands of subfiles based on their metrical rhythm, in a probably misguided attempt to conserve memory space in the next step. I only try to rhyme sentences that have the same meter, so no use loading up all those sentences with different meters. (Though in fact it sounded better when I told it to ignore the first syllable of 'because' in matching meters, so that's what the final version does.)

`uniqify.py` looks at each of the split files and removes duplicate texts.

`rhymer.py` goes through each of the different metrical rhythm files and for each _because_ line, attempts to find a rhyming _why_ line. I saved the results in the file `firstrun.rhymes`, which despite the name is not the first run - I kept rerunning the command with the same filename.

I used `sorter.py` to get some information about what was in the rhymes file, like finding the most common words (`topwords.txt`), which I then used to make a list of about 25 subject categories. I used those categories to sort the questions and answers, and then pick up to 140 question-answer pairs for each chapter of the resulting book. (It's also encouraged to make a sorting mistake now and then, for variety.) It prints out the chapters of the book as an html file `explanations.html`. 

I made a css file `explanations.css` with some advice from Liza Daly to make the printed version of the text look better. I printed the html file in Chrome to create the final pdf file `explanations.pdf`.
