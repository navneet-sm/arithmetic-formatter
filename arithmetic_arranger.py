def arithmetic_arranger(problems, answers=False):

    list1, list2, arranged = [], [], ''
    calculations = False
    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
    else:
        for problem in problems:
            x = problem.split()
            list1.append(x)
            if x[1] != '+' and x[1] != '-':
                arranged_problems = "Error: Operator must be '+' or '-'."
                break
            elif (x[0].isnumeric() and x[2].isnumeric()) is False:
                arranged_problems = 'Error: Numbers must only contain digits.'
                break
            elif len(x[0]) > 4 or len(x[2]) > 4:
                arranged_problems = 'Error: Numbers cannot be more than four digits.'
                break
            else:
                calculations = True

    if calculations == True:
        for problem in list1:
            if problem[1] == '+':
                ans = int(problem[0]) + int(problem[2])
            if problem[1] == '-':
                ans = int(problem[0]) - int(problem[2])
            col_width = max(len(problem[0]), len(
                problem[2])) + 2  # +2 for operator
            problem[0] = problem[0].rjust(col_width)
            problem[1] = (problem[1] +
                          ((col_width - 1 - len(problem[2])) * ' ') +
                          problem[2]).rjust(col_width)
            problem[2] = '-' * col_width
            problem.append(str(ans).rjust(col_width))
            list2.append(problem)
            list1 = list(map(list, zip(*list2)))

        for x in list1:
            arranged += "    ".join(y for y in x) + '\n'
        arranged = arranged.rstrip('\n')
        if answers == True:
            arranged_problems = arranged
        if answers == False:
            arranged_problems = arranged[:(arranged.rfind('\n'))]

    return arranged_problems
