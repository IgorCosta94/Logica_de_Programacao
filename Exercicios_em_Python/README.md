# 📚 Programas em Python

Exercícios resolvidos em Python a partir do livro Lógica de Programação: a construção de algoritmos e estruturas de dados com aplicações em Python , de André Luiz Villar Forbellone e Henri Frederico Eberspächer

## 📋 Índice de Exercícios

### 🔄 Estruturas de Controle - Repetição (Loops)

1. **[analise_dados_populacao.py](analise_dados_populacao.py)**
   - Análise de dados de habitantes com múltiplas condições
   - Conceitos: loops, acumuladores, estruturas condicionais aninhadas
   - Calcula: maior idade, porcentagens por critérios específicos

2. **[comparacao_crescimento_altura.py](comparacao_crescimento_altura.py)**
   - Simulação de crescimento de altura ao longo dos anos
   - Conceitos: loops com variável de controle, incrementos
   - Determina: quantos anos até uma pessoa ficar mais alta que outra

3. **[busca_maior_empresa.py](busca_maior_empresa.py)**
   - Busca da empresa com mais funcionários em cada categoria
   - Conceitos: condicionais aninhadas, variáveis de máximo, validação de entrada
   - Agrupa: dados por porte (Grande, Média, Pequena, Micro)

4. **[calculo_imposto_renda.py](calculo_imposto_renda.py)**
   - Cálculo de imposto de renda com alíquotas progressivas
   - Conceitos: estruturas condicionais múltiplas, cálculos com percentuais
   - Aplica: deduções por dependentes

---

### 📦 Estruturas de Dados Avançadas

5. **[estrutura_pilha_lifo.py](estrutura_pilha_lifo.py)** ⭐
   - Implementação e demonstração de PILHA (Last In, First Out)
   - Conceitos: estrutura de dados linear, push/pop
   - Uso: histórico de ações, desfazer/refazer

6. **[estrutura_fila_fifo.py](estrutura_fila_fifo.py)** ⭐
   - Implementação e demonstração de FILA (First In, First Out)
   - Conceitos: estrutura de dados linear, enqueue/dequeue
   - Uso: filas de atendimento, processamento sequencial

7. **[lista_encadeada_tarefas.py](lista_encadeada_tarefas.py)** ⭐
   - Implementação de LISTA ENCADEADA com sequência de tarefas
   - Conceitos: nós, referências/ponteiros, navegação por encadeamento
   - Uso: ordem customizável de elementos

8. **[gerenciamento_nomes_crud.py](gerenciamento_nomes_crud.py)**
   - Sistema completo CRUD (Create, Read, Update, Delete)
   - Conceitos: listas, funções, operações de busca e modificação
   - Operações: exclusão, localização, alteração de nomes

---

### 🔧 Funções e Módulos

9. **[converter_numero_extenso.py](converter_numero_extenso.py)**
   - Converte números inteiros em sua representação textual
   - Conceitos: funções personalizadas, estruturas condicionais múltiplas
   - Intervalo: 1 a 999.999

10. **[registro_cheques_dataclass.py](registro_cheques_dataclass.py)**
    - Gerenciamento de cheques usando dataclasses
    - Conceitos: dataclasses, estruturas de dados, funções auxiliares
    - Recursos: cálculo de dígito verificador, relatório de cheques

---

### 📐 Estruturas Sequenciais

11. **[calculo_idade_aniversario.py](calculo_idade_aniversario.py)**
    - Calcula idade em anos, meses e dias
    - Conceitos: operações sequenciais, aritmética com datas
    - Tipo: exercício básico sem loops

12. **[calculo_juros_desconto.py](calculo_juros_desconto.py)**
    - Calcula juros e descontos sobre uma prestação
    - Conceitos: cálculo de percentuais, operações financeiras
    - Tipo: exercício básico com fórmulas

---

### 🎓 Exercícios Diversos

13. **[resolver_equacao_segundo_grau.py](resolver_equacao_segundo_grau.py)**
    - Resuelve equações quadráticas (ax² + bx + c = 0)
    - Conceitos: fórmula de Bhaskara, discriminante, operações matemáticas
    - Fórmula: x = (-b ± √Δ) / 2a

14. **[calcular_media_notas.py](calcular_media_notas.py)**
    - Calcula a média aritmética de 4 notas
    - Conceitos: loops, acumuladores, cálculo de média
    - Recursos: exibe status do aluno (aprovado/recuperação/reprovado)

15. **[calcular_volume_esfera.py](calcular_volume_esfera.py)**
    - Calcula o volume de uma esfera dado o raio
    - Conceitos: geometria tridimensional, fórmulas matemáticas
    - Fórmula: V = (4/3)πr³

---

## 🎯 Nível de Dificuldade

| Nível             | Exercícios                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Iniciante**     | calculo_idade_aniversario, calculo_juros_desconto, resolver_equacao_segundo_grau, calcular_media_notas, calcular_volume_esfera |
| **Intermediário** | analise_dados_populacao, comparacao_crescimento_altura, converter_numero_extenso, estrutura_pilha_lifo, estrutura_fila_fifo    |
| **Avançado**      | busca_maior_empresa, calculo_imposto_renda, lista_encadeada_tarefas, gerenciamento_nomes_crud, registro_cheques_dataclass      |

---

## 📺 Demos em Ação

