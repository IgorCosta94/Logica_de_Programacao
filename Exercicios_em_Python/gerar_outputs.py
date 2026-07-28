"""
SCRIPT SIMPLIFICADO PARA GERAR OUTPUTS DOS EXERCÍCIOS
======================================================
Este script executa os exercícios e gera um markdown com as saídas.
"""

import subprocess
import sys
from pathlib import Path
import json

class GeradorOutputs:
    def __init__(self):
        self.pasta_atual = Path(__file__).parent
        self.pasta_gifs = self.pasta_atual / "gifs"
        self.pasta_gifs.mkdir(exist_ok=True)
    
    def executar_exercicio(self, nome_arquivo, inputs):
        """Executa um exercício e retorna a saída"""
        caminho = self.pasta_atual / f"{nome_arquivo}.py"
        
        if not caminho.exists():
            return None, f"Arquivo não encontrado: {nome_arquivo}"
        
        try:
            processo = subprocess.Popen(
                [sys.executable, str(caminho)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                errors='replace'
            )
            
            stdout, _ = processo.communicate(input=inputs, timeout=5)
            return stdout, None
        
        except subprocess.TimeoutExpired:
            processo.kill()
            return None, "Timeout"
        except Exception as e:
            return None, str(e)
    
    def gerar_secao_demos(self):
        """Gera a seção de demos em markdown"""
        
        exercicios = [
            ("estrutura_pilha_lifo", "Estrutura de Dados - Pilha (LIFO)", ""),
            ("estrutura_fila_fifo", "Estrutura de Dados - Fila (FIFO)", ""),
            ("lista_encadeada_tarefas", "Estrutura de Dados - Lista Encadeada", ""),
            ("comparacao_crescimento_altura", "Simulação - Crescimento de Altura", ""),
            ("calcular_media_notas", "Cálculo - Média de Notas", "7.5\n8.0\n9.5\n8.0\n"),
            ("resolver_equacao_segundo_grau", "Matemática - Equação do 2º Grau", "1\n-5\n6\n"),
            ("calcular_volume_esfera", "Geometria - Volume da Esfera", "5\n"),
            ("converter_numero_extenso", "Funções - Converter Número em Extenso", "123\n"),
            ("calculo_juros_desconto", "Financeiro - Juros e Desconto", "100\n"),
            ("calculo_idade_aniversario", "Datas - Cálculo de Idade", "2000\n15\n3\n2025\n25\n3\n"),
        ]
        
        secao = "## 📺 Demos em Ação\n\n"
        secao += "Aqui estão as execuções dos exercícios:\n\n"
        
        for nome, descricao, inputs in exercicios:
            output, erro = self.executar_exercicio(nome, inputs)
            
            if output is None:
                secao += f"### {descricao}\n"
                secao += f"```\nErro: {erro}\n```\n\n"
            else:
                # Salva output em arquivo
                arquivo_saida = self.pasta_gifs / f"{nome}_output.txt"
                try:
                    with open(arquivo_saida, 'w', encoding='utf-8') as f:
                        f.write(output)
                except:
                    pass
                
                # Adiciona ao markdown
                secao += f"### {descricao}\n"
                secao += "```\n"
                # Limita o tamanho da saída para não ficar muito grande
                linhas = output.split('\n')[:30]
                secao += '\n'.join(linhas)
                if len(output.split('\n')) > 30:
                    secao += "\n... (saída truncada)\n"
                secao += "\n```\n\n"
                
                print(f"✓ {nome}")
        
        return secao
    
    def atualizar_readme(self):
        """Atualiza o README com as demos"""
        readme_path = self.pasta_atual / "README.md"
        
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # Remove seção antiga de demos se existir
            if "## 📺 Demos em Ação" in conteudo:
                inicio = conteudo.find("## 📺 Demos em Ação")
                fim = conteudo.find("\n## ", inicio + 1)
                if fim == -1:
                    fim = len(conteudo)
                conteudo = conteudo[:inicio] + conteudo[fim:].lstrip()
            
            # Gera nova seção
            secao_demos = self.gerar_secao_demos()
            
            # Encontra local para inserir (antes de "Como Executar")
            posicao = conteudo.find("## 🚀 Como Executar")
            
            if posicao == -1:
                # Se não encontrar, adiciona antes de "Últimas atualizações"
                posicao = conteudo.find("**Última atualização**")
            
            if posicao == -1:
                # Se ainda não encontrar, adiciona no final
                novo_conteudo = conteudo + "\n\n" + secao_demos
            else:
                novo_conteudo = conteudo[:posicao] + secao_demos + "\n" + conteudo[posicao:]
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(novo_conteudo)
            
            print("\n✅ README.md atualizado com sucesso!")
            
        except Exception as e:
            print(f"❌ Erro ao atualizar README: {e}")


if __name__ == "__main__":
    print("🚀 Gerando demonstrações dos exercícios...\n")
    gerador = GeradorOutputs()
    gerador.atualizar_readme()
