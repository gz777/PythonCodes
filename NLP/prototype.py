# NLP prototyping script gz 4/7/21

from nltk.corpus import wordnet as wn
import math

def sig(t): #sigmoid function
    return 1/(1+math.exp(-t))

def tanh(t): #hyperbolic tangent function
    return (math.exp(2*t)-1)/(math.exp(2*t)+1)

def logistic(t,a,b): #logistic regression function, smoothed sigmoid function.
    return 1/(1+math.exp(-(a+b*t)))

def getSynAnt(word):
    synonyms = []
    antonyms = []
    hypernyms = [] # The generic term used to designate a class of specifics
    holonyms = [] # part of
    meronyms = []
    # Use a breakpoint in the code line below to debug your script.
    print(f'Here we go - {word}')  # Press ⌘F8 to toggle the breakpoint.

    syns = wn.synsets(word)
    print(syns)

    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
            if l.hypernyms():
                hypernyms.append(l.hypernyms()[0].name())
            #if l.holonyms():
            #    holonyms.append(l.holonyms()[0].name())
            #if l.meronyms():
            #    meronyms.append(l.meronyms()[0].name())

    print(set(synonyms))
    print(set(antonyms))
    print(set(hypernyms))



# test script
if __name__ == '__main__':
    getSynAnt('marketing')
    list = [1,2,3,4,5,6,7,8,9,10,20]
    result1 = []
    result2 = []
    result3 = []
    for l in list:
        result1.append(sig(l))
        result2.append(tanh(l))
        result3.append(logistic(l,0.5,0.2))
    print(result1)
    print(result2)
    print(result3)
