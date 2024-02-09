import random

# array com as palavras 
# selecionar a palavra aleatoriamente
# informar o usuario para advinhar animal 
# nao pode aceitar numeros
# receber as letras atraves do usuario atraves do input 
# realizar a comparação das letras com a palavra selecionada 

animais = ['macaco','elefante','girafa','leão'] 
palavra_selecionada = [animais]

teste = random.choice(animais)

print('Adivinhe o animal: ' + ', '.join(animais)  )

palavra_digitada = input('digite o nome do animal:')

for palavra_digitada in teste:
    

    if teste == palavra_digitada:
        
        print('otimo vc acertou miserave')
    #else:
print ("tente novamente!!!")

#for i in range(0,10):
#    print(i)
#for i in animais:
#    print(i)

exit()

print("welcome to hangmam")

leters = input("digite uma letra:")
 
if leters == 's':
    print("incorrect")

 
 