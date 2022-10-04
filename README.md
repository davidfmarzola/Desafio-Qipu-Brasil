# Desafio-Qipu-Brasil
Exercícios do Processo de Estágio em Desenvolvimento para a Qipu Brasil

## Exercício 1
Escreva um código que leia no terminal um valor numérico representando um valor em reais, e tenha como saída este valor escrito por extenso. <br>
Ex: 1,00 => um real, 1000,54 => mil reais e cinquenta e quatro centavos <br>
O programa deve aceitar valores sempre com dois digitos após a virgula e com até 9 dígitos antes da vírgula <br>

Para compilar o programa no `Terminal`
~~~C
pip install num2words
python valornumerico.py
~~~

## Exercício 2
### Extração de dados da web com a API playwright
Exercício 2: Para todo aviador, é vital saber antes de qualquer vôo as condições meteorológicas dos aeródromos de partida ou de chegada, 
assim como a existência de cartas disponíveis e horários de nascer e pôr do sol. No Brasil, estas informações são disponibilizadas pelo 
site https://aisweb.decea.mil.br/. Nesta página é possível encontrar links para cartas, horarios do sol e as informações de TAF e METAR, 
que são boletins meteorológicos codificados.

Escreva um código que leia no terminal o código ICAO qualquer de um aeródromo (SBMT = campo de marte, SBJD = aeroporto de jundiaí, etc...) 
e imprima na tela:

- As cartas disponíveis
- Os horários de nascer e pôr do sol de hoje
- A informação de TAF e METAR disponíveis


Vale ressaltar que estas informações devem ser obtidas em tempo real do site, através de SCRAPPING.


Para compilar o programa no `Terminal`
~~~C
pip install playwright
python informacoesaereas.py
~~~
