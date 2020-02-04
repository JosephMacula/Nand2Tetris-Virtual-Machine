def writeArithmetic(command, label_counter1, label_counter2, input_array):
    if command[0] == 'add':
        x = ['// add', '@SP', 'AM=M-1', 'D=M', '@SP', 'AM=M-1', 'D=M+D', '@SP', 
                'A=M', 'M=D', '@SP', 'M=M+1']
    if command[0] == 'sub':
        x = ['// sub', '@SP', 'AM=M-1', 'D=M', '@SP', 'AM=M-1', 'D=M-D', '@SP',
                'A=M', 'M=D', '@SP', 'M=M+1']
    if command[0] == 'neg':
        x = ['// neg', '@SP', 'AM=M-1', 'D=-M', '@SP', 'A=M', 'M=D', '@SP',
                'M=M+1']
    if command[0] == 'eq':
        x = ['// eq', '@SP', 'AM=M-1', 'D=M', '@SP', 'AM=M-1', 'D=M-D', 
                '@EQ'+str(label_counter1), 'D;JEQ', '@SP', 'A=M', 'M=0', '@SP', 'M=M+1', 
                '@END'+str(label_counter2), '0;JMP', '(EQ'+str(label_counter1)+')',
                '@SP', 'A=M', 'M=-1', '@SP', 'M=M+1', '(END'+str(label_counter2)+')']
    if command[0] == 'gt':
        x = ['// gt', '@SP', 'AM=M-1', 'D=M', '@SP', 'AM=M-1', 'D=M-D', 
                '@GT'+str(label_counter1), 'D;JGT', '@SP', 'A=M', 'M=0', '@SP', 'M=M+1', 
                '@END'+str(label_counter2), '0;JMP', '(GT'+str(label_counter1)+')', 
                '@SP', 'A=M', 'M=-1', '@SP', 'M=M+1', '(END'+str(label_counter2)+')']
    if command[0] == 'lt':
        x = ['// lt', '@SP', 'AM=M-1', 'D=M', '@SP', 'AM=M-1', 'D=M-D', 
                '@LT'+str(label_counter1), 'D;JLT', '@SP', 'A=M', 'M=0', '@SP', 'M=M+1', 
                '@END'+str(label_counter2), '0;JMP', '(LT'+str(label_counter1)+')', 
                '@SP', 'A=M', 'M=-1', '@SP', 'M=M+1', '(END'+str(label_counter2)+')']
    if command[0] == 'and':
        x = ['// and', '@SP', 'AM=M-1', 'D=M', '@SP', 'AM=M-1', 'D=D&M', '@SP',
                'A=M', 'M=D', '@SP', 'M=M+1']
    if command[0] == 'or':
        x = ['// or', '@SP', 'AM=M-1', 'D=M', '@SP', 'AM=M-1', 'D=D|M', '@SP',
                'A=M', 'M=D', '@SP', 'M=M+1']
    if command[0] == 'not':
        x = ['// not', '@SP', 'AM=M-1', 'D=!M', '@SP', 'A=M', 'M=D', '@SP',
                'M=M+1']
    for i in x:
        input_array.append(i) 
