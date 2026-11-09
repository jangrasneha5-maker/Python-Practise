# factorial ka recurssion
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("enter the number:"))
print(f"the factorial of the number is :{factorial(n)}")

# lamda function
# anonymous function jisme def nhi likhna padta and one line mei hi Overrrrrrrr
# example mam ne hta dia (*cry*cry*cry *)