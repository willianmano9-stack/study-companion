import gradio as gr
import os
from dotenv import load_dotenv

load_dotenv() # Carrega o nosso novo arquivo .env
from src.supabase_client import get_supabase
from src.socratic_engine import generate_socratic_insight

def process_notebook(student_name, lesson_context, notebook_img):
    """
    Fluxo: Recebe a imagem, gera o insight via Gemini e registra no Supabase.
    """
    if notebook_img is None:
        return "⚠️ Por favor, carregue uma foto do caderno para análise."

    try:
        # 1. Gerar o Insight Socrático (Metacognição)
        # O motor usa a instrução de sistema que definimos para ser preciso e acadêmico.
        insight = generate_socratic_insight(notebook_img, lesson_context)

        # 2. Conectar ao Supabase
        supabase = get_supabase()

        # Busca o ID do aluno no banco de dados para vincular a tarefa
        # Usamos o Joaquim Silva como teste inicial conforme seu seed_data.
        student_res = supabase.table("perfis").select("id").eq("nome", student_name).single().execute()
        
        if not student_res.data:
            return "❌ Erro: Aluno não encontrado no sistema."
            
        student_id = student_res.data['id']

        # 3. Salvar a análise na tabela 'tarefas'
        # O status 'analisado' indica que a IA já processou este registro.
        supabase.table("tarefas").insert({
            "aluno_id": student_id,
            "titulo": f"Análise Socrática: {lesson_context}",
            "descricao": f"Registro fotográfico da aula sobre {lesson_context}",
            "status": "analisado",
            "insight_ia": insight
        }).execute()

        return insight

    except Exception as e:
        return f"❌ Falha no processamento: {str(e)}"

# --- Interface Visual (Gradio) ---
with gr.Blocks(theme=gr.themes.Soft(), title="Study Companion Admin") as demo:
    gr.Markdown("# 🎓 Study Companion - Motor de IA Socrática")
    gr.Markdown("Analise registros de aula e gere provocações cognitivas para os alunos.")

    with gr.Row():
        with gr.Column():
            # Seleção baseada nos dados do seu seed_data.sql
            student_input = gr.Textbox(
                label = "Nome do Aluno",
                placeholder="Insira o nome completo do aluno",
            )
            context_input = gr.Textbox(
                label="Contexto da Aula", 
                placeholder="Ex: Revolução Industrial ou Equações de 2º Grau"
            )
            image_input = gr.Image(type="filepath", label="Upload da Foto do Caderno")
            submit_btn = gr.Button("Gerar Insight Pedagógico", variant="primary")

        with gr.Column():
            output_display = gr.Textbox(
                label="Resultado da Análise (Salvo no Banco de Dados)", 
                interactive=False, 
                lines=12
            )

    submit_btn.click(
        fn=process_notebook,
        inputs=[student_input, context_input, image_input],
        outputs=output_display
    )

if __name__ == "__main__":
    demo.launch()