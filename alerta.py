import requests
import yfinance as yf
import pandas as pd
import winsound
from datetime import datetime

# --- CONFIGURAÇÃO DA CARTEIRA (Preços Médios do Moshe) ---
MEU_MEDIO = {
    "MXRF11.SA": 9.27,
    "GARE11.SA": 8.63,
    "BTCI11.SA": 9.37,
    "HGLG11.SA": 158.02
}

def monitor_completo():
    print("-" * 55)
    print(f"🚀 RELATÓRIO DE ATIVOS - {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("-" * 55)

    lista_resultados = []

    # 1. Criptomoedas (API CoinGecko)
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
        c = requests.get(url).json()
        btc_price = c['bitcoin']['usd']
        eth_price = c['ethereum']['usd']
        print(f"Bitcoin:  US$ {btc_price} | Ethereum: US$ {eth_price}")
    except:
        print("⚠️ Erro ao procurar Criptos")

    print("-" * 55)

    # 2. FIIs e Lógica de Alerta
    tickers = list(MEU_MEDIO.keys())
    try:
        dados_f = yf.download(tickers, period="1d", progress=False)['Close']
        
        for t in tickers:
            atual = dados_f[t].iloc[-1]
            medio = MEU_MEDIO[t]
            dif = ((atual / medio) - 1) * 100
            
            # Define se é oportunidade (Preço atual < Preço Médio)
            if atual < medio:
                status = "📉 OPORTUNIDADE"
                winsound.Beep(1000, 400) # Emite um bipe
            else:
                status = "✅ VALORIZADO"

            nome_exibicao = t.replace(".SA", "")
            print(f"{nome_exibicao:<7} | Atual: R$ {atual:>6.2f} | Médio: R$ {medio:>6.2f} | {status}")
            
            # Guardar para o Pandas
            lista_resultados.append({
                "Data/Hora": datetime.now().strftime('%d/%m/%Y %H:%M'),
                "Ativo": nome_exibicao,
                "Preço Atual": round(atual, 2),
                "Preço Médio": medio,
                "Variação (%)": round(dif, 2),
                "Status": status
            })

        # 3. Gerar o ficheiro Excel/CSV com Pandas
        df = pd.DataFrame(lista_resultados)
        # Salvamos com ponto e vírgula para abrir direto no Excel em português
        df.to_csv("relatorio_investimentos.csv", index=False, sep=";", encoding="utf-16")
        
        print("-" * 55)
        print("📁 Ficheiro 'relatorio_investimentos.csv' gerado com sucesso!")

    except Exception as e:
        print(f"⚠️ Erro ao processar FIIs: {e}")

if __name__ == "__main__":
    monitor_completo()