# 문제 설명
# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer

def solution(arr):
    answer = []
    for i in arr:
        # -1 뒤에 : 를 붙이면 list 형태로 반환이 됨 
        # -> 이렇게 하면 인덱스 오류가 안 남
        if answer[-1:] != [i]:
            answer.append(i)
    return answer