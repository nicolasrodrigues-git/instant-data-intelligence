# 📊 Instant Data Intelligence

> Transforme qualquer planilha em um dashboard analítico completo — em segundos. Sem código. Sem configuração. Só fazer upload e explorar.

🔗 **App ao vivo:** [instant-data-intelligence.streamlit.app](https://instant-data-intelligence.streamlit.app/)

---

## 📌 Visão Geral

O **Instant Data Intelligence** é uma aplicação de análise de dados desenvolvida para transformar conjuntos de dados brutos em insights acionáveis de forma rápida e automatizada.

A proposta do projeto é simular um cenário real de negócio onde decisões precisam ser tomadas com agilidade, utilizando análise exploratória, métricas e visualização de dados para gerar valor.

---

## 🎯 Problema de Negócio

Empresas frequentemente enfrentam dificuldades em:

- Consolidar dados de múltiplas fontes
- Identificar padrões e tendências rapidamente
- Traduzir dados em decisões práticas
- Monitorar métricas de performance (KPIs) de forma eficiente

Esse atraso na análise impacta diretamente a tomada de decisão, a performance comercial e a eficiência operacional.

---

## 💡 Solução Proposta

O projeto entrega uma aplicação que:

- Automatiza a análise exploratória de dados
- Organiza e trata informações de forma estruturada
- Gera visualizações claras e objetivas
- Destaca métricas relevantes para o negócio
- Facilita a identificação de padrões e insights

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-antiX-FCC624?style=flat&logo=linux&logoColor=black)

| Camada | Tecnologia |
|--------|-----------|
| Frontend | Streamlit + CSS customizado (UI glassmorphism) |
| Processamento | Pandas + NumPy |
| Visualização | Plotly Express + Plotly Graph Objects |
| Inteligência | Classificação automática de colunas |
| Performance | st.cache_data para re-renders rápidos |

---

## 📊 Principais Funcionalidades

- 📥 **Upload inteligente** — CSV, XLS e XLSX até 50MB
- 📈 **Análise de tendências** — séries temporais com detecção automática de datas
- 📊 **Distribuições** — box plots e proporções por categoria
- 🔗 **Mapa de correlações** — relações entre variáveis numéricas
- 🧠 **Insights automáticos** — métrica mais volátil, top categoria, correlação mais forte
- 🧹 **Relatório de qualidade** — nulos, duplicatas e outliers sinalizados
- 💾 **Exportação** — download dos dados tratados em CSV

---

## 🧠 Inteligência Automática

### Classificação de Colunas
O app detecta automaticamente o tipo de cada coluna sem configuração manual:
- **Numéricas** → métricas, gráficos, correlações
- **Categóricas** → agrupamentos, proporções, top segmentos
- **Datas** → séries temporais e análise de tendência
- **IDs** → excluídos automaticamente das agregações

### Motor de Insights
A cada upload, 3 insights são gerados automaticamente:
1. **Métrica mais volátil** — coluna com maior variância
2. **Top categoria** — segmento que mais contribui para o volume
3. **Correlação mais forte** — as duas variáveis mais relacionadas

---

## 🧠 Impacto de Negócio

Este projeto simula como dados podem apoiar decisões como:

- Otimização de campanhas ou operações
- Redução de custos operacionais
- Melhoria de performance de KPIs
- Aumento de eficiência na análise de dados

---

## ⚙️ Como Executar o Projeto

git clone https://github.com/nicolasrodrigues-git/instant-data-intelligence.git
cd instant-data-intelligence
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

---

## 🚀 Próximos Passos

- Integração com APIs de dados em tempo real
- Automações mais avançadas de limpeza de dados
- Novas métricas e KPIs customizáveis
- Uso de IA para geração de insights automatizados

---

## 👤 Autor

**Nicolas Rodrigues**
Transição de carreira para a área de Dados | Python | SQL | Analytics

---

## ⭐ Considerações Finais

Este projeto representa a aplicação prática de análise de dados com foco em geração de valor para o negócio, indo além da parte técnica e explorando o uso estratégico da informação.

---
---

# 🌐 English Version

---

# 📊 Instant Data Intelligence

> Transform any CSV or Excel file into a full analytics dashboard in seconds. No code. No setup. Just upload and explore.

🔗 **Live App:** [instant-data-intelligence.streamlit.app](https://instant-data-intelligence.streamlit.app/)

---

## 📌 Overview

**Instant Data Intelligence** is a production-ready data analytics app built to transform raw datasets into actionable insights quickly and automatically.

---

## 🎯 Business Problem

Companies frequently struggle to:

- Consolidate data from multiple sources
- Identify patterns and trends quickly
- Translate data into practical decisions
- Monitor KPIs efficiently

---

## 💡 Proposed Solution

The app delivers:

- Automated exploratory data analysis
- Structured data organization and cleaning
- Clear and objective visualizations
- Highlighted business-relevant metrics
- Easy pattern and insight identification

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit + Custom CSS (glassmorphism UI) |
| Data processing | Pandas + NumPy |
| Visualization | Plotly Express + Plotly Graph Objects |
| Intelligence | Auto column classification engine |
| Performance | st.cache_data for fast re-renders |

---

## 📊 Key Features

- 📥 **Smart upload** — CSV, XLS and XLSX up to 50MB
- 📈 **Trend analysis** — time series with automatic date detection
- 📊 **Distributions** — box plots and category proportions
- 🔗 **Correlation heatmaps** — relationships between numeric variables
- 🧠 **Auto insights** — most volatile metric, top category, strongest correlation
- 🧹 **Quality report** — nulls, duplicates and outliers flagged instantly
- 💾 **Export** — download cleaned data as CSV

---

## 🧠 Business Impact

This project demonstrates how data can support decisions like:

- Campaign or operations optimization
- Operational cost reduction
- KPI performance improvement
- Increased efficiency in data analysis

---

## ⚙️ Running Locally

git clone https://github.com/nicolasrodrigues-git/instant-data-intelligence.git
cd instant-data-intelligence
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

---

## 🚀 Next Steps

- Integration with real-time data APIs
- Advanced data cleaning automations
- New customizable metrics and KPIs
- AI-powered automatic insight generation

---

## 👤 Author

**Nicolas Rodrigues**
Career transition into Data | Python | SQL | Analytics

---

Built with Python + Streamlit · Data processed locally · No data stored
