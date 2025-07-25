# Curso de Python Flask

Este repositório contém os exercícios e exemplos de código desenvolvidos durante o curso de Python com o framework Flask.
Cada diretório representa um exercício ou um tópico específico abordado no curso.

## Como Executar os Exercícios

Para executar cada projeto de exercício, siga os passos abaixo. Todos os comandos devem ser executados no terminal, dentro do diretório do exercício correspondente (por exemplo, `cd "Hello World"`).

### Passo 1: Criar o Ambiente Virtual (Virtual Environment)

Um ambiente virtual isola as dependências do seu projeto, evitando conflitos com outros projetos Python em sua máquina.

Navegue até o diretório do exercício que deseja executar e crie o ambiente virtual:

```bash
python -m venv venv
```

Ou, se você tiver múltiplas versões do Python instaladas e quiser usar a versão 3:

```bash
python3 -m venv venv
```

Isso criará um diretório chamado `venv` contendo os arquivos do ambiente virtual.

### Passo 2: Ativar o Ambiente Virtual

Antes de instalar as dependências ou executar a aplicação, você precisa ativar o ambiente virtual.

**No Linux ou macOS:**

```bash
source venv/bin/activate
```

**No Windows (PowerShell ou CMD):**

```bash
venv\Scripts\activate
```

Após a ativação, o nome do ambiente virtual (`(venv)`) aparecerá no início do seu prompt de comando, indicando que ele está ativo.

### Passo 3: Instalar as Dependências

Cada exercício possui um arquivo `requirements.txt` que lista todas as bibliotecas Python necessárias. Com o ambiente virtual ativado, instale as dependências com o seguinte comando:

```bash
pip install -r requirements.txt
```

### Passo 4: Executar a Aplicação Flask

Após instalar as dependências, você pode iniciar o servidor de desenvolvimento do Flask. O arquivo principal da aplicação em cada exercício é o `app.py`.

Existem duas maneiras comuns de executar a aplicação:

#### Método 1: Usando o comando `flask` (Recomendado)

Esta é a forma moderna e mais flexível de iniciar o servidor.

```bash
flask --app app run
```
#### Método 2: Usando o comando `python` 

Para iniciar a aplicação, execute o script principal diretamente com o interpretador Python. Certifique-se de que você está no diretório raiz do projeto.

```bash
python app.py
```

Após executar o comando, o terminal mostrará o endereço onde a aplicação está rodando, geralmente `http://127.0.0.1:5000`. Abra este endereço no seu navegador para ver a aplicação em funcionamento.