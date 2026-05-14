import google.generativeai as genai
from datetime import datetime

# Configurações da API da IA ou buscador utilizado
#Key do API
GOOGLE_API_KEY = "SUA KEY DO API INSIRA AQUI"
#Key ao API
genai.configure(api_key=GOOGLE_API_KEY)

print("Verificando modelos disponíveis...")
try:
    modelos_disponiveis = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]

    if modelos_disponiveis:
        nome_modelo = modelos_disponiveis[0]
        print(f"Usando o modelo: {nome_modelo}")
        
        model = genai.GenerativeModel(nome_modelo)
        
        # Prompt de pesquisa do tema desejado
        prompt = (
            "Crie um post de LinkedIn. "
            "Tema:  ESG e sustentabilidade . "
            "O tom deve ser profissional e focado em resultados práticos, porém mantendo o bom humor e leveza."
        )

        # Resultado
        print("Gerando o post... Aguarde.")
        response = model.generate_content(prompt)
        conteudo_post = response.text

        print("\n" + "="*40)
        print("POST GERADO COM SUCESSO:")
        print("="*40 + "\n")
        print(conteudo_post)

        # Salvar o post direto num bloco de notas
        # Lembre-se de sempre atualizar o diretorio de sua maquina antes de executar, para garantir que o bloco
        # de notas será gerado, bastando o cd "etc......\Pesquisa automatizada" no terminal
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open("dados-pesquisa.json", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"\n--- DATA DE GERAÇÃO: {data_atual} ---\n")
            arquivo.write(conteudo_post)
            arquivo.write("\n" + "="*30 + "\n")

        print(f"\nO post foi salvo com sucesso em 'dados-pesquisa.json'!")

    else:
        print("Nenhum modelo disponível encontrado. Verifique sua API Key.")

except Exception as e:
    print(f"Ocorreu um erro no processo: {e}")