from itertools import permutations

def solution(expression):
    mid_exp = []
    number = ""
    
    for ex in expression:
        if ex.isdigit():
            number += ex
        else:
            mid_exp.append(int(number))
            mid_exp.append(ex)
            number = ""
    mid_exp.append(int(number))
    # print(mid_exp)
    
    answer = 0
    for op_rank in permutations([1,2,3], 3):
        op_dict = {}
        op_dict["+"] = op_rank[0]
        op_dict["-"] = op_rank[1]
        op_dict["*"] = op_rank[2]
        
        # print(op_dict)
        
        stack = []
        suff_exp = []
        for exp in mid_exp:
            if type(exp) == int:
                suff_exp.append(exp)
            else:
                while stack and op_dict[stack[-1]] >= op_dict[exp]:
                    suff_exp.append(stack.pop())
                stack.append(exp)
        
        while stack:
            suff_exp.append(stack.pop())
        
        # print(suff_exp)
        
        stack = []
        for exp in suff_exp:
            if type(exp) == int:
                stack.append(exp)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if exp == "+":
                    stack.append(num1 + num2)
                elif exp == "-":
                    stack.append(num1 - num2)
                elif exp == "*":
                    stack.append(num1 * num2)
        tmp_answer = abs(stack.pop())
        # print(tmp_answer)
        answer = max(answer, tmp_answer)

    return answer