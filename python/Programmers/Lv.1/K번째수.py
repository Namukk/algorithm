def solution(array, commands):
    answer = []

    for num in range(len(commands)):
        i = commands[num][0] - 1
        j = commands[num][1] - 1
        k = commands[num][2] - 1

        newList = []
        for idx in range(i, j+1):
            newList.append(array[idx])

        newList.sort()

        answer.append(newList[k])

    return answer