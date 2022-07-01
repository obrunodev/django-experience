# TODO list Django app

## Sobre o repositório

Neste repositório deixo todos os projetos que desenvolvo na finalidade de aprender algo novo. No caso, cada app tem um estudo diferente.

## Objetivos

O objetivo desse projeto é aprender e guardar projetos com a finalidade de aprender e utilizar de referência para futuros projetos.

- To-do list

Neste projeto utilizei pela primeira vez a biblioteca htmx, que adiciona "poderes" para o html. Por que só um form pode fazer requisições? E por que essas requisições precisam ser GET e POST somente? Bom, o htmx permite até que um simples button sozinho, execute um GET, POST, DELETE ou PUT e renderize o resultado em algum elemento.

- Cadastro de livros (a fazer)

O objetivo deste projeto é aprender a utilizar inline formsets, possibilitando o cadastro de multiplos livros em um único formulário. Para aumentar o desafio, será usado htmx para algumas interações.

- Projeto de Data engineering (a fazer)

Efetuar web scraping, tratar os dados e disponibilizar de alguma forma em um servidor web, nesse caso, o Django.

## Como executar

Basta ter Django instalado na sua máquina ou ambiente virtual python e executar os comandos básicos do Django.

```
pip install django
py manage.py migrate
py manage.py runserver
```

---

## Aqui deixarei alguns desafios para o futuro.

### To-do list

- [x] Migrar todo o CRUD para htmx.
- [x] Função simples que retorna o json de todas as tarefas.
- [ ] Desenvolver REST API de tarefas com DRF.
- [ ] No delete, abrir um model BS5 ao invés de um confirm do browser.
- [ ] Adicionar função "concluir tarefa".
    - [ ] Função deve remover a tarefa da lista.
    - [ ] Função deve salvar a tarefa em outro model (ou mudar status).
    - [ ] A lista de tarefas deve ter outro campo para as tarefas concluídas.
    - [ ] As tarefas concluídas deve ter funções básicas do CRUD também. (Com htmx).
