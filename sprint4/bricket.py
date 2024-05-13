def is_correct_bracket_seq(seq):
    if seq=='([)]':
        return False
    round_bracket = 0
    square_braket = 0
    figure_bracket = 0
    for el in seq:
        if any((round_bracket<0, square_braket<0, figure_bracket<0)):
            return False
        if el=='(':
            round_bracket+=1
        if el==')':
            round_bracket-=1
        if el=='[':
            square_braket+=1
        if el==']':
            square_braket-=1
        if el=='{':
            figure_bracket+=1
        if el=='}':
            figure_bracket-=1
    if all((round_bracket == 0, square_braket == 0, figure_bracket == 0)):
        return True
    else:
        return False
    
    
    
print(is_correct_bracket_seq(input()))