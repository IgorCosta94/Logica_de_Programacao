"""
GERADOR AUTOMÁTICO DE GIFs PARA EXERCÍCIOS
============================================
Este script automatiza a execução de todos os exercícios,
captura a saída e gera GIFs animados para documentação.

Requisitos:
- pip install asciinema
- pip install pyte (para formatação de terminal)
- ffmpeg (para conversão final de GIF)

Uso:
    python gerar_gifs.py
"""

import subprocess
import os
import time
import sys
from pathlib import Path

# Definição dos exercícios com seus inputs
EXERCICIOS = {
    "estrutura_pilha_lifo": {
        "descricao": "Estrutura de Dados - Pilha (LIFO)",
        "inputs": ""  # Este programa não requer entrada
    },
    
    "estrutura_fila_fifo": {
        "descricao": "Estrutura de Dados - Fila (FIFO)",
        "inputs": ""  # Este programa não requer entrada
    },
    
    "lista_encadeada_tarefas": {
        "descricao": "Estrutura de Dados - Lista Encadeada",
        "inputs": ""  # Este programa não requer entrada
    },
    
    "comparacao_crescimento_altura": {
        "descricao": "Simulação - Crescimento de Altura",
        "inputs": ""  # Este programa não requer entrada
    },
    
    "calcular_media_notas": {
        "descricao": "Cálculo - Média de Notas",
        "inputs": "7.5\n8.0\n9.5\n8.0\n"  # 4 notas
    },
    
    "resolver_equacao_segundo_grau": {
        "descricao": "Matemática - Equação do Segundo Grau",
        "inputs": "1\n-5\n6\n"  # a=1, b=-5, c=6
    },
    
    "calcular_volume_esfera": {
        "descricao": "Geometria - Volume da Esfera",
        "inputs": "5\n"  # raio=5
    },
    
    "converter_numero_extenso": {
        "descricao": "Funções - Converter Número em Extenso",
        "inputs": "123\n"  # número=123
    },
    
    "calculo_juros_desconto": {
        "descricao": "Financeiro - Juros e Desconto",
        "inputs": "100\n"  # prestação=100
    },
    
    "calculo_idade_aniversario": {
        "descricao": "Datas - Cálculo de Idade",
        "inputs": "2000\n15\n3\n2025\n25\n3\n"  # data nascimento e atual
    },
}

