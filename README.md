# 🖥️ Gestão de Inventário - Loja de Informática

Uma aplicação desktop simples e intuitiva desenvolvida em Python utilizando **PyQt5** para a interface gráfica e **MySQL** para a gestão e persistência de dados em tempo real.

---

## 🚀 Funcionalidades

* **Visualização em Tempo Real:** Listagem dinâmica de produtos diretamente da base de dados numa tabela (`QTableWidget`).
* **Registo de Produtos:** Adição de novos produtos definindo Nome, Categoria, Preço e Stock inicial.
* **Gestão de Stock Rápida:** * Botão **Vender**: Deduz automaticamente 1 unidade do stock do produto selecionado (com salvaguarda para não descer abaixo de 0).
    * Botão **Repor**: Incrementa automaticamente 1 unidade ao stock do produto selecionado.
* **Tratamento de Erros:** Prevenção de falhas comuns, como a conversão de vírgulas em pontos para valores decimais e validação de campos obrigatórios.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface Gráfica (GUI):** PyQt5 (carregamento dinâmico via ficheiro `.xml`/`.ui`)
* **Base de Dados:** MySQL
* **Conector:** `mysql-connector-python`

---

## 📋 Pré-requisitos & Instalação

Antes de começares, vais precisar de ter instalado na tua máquina o Python e um servidor MySQL (como o XAMPP, WampServer ou Docker).

### 1. Clonar o Repositório
```bash
git clone [https://github.com/o-teu-utilizador/nome-do-repositorio.git](https://github.com/o-teu-utilizador/nome-do-repositorio.git)
cd nome-do-repositorio
