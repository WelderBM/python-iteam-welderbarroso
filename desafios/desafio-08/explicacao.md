# Explicação — Desafio 08 — Banco Digital

**Aluno:** _(welder barroso de melo)_
**Data:** _(28-05-2026)_

---

## O que meu programa faz

_(o programa tem uma classe ContaBancaria que guarda o nome do titular e o saldo da conta. ela tem 3 metodos, o depositar que soma o valor no saldo mas so se for um valor positivo, o sacar que tira do saldo mas verifica se tem saldo suficiente e se o valor é valido, e o exibir_extrato que mostra o nome do titular e quanto tem na conta. no programa principal eu crio 2 contas, uma pra mim e outra pro joao, faco depositos e saques e no final testo umas situações que tem que dar erro tipo sacar mais do que tem na conta ou depositar zero)_

---

## Resposta à Pergunta Obrigatória

> Por que `saldo` deve ser um **atributo da instância** (`self.saldo`) e não uma variável comum dentro do método? O que mudaria no comportamento do programa?

_(se o saldo fosse uma variavel comum dentro do metodo tipo so saldo = 0 sem o self, toda vez que voce chamasse o metodo depositar ou sacar ela ia criar uma variavel nova do zero e morrer quando o metodo terminasse. ou seja o saldo nunca ia ser salvo, ia depositar 500 reais e na hora de sacar o saldo ja tava zerado de novo porque a variavel sumiu. com o self.saldo o valor fica grudado no objeto, entao cada conta tem seu proprio saldo que persiste entre as chamadas dos metodos. sem o self basicamente o programa nao ia funcionar porque nao ia lembrar de nada)_

---

## Dificuldades encontradas

_(pesquisei sintaxe de classes em python, o __init__ e como usar o self)_
