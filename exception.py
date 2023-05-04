x = int(input ("Enter number1 :"))
y = input ("Enter number2 :")
try:
    div = x / y
except Exception as e:
    print("exception :", e)
    print("exception type name :", type(e).__name__)
    div = None

print(div)