*NÃO APAGAR*
🧠 TIPOS DE COMMIT (padrão profissional)
feat: → adiciona nova funcionalidade
fix: → corrige bug
refactor: → melhora o código sem mudar comportamento
style: → formatação (espaço, identação, etc)
docs: → documentação (README, comentários)
test: → adiciona ou altera testes
chore: → tarefas gerais (config, build, dependências)

------------------------------------------

Exemplos reais

feat: adiciona envio automático de mensagens
fix: corrige erro no xpath do botão
refactor: melhora organização do código de envio
docs: adiciona instruções no README
chore: atualiza gitignore

------------------------------------------

comandos basicos do git (decora isso)
git pull
git add .
git commit -m "feat: alguma coisa"
git push

*apartir daqui pode apagar* -> lembrar

arrumei o erro no parser, mas ele so retorna 1 argumento por comando, vai dar erro em funções com multiplos comandos por exemplo a move_item().
Pensei em por enquanto a gente so passar 1 argumento, ai a função pega esse argumento (exemplo: target) e depois pergunta : ("mover de onde?") resposta -> "pasta1" ;  em seguida ("para onde") resposta "pasta2"
ou so passar isso em uma unica resposta : ("mover de onde para onde?") resposta -> "pasta1 pasta2".
