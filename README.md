🛠️ Configuração e Uso

Instalar a biblioteca para poder utilizar o gemini, diretamente no terminal
pip install -U -q google-generativeai

1. Obtenha sua API Key do Gemini
Para que o script funcione, você precisa de uma chave de acesso oficial da Google:

Acesse o Google AI Studio.
Faça login com sua conta Google.
Clique em "Create API key".
Copie a chave gerada.

No código Python, substitua o valor da de onde está sinalizada a GOOGLE_API_KEY pela sua chave:

Python
GOOGLE_API_KEY = "SUA KEY DO API INSIRA AQUI"

2. Como Alterar o Tema (Prompt)
O script é flexível. Para mudar o assunto do post ou o tom de voz da IA, localize a seção # Prompt de pesquisa no código:
Onde mudar: Altere o texto dentro da variável prompt.

3. Como Alterar a Saída (Bloco de Notas)
O resultado é salvo automaticamente em um arquivo de texto para garantir a persistência dos dados. Se você quiser mudar o nome do arquivo ou onde ele é salvo:
Nome do arquivo: Localize a linha with open("dados-pesquisa.txt", "a", ...). Altere "dados-pesquisa.txt" para o nome que desejar (ex: "posts-linkedin.txt").
Pasta de destino: Por padrão, o arquivo é criado na mesma pasta do script. Para salvar em outro lugar, insira o caminho completo (ex: C:\Users\Nome\Desktop\Pasta\arquivo.txt).
