'''
age = 18

if age >= 18:
	message = "opa, bem vindo(a)!!"
else:
	message = "ops, não pode entrar."

print(message)
'''
age = input("informe a sua idade: ")
message = "opa, bem vindo(a)!!" if int(age) > 18 else "ops, não pode entrar."
print(message)