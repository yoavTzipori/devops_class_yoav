# Define the patterns for each letter 'S', 'A', 'M'
letter_Y = [
    '*   *',
    ' * * ',
    '  *  ',
    '  *  ',
    '  *  '
]

letter_O = [
    ' *** ',
    '*   *',
    '*   *',
    '*   *',
    ' *** '
]

letter_A = [
    '  *  ',
    ' * * ',
    '*   *',
    '*****',
    '*   *'
]

letter_V = [
    '*   *',
    '*   *',
    ' * * ',
    '  *  ',
    '  *  '
]

# Print each letter pattern vertically with space between letters
for i in range(len(letter_Y)):  # Iterate over the length of any letter pattern (assuming they have the same length)
    print(letter_Y[i] + ' ' + letter_O[i] + ' ' + letter_A[i] + ' ' + letter_V[i])  # Add space between letters
