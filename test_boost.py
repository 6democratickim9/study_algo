def solution(params):
    regiA = []
    regiB = []
    stack = []*8
    answer = []
    command = {"POPA": "EMPTY", "POPB": "EMPTY", "ADD": "ERROR", "SUB": "ERROR",
               "PUSH0": 0, "PUSH1": 1, "PUSH2": 2, "PUSH3": 3, "SWAP": "ERROR", "PRINT": "EMPTY"}
    print()
    for idx in range(len(params)):
        if params[idx] == "POPA":
            if len(stack) == 0:
                answer.append(command["POPA"])
            else:
                regiA.append(stack.pop())
                
        elif params[idx] == "POPB":
            if len(stack) == 0:
                answer.append(command["POPB"])
            else:
                regiB.append(stack.pop())

        elif params[idx] == "ADD":
            if len(regiA) == 0 or len(regiB) == 0:
                answer.append(command["ADD"])
            elif len(stack) > 8:
                answer.append("OVERFLOW")
            else:
                num = regiA.pop()+regiB.pop()
                stack.append(num)

        elif params[idx] == "SUB":
            if len(regiA) == 0 or len(regiB) == 0:
                answer.append(command["SUB"])
            elif len(stack) > 8:
                answer.append("OVERFLOW")
            else:
                num = regiA.pop()-regiB.pop()
                stack.append(num)

        elif params[idx] == "PUSH0":
            if len(stack) < 8:
                stack.append(command["PUSH0"])
            else:
                answer.append("OVERFLOW")
                
        elif params[idx] == "PUSH1":
            if len(stack) < 8:
                stack.append(command["PUSH1"])
            else:
                answer.append("OVERFLOW")

        elif params[idx] == "PUSH2":
            if len(stack) < 8:
                stack.append(command["PUSH2"])
            else:
                answer.append("OVERFLOW")

        elif params[idx] == "PUSH3":
            if len(stack) < 8:
                stack.append(command["PUSH3"])
            else:
                answer.append("OVERFLOW")

        elif params[idx] == "SWAP":
            if len(regiA) == 0 or len(regiB) == 0:
                answer.append(str(command["SWAP"]))
            else:
                tmp = regiA.pop()
                tmp1 = regiB.pop()
                regiB.append(tmp)
                regiA.append(tmp1)

        elif params[idx] == "PRINT":
            if len(stack) == 0:
                answer.append(str(command["PRINT"]))
            else:
                answer.append(str(stack.pop()))
        elif command.get(params[idx]) == None:
            answer.append("UNKNOWN")
    return answer


print(solution(["PRINT", "PUSH0", "PRINT", "POPA"]))
print(solution(["PUSH3", "PUSH2", "PUSH1", "POPA", "POPB",
      "SWAP", "SUB", "POPA", "POPB", "ADD", "PRINT"]))
print(solution(["PUSH1", "PUSH1", "PUSH2", "POPA",
      "POPB", "SWAP", "ADD", "PRINT", "PRINT"]))
print(solution(["ADD", "PUSH3", "PUSH1", "PUSH0", "PUSH2",
      "PUSH1", "PUSH3", "PUSH2", "PUSH0", "PUSH3", "PUSH4"]))
