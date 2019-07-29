""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1
def no_new_line(str):
    if '\n' in str:
        start=str.find('\n')
        return no_new_line(str[:start]+str[start+2:])
    else:
        return str
def lines_from_file(path):
    file=open(path)
    assert readable(file),"The file is not readable..."
    lines=readlines(file)
    result=[]
    for l in lines:
        l=no_new_line(l)
        l=strip(l)
        #print ('DEBUG:',l)
        result+=[l]
    #print("DEBUG:", result)
    close(file)
    return result
def new_sample(path,i):
    return lines_from_file(path)[i]
# END Q1
# BEGIN Q2
def analyze(sample_paragraph,typed_string,start_time,end_time):
    result=[(len(typed_string)/5)/((end_time-start_time)/60),0.0]
    accuracy=0
    sample_words=split(sample_paragraph)
    typed_words=split(typed_string)
    for i in range(min(len(sample_words),len(typed_words))):
        if sample_words[i]==typed_words[i]:
            accuracy+=1
    if min(len(sample_words),len(typed_words))==0:
        return result
    result[1]=accuracy/min(len(sample_words),len(typed_words))*100.0
    return result

# END Q2
# BEGIN Q3
def pig_latin(word):
    if word[0] in ['a','e','i','o','u']:
        return word+'way'
    else:
        start=len(word)
        min=len(word)
        for letter in ['a','e','i','o','u']:

            if letter in word:
                start=word.find(letter)
                if start<min:
                    min=start
        if min==len(word):
            return word+'ay'
        else:
            return word[min:]+word[:min]+'ay'
# END Q3
# BEGIN Q4
def autocorrect(input_word,words_list,score_function):
    if input_word in words_list:
        return input_word
    else:
        return min(words_list,key=lambda x: score_function(input_word,x))
# END Q4
# BEGIN Q5
def swap_score(w1,w2):
    '''
    You should consider the leftmost character of each string to correspond to each other. For example, if the two inputs are "word" and "weird", we'll only consider potential substitutions for "word" and "weir".
    '''
    if w1==w2:
        return 0
    if len(w1)>len(w2):
        w1=w1[:len(w2)]
    else:
        w2=w2[:len(w1)]
    if w1[0]==w2[0]:
        return swap_score(w1[1:],w2[1:])
    else:
        return 1+swap_score(w1[1:],w2[1:])
# END Q5
# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""
    added=0
    swapped=0
    if len(word1)>len(word2): # Assume word1 is the shorter word.
        word1,word2=word2,word1
    if word1==word2: # same words. Nothing to do.
        # BEGIN Q6
        return 0
        # END Q6

    if not word1:
        added+=len(word2)
        return len(word2)
    elif word1[0]==word2[0]:
        # BEGIN Q6
        return score_function(word1[1:],word2[1:])
        # END Q6

    else:
        if word1 in word2:
            added+=len(word2)-len(word1)
            return len(word2)-len(word1)
        elif len(word2)==len(word1) or True in [word1[i]==word2[i] for i in range(len(word1))]:
            swapped+=1
            return 1+score_function(word2[0]+word1[1:],word2)
        else:
            added+=1
            return 1+score_function(word2[0]+word1,word2)




        # BEGIN Q6

        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7
def score_function_accurate(word1, word2):
        added=0
        swapped=0
        if len(word1)>len(word2): # Assume word1 is the shorter word.
            word1,word2=word2,word1
        if word1==word2: # same words. Nothing to do.
            # BEGIN Q6
            return 0
            # END Q6

        if not word1:
            added+=len(word2)
            return len(word2)
        if word1[0]==word2[0]:
            # BEGIN Q6
            return score_function_accurate(word1[1:],word2[1:])
            # END Q6

        else:
            if word1 in word2:
                added+=len(word2)-len(word1)
                return len(word2)-len(word1)
            elif len(word2)==len(word1) or True in [word1[i]==word2[i] for i in range(len(word1))]:
                swapped+=1
                #print('DEBUG:',word1[0],word2[0],KEY_DISTANCES[word1[0],word2[0]] )
                return KEY_DISTANCES[word1[0],word2[0]]+score_function_accurate(word2[0]+word1[1:],word2)
            else:
                added+=1
                return 1+score_function_accurate(word2[0]+word1,word2)


# END Q7
#BEGIN Q8
table={}
def score_function_final(word1, word2):

        if len(word1)>len(word2): # Assume word1 is the shorter word.
            word1,word2=word2,word1

        if word1==word2: # same words. Nothing to do.
            # BEGIN Q6
            return 0
            # END Q6

        if not word1:
            #added+=len(word2)
            return len(word2)
        if word1+word2 in table:
            return table[word1+word2]
        if word1[0]==word2[0]:
            # BEGIN Q6
            result=score_function_final(word1[1:],word2[1:])
            table[word1+word2]=result
            return result
            # END Q6

        else:
            if word1 in word2:
            #    added+=len(word2)-len(word1)
                return len(word2)-len(word1)
            elif len(word2)==len(word1) or True in [word1[i]==word2[i] for i in range(len(word1))]:
            #    swapped+=1
                #print('DEBUG:',word1[0],word2[0],KEY_DISTANCES[word1[0],word2[0]] )
                result=KEY_DISTANCES[word1[0],word2[0]]+score_function_final(word2[0]+word1[1:],word2)
                table[word1+word2]=result
                return result
            else:
            #    added+=1
                result=1+score_function_final(word2[0]+word1,word2)
                table[word1+word2]=result
                return 1+score_function_final(word2[0]+word1,word2)
#END Q8
