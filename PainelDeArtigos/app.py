from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt, QTimer
import mysql.connector
from mysql.connector import Error
import sys

# ==========================================
# 1. LIGAÇÃO À BASE DE DADOS
# ==========================================
try:
    conn = mysql.connector.connect(
        host='localhost',
        database='loja_informatica',
        user='root',
        password=''
    )
    print("Ligado ao inventário da Loja de Informática.")
except Error as erro:
    print(f"Erro ao ligar ao MySQL: {erro}")
    sys.exit()

# ==========================================
# 2. FUNÇÕES DO SISTEMA (PRODUTOS E STOCK)
# ==========================================
def carregar_dados_tabela():
    """ Procura os dados no MySQL e atualiza a QTableWidget """
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    linhas = cursor.fetchall()
    
    janela.tabela_produtos.setRowCount(len(linhas))
    janela.tabela_produtos.setHorizontalHeaderLabels(["ID", "Nome", "Categoria", "Preço", "Stock"])
    
    for num_linha, linha in enumerate(linhas):
        janela.tabela_produtos.setItem(num_linha, 0, QTableWidgetItem(str(linha['id_produto'])))
        janela.tabela_produtos.setItem(num_linha, 1, QTableWidgetItem(linha['nome']))
        janela.tabela_produtos.setItem(num_linha, 2, QTableWidgetItem(linha['categoria']))
        janela.tabela_produtos.setItem(num_linha, 3, QTableWidgetItem(f"{linha['preco']} €"))
        janela.tabela_produtos.setItem(num_linha, 4, QTableWidgetItem(str(linha['quantidade'])))
        
    cursor.close()

def adicionar_produto():
    """ Adiciona o produto do formulário na base de dados """
    nome = janela.txt_nome.text().strip()
    categoria = janela.cb_categoria.currentText()
    preco = janela.txt_preco.text().replace(',', '.')
    qtd = janela.txt_qtd.value()
    
    if not nome or not preco:
        print("Erro: Preencha todos os campos obrigatórios!")
        return

    try:
        cursor = conn.cursor()
        sql = "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, categoria, float(preco), int(qtd)))
        conn.commit()
        cursor.close()
        
        # Limpar campos e atualizar
        janela.txt_nome.setText("")
        janela.txt_preco.setText("")
        janela.txt_qtd.setValue(0)
        carregar_dados_tabela()
        print(f"'{nome}' adicionado com sucesso!")
        
    except (Error, ValueError) as err:
        print(f"Erro ao salvar: {err}")

def alterar_stock(quantidade_mudanca):
    """ Altera o stock do produto selecionado """
    linha_selecionada = janela.tabela_produtos.currentRow()
    
    if linha_selecionada == -1:
        print("Aviso: Selecione um produto na tabela primeiro!")
        return
        
    id_produto = janela.tabela_produtos.item(linha_selecionada, 0).text()
    
    try:
        cursor = conn.cursor()
        sql = """UPDATE produtos 
                 SET quantidade = GREATEST(0, quantidade + %s) 
                 WHERE id_produto = %s"""
        cursor.execute(sql, (quantidade_mudanca, id_produto))
        conn.commit()
        cursor.close()
        
        carregar_dados_tabela()
    except Error as err:
        print(f"Erro ao atualizar stock: {err}")

def fechar_programa():
    if conn.is_connected():
        conn.close()
    app.quit()

# ==========================================
# INICIALIZAÇÃO DA APLICAÇÃO E TIMER
# ==========================================
app = QtWidgets.QApplication(sys.argv)
app.aboutToQuit.connect(fechar_programa)

# Carrega a tela de carregamento (Splash)
tela_splash = uic.loadUi("scr/UI/splash.xml")
# Remove as bordas da janela para parecer um splash profissional
tela_splash.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
tela_splash.show()

# Carrega a janela principal (mas mantém-na oculta por enquanto)
janela = uic.loadUi("scr/UI/dashboard.xml")
janela.btn_adicionar.clicked.connect(adicionar_produto)
janela.btn_vender.clicked.connect(lambda: alterar_stock(-1))
janela.btn_repor.clicked.connect(lambda: alterar_stock(1))

# Variável de controlo para a animação da barra
contador = 0

# ==========================================
#  TELA DE CARREGAMENT0
# ==========================================
def animar_carregamento():
    global contador
    contador += 5  # Avança a barra de 5 em 5%
    tela_splash.barra_progresso.setValue(contador)
    
    # Quando o progresso chega a meio, carrega os dados da BD em background
    if contador == 50:
        carregar_dados_tabela()
        
    # Quando chega a 100%, fecha o carregamento e abre o programa real
    if contador >= 100:
        timer.stop()
        tela_splash.close()
        janela.show()

#  TIMER PARA A TELA DE CARREGAMENTO
timer = QTimer()
timer.timeout.connect(animar_carregamento)
timer.start(100) 

sys.exit(app.exec_())
