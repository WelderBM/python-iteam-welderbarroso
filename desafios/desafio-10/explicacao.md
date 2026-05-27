# Explicação — Desafio 10 — Projeto Final — Urna Eletrônica

**Aluno:** _(welder barroso de melo)_
**Data:** _(29-05-2026)_

---

## O que meu programa faz

_(o sistema simula uma urna eletronica onde da pra cadastrar candidatos com numero e nome e depois abrir a votação pra que as pessoas votem digitando o numero do candidato. no final ele mostra o resultado com a contagem de votos de cada um e quem ganhou)_

---

## Resposta à Pergunta Obrigatória

> Responda às três perguntas abaixo (cada uma em um parágrafo):
1. Como a herança ou dicionários facilitaram o cadastro de candidatos na sua solução?
2. Como você garantiu que o voto permanecesse anônimo e seguro?
3. Qual foi o maior obstáculo técnico que você superou e como resolveu?

_(1. usei dicionario pra guardar os candidatos porque com o numero do candidato como chave fica muito rapido de achar ele na hora da votação sem precisar ficar percorrendo lista inteira. cada candidato tem um dicionario com nome e votos e isso organiza tudo de um jeito que faz sentido pra acessar depois)_

_(2. o voto fica anonimo porque o sistema so registra o numero digitado e soma no contador do candidato sem guardar nenhuma informação de quem votou. nao tem variavel nenhuma que associe o voto a um eleitor entao nao tem como saber quem votou em quem)_

_(3. a parte mais dificil foi fazer a validação dos votos porque o usuario pode digitar qualquer coisa e o programa nao pode quebrar. tive que usar try except pra tratar quando digitam letras em vez de numeros e tambem verificar se o numero digitado realmente existe na lista de candidatos)_

---

## Dificuldades encontradas

_(a logica da votação em si não foi tao dificil mas organizar tudo em classes e garantir que o voto nulo e branco funcionassem direito deu um trabalho. pesquisei bastante sobre como fazer o menu ficar bonito no terminal)_
