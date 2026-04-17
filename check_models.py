import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega a sua GOOGLE_API_KEY do arquivo .env
load_dotenv()
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

print("Buscando modelos disponíveis para a sua chave...\n")

# Lista todos os modelos que suportam geração de conteúdo (texto/imagem)
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)