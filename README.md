<h1 align="center"> 🏦 Sistema Bancário em Python</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python Badge">
  <img src="https://img.shields.io/badge/Status-Finalizado-green?style=for-the-badge" alt="Status Badge">
</p>

<p align="center">
  <b>Uma interface de terminal (CLI) moderna e modularizada para gerenciamento bancário.</b>
</p>

---

## 📖 Sobre o Projeto

Este desafio consistiu em refatorar um sistema bancário inicial para torná-lo **modular**. O código foi organizado em funções específicas para depósito, saque, extrato, cadastro de usuários e contas correntes, aplicando conceitos de boas práticas e diferentes tipos de passagens de argumentos em Python.



## 🚀 Funcionalidades Principal

### 🔧 Gestão de Clientes e Contas
* **Novo Usuário:** Cadastra nome, data de nascimento, CPF (único) e endereço.
* **Nova Conta:** Cria uma conta corrente vinculada a um usuário (Agência fixa: `0001`).
* **Listar Contas:** Exibe todas as contas registradas e seus titulares de forma tabular.

### 💸 Operações Financeiras
* **Depósito:** Processado via *Positional-Only arguments*.
* **Saque:** Processado via *Keyword-Only arguments*, com limites de valor e quantidade diária.
* **Extrato:** Interface híbrida que detalha todas as movimentações do saldo.

---

## 💻 Como Rodar no VS Code

1. Abra o seu **VS Code**.
2. No terminal integrado (`Ctrl + '`), certifique-se de estar na pasta do arquivo.
3. Execute o comando:
```bash
python python_sistema_bancario.py
