# Casos de teste manuais

1. Nome válido: digitar Ana, clicar Cadastrar e conferir a mensagem.        O campo é limpo, pois está trocado com a função limpar
2. Nome vazio: clicar Cadastrar sem digitar e exigir orientação.
3. Somente espaços: digitar espaços e exigir orientação.
4. Espaços antes/depois: digitar "  Ana  " e conferir "Ana".
5. Botões: Cadastrar deve cadastrar; Limpar deve apagar o campo.            O botao está funcionando normalmente

Botao cadastrar corrigido: 
self.botao_cadastrar.clicked.connect(self.cadastrar)