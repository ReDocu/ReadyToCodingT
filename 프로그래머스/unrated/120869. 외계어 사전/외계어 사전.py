def solution(spell, dic):
    
    spell = set(spell)
    
    for item in dic:
        if spell.issubset(set(item)):
            return 1
    
    return 2