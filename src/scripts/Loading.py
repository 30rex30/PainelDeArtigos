from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt, QTimer
import mysql.connector
from mysql.connector import Error
import sys


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
