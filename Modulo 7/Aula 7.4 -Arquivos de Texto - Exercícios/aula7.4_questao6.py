import csv
import os

nome_arquivo = 'spotify-2023.csv'

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)

musicas_por_ano = {}

with open(caminho_arquivo, encoding='latin-1') as f:
    leitor = csv.DictReader(f)

    for linha in leitor:
        try:
            ano = int(linha['released_year'])
            if 2012 <= ano <= 2022:
                streams = int(linha['streams'])

                if ano not in musicas_por_ano or streams > musicas_por_ano[ano]['streams']:
                    musicas_por_ano[ano] = {
                        'track_name': linha['track_name'],
                        'artist': linha["artist(s)_name"],
                        'released_year': ano,
                        'streams': streams
                    }
        except (ValueError, KeyError):
            continue

resultado_final = []
for ano in sorted(musicas_por_ano.keys()):
    m = musicas_por_ano[ano]
    resultado_final.append([m['track_name'], m['artist'], m['released_year'], m['streams']])

print("\nMúsicas mais tocadas por ano (2012–2022):\n")
for item in resultado_final:
    print(item)