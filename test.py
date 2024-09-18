if __name__ == "__main__":
    pasta = "caminho/para/a/pasta/com/json"
    print(f"Verificando a pasta: {pasta}")
    df = extrair_dados(pasta)
    if df.empty:
        print("Nenhum dado extraído.")
    else:
        df_kpi = calcular_kpi_vendas(df)
        print(df_kpi)
        
        
        
    