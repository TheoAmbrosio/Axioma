# Orientações para a IA

Este é o Axioma, repositório pessoal de estudos. As aulas de probabilidade ficam em `Aulas de probabilidade/`.

## Trabalhar com Delta

Antes de criar ou modificar arquivos `.dlt`, leia `docs/DELTA_README.md`, cópia do README oficial de https://github.com/rbribeiro/delta.
Para detalhes da linguagem e das tags, consulte https://rbribeiro.github.io/delta/ e os fontes da documentação em https://github.com/rbribeiro/delta/tree/main/site.
Não invente tags, atributos ou comandos: confirme-os na documentação oficial ou nos exemplos do professor.

- Escreva o material em português, salvo pedido diferente.
- Delta usa marcação XML; atributos devem ter valores explícitos, por exemplo `collapsible="true"`.
- Na prosa, escape os caracteres XML quando necessário: `&lt;`, `&gt;`, `&amp;`.
- Use `$...$` para matemática em linha e `$$...$$` para matemática em destaque.
- Para equações numeradas, consulte `<equation>`; para blocos alinhados, `<equations>`.
- O pacote npm é `delta-lang` e o executável é `delta`.
- Com o CLI instalado, compile com `delta build "caminho/arquivo.dlt" -o "caminho/arquivo.html"`.
- Antes de concluir uma alteração em `.dlt`, compile o documento e corrija eventuais erros. Se o CLI não estiver disponível, informe que a compilação não foi verificada.
- Preserve a cópia original do README em `docs/DELTA_README.md`; escreva orientações próprias neste arquivo ou no README do Axioma.
