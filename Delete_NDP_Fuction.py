def Delete(x, NDB):
    # Step 1: Identify the subset Dx of NDB that matches x
    Dx = [y for y in NDB if all(y[i] == x[i] or x[i] == '*' for i in range(len(x)))]

    # Step 2: Remove Dx from NDB
    for y in Dx:
        NDB.remove(y)

    # Step 3: Reinsert strings represented by Dx except x
    for y in Dx:
        unspecified_positions = [i for i, char in enumerate(y) if char == '*']
        for i in unspecified_positions:
            y0 = list(y)
            y0[i] = '1' if x[i] == '0' else '0'  # complement of the bit specified at the i-th position of x
            NDB.append(''.join(y0))

# Example usage
x = '1**0*1'
NDB = ['10*10', '1*100', '10100']

Delete(x, NDB)
print(NDB)