# 🧠 Trabalho I – Sistemas Distribuídos (RPC com Python)

## 📘 Descrição do Projeto
Este projeto implementa uma aplicação distribuída utilizando o conceito de **RPC (Remote Procedure Call)** com **Python**, onde duas máquinas virtuais se comunicam através de chamadas remotas de funções.  

- **Servidor:** expõe métodos remotos (`soma` e `multiplica`) por meio de um servidor XML-RPC multithread.  
- **Cliente:** conecta-se ao servidor e realiza chamadas remotas para executar operações matemáticas.  

A implementação utiliza as bibliotecas padrão do Python (`xmlrpc.server` e `xmlrpc.client`), sem frameworks externos.

---

## ⚙️ Estrutura do Projeto

```
📁 RPC-Project
┣ 📜 server.py # Código do servidor (multithread)
┣ 📜 client.py # Código do cliente
```

---

## 🖥️ Ambiente Utilizado

Foram utilizadas **duas máquinas virtuais distintas** criadas com **VirtualBox**:

- **VM Servidor:** executa o `server.py`
- **VM Cliente:** executa o `client.py`
- **Sistema Operacional:** Ubuntu 22.04 (pode ser outro Linux)
- **Python:** versão 3.10 ou superior

A comunicação foi feita no modo “rede interna”.

---

## 🔧 Execução Passo a Passo

### 🧩 1. Configuração da Rede

1. No **VirtualBox**, abra as configurações de **rede** das duas VMs.  
2. Configure ambas na **mesma rede interna** (por exemplo: `intnet`).  
3. Inicie as máquinas e descubra o **endereço IP da VM Servidora**:

```bash
ip addr show
```
  
O IP deve aparecer em algo como `192.168.X.X`.

Você deve alterar a seguinte linha do código `cliente.py` para o seu endereço ip

```python
SERVER = "http://192.168.X.X:8000/RPC2" 
```

## 🖥️ 2. Executando o Servidor

Na VM servidor, salve o código abaixo como server.py:

```bash
nano server.py
```
Cole o conteúdo e salve.

Depois, execute o servidor:

```bash
python3 server.py
```

Você deverá ver:
```scss
Servidor RPC rodando na porta 8000 (multithread)...
```

## 💻 3. Executando o Cliente

Na VM cliente, salve o código abaixo como cliente.py:

```bash
nano cliente.py
```
Cole o conteúdo e salve (lembre de alterar o ip).

Depois, execute o cliente (o servidor já deve estar rodando na outra máquina):

```bash
python3 cliente.py
```

## 🧩 Conceitos Implementados

| Conceito | Implementação |
|-----------|----------------|
| **RPC (Remote Procedure Call)** | Comunicação entre cliente e servidor usando `xmlrpc` |
| **Stubs** | Criados automaticamente pela biblioteca `xmlrpc` |
| **Interface Remota** | Métodos públicos da classe `MathService` (`soma`, `multiplica`) |
| **Servidor Multithread** | Uso de `ThreadingMixIn` para atender múltiplos clientes simultaneamente |
| **Atraso Artificial (Simulação de carga)** | Uso de `time.sleep(2)` para demonstrar concorrência |