#%%
def writePush(command, file_name_noext, input_array):
    if command[1] == 'argument':
        x = ['// push argument '+command[2], '@ARG', 'D=M', '@'+command[2], 
                'A=D+A', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    if command[1] == 'local':
        x = ['// push local '+command[2], '@LCL', 'D=M', '@'+command[2], 
                'A=D+A', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    if command[1] == 'constant':
        x = ['// push constant '+command[2], '@'+command[2], 'D=A', '@SP', 
                'A=M', 'M=D', '@SP', 'M=M+1']
    if command[1] == 'this':
        x = ['// push this '+command[2], '@THIS', 'D=M', '@'+command[2], 
                'A=D+A', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    if command[1] == 'that':
        x = ['// push that '+command[2], '@THAT', 'D=M', '@'+command[2], 
                'A=D+A', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    if command[1] == 'temp':
        x = ['// push temp '+command[2], '@R5', 'D=A', '@'+command[2], 
                'A=D+A', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    if command[1] == 'pointer':
        if command[2] == '0':
            x = ['// push pointer 0', '@THIS', 'D=M', '@SP', 'A=M', 'M=D', 
                    '@SP', 'M=M+1']
        else:
            x = ['// push pointer 1', '@THAT', 'D=M', '@SP', 'A=M', 'M=D',
                    '@SP', 'M=M+1']
    if command[1] == 'static':
        x = ['// push static '+command[2], '@'+file_name_noext+'.'+command[2],
                'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    for i in x:
        input_array.append(i)
#%%
def writePop(command, file_name_noext, input_array):
    if command[1] == 'argument':
        x = ['// pop argument '+command[2], '@ARG', 'D=M', '@'+command[2], 
                'D=D+A', '@R13', 'M=D', '@SP', 'AM=M-1', 'D=M', '@R13', 
                'A=M', 'M=D']
    if command[1] == 'local':
        x = ['// pop local '+command[2], '@LCL', 'D=M', '@'+command[2], 
                'D=D+A', '@R13', 'M=D', '@SP', 'AM=M-1', 'D=M', '@R13', 
                'A=M', 'M=D']
    if command[1] == 'this':
        x = ['// pop this '+command[2], '@THIS', 'D=M', '@'+command[2], 
                'D=D+A', '@R13', 'M=D', '@SP', 'AM=M-1', 'D=M', '@R13', 
                'A=M', 'M=D']
    if command[1] =='that':
        x = ['// pop that '+command[2], '@THAT', 'D=M', '@'+command[2], 
                'D=D+A', '@R13', 'M=D', '@SP', 'AM=M-1', 'D=M', '@R13', 
                'A=M', 'M=D']
    if command[1] == 'temp':
        x = ['// pop temp '+command[2], '@R5', 'D=A', '@'+command[2], 
                'D=D+A', '@R13', 'M=D', '@SP', 'AM=M-1', 'D=M', '@R13', 
                'A=M', 'M=D']
    if command[1] == 'pointer':
        if command[2] == '0':
            x = ['// pop pointer 0', '@SP', 'AM=M-1', 'D=M', '@THIS',
                    'M=D']
        else:
            x = ['// pop pointer 1', '@SP', 'AM=M-1', 'D=M', '@THAT',
                    'M=D']
    if command[1] == 'static':
        x = ['// pop static '+command[2], '@SP', 'M=M-1', 'A=M', 'D=M',
                '@'+file_name_noext+'.'+command[2], 'M=D']
    for i in x:
        input_array.append(i)
#%%
def writeLabel(command, input_array):
    x = ['// symbol command', '('+command[1]+')']
    for i in x:
        input_array.append(i)

def writeLabel_in_func(command, function_name, input_array):
    x = ['// symbol command', '('+function_name+'$'+command[1]+')']
    for i in x:
        input_array.append(i)
        
def write_goto(command, input_array):
    x = ['// goto '+command[1], '@'+command[1], '0;JMP']
    for i in x:
        input_array.append(i)

def write_goto_in_func(command, function_name, input_array):
    x = ['// goto '+command[1], '@'+function_name+'$'+command[1], '0;JMP']
    for i in x:
        input_array.append(i)
    
def write__if_goto(command, input_array):
    x =['//if-goto '+command[1], '@SP', 'AM=M-1', 'D=M', '@'+command[1], 'D;JNE']
    for i in x:
        input_array.append(i)

def write__if_goto_in_func(command, function_name, input_array):
    x =['//if-goto '+command[1], '@SP', 'AM=M-1', 'D=M', '@'+function_name+'$'+command[1],
        'D;JNE']
    for i in x:
        input_array.append(i)
#%%
def fileWriter(output_file, converted_commands_array):
    with open(output_file, "w") as writing_function:
        for i in converted_commands_array:
            writing_function.write('%s\n' % i)
            
#%%            
def writeFunction(command, input_array):
    if command[2] == '0':
        x = ['//function '+command[1]+' '+command[2], '('+command[1]+')']
    else:
        x = ['//function '+command[1]+' '+command[2], '('+command[1]+')',
         '@'+command[2], 'D=A', '(LOOP.'+command[1]+')', '@SP', 'A=M', 'M=0', '@SP', 
         'M=M+1', 'D=D-1', '@'+'LOOP.'+command[1], 'D;JGT',]
    for i in x:
        input_array.append(i)

def writeCall(command, function_number, input_array):
    x = ['//call '+command[1]+' '+command[2], '@RETURN_TO_'+command[1]+str(function_number), 'D=A',
         '@SP', 'A=M', 'M=D', '@SP', 'M=M+1', '@LCL', 'D=M', '@SP', 'A=M', 'M=D',
         '@SP', 'M=M+1', '@ARG', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1',
         '@THIS', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1', '@THAT', 'D=M', 
         '@SP', 'A=M', 'M=D', '@SP', 'M=M+1', '@'+command[2], 'D=A', '@5', 'D=D+A',
         '@SP', 'D=M-D', '@ARG', 'M=D', '@SP', 'D=M', '@LCL', 'M=D', 
         '@'+command[1], '0;JMP', '(RETURN_TO_'+command[1]+str(function_number)+')']
    for i in x:
        input_array.append(i)

def writeReturn(input_array):
    x = ['//return', '@LCL', 'D=M', '@R14', 'M=D', '@5', 'D=A', '@R14', 
         'A=M-D', 'D=M', '@R15', 'M=D', '@SP', 'A=M-1', 'D=M', '@ARG', 'A=M', 'M=D', 
         '@ARG', 'D=M+1', '@SP', 'M=D', '@R14', 'AM=M-1', 'D=M', '@THAT', 'M=D', '@R14',
         'AM=M-1', 'D=M', '@THIS', 'M=D', '@R14', 'AM=M-1', 'D=M', '@ARG', 'M=D', '@R14',
         'AM=M-1', 'D=M', '@LCL', 'M=D', '@R15', 'A=M', '0;JMP']
    for i in x:
        input_array.append(i)


def writeCall_Sys_init(command, input_array):
    x = ['//call '+command[1]+' '+command[2], '@RETURN_TO_'+command[1], '@5', 'D=A',
         '@SP', 'M=D+M',
         '@'+command[1], '0;JMP', '(RETURN_TO_'+command[1]+')']
    for i in x:
        input_array.append(i)  