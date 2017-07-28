data = open('count_big.txt').read()
line = [s.strip() for s in data.splitlines()]
words = {}
N = 0
for i in line :
    value = i.split("\t")
    words[value[0]] = int(value[1])
    N += int(value[1])
    N = float(N)


def probability(candidate) :
    #Here we generate the probability of the candidates
    return (words[candidate]/N)


def generate_edit(word):
    #Here we generate random words with edit distance 1
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def check_generates(prob_candidates): 
    #Here we check if the candidates are in our corpus
    return set(w for w in prob_candidates if w in words)


def return_candidates(word): 
    #Here we return our candidates for the spelling correction
    return (check_generates(generate_edit(word)))

def spelling_correct(misspelled):
    #Here we generate the correct spelling
    max_prob = 0
    correct = ''
    print(return_candidates(misspelled))
    for candidate in return_candidates(misspelled) :
        prob = probability(candidate)
        if prob > max_prob :
            correct = candidate
            max_prob = prob
    print(correct)


misspelled = input('Give incorrect word:')
spelling_correct(str(misspelled))
