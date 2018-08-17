'''
runnerup.py

Hacker Rank Challenge: Runner Up from Basic Data Types in Python Track
'''
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max = arr[0]
    runnerUp = -1
    index = 1
    while index < len(arr):
        if (arr[index] != runnerUp and arr[index] != max):
            if arr[index] > max:
                runnerUp = max
                max = arr[index]
            elif arr[index] > runnerUp:
                runnerUp= arr[index]
        index += 1
    print(runnerUp)
