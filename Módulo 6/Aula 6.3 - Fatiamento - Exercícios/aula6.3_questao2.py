urls = []

print("Digite URL's que comecem com www. e terminem com .com Digite 'ok' para finalizar")

while True:
    url = input("Digite uma url válida: ")

    if url.lower() == "ok":
        break
    
    if len(url) > 9 and url[:4] == "www." and url [-4:] == ".com":
        urls.append(url)
    else:
        print("Url inválida, digite a url no modelo 'www.url.com")

dominios = [url[4:-4] for url in urls]

print("\nLista de domínios extraídos: ", dominios)