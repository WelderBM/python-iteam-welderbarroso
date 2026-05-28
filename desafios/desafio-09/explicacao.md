# Explicação — Desafio 09 — Sistema de Frota

**Aluno:** _(welder barroso de melo)_
**Data:** _(28-05-2026)_

---

## O que meu programa faz

_(o programa cria uma classe pai Veiculo que tem marca modelo ano e uma quilometragem privada que começa em zero. tem o metodo rodar que adiciona km e não deixa passar valor negativo e o exibir_dados que mostra tudo. depois tem duas classes filhas Caminhao e Moto que herdam de Veiculo e cada uma adiciona um atributo extra, o caminhao tem capacidade de carga em toneladas e a moto tem cilindrada em cc. as duas fazem override do exibir_dados usando super() pra puxar os dados do pai e depois mostram o dado extra. no fim o programa principal cria um caminhao e uma moto, registra km em cada um, tenta registrar km negativo pra ver o erro e depois percorre uma lista com os dois veiculos chamando exibir_dados em cada um que é o polimorfismo funcionando)_

---

## Resposta à Pergunta Obrigatória

> Por que `Caminhao` e `Moto` 'herdam de' `Veiculo` e não simplesmente repetem os atributos? O que você ganha e o que arrisca ao usar herança?

_(se a gente repetisse tudo em cada classe ia ser um monte de codigo copiado e colado e na hora de corrigir um bug ou mudar alguma coisa ia ter que sair caçando em todos os lugares. com herança o codigo fica centralizado no pai e os filhos só adicionam o que é diferente deles. tipo se eu precisar mudar como a quilometragem funciona eu mudo só no Veiculo e ja vale pra todo mundo. o risco é que se a classe pai mudar de um jeito inesperado pode quebrar os filhos sem voce perceber, tipo se alguem mexe no __init__ do Veiculo e esquece que o Caminhao depende daquilo vai dar ruim. mas no geral compensa muito mais usar herança do que ficar repetindo codigo)_

---

## Dificuldades encontradas

_(pesquisei sintaxe de python pra usar super() e o atributo privado com dois underline)_
