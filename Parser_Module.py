def open_and_clean_text(file_name):
    y = open(file_name)
    text = y.readlines()
    separator = '//'
    for i in range(0, len(text)):
        text[i] = text[i].rstrip('\n')
        text[i] = text[i].split(separator, 1)[0]
        i = 0
    j = len(text)
    while i < j:
        if text[i] == '' or text[i][0] == '/':
            del text[i]
            j -= 1
        else:
            i += 1
    return text

def commandType(current_line):
    if current_line[0] == 'push':
        return 'C_PUSH'
    if current_line[0] == 'pop':
        return 'C_POP'
    if current_line[0] == 'label':
        return 'C_LABEL'
    if current_line[0] == 'goto':
        return 'C_GOTO'
    if current_line[0] == 'if-goto':
        return 'C_IF'
    if current_line[0] == 'function':
        return 'C_FUNCTION'
    if current_line[0] == 'call':
        return 'C_CALL'
    if current_line[0] == 'return':
        return 'C_RETURN'
    else:
        return 'C_ARITHMETIC'