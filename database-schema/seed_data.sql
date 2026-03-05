INSERT INTO perfis (nome, email, tipo) VALUES 
('Willian Professor', 'willian@escola.com', 'professor'),
('Aluno Teste', 'aluno@estudo.com', 'aluno');

INSERT INTO registros_aula (professor_id, titulo, conteudo_planejado)
SELECT id, 'Introdução à Lógica de Programação', 'Variáveis e Tipos de Dados'
FROM perfis WHERE email = 'willian@escola.com';