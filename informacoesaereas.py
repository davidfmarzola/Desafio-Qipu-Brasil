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
    codigoICAO = input('Entre com o código ICAO: ') # código identificador de localidade do aeródromo
    browser = p.chromium.launch() # instância do navegador
    page = browser.new_page() # create a new page in a browse
    page.goto("https://aisweb.decea.mil.br/?i=aerodromos&codigo="+codigoICAO) # procuro o identificador no link do site

    # extraio o texto dos xpath (identifica as tags)
    nascerdosol = page.locator('xpath=/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/h4/sunrise').text_content() 
    print("Nascer do sol: ", nascerdosol)
    pordosol = page.locator('xpath=/html/body/div/div/div/div[2]/div[2]/div[1]/div[2]/h4/sunset').text_content()
    print("Pôr do sol: ", pordosol)
    
    metar = page.locator('xpath=/html/body/div/div/div/div[2]/div[2]/p[2]').text_content()
    print("Metar: ", metar)
    taf = page.locator('xpath=/html/body/div/div/div/div[2]/div[2]/p[3]').text_content()
    print("Taf: ", taf)

    # classe das Ul's desejadas: .list-icons-style-2
    # ul > li > a
    # Acho as tags desejadas por meio da classe e dos filhos respectivos
    cartas = page.locator('.list-icons-style-2 > li > a')
    # retorna uma lista de todas as cartas disponíveis
    listadecartas = cartas.all_text_contents()
    print("Cartas disponíveis: ", listadecartas)

