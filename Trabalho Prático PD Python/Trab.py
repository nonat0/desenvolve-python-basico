# Importando as bibliotecas necessárias para:
# Criar a interface gráfica do programa (tkinter, ttk, messagebox, filedialog)
# Manipular arquivos e pastas (os, shutil)
# Ler arquivos CSV (csv)
# Trabalhar com imagens (Pillow). 




import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import os
import csv
import shutil
from PIL import Image, ImageTk

# Definindo as três variáveis que armazenam os caminhos principais do sistema:

# >> USERS_FILE : pasta contendo o arquivo txt com os dados de cada usuário criado.
# Será acessada para editar e excluir usuários

# >> USERCODES_FILE : pasta que contem o código atrelado ao nível de acesso que cada usuário pode ter 
# ex: manager = 1; admin = 2; cliente = sem código.

# >> PRODUCTS_DIR : pasta onde os produtos são armazenados pelo seu código, que é uma pasta
#contendo a imagem do produto e um arquivo txt com nome e preço do produto 

USERS_FILE = "usuarios.txt"
USERCODES_FILE = "usercode.csv"
PRODUCTS_DIR = "products"

if not os.path.exists(PRODUCTS_DIR):
    os.makedirs(PRODUCTS_DIR)

#Adiciona uma nova linha ao arquivo usuarios.txt, com nome de usuário, senha e nível de permissão da conta recém criada.
def salvar_usuario(username, password, nivel):
    with open(USERS_FILE, "a") as f:
        f.write(f"{username};{password};{nivel}\n")

# Verifica se existe um usuário com o nome e a senha informados; se encontrar, retorna o nível de acesso para saber se o usuário
#é manager, admin, ou cliente.
def verificar_credenciais(username, password):
    if not os.path.exists(USERS_FILE):
        return None
    with open(USERS_FILE, "r") as f:
        for linha in f:
            u, p, nivel = linha.strip().split(";")
            if u == username and p == password:
                return nivel
    return None

# Verificando se o nome de usuário informado já está cadastrado no arquivo.
def usuario_existe(username):
    if not os.path.exists(USERS_FILE):
        return False
    with open(USERS_FILE, "r") as f:
        for linha in f:
            u, *_ = linha.strip().split(";")
            if u == username:
                return True
    return False

# Abrindo o arquivo usercode.csv e verificando se o código digitado corresponde a algum dos níveis de acesso; se sim, retorna o nível associado.
def obter_nivel_por_codigo(usercode):
    if not os.path.exists(USERCODES_FILE):
        return None
    with open(USERCODES_FILE, newline='', encoding='latin-1') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            if linha.get("usercode", "").strip() == usercode.strip():
                return linha.get("nível", "").strip()
    return None

