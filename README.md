# TODO list Django app

## Sobre o projeto

Aplicação web simples de lista de tarefas feito com Framework Django para fins de aprendizado.

## Objetivos

O objetivo desse projeto era aprender a utilizar uma ferramenta que melhorasse a experiência do usuário em aplicações que utilizar arquitetura MVC/MTV.
O escolhido para está situação foi o htmx.js, ele permite que possamos executar diversas tarefas que necessitam de JS diretamente no nosso HTML.
De forma resumida, ele adiciona atributos para o html que possibilita qualquer elemento fazer, por exemplo, uma requisição AJAX e atualizar a DOM da página sem dar refresh.

## Como executar

Basta ter Django instalado na sua máquina ou ambiente virtual python e executar os comandos básicos do Django.

```
pip install django
py manage.py migrate
py manage.py runserver
```

---

### Aqui deixarei alguns desafios para o futuro.

- [x] Migrar todo o CRUD para htmx.
- [x] Função simples que retorna o json de todas as tarefas.
- [ ] No delete, abrir um model BS5 ao invés de um confirm do browser.
- [ ] Adicionar função "concluir tarefa".
    - [ ] Função deve remover a tarefa da lista.
    - [ ] Função deve salvar a tarefa em outro model (ou mudar status).
    - [ ] A lista de tarefas deve ter outro campo para as tarefas concluídas.
    - [ ] As tarefas concluídas deve ter funções básicas do CRUD também. (Com htmx).
