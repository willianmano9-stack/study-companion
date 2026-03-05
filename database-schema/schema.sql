CREATE TABLE perfis (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    tipo TEXT CHECK (tipo IN ('professor', 'aluno')),
    criado_em TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE registros_aula (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    professor_id UUID REFERENCES perfis(id),
    titulo TEXT NOT NULL,
    conteudo_planejado TEXT,
    data_aula DATE DEFAULT CURRENT_DATE
);

CREATE TABLE tarefas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aluno_id UUID REFERENCES perfis(id),
    aula_id UUID REFERENCES registros_aula(id),
    url_imagem_caderno TEXT,
    insight_ia TEXT,
    nota_professor TEXT,
    metodologia_aplicada TEXT,
    status TEXT DEFAULT 'pendente'
)