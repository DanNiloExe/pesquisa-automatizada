import google.generativeai as genai
from datetime import datetime

# Configuração da API
GOOGLE_API_KEY = "SUA KEY AQUI"
genai.configure(api_key=GOOGLE_API_KEY)

try:
    # Seleção automática do modelo
    modelos = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model = genai.GenerativeModel(modelos[0])

    # PROMPT OTIMIZADO PARA ROTEIROS DE YOUTUBE
    prompt = (
        "Atue como um Roteirista Profissional de canais de grande alcance no YouTube. "
        "Objetivo: Criar um roteiro estruturado para um vídeo sobre o tema [Práticas ESG (Ambiental, Social e Governança)]. "
        "\n\nSiga rigorosamente esta estrutura de roteiro:\n"
        "1. O GANCHO (HOOK): Crie uma abertura de 15 a 30 segundos que apresente um problema ou curiosidade impossível de ignorar.\n"
        "2. INTRODUÇÃO: Breve apresentação do que será aprendido ou visto, focando na proposta de valor.\n"
        "3. CORPO DO ROTEIRO: Divida em tópicos (Cenas), incluindo sugestões de falas e indicações de B-Roll (o que deve aparecer na tela, como imagens, gráficos ou cortes de vídeo).\n"
        "4. RETENÇÃO: Insira um 'loop aberto' na metade do roteiro (algo que será revelado apenas no final).\n"
        "5. CTA (Chamada para Ação): Um pedido de inscrição ou comentário que faça sentido com o contexto do vídeo.\n"
        "6. TÍTULO E THUMBNAIL: Sugira 3 títulos clicáveis (estilo Clickgap) e uma ideia de design para a miniatura.\n\n"
        "Estilo de linguagem: Dinâmico, conversacional e adaptado para o público-alvo do tema."
    )

    print("Gerando seu roteiro... Isso pode levar alguns segundos.")
    response = model.generate_content(prompt)
    conteudo_roteiro = response.text

    print("\n" + "="*40)
    print("ROTEIRO GERADO COM SUCESSO:")
    print("="*40 + "\n")
    print(conteudo_roteiro)

    # Salvando em Markdown (.md) para facilitar a leitura das cenas e marcações
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"roteiro_youtube_{data_atual}.md"
    
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"# Roteiro de Vídeo - Gerado em {data_atual}\n\n")
        arquivo.write(conteudo_roteiro)

    print(f"\nO roteiro foi salvo com sucesso em '{nome_arquivo}'!")

except Exception as e:
    print(f"Erro ao gerar roteiro: {e}")