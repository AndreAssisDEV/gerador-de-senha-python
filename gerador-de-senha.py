import random
import string

alfabeto_menos = string.ascii_lowercase
alfabeto_mais = string.ascii_uppercase
numeros = '123456789'
simbolos = "[]{}()*;/,_-"
combinar = alfabeto_mais
combinar = combinar + alfabeto_menos
combinar = combinar + numeros
combinar = combinar + simbolos

#comprimento vc pode por a quantidade de caracteres desejado :)
comprimento = 20
senha = "".join(random.sample(combinar, comprimento))

print(senha)

