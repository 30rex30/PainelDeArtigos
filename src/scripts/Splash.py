from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

tela_splash = None
contador = 0
timer = None
funcao_terminar = None
funcao_dados = None

def iniciar_splash(funcao_ao_terminar, funcao_carregar_dados):
    # Usamos 'global' para o Python saber que queremos guardar os dados nas variáveis lá de cima
    global tela_splash, timer, funcao_terminar, funcao_dados, contador
    
    funcao_terminar = funcao_ao_terminar
    funcao_dados = funcao_carregar_dados
    contador = 0
    
    # Carrega o ecrã Splash
    tela_splash = uic.loadUi("src/UI/splash.xml")
    tela_splash.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    
    # Coloca a imagem no QLabel
    pixmap = QPixmap("src/foto/logotipo.png")
    tela_splash.lbl_foto.setPixmap(pixmap.scaled(300, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    
    # Configurar o Timer (agora aponta para a função solta)
    timer = QTimer()
    timer.timeout.connect(animar_carregamento)
    timer.start(100) 
    
    tela_splash.show()

def animar_carregamento():
    global contador, timer, tela_splash
    
    contador += 5
    
    # Atualiza o texto conforme o progresso
    if contador == 25:
        tela_splash.lbl_loading.setText("A CONECTAR À BASE DE DADOS...")
    elif contador == 50:
        tela_splash.lbl_loading.setText("A CARREGAR PRODUTOS...")
        funcao_dados() # Carrega os dados da BD
    elif contador == 75:
        tela_splash.lbl_loading.setText("TUDO PRONTO...")
        
    # Quando chega ao fim, para o timer e fecha a janela
    if contador >= 100:
        timer.stop()
        tela_splash.close()
        funcao_terminar() 