class App:

    #Tela inicial do sistema com campos para inserir nome de usuário e senha, e botões para login, etc...
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x250")

        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack()
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()

        self.btn_login = tk.Button(root, text="Login", command=self.login)
        self.btn_login.pack(pady=5)

        self.btn_create = tk.Button(root, text="Create Account", command=self.tela_criar_conta)
        self.btn_create.pack()


    # Verifica as credenciais do usuário e seu nível de acesso
    # Conforme o nível retornado, abre a interface correspondente (cliente, admin ou manager)
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        nivel = verificar_credenciais(username, password)
        if nivel:
            if nivel == "client":
                self.tela_cliente()
            elif nivel == "admin":
                self.tela_admin()
            elif nivel == "manager":
                self.tela_manager()
            else:
                messagebox.showerror("Erro", "Nível de acesso desconhecido.")
        else:
            messagebox.showerror("Erro", "Credenciais inválidas")

    # Abre uma janela para cadastro de novos usuários, com opção de inserir um código
    # Os códigos estão atrelados aos níveis de acesso no arquivo usercode.csv
    # O usuário cadastrado com o código '1' que aponta para o nível 'manager' terá a conta criada atrelada ao nível 'manager'
    #que poderá acessar funcionalidades que os outros níveis de acesso (admin, cliente) não podem

    def tela_criar_conta(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Criar Conta")
        nova_janela.geometry("300x300")

        tk.Label(nova_janela, text="Username:").pack()
        entry_user = tk.Entry(nova_janela)
        entry_user.pack()

        tk.Label(nova_janela, text="Password:").pack()
        entry_pass = tk.Entry(nova_janela, show="*")
        entry_pass.pack()

        select_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(nova_janela, text="Inserir User Code", variable=select_var)
        checkbox.pack()

        tk.Label(nova_janela, text="User Code:").pack()
        entry_code = tk.Entry(nova_janela, state="disabled")
        entry_code.pack()

        def toggle_code():
            if select_var.get():
                entry_code.config(state="normal")
            else:
                entry_code.delete(0, tk.END)
                entry_code.config(state="disabled")

        select_var.trace_add("write", lambda *args: toggle_code())

        def confirmar():
            user = entry_user.get()
            pwd = entry_pass.get()
            code = entry_code.get() if select_var.get() else ""

            if not user or not pwd:
                messagebox.showerror("Erro", "Preencha todos os campos")
                return

            if usuario_existe(user):
                messagebox.showerror("Erro", "Nome de usuário já existe")
                return

            nivel = obter_nivel_por_codigo(code) if code else "client"
            salvar_usuario(user, pwd, nivel)
            messagebox.showinfo("Sucesso", f"Usuário criado com nível: {nivel}")
            nova_janela.destroy()

        tk.Button(nova_janela, text="Confirm", command=confirmar).pack(pady=10)

    # Abre a interface de nível 'client', onde é possível visualizar produtos e buscar pelo EAN.
    def tela_cliente(self): 
        self.root.withdraw()
        janela_cliente = tk.Toplevel()
        janela_cliente.title("Área do Cliente")
        janela_cliente.geometry("400x250")

        tk.Button(janela_cliente, text="Products", command=self.tela_produtos).pack(pady=10)

        tk.Label(janela_cliente, text="Search by EAN:").pack()
        search_entry = tk.Entry(janela_cliente)
        search_entry.pack()

        tk.Button(janela_cliente, text="Search", command=lambda: self.buscar_ean(search_entry.get())).pack(pady=5)

    # Exibe a interface para usuários com nível admin, permitindo visualizar, criar e editar produtos, e pesquisar produto 
    #pelo código
    def tela_admin(self):
        self.root.withdraw()
        janela_admin = tk.Toplevel()
        janela_admin.title("Área do Admin")
        janela_admin.geometry("400x300")

        tk.Label(janela_admin, text="Bem-vindo, Admin").pack(pady=5)

        tk.Button(janela_admin, text="Visualizar Produtos", command=self.tela_produtos).pack(pady=5)
        tk.Button(janela_admin, text="Criar Produto", command=self.criar_produto).pack(pady=5)
        tk.Button(janela_admin, text="Editar Produto", command=self.editar_produto).pack(pady=5)

        tk.Label(janela_admin, text="Search by EAN:").pack()
        search_entry = tk.Entry(janela_admin)
        search_entry.pack()

        tk.Button(janela_admin, text="Search", command=lambda: self.buscar_ean(search_entry.get())).pack(pady=5)

    # Carrega a tela para contas nível 'manager', com todas as permissões: excluir produtos, gerenciar usuários visualizar, criar, editar e pesquisar produtos.
    def tela_manager(self):
        self.root.withdraw()
        janela_manager = tk.Toplevel()
        janela_manager.title("Área do Manager")
        janela_manager.geometry("400x350")

        tk.Label(janela_manager, text="Bem-vindo, Manager").pack(pady=5)

        tk.Button(janela_manager, text="Visualizar Produtos", command=self.tela_produtos).pack(pady=5)
        tk.Button(janela_manager, text="Criar Produto", command=self.criar_produto).pack(pady=5)
        tk.Button(janela_manager, text="Editar Produto", command=self.editar_produto).pack(pady=5)
        tk.Button(janela_manager, text="Excluir Produto", command=self.excluir_produto).pack(pady=5)
        tk.Button(janela_manager, text="Gerenciar Usuários", command=self.gerenciar_usuarios).pack(pady=5)

        tk.Label(janela_manager, text="Search by EAN:").pack()
        search_entry = tk.Entry(janela_manager)
        search_entry.pack()

        tk.Button(janela_manager, text="Search", command=lambda: self.buscar_ean(search_entry.get())).pack(pady=5)

    # Abre uma janela que exibe todos os produtos cadastrados, com imagem, nome e preço, organizados por linha e coluna, tem também botão para voltar.
    def tela_produtos(self):
        janela = tk.Toplevel()
        janela.title("Produtos")
        janela.geometry("600x400")

        canvas = tk.Canvas(janela)
        frame_scroll = tk.Frame(canvas)
        scrollbar = ttk.Scrollbar(janela, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame_scroll, anchor="nw")

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        frame_scroll.bind("<Configure>", on_configure)

        linha = 0
        coluna = 0

        for pasta in os.listdir(PRODUCTS_DIR):
            pasta_prod = os.path.join(PRODUCTS_DIR, pasta)
            txt_path = os.path.join(pasta_prod, "product.txt")
            img_path = os.path.join(pasta_prod, "image.jpg")

            if os.path.isdir(pasta_prod) and os.path.exists(txt_path) and os.path.exists(img_path):
                with open(txt_path, "r", encoding="utf-8") as f:
                    linhas = f.readlines()
                    nome = linhas[0].strip()
                    preco = linhas[1].strip()

                try:
                    img_original = Image.open(img_path)
                    img_redimensionada = img_original.resize((100, 100)) 
                    img = ImageTk.PhotoImage(img_redimensionada)
                except:
                    img = None

                frame = tk.Frame(frame_scroll, bd=2, relief="groove", padx=5, pady=5)
                frame.grid(row=linha, column=coluna, padx=10, pady=10)

                if img:
                    img_label = tk.Label(frame, image=img)
                    img_label.image = img
                    img_label.pack()
                else:
                    tk.Label(frame, text="[Imagem inválida]").pack()

                tk.Label(frame, text=nome).pack()
                tk.Label(frame, text=f"R$ {preco}").pack()

                coluna += 1
                if coluna == 3:
                    coluna = 0
                    linha += 1

        btn_voltar = tk.Button(janela, text="Voltar", command=janela.destroy)
        btn_voltar.pack(pady=10)

    # Procura a pasta de um produto com base no código EAN digitado, lê as informações e exibe o produto com imagem, nome e preço, caso seja encontrado
    #se o produto não existir, exibe o erro.
    def buscar_ean(self, ean):
        pasta_produto = os.path.join(PRODUCTS_DIR, ean.strip())
        txt_path = os.path.join(pasta_produto, "product.txt")
        img_path = os.path.join(pasta_produto, "image.jpg")

        if not os.path.exists(pasta_produto) or not os.path.exists(txt_path) or not os.path.exists(img_path):
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        with open(txt_path, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            nome = linhas[0].strip()
            preco = linhas[1].strip()

        try:
            from PIL import Image, ImageTk
            img_original = Image.open(img_path)
            img_redimensionada = img_original.resize((150, 150))
            img = ImageTk.PhotoImage(img_redimensionada)
        except:
            img = None

        janela = tk.Toplevel()
        janela.title(f"Produto: {ean}")
        janela.geometry("300x300")

        frame = tk.Frame(janela, bd=2, relief="groove", padx=10, pady=10)
        frame.pack(pady=20)

        if img:
            img_label = tk.Label(frame, image=img)
            img_label.image = img
            img_label.pack()
        else:
            tk.Label(frame, text="[Imagem inválida]").pack()

        tk.Label(frame, text=f"Nome: {nome}").pack()
        tk.Label(frame, text=f"Preço: R$ {preco}").pack()

        tk.Button(janela, text="Fechar", command=janela.destroy).pack(pady=10)

    # Abre uma janela pro usuário inserir o código EAN, nome, preço e escolher uma imagem do produto.
    # Se os dados forem válidos, o produto é salvo criando dentro da pasta 'products' uma pasta cujo nome é o código EAN
    #inserido e dentro da pasta do produto, será salva a imagem e um txt com o nome e preço do produto criado.
    def criar_produto(self):
        janela_criar = tk.Toplevel()
        janela_criar.title("Criar Produto")
        janela_criar.geometry("400x400")

        tk.Label(janela_criar, text="Código EAN:").pack()
        entry_ean = tk.Entry(janela_criar)
        entry_ean.pack()

        tk.Label(janela_criar, text="Nome do Produto:").pack()
        entry_nome = tk.Entry(janela_criar)
        entry_nome.pack()

        tk.Label(janela_criar, text="Preço:").pack()
        entry_preco = tk.Entry(janela_criar)
        entry_preco.pack()

        img_path_var = tk.StringVar()

        def selecionar_imagem():
            path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])
            if path:
                img_path_var.set(path)
                lbl_img.config(text=os.path.basename(path))

        tk.Button(janela_criar, text="Selecionar Imagem", command=selecionar_imagem).pack(pady=5)
        lbl_img = tk.Label(janela_criar, text="Nenhuma imagem selecionada")
        lbl_img.pack()

        def confirmar():
            ean = entry_ean.get().strip()
            nome = entry_nome.get().strip()
            preco = entry_preco.get().strip()
            img_path = img_path_var.get().strip()

            if not ean or not nome or not preco or not img_path:
                messagebox.showerror("Erro", "Preencha todos os campos e selecione uma imagem")
                return

            try:
                float(preco)
            except ValueError:
                messagebox.showerror("Erro", "Preço inválido")
                return

            pasta_produto = os.path.join(PRODUCTS_DIR, ean)
            if not os.path.exists(pasta_produto):
                os.makedirs(pasta_produto)
            else:
                messagebox.showerror("Erro", "Produto com este código EAN já existe")
                return

            with open(os.path.join(pasta_produto, "product.txt"), "w", encoding="utf-8") as f:
                f.write(nome + "\n")
                f.write(preco)

            shutil.copy(img_path, os.path.join(pasta_produto, "image.jpg"))

            messagebox.showinfo("Sucesso", "Produto criado com sucesso")
            janela_criar.destroy()

        tk.Button(janela_criar, text="Confirmar", command=confirmar).pack(pady=10)

    # Mostra todos os produtos numa aba, com botão 'Editar' abaixo de cada um. Quando clickar em 'Editar', abre a janela de edição
    def editar_produto(self):
        janela = tk.Toplevel()
        janela.title("Selecionar Produto para Editar")
        janela.geometry("600x400")

        from PIL import Image, ImageTk

        container = tk.Frame(janela)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def abrir_editor(ean):
            janela.destroy()
            self.janela_editar_detalhes(ean)

        linha = 0
        coluna = 0

        for pasta in os.listdir(PRODUCTS_DIR):
            pasta_prod = os.path.join(PRODUCTS_DIR, pasta)
            txt_path = os.path.join(pasta_prod, "product.txt")
            img_path = os.path.join(pasta_prod, "image.jpg")

            if os.path.isdir(pasta_prod) and os.path.exists(txt_path) and os.path.exists(img_path):
                with open(txt_path, "r", encoding="utf-8") as f:
                    nome = f.readline().strip()
                    preco = f.readline().strip()

                try:
                    img = Image.open(img_path).resize((100, 100))
                    img = ImageTk.PhotoImage(img)
                except:
                    img = None

                frame = tk.Frame(scrollable_frame, bd=2, relief="groove", padx=5, pady=5)
                frame.grid(row=linha, column=coluna, padx=10, pady=10)

                if img:
                    lbl_img = tk.Label(frame, image=img)
                    lbl_img.image = img
                    lbl_img.pack()

                tk.Label(frame, text=nome).pack()
                tk.Label(frame, text=f"R$ {preco}").pack()

                btn = tk.Button(frame, text="Editar", command=lambda ean=pasta: abrir_editor(ean))
                btn.pack(pady=5)

                coluna += 1
                if coluna == 3:
                    coluna = 0
                    linha += 1

    #Essa é a janela de edição mencionada no comentário anterior, permite editar os dados preenchidos para nome e preço, carrega a imagem atual,
    #e permite selecionar uma nova imagem e salvar as alterações para o produto escolhido para edição.
    def janela_editar_detalhes(self, ean):
        from PIL import Image, ImageTk

        pasta_produto = os.path.join(PRODUCTS_DIR, ean)
        txt_path = os.path.join(pasta_produto, "product.txt")
        img_path = os.path.join(pasta_produto, "image.jpg")

        if not os.path.exists(txt_path) or not os.path.exists(img_path):
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        with open(txt_path, "r", encoding="utf-8") as f:
            nome = f.readline().strip()
            preco = f.readline().strip()

        janela = tk.Toplevel()
        janela.title(f"Editar Produto: {ean}")
        janela.geometry("350x400")

        tk.Label(janela, text="Nome do Produto:").pack()
        entry_nome = tk.Entry(janela)
        entry_nome.insert(0, nome)
        entry_nome.pack()

        tk.Label(janela, text="Preço:").pack()
        entry_preco = tk.Entry(janela)
        entry_preco.insert(0, preco)
        entry_preco.pack()

        img_preview = None
        img_label = tk.Label(janela)
        img_label.pack(pady=5)

        def carregar_imagem(path):
            nonlocal img_preview
            try:
                img = Image.open(path)
                img = img.resize((150, 150))
                img_preview = ImageTk.PhotoImage(img)
                img_label.config(image=img_preview)
                img_label.image = img_preview
            except:
                img_label.config(text="Erro ao carregar imagem")

        carregar_imagem(img_path)

        img_path_var = tk.StringVar(value=img_path)

        def selecionar_imagem():
            path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])
            if path:
                img_path_var.set(path)
                carregar_imagem(path)

        tk.Button(janela, text="Selecionar Nova Imagem", command=selecionar_imagem).pack(pady=5)

        def salvar_alteracoes():
            novo_nome = entry_nome.get().strip()
            novo_preco = entry_preco.get().strip()
            nova_img = img_path_var.get().strip()

            if not novo_nome or not novo_preco:
                messagebox.showerror("Erro", "Preencha todos os campos")
                return

            try:
                float(novo_preco)
            except ValueError:
                messagebox.showerror("Erro", "Preço inválido")
                return

            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(novo_nome + "\n")
                f.write(novo_preco)

            if nova_img != img_path:
                shutil.copy(nova_img, img_path)

            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso")
            janela.destroy()

        tk.Button(janela, text="Salvar Alterações", command=salvar_alteracoes).pack(pady=10)
        tk.Button(janela, text="Cancelar", command=janela.destroy).pack()

    # Exibe os produtos presentes na pasta products, com botões 'Excluir'
    # ao clicar, o sistema pede confirmação e deleta a pasta do código do produto de dentro da pasta 'products'
    def excluir_produto(self):
        janela = tk.Toplevel()
        janela.title("Excluir Produto")
        janela.geometry("600x400")

        from PIL import Image, ImageTk

        container = tk.Frame(janela)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        linha = 0
        coluna = 0

        for pasta in os.listdir(PRODUCTS_DIR):
            pasta_prod = os.path.join(PRODUCTS_DIR, pasta)
            txt_path = os.path.join(pasta_prod, "product.txt")
            img_path = os.path.join(pasta_prod, "image.jpg")

            if os.path.isdir(pasta_prod) and os.path.exists(txt_path) and os.path.exists(img_path):
                with open(txt_path, "r", encoding="utf-8") as f:
                    nome = f.readline().strip()
                    preco = f.readline().strip()

                try:
                    img = Image.open(img_path).resize((100, 100))
                    img = ImageTk.PhotoImage(img)
                except:
                    img = None

                frame = tk.Frame(scrollable_frame, bd=2, relief="groove", padx=5, pady=5)
                frame.grid(row=linha, column=coluna, padx=10, pady=10)

                if img:
                    lbl_img = tk.Label(frame, image=img)
                    lbl_img.image = img
                    lbl_img.pack()

                tk.Label(frame, text=nome).pack()
                tk.Label(frame, text=f"R$ {preco}").pack()

                def confirmar_exclusao(ean=pasta):
                    if messagebox.askyesno("Confirmar", f"Deseja realmente excluir o produto {ean}?"):
                        shutil.rmtree(os.path.join(PRODUCTS_DIR, ean))
                        messagebox.showinfo("Sucesso", f"Produto {ean} excluído com sucesso.")
                        janela.destroy()
                        self.excluir_produto()

                tk.Button(frame, text="Excluir", command=confirmar_exclusao).pack(pady=5)

                coluna += 1
                if coluna == 3:
                    coluna = 0
                    linha += 1

    # exibe uma janela com todos os usuários cadastrados, permitindo que um usuário seja selecionado e tenha a senha alterada ou seja excluído,
    #  exceto se for uma conta admin, que é protegido contra exclusão.
    def gerenciar_usuarios(self):
        janela = tk.Toplevel()
        janela.title("Gerenciar Usuários")
        janela.geometry("500x400")

        usuarios = []
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as f:
                usuarios = [linha.strip().split(";") for linha in f]

        tree = ttk.Treeview(janela, columns=("Username", "Nível"), show="headings")
        tree.heading("Username", text="Username")
        tree.heading("Nível", text="Nível")

        for user, _, nivel in usuarios:
            tree.insert("", tk.END, values=(user, nivel))

        tree.pack(pady=10, fill="both", expand=True)

        def excluir_usuario():
            selected = tree.selection()
            if not selected:
                messagebox.showerror("Erro", "Selecione um usuário para excluir")
                return
            username = tree.item(selected[0])["values"][0]
            if username == "admin":
                messagebox.showerror("Erro", "Não é possível excluir o usuário admin")
                return
            usuarios_novos = [u for u in usuarios if u[0] != username]
            with open(USERS_FILE, "w") as f:
                for u in usuarios_novos:
                    f.write(";".join(u) + "\n")
            tree.delete(selected[0])
            messagebox.showinfo("Sucesso", f"Usuário '{username}' excluído")

        def alterar_senha():
            selected = tree.selection()
            if not selected:
                messagebox.showerror("Erro", "Selecione um usuário para alterar senha")
                return
            username = tree.item(selected[0])["values"][0]

            def salvar_nova_senha():
                nova = nova_senha_entry.get()
                if not nova:
                    messagebox.showerror("Erro", "Senha não pode ser vazia")
                    return
                for u in usuarios:
                    if u[0] == username:
                        u[1] = nova
                with open(USERS_FILE, "w") as f:
                    for u in usuarios:
                        f.write(";".join(u) + "\n")
                messagebox.showinfo("Sucesso", "Senha alterada com sucesso")
                nova_janela.destroy()

            nova_janela = tk.Toplevel(janela)
            nova_janela.title("Alterar Senha")
            tk.Label(nova_janela, text=f"Nova senha para {username}:").pack()
            nova_senha_entry = tk.Entry(nova_janela, show="*")
            nova_senha_entry.pack()
            tk.Button(nova_janela, text="Salvar", command=salvar_nova_senha).pack(pady=5)

        tk.Button(janela, text="Excluir Usuário", command=excluir_usuario).pack(pady=5)
        tk.Button(janela, text="Alterar Senha", command=alterar_senha).pack(pady=5)

root = tk.Tk()
app = App(root)
root.mainloop()