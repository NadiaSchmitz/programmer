# The task is to write a very useful function that would ease the life of all the department programmers.
# For each integer from 0 to M the function would calculate how many times this number appears
# in the N-element array. Boss deems that the function should work as follows (the sample code for N = 3, M = 1):
# C
# if (arr[0]==0) ++count[0];
# if (arr[0]==1) ++count[1];
# if (arr[1]==0) ++count[0];
# if (arr[1]==1) ++count[1];
# if (arr[2]==0) ++count[0];
# if (arr[2]==1) ++count[1];

# Boss wants to estimate the time that Programmer will need to execute the task.
# We know that Programmer needs one second to write a line of the code (he’s fast, isn’t he?).
# Boss doesn’t know exactly bounds for M and N. Your task is to write program
# that would calculate a number of seconds that Programmer will write the code.
# Input
# The only line contains integers N (0 ≤ N ≤ 40000) and M (0 ≤ M ≤ 40000).
# Output
# Output an amount of seconds that Programmer needs to write the program.

check = 0
time = 0

while check == 0:
    n = int(input("Enter n 0-40 000: "))
    m = int(input("Enter m 0-40 000: "))
    if n < 0 or n > 40000 or m < 0 or m > 40000:
        print("Wrong number.")
    else:
        check = 1
        time = (m + 1) * n
print(time)
