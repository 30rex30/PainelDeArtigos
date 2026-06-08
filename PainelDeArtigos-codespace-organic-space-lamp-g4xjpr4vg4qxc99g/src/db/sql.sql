DROP DATABASE IF EXISTS loja_informatica;
CREATE DATABASE loja_informatica;
USE loja_informatica;

CREATE TABLE produtos (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL DEFAULT 0
);

-- Dados  teste
INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES
('Processador AMD Ryzen 5', 'Componentes', 159.90, 12),
('Rato Gaming Logitech G502', 'Periféricos', 59.99, 25),
('Portátil Asus ROG Strix', 'Computadores', 1249.99, 4),
('Memória RAM Corsair 16GB', 'Componentes', 75.50, 18);