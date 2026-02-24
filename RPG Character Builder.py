full_dot = '●'
empty_dot = '○'

def create_character(name, s, i, c):
    if not isinstance(name, str):
        return "The character name should be a string"
    
    if len(name) == 0:
        return "The character should have a name"
    
    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    if not all(isinstance(x, int) for x in (s, i, c)): 
        return "All stats should be integers"

    if min(s, i, c) < 1:
        return "All stats should be no less than 1" 
        
    if max(s, i, c) > 4:
        return "All stats should be no more than 4" 
        
    if s + i + c != 7:
        return "The character should start with 7 points"

    s = "STR " + full_dot * s + empty_dot * (10 - s)
    i = "INT " + full_dot * i + empty_dot * (10 - i)
    c = "CHA " + full_dot * c + empty_dot * (10 - c)

    return f"{name}\n{s}\n{i}\n{c}"

