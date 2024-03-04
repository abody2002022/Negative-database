import random

def Negative_Pattern_Generate(word, NDB):
    # Implementation of Negative Pattern Generate algorithm (as provided in the previous response)
    # This function generates a string that matches the input word and nothing else outside of NDB
    # You can reuse the Negative_Pattern_Generate function from the previous response here

def Insert(x, NDB, l, n):
    # Step 1: Randomly choose 1 ≤ j ≤ l
    j = random.randint(1, l)
    
    for k in range(1, j+1):
        # Step 3: Randomly select at most n distinct unspecified bit positions
        unspecified_positions = random.sample([i for i, char in enumerate(x) if char == '*'], min(n, x.count('*')))
        
        for i in range(2 ** len(unspecified_positions)):
            # Step 4: Generate all possible bit assignments Bp of the selected positions
            bit_assignment = format(i, '0' + str(len(unspecified_positions)) + 'b')
            x0 = list(x)
            for idx, pos in enumerate(unspecified_positions):
                x0[pos] = bit_assignment[idx]
            
            # Step 6: Generate y using Negative Pattern Generate with x0 and NDB
            y = Negative_Pattern_Generate(''.join(x0), NDB)
            
            # Step 7: Add y to NDB
            NDB.append(y)

# Example usage
x = '1**0*1'
NDB = ['10*10', '1*100', '10100']
l = 5
n = 2

Insert(x, NDB, l, n)
print(NDB)