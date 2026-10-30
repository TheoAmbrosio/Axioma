# Probabilidade

- [Documento Delta](notas_probabilidade.dlt).
- [Abrir no navegador](notas_probabilidade.html).
- [Referências e numeração](REFERENCIAS.md).

O conteúdo está organizado por assunto, com a numeração original dos resultados
de Casella e Berger e indicação da página impressa. As figuras vetoriais em
`figuras/` são incorporadas ao HTML pelo Delta e podem ser editadas ou regeneradas.

Para compilar nesta pasta:

```powershell
delta.cmd build notas_probabilidade.dlt -o notas_probabilidade.html
```

Referência principal: [Statistical Inference, 2ª edição, capítulo 1](https://pages.stat.wisc.edu/~shao/stat610/Casella_Berger_Statistical_Inference.pdf).

## Listas de exercícios

- [Lista das seções 1.1 a 1.3 — Delta](lista%20de%20exercicios/lista_exercicios_1_1_a_1_3.dlt).
- [Lista das seções 1.1 a 1.3 — abrir no navegador](lista%20de%20exercicios/lista_exercicios_1_1_a_1_3.html).
- [Lista da seção 1.4 até esperança e variância — Delta](lista%20de%20exercicios/lista_exercicios_1_4_a_esperanca_variancia.dlt).
- [Lista da seção 1.4 até esperança e variância — abrir no navegador](lista%20de%20exercicios/lista_exercicios_1_4_a_esperanca_variancia.html).

A primeira lista tem 10 questões e enfatiza probabilidade condicional, Bayes
e independência. A segunda tem 15 questões sobre variáveis aleatórias, CDF,
PMF, densidade, esperança e variância. Inclui adaptações do livro e questões
discretas mais simples; as duas questões com integrais são opcionais.
Para recompilar a partir desta pasta:

```powershell
delta.cmd build 'lista de exercicios/lista_exercicios_1_1_a_1_3.dlt' -o 'lista de exercicios/lista_exercicios_1_1_a_1_3.html'
delta.cmd build 'lista de exercicios/lista_exercicios_1_4_a_esperanca_variancia.dlt' -o 'lista de exercicios/lista_exercicios_1_4_a_esperanca_variancia.html'
```
