def _one_frame(text):                 
    lt = len(text[0])
    horz = '#' + '#'*lt + '#'         
    result = [horz]                   
    for line in text:
        result.append( '#'+line+'#' ) 
    result.append(horz)               
    return result

def frame(text, repeat, thickness):
    text = [" %s "%text]*repeat       
    for i in range(thickness):
        text = _one_frame(text)      
    return '\n'.join(text)            

print(frame('Hello World I am Paul', 1, 1 ))