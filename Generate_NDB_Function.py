import random

def Negative_Pattern_Generate(word, NDB):
    # Step 1: Create a random permutation π
    pi_word = list(word)
    random.shuffle(pi_word)
    
    # Step 2: Iterate over specified characters in π(word)
    SIV = set()
    for i, char in enumerate(pi_word):
        # Step 3: Replace the i-th character with '0'
        word_0 = pi_word.copy()
        word_0[i] = '0'
        
        # Step 4: Check if word_0 is subsumed by some string in π(NDB)
        subsumed = False
        for string in NDB:
            if all(c == char or c == '*' for c, char in zip(word_0, string)):
                subsumed = True
                break
        
        # Step 5: Update π(word) if word_0 is subsumed
        if subsumed:
            pi_word[i] = '0*0'
            SIV.add(i)
    
    # Step 7: Randomly choose t characters from SIV
    t = random.randint(0, len(SIV))
    R = random.sample(SIV, t)
    
    # Step 9: Create pattern Vk using π(word) and characters indicated by R
    Vk = pi_word.copy()
    for r in R:
        Vk[r] = '0*0'
    
    # Step 10: Return the inverse permutation of Vk
    Vk_inv = [''] * len(Vk)
    for i, val in enumerate(Vk):
        Vk_inv[pi_word.index(val)] = val
    
    return ''.join(Vk_inv)

# Example usage
word = 'Abdullah'
NDB = ['Abd*ll*', 'A*dull*', 'Abdullah']
result = Negative_Pattern_Generate(word, NDB)
print(result)