Aqui estão as execuções dos exercícios:

### Estrutura de Dados - Pilha (LIFO)

```
Estado 1 - Tamanho: 2, Pilha: ['Ciclano', 'João']
Estado 2 - Tamanho: 4, Pilha: ['Ciclano', 'João', 'Beltrano', 'José']
Estado 3 - Tamanho: 5, Pilha: ['Ciclano', 'João', 'Beltrano', 'José', 'Fulano']

Removendo elementos da pilha (LIFO):
Atendendo:  Fulano
Atendendo:  José
Atendendo:  Beltrano
Atendendo:  João
Atendendo:  Ciclano

Pilha vazia!

```

### Estrutura de Dados - Fila (FIFO)

```
Estado 1 - Tamanho: 2, Fila: deque(['Ciclano', 'João'])
Estado 2 - Tamanho: 4, Fila: deque(['Ciclano', 'João', 'Beltrano', 'José'])
Estado 3 - Tamanho: 5, Fila: deque(['Ciclano', 'João', 'Beltrano', 'José', 'Fulano'])

Removendo elementos da fila (FIFO):
Atendendo:  Ciclano
Atendendo:  João
Atendendo:  Beltrano
Atendendo:  José
Atendendo:  Fulano

Fila vazia!

```

### Estrutura de Dados - Lista Encadeada

```
Tarefa 1: Deixar o carro no estacionamento
Tarefa 2: Comprar calçaados no shopping
Tarefa 3: Autenticar documentos no cartório
Tarefa 4: Buscar encomenda no correio
Tarefa 5: Efetuar um saque no caixa
Tarefa 6: Comprar presente
Tarefa 7: Comprar livros na livraria
Tarefa 8: Pegar as roupas na lavanderia

Total de tarefas na sequência: 8

```

### Simulação - Crescimento de Altura

```
A quantidade de anos para Felisberto ficar maior que Anacleto é: 42 anos
Altura de Anacleto após 42 anos: 2.34m
Altura de Felisberto após 42 anos: 2.36m

```

### Cálculo - Média de Notas

```
Digite a nota do aluno (digite uma por vez): Digite a nota do aluno (digite uma por vez): Digite a nota do aluno (digite uma por vez): Digite a nota do aluno (digite uma por vez):
========================================
RESULTADO
========================================
Soma das notas: 33.00
A média das notas do aluno é: 8.25
========================================
Status: APROVADO [OK]

```

### Matemática - Equação do 2º Grau

```
Digite o valor de A: Digite o valor de B: Digite o valor de C:
========================================
SOLUCAO DA EQUACAO DO SEGUNDO GRAU
========================================
Equacao: 1$x^2$ + -5x + 6 = 0
Discriminante (Delta): 49
X1 = 6.00
X2 = -1.00
========================================

```

### Geometria - Volume da Esfera

```
Forneça o raio da esfera (em unidades):
==================================================
CÁLCULO DO VOLUME DA ESFERA
==================================================
Raio da esfera: 5.0 unidades
Volume da esfera: 523.33 unidades
==================================================

Formula utilizada: V = (4/3) * pi * $r^2$
Onde pi = 3.14

```

### Funções - Converter Número em Extenso

```
Informe um número no intervalo de 1 a 999.999:
```

### Financeiro - Juros e Desconto

```
Informe o valor da prestação em atraso (R$):
==================================================
CÁLCULO DE JUROS E DESCONTO
==================================================
Valor original da prestação: R$ 100.00
Valor com juros de 10%:      R$ 110.00
Valor final com desconto:    R$ 99.00
Prejuízo para o comerciante: R$ 11.00
==================================================

```

### Datas - Cálculo de Idade

```
Informe o ano do aniversário: Informe o dia do aniversário: Informe o més do aniversário (formato numérico 01-12): Informe o ano atual: Informe o dia atual: Informe o més atual:
Idade calculada:
  Anos: 25
  Meses aproximados: 912
  Dias aproximados: 10950

```

## 🚀 Como Executar

Todos os programas requerem **Python 3.10+** e não possuem dependências externas.

### ⭐ Melhores Exercícios (Recomendado)

Os exercícios na pasta `melhores_exercicios/` têm nomes significativos e são totalmente comentados:

```bash
# Executar um exercício específico
python3 melhores_exercicios/nome_do_arquivo.py

# Exemplos:
python3 melhores_exercicios/estrutura_pilha_lifo.py
python3 melhores_exercicios/converter_numero_extenso.py
python3 melhores_exercicios/calcular_media_notas.py
```
---

## 📖 Conceitos-Chave por Categoria

### Loops e Condições

- Estruturas `while` e `for`
- Condições `if`, `elif`, `else`
- Operadores lógicos

### Estruturas de Dados

- Listas (arrays)
- Dicionários
- Dataclasses
- Listas encadeadas, Pilhas (LIFO), Filas (FIFO)

### Funções e Modularização

- Definição de funções
- Parâmetros e retorno
- Escopo de variáveis

### Operações Matemáticas

- Aritmética básica
- Percentuais e cálculos financeiros
- Geometria

---

## 📌 Observações

Este é um repositório de estudo. Alguns exercícios básicos não tratam erros de entrada (`try/except`) de propósito, para manter o foco no conceito do capítulo.

---

**Última atualização**: 2026-07-25
