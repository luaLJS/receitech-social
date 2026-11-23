# Processo diário (tarefa agendada)

## 0. Preparar o ambiente
1. Clonar o repositório público `luaLJS/receitech-social` em /home/claude/receitech-social (com acesso de push; use add_repo com access "push" se precisar).
2. Rodar `bash /home/claude/receitech-social/gerador/setup.sh` (recria /home/claude/assets, posts, fotos, cut, cut2 como links pro repo).
3. Ler `gerador/REGRAS.md` inteiro e a memória do projeto (areas/receitech-conteudo-social.md e principles.md).
4. Ler o canvas.json atual com a ferramenta Artifact (action read, url https://claude.ai/artifact/KbnEDoPp5MMfTtQifPpSEt, path project/canvas.json); antes de publicar, fazer um read sem path (senão o publish é recusado) e publicar com root na pasta salva pelo read e salvar em /mnt/user-data/outputs/artifacts/969fa822-132d-4a02-8ed1-b92e5c3beee1/project/canvas.json. Sempre reler antes de publicar (a Luana pode ter editado).

## 1. Planejar (sem montar nada)
- Escolher 2 temas: 1 carrossel de 2 telas + 1 foto única (desde 23/11; nunca 3 telas). Conferir no feed real (capas já postadas, ordem do Buffer) se a funcionalidade já apareceu. Funcionalidades do Receitech que ainda não apareceram nos últimos dias (ver histórico em REGRAS.md). Exemplos: preço do produto, cardápio online, lista de compras, aba Lucro / retirada, lucro por canal (iFood), estoque de pronta-entrega, encomendas por data de entrega, gastos do negócio, precificação por foto, vendas por cliente (só se já existir no app).
- Um post de cada vez, já com a imagem: renderizar a tela 1 com cada opção de frase (no layout escolhido) ao lado da tela 2 e mandar essa imagem junto com as opções de texto (Luana, 19/11). Como a funcionalidade funciona (1 ou 2 frases) + 2 ou 3 opções de frase da tela 1 (com a funcionalidade) + frase da tela 2 e o que aparece no celular. Mandar numa mensagem numerada (SendUserMessage) e ESPERAR a resposta antes do próximo post.
- Layout: abrir os quadros do Feed proposto, simular o feed real com o post novo e mostrar as opções de layout desenhadas no canvas. Foto nova sempre que a do banco for parecida com uma já usada.

## 2. Montar
- Usar os scripts de gerador/posts como base (c3.py, c3_s2.py, f1.py, f2.py mostram o padrão: tela do app em HTML + phone() + layout; feed.py/feed_new.py têm os 21 layouts).
- Fotos: banco-imagens/ (ver index.json, respeitar 30 dias). Subir no canvas com upload_asset e usar /_blob/<id>.
- Publicar as pranchas no canvas com publish_files (mode patch, base_version atual), linha nova por dia, título do dia como nota. Apagar do canvas o que for rejeitado.
- Conferir cada tela renderizando com Playwright (/usr/bin/google-chrome, viewport 540x720) e olhando a imagem antes de mostrar.
- Mostrar a prancha numerada no chat + canvas. Pedir aprovação. Ajustar até ela dar OK.

## 3. Publicar (só com OK explícito)
- Exportar 1080x1440 JPEG (viewport 540x720, device_scale_factor 2) para receitech-social/AAAA-MM-DD/.
- Commit + push (rodapé de commit padrão). Conferir que as URLs raw.githubusercontent.com respondem 200.
- Buffer (organização 6af5af1b63e814e4f5d5ff47, fuso America/Sao_Paulo):
  - Instagram: channelId 6af5b4af62b70b94b007588d, metadata {"instagram":{"type":"post","shouldShareToFeed":true}}
  - TikTok: channelId 6af5b4ff62b70b94b0075af7, metadata {"tiktok":{"title":"<máx 90 caracteres>"}}
  - mode customScheduled, schedulingType automatic, dueAt com -03:00. Carrossel = várias imagens em assets, na ordem.
- Atualizar banco-imagens/index.json (usos) e o histórico em REGRAS.md. Commit + push.

## 4. Imagens novas (quando o banco estiver acabando)
- Pelo Chrome da Luana (Claude in Chrome), se estiver conectado: Google Imagens (termos tipo "venda salgados", "encomenda doce Natal", nome do produto). Pegar URLs grandes parseando document.documentElement.innerHTML com a regex \["(https?://[^"]+?)",(\d+),(\d+)\] (3º grupo = largura, filtrar >= 900).
- Downloads diretos falham: abrir a URL da imagem com navigate, reconstruir a página com JS como <img> fixo no tamanho natural, passar o mouse no canto (1275,400), tirar screenshots com save_to_disk (scale 1) em duas faixas e costurar localmente.
- Sem marca de terceiros nas fotos. Salvar em banco-imagens/ e registrar no index.json.
- Se o Chrome não estiver conectado, usar o banco e avisar a Luana quantas fotos sobram.
