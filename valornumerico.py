# Exercício 1: Escreva um código que leia no terminal um valor numérico representando um valor em reais, e tenha como saída este valor escrito por extenso.
# Ex: 1,00 => um real, 1000,54 => mil reais e cinquenta e quatro centavos
# O programa deve aceitar valores sempre com dois digitos após a virgula e com até 9 dígitos antes da vírgula

# Importo a biblioteca
from num2words import num2words

# Leio um valor do tipo float do teclado
# Tratamento número digitados com vírgula
valor_em_reais = 0
try:
    valor_em_reais = float(input('Digite um valor em reais: '));
except ValueError:
    print("Digite um valor válido")

if(valor_em_reais % 1 != 0):
    # Formato este valor com duas casas decimais
    valor_em_reais = "{:.2f}".format(valor_em_reais)
    # Divido este valor entre a parte inteira e a parte decimal
    divididopelopontodecimal = valor_em_reais.split('.')
    # Escrevo o número por extenso - no padrão pt-br
    parte_inteira = num2words(divididopelopontodecimal[0], lang='pt-br')
    parte_fracionaria = num2words(divididopelopontodecimal[1], lang='pt-br')
    print(parte_inteira + ' reais e ' + parte_fracionaria + ' centavos')
else:
    valor_em_reais = num2words(valor_em_reais, lang = 'pt-br')
    if(valor_em_reais == 'um'):
        print(valor_em_reais + ' real')
    else:
        print(valor_em_reais + ' reais')

