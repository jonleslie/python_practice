Value = int(input("Enter an integer: "))

n1 = int("%s" %Value)
n2 = int("%s%s" %(Value, Value))
n3 = int("%s%s%s" %(Value, Value, Value))

print("Sum is: %d" %(n1 + n2 + n3))