def arithmetic_arranger(problems,B = False):
    problems = [x.split() for x in problems]
    arranged_problems = ''
    if len(problems)>5:
        return("Error: Too many problems.")
    for x in range(len(problems)):
        if problems[x][1] not in ['+','-']:
            return("Error: Operator must be '+' or '-'.")
        try:
            int(problems[x][0]),int(problems[x][2])
        except:
            return("Error: Numbers must only contain digits.")
        if len(problems[x][0])>4 or len(problems[x][2])>4:
            return("Error: Numbers cannot be more than four digits.")

    for x in range(len(problems)):
        a,b = len(problems[x][0]),len(problems[x][2])
        if a==b:
            problems[x][0],problems[x][2] = '  '+problems[x][0],problems[x][1]+' '+problems[x][2]
        elif a<b:
            d = b-a
            problems[x][0],problems[x][2] = '  '+' '*d+problems[x][0],problems[x][1]+' '+problems[x][2]
        else:
            d = a-b
            problems[x][0],problems[x][2] = '  '+problems[x][0],problems[x][1]+' '+' '*d+problems[x][2]

    for x in range(0,3,2):
        for y in range(len(problems)):
            arranged_problems = arranged_problems+problems[y][x]+'    '
        arranged_problems=arranged_problems+'\n'

    for x in range(len(problems)):
        arranged_problems=arranged_problems+'-'*len(problems[x][0])+'    '
    arranged_problems=arranged_problems+'\n'
    if B:
        for x in range(len(problems)):
            if(problems[x][1]=='+'):
                problems[x][0]=str(int(problems[x][0])+int(problems[x][2][1::]))
            else:
                problems[x][0]=str(int(problems[x][0])-int(problems[x][2][1::]))
            a,b=len(problems[x][0]),len(problems[x][2])
            if(a<b):
                d = b-a
                arranged_problems=arranged_problems+' '*d+problems[x][0]+'    '
            else:
                arranged_problems=arranged_problems+' '+problems[x][0]+'    '
        
    return(arranged_problems)


problems = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems,True))
