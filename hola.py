"""m= input("Dime un numero del 0 al infinito galletas:")
f= input("Dime un numero del 0 al 2 personas:")
x= int(m)+int(f); 
if (x*int(m)<700000000):
    print("Eres gay")
else:
    print("Eres buena penyita")"""
def fibonachi(n):
    if n==0:
        return 0
    if n==1:
        return 1 
    return fibonachi(n-1) + fibonachi(n-2)
res=fibonachi(int(input()))
print(res)