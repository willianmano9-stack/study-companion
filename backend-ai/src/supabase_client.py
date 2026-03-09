import os
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

def get_supabase() -> Client:
    if not url or not key:
        raise ValueError("Erro crítico: SUPABASE_URL ou SUPABASE_KEY não configurados")

    return create_client(url, key)

if __name__ == "__main__":
    try:
        supabase = get_supabase()

        response = supabase.table("perfis").select("*").eq("email", "willian@escola.com").execute()

        if response.data:
            print("✅ Sucesso! O backend conseguiu ler o banco de dados.")
            print(f"Usuário identificado: {response.data[0]['nome']}")
        else:
            print("⚠️ Conexão estabelecida, mas nenhum dado foi retornado. Verifique o seed_data.sql.")

    except Exception as e:
        print(f"❌ Falha na conexão: {e}")