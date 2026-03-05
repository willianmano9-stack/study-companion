import os
import google.generativeai as genai
from PIL import Image

# Configuração da API Key que você salvou nos Secrets
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Instrução de Sistema: O "Contrato" da IA
SYSTEM_PROMPT = """
Você é um facilitador pedagógico especializado em metacognição. 
Sua função é analisar evidências de aprendizagem em registros visuais (cadernos) e atuar como um guia socrático.

DIRETRIZES DE ATUAÇÃO:
1. OBJETIVIDADE ANALÍTICA: Identifique lacunas conceituais ou erros procedimentais na imagem sem julgamentos de valor.
2. INTERVENÇÃO MÍNIMA: Jamais forneça a solução direta ou corrija o erro explicitamente. O objetivo é a autonomia do aluno.
3. PROVOCAÇÃO COGNITIVA: Formule uma única pergunta ou observação técnica que force o aluno a reavaliar sua própria lógica.
4. ALINHAMENTO PEDAGÓGICO: Utilize o contexto da aula fornecido para garantir que sua pista esteja dentro da zona de desenvolvimento proximal do estudante.

ESTILO DE RESPOSTA:
- Tom: Acadêmico, encorajador e preciso.
- Formato: Uma breve observação do que foi detectado seguida de um questionamento reflexivo.
"""

def generate_socratic_insight(image_path, context_lesson):
    """
    Analisa a imagem do caderno e gera uma pista pedagógica.
    """
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=SYSTEM_PROMPT)
    
    img = Image.open(image_path)
    
    prompt = f"O aluno está estudando: {context_lesson}. Analise a imagem e dê uma pista socrática."
    
    response = model.generate_content([prompt, img])
    return response.text