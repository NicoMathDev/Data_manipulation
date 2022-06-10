# This function take one piece on string with based on a character. The function read each characters of string and starting from
# right or left. This function don't take one piece between two characteres on string, onlye the marker from final (right or left)

# text:        Is a string
# direction:   Is the direction from which the extration will be performed
# marker:      Highlighter caractere
# type:        If == 0 return string containing the marker, if == 1 return string not containing the marker
# irrelevant:  Number of times to ignore the marker charactere repeat

def txt_change(text:str, direction:str, marker:str, type:int, irrelevant:int):
    # Possible errors
    if text == '':
        return 'ERROR: no text'
    elif direction != 'right' and direction != 'left':
        return 'ERROR: direction not defined'
    elif marker == '':
        return 'ERROR: marker not defined'
    elif type != 0 and type != 1:
        return 'ERROR: type not defined'

    # Code
    for i in range(len(text)):
        if direction == 'right':
            j = (len(text) - (1+i))
            if text[j] == marker:
                if irrelevant == 0:
                    if type == 0:
                        return text[j:]
                        break
                    else:
                        return text[j+1:]
                        break
                else:
                    irrelevant -= 1
        elif direction == 'left':
            if text[i] == marker:
                if irrelevant == 0:
                    if type == 0:
                        return text[:i+1]
                        break
                    else:
                        return text[:i]
                        break
                else:
                    irrelevant -= 1


#Example:
tx = 'Welcome to my world!'
print(txt_change(tx, 'left',  ' ', 1, 1) 
  # answer: 'my world!'  
      
# Thanks :)