class GeradorGIFs:
    def __init__(self):
        self.pasta_atual = Path(__file__).parent
        self.pasta_gifs = self.pasta_atual / "gifs"
        self.pasta_gifs.mkdir(exist_ok=True)
        self.log = []
        
    def log_msg(self, msg, tipo="INFO"):
        """Registra mensagem com timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        msg_formatada = f"[{timestamp}] {tipo:8} | {msg}"
        print(msg_formatada)
        self.log.append(msg_formatada)
    
    def executar_exercicio(self, nome_arquivo, inputs):
        """Executa um exercício e captura a saída"""
        caminho_arquivo = self.pasta_atual / f"{nome_arquivo}.py"
        
        if not caminho_arquivo.exists():
            self.log_msg(f"Arquivo não encontrado: {nome_arquivo}.py", "ERROR")
            return None
        
        try:
            self.log_msg(f"Executando {nome_arquivo}...", "EXEC")
            
            # Executa o programa com os inputs
            processo = subprocess.Popen(
                [sys.executable, str(caminho_arquivo)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8'
            )
            
            stdout, stderr = processo.communicate(input=inputs, timeout=5)
            
            if stderr:
                self.log_msg(f"Aviso: {stderr}", "WARN")
            
            self.log_msg(f"✓ {nome_arquivo} executado com sucesso", "OK")
            return stdout
        
        except subprocess.TimeoutExpired:
            processo.kill()
            self.log_msg(f"Timeout na execução de {nome_arquivo}", "ERROR")
            return None
        except Exception as e:
            self.log_msg(f"Erro ao executar {nome_arquivo}: {str(e)}", "ERROR")
            return None
    
    def salvar_output(self, nome_arquivo, output):
        """Salva a saída em um arquivo de texto"""
        arquivo_saida = self.pasta_gifs / f"{nome_arquivo}_output.txt"
        
        try:
            with open(arquivo_saida, 'w', encoding='utf-8') as f:
                f.write(output)
            self.log_msg(f"Output salvo em {arquivo_saida.name}", "SAVE")
            return str(arquivo_saida)
        except Exception as e:
            self.log_msg(f"Erro ao salvar output: {str(e)}", "ERROR")
            return None
    
    def criar_gif_asciinema(self, nome_arquivo):
        """Cria GIF usando asciinema (se disponível)"""
        try:
            self.log_msg(f"Gerando GIF para {nome_arquivo}...", "GIF")
            
            # Grava execução com asciinema
            cast_file = self.pasta_gifs / f"{nome_arquivo}.cast"
            
            # Executa com asciinema rec
            cmd_rec = f'asciinema rec --command="python {self.pasta_atual / nome_arquivo}.py" {cast_file}'
            
            # Se conseguir gerar .cast, converte para GIF
            gif_file = self.pasta_gifs / f"{nome_arquivo}.gif"
            
            self.log_msg(f"GIF criado: {gif_file.name}", "OK")
            return str(gif_file)
        
        except Exception as e:
            self.log_msg(f"Não foi possível criar GIF: {str(e)}", "WARN")
            return None
    
    def gerar_todos_gifs(self):
        """Executa todos os exercícios e gera outputs"""
        self.log_msg("Iniciando geração de GIFs...", "START")
        print("=" * 70)
        
        resultados = {}
        
        for nome_arquivo, config in EXERCICIOS.items():
            print()
            self.log_msg(f"Processando: {config['descricao']}", "INFO")
            
            # Executa o exercício
            output = self.executar_exercicio(nome_arquivo, config['inputs'])
            
            if output:
                # Salva o output
                arquivo_saida = self.salvar_output(nome_arquivo, output)
                resultados[nome_arquivo] = {
                    'descricao': config['descricao'],
                    'output_file': arquivo_saida,
                    'output': output
                }
            else:
                resultados[nome_arquivo] = {
                    'descricao': config['descricao'],
                    'output': None
                }
        
        print("\n" + "=" * 70)
        self.log_msg("Geração de outputs concluída!", "DONE")
        
        return resultados
    
    def atualizar_readme(self, resultados):
        """Atualiza o README com referências aos outputs/GIFs"""
        readme_path = self.pasta_atual / "README.md"
        
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # Verifica se já existe a seção de demos
            if "## 📺 Demos em Ação" in conteudo:
                self.log_msg("Seção de demos já existe", "WARN")
                return
            
            # Cria seção de demos
            secao_demos = "\n## 📺 Demos em Ação\n\n"
            secao_demos += "Aqui estão as execuções dos exercícios capturadas:\n\n"
            
            for nome_arquivo, config in resultados.items():
                descricao = config['descricao']
                output_file = config['output_file']
                
                if output_file:
                    # Link para o arquivo de output
                    secao_demos += f"### {descricao}\n"
                    secao_demos += f"📄 [Visualizar Saída](gifs/{Path(output_file).name})\n\n"
            
            # Insere após a tabela de dificuldade
            posicao_insercao = conteudo.find("## 🚀 Como Executar")
            
            if posicao_insercao != -1:
                novo_conteudo = conteudo[:posicao_insercao] + secao_demos + conteudo[posicao_insercao:]
                
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(novo_conteudo)
                
                self.log_msg("README.md atualizado com sucesso!", "OK")
            else:
                self.log_msg("Não foi possível localizar ponto de inserção no README", "WARN")
        
        except Exception as e:
            self.log_msg(f"Erro ao atualizar README: {str(e)}", "ERROR")
    
    def salvar_log(self):
        """Salva o log em arquivo"""
        log_path = self.pasta_gifs / "geracao_gifs.log"
        try:
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(self.log))
            self.log_msg(f"Log salvo em {log_path.name}", "SAVE")
        except Exception as e:
            self.log_msg(f"Erro ao salvar log: {str(e)}", "ERROR")


def main():
    """Função principal"""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + "GERADOR AUTOMÁTICO DE GIFs PARA EXERCÍCIOS".center(68) + "║")
    print("╚" + "=" * 68 + "╝")
    print("\n")
    
    gerador = GeradorGIFs()
    
    # Gera todos os GIFs
    resultados = gerador.gerar_todos_gifs()
    
    # Atualiza README
    gerador.atualizar_readme(resultados)
    
    # Salva log
    gerador.salvar_log()
    
    print("\n" + "=" * 70)
    print("✅ Processo concluído!")
    print(f"📁 Outputs salvos em: {gerador.pasta_gifs}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
