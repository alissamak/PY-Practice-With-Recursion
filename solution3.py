# Write code for algorithm 3 below
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n=2
for i in range(n):
    print(fibonacci(i))

#print(fibonacci(2))

# def tri(n):
#     if n < 2:
#           return 0
#     if == 2:
#            return 1
#--clever way
#     if n <= 2:
#         return max((n-1,0))
#------------------------------
#     else:
#         return tri(n-1) + tri(n-2) + tri(n-3)
#print(tri(2))