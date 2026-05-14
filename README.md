# ODE_MATERIAL

## 📝 Descrição
Este repositório contém materiais e scripts relacionados à resolução de Equações Diferenciais Ordinárias (EDOs). Ele inclui implementações numéricas, simbólicas e visualizações gráficas para explorar diferentes métodos e conceitos. Esses são alguns dos scripts que foram construídos na pesquisa `A computação aplicada ao estudo de Equações Diferenciais Ordinárias`, fruto do trabalho do autor ao longo do Programa de Iniciação Científica e Mestrado - PICME, sob a orientação do Dr. Yagor Carvalho Romano.

## 🧔 Autor
João Gabriel Pieroli da Silva  
Graduando em Bacharelado de Ciências de Computação

## 🔨 Dependências 

| Biblioteca | Descrição | Versão |
| :--- | :--- | :---: |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Linguagem principal do projeto | `3.10+` |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | Operações numéricas e vetoriais | `1.24+` |
| ![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white) | Métodos numéricos e integração de EDOs | `1.10+` |
| ![SymPy](https://img.shields.io/badge/SymPy-3E475E?style=flat-square&logo=sympy&logoColor=white) | Computação simbólica e soluções analíticas | `1.12+` |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-ffffff?style=flat-square&logo=matplotlib&logoColor=black) | Geração de gráficos e visualizações | `3.7+` |

## 📂 Estrutura do Repositório

```text
.
├── LICENSE                   # Arquivo de licença do projeto.
├── README.md
├── requirements.txt          # Lista de dependências Python necessárias
├── setup.bat                 # Script para configurar o ambiente no Windows.
├── setup.sh                  # Script para configurar o ambiente no Linux/macOS.
└── src/
    ├── basics/
    │   ├── EDOsympy.py       # Resolução simbólica (analítica)
    │   ├── IVP_Solver.py     # Foco em Problemas de Valor Inicial
    │   └── piccard.py        # Aproximações sucessivas de Picard
    ├── tool/
    │   └── EDOsolver.py      # Solver principal e utilitários
    ├── visualization/
    │   └── camposDirecoes.py # Visualização de campos de vetores/direções
    ├── graphics.py           # Plotagem de múltiplas trajetórias
    └── lipschitz.py          # Demonstração visual da Condição de Lipschitz

```

## 🐍 Conteúdo dos Arquivos em `src/`

- **camposDirecoes.py**: Gera e plota campos de direções para uma EDO específica.
- **EDOsolver.py**: Resolve EDOs numericamente e analiticamente, com visualizações interativas.
- **EDOsympy.py**: Utiliza a biblioteca SymPy para resolver EDOs simbolicamente.
- **IVP_Solver.py**: Resolve problemas de valor inicial (PVI) usando métodos numéricos.
- **piccard.py**: Implementa o método de aproximação de Picard para resolver EDOs.


## ⚙️ Como Usar

### 1. Configurar o Ambiente

#### Linux/macOS
1. Certifique-se de ter o Python 3 instalado.
2. Execute o script `setup.sh`. Há duas formas de executá-lo:
  - Instala as dependências criando um ambiente virtual no terminal:
   ```bash
   ./setup.sh
   ```
  - Instala as dependências e já ativa automaticamente o ambiente no terminal:
   ```bash
   source ./setup.sh
   ```

#### Windows
1. Certifique-se de ter o Python 3 instalado.
2. Execute o script `setup.bat`:
   ```cmd
   setup.bat
   ```
   Após isso, para ativar o ambiente no terminal atual:
   ```cmd
   call .\.venv\Scripts\activate.bat
   ```

### 2. Executar os Scripts
1. Navegue até o diretório `src/`:
   ```bash
   cd src
   ```
2. Execute qualquer script com o Python:
   ```bash
   python3 nome_do_arquivo.py
   ```

## 📎 Licença
Consulte o arquivo `LICENSE` para mais informações sobre a licença do projeto.