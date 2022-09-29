# Exercício 2: Para todo aviador, é vital saber antes de qualquer vôo as condições meteorológicas dos aeródromos de partida ou de chegada, 
# assim como a existência de cartas disponíveis e horários de nascer e pôr do sol. No Brasil, estas informações são disponibilizadas pelo 
# site https://aisweb.decea.mil.br/. Nesta página é possível encontrar links para cartas, horarios do sol e as informações de TAF e METAR, 
# que são boletins meteorológicos codificados.

# Escreva um código que leia no terminal o código ICAO qualquer de um aeródromo (SBMT = campo de marte, SBJD = aeroporto de jundiaí, etc...) 
# e imprima na tela:

# - As cartas disponíveis
# - Os horários de nascer e pôr do sol de hoje
# - A informação de TAF e METAR disponíveis


# Vale ressaltar que estas informações devem ser obtidas em tempo real do site, através de SCRAPPING.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    codigoICAO = input('Entre com o código ICAO: ')
    browser = p.chromium.launch() # posso ver o chrome em tempo real
    page = browser.new_page()
    page.goto("https://aisweb.decea.mil.br/?i=aerodromos&codigo="+codigoICAO)

    nascerdosol = page.locator('xpath=/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/h4/sunrise').text_content()
    print("Nascer do sol: ", nascerdosol)
    pordosol = page.locator('xpath=/html/body/div/div/div/div[2]/div[2]/div[1]/div[2]/h4/sunset').text_content()
    print("Pôr do sol: ", pordosol)
    
    print(page.title())

