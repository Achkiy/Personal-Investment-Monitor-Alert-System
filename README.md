# Personal Investment Monitor & Alert System 📈🐍

Sistema automatizado desenvolvido em **Python** para monitoramento em tempo real de ativos financeiros (FIIs e Criptomoedas).

## 🚀 Funcionalidades
- **Integração de APIs:** Consumo de dados em tempo real via Yahoo Finance e CoinGecko.
- **Análise Estratégica:** Comparação automática entre preço de mercado e preço médio do investidor.
- **Alertas Inteligentes:** Notificação sonora (Beep) integrada ao sistema para identificar oportunidades de aporte.
- **Persistência de Dados:** Geração automática de relatórios em CSV/Excel utilizando a biblioteca **Pandas**.

## 🛠️ Tecnologias Utilizadas
- **Python 3.11**
- **Pandas:** Para manipulação e exportação de dados.
- **YFinance:** Para extração de dados da B3.
- **Requests:** Para integração com APIs de Criptomoedas.
- **Winsound:** Para automação de alertas sonoros.

## 📊 Exemplo de Saída (Relatório)
O sistema gera um arquivo estruturado com:
`Data;Ativo;Preço Atual;Preço Médio;Variação (%);Status`
