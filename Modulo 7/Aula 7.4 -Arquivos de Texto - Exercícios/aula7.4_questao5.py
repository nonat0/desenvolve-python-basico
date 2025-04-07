livros = [
    ["Ação Humana", "Ludwig von Mises", 1949, 907],
    ["As Seis Lições", "Ludwig von Mises", 1959, 142],
    ["O Caminho da Servidão", "Friedrich Hayek", 1944, 274],
    ["A Mente do Mercado", "Michael Shermer", 2007, 400],
    ["A Riqueza das Nações", "Adam Smith", 1776, 1152],
    ["O Dilema da Inovação", "Clayton Christensen", 1997, 288],
    ["1984", "George Orwell", 1949, 328],
    ["O Andar do Bêbado", "Leonard Mlodinow", 2008, 272],
    ["A Máquina do Tempo", "H.G. Wells", 1895, 128],
    ["O Código da Vinci", "Dan Brown", 2003, 480]
]

with open("meus_livros.csv", "w", encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        f.write(f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n")