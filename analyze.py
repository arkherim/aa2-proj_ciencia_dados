import pandas as pd
import sqlite3
import plotly.express as px
import numpy as np

# Função para ler dados do data warehouse
def read_dw(query: str) -> pd.DataFrame:
    conn = sqlite3.connect("databases/datawarehouse.db")
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Análise 1: Top 10 Pilotos por Vitórias
def top_vitorias():
    query = """
        SELECT 
            d.forename || ' ' || d.surname as piloto,
            COUNT(*) as vitorias
        FROM fato_resultado f
        JOIN dim_piloto d ON f.driverId = d.driverId
        WHERE f.position = 1
        GROUP BY d.driverId
        ORDER BY vitorias DESC
        LIMIT 10
    """
    
    df = read_dw(query)
    
    fig = px.bar(
        df,
        x="piloto",
        y="vitorias",
        title="Top 10 Pilotos por Vitórias",
        text="vitorias",
        labels={"vitorias": "Número de Vitórias", "piloto": "Piloto"},

        )
    fig.update_layout(
        plot_bgcolor="#1a1a2e",
        paper_bgcolor="#1a1a2e",
        font=dict(family="Century Gothic", size=14, color="#e0e0e0"),
        title_font=dict(family="Century Gothic", size=24, color="#e0e0e0"),
        title_x=0.5,
        xaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),      
            showgrid=False,
        ),
        yaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),
             gridcolor="#2a2a4a",       
            showgrid=True,
        )
    )
    fig.update_traces(
        textposition="outside",
        textfont=dict(color="#e0e0e0", size=14),
        hovertemplate="<b>%{x}</b><br>%{y}<extra></extra>"
    )
    fig.show()

# Análise 2: Top 10 Pilotos por Pódios    
def top_podios():
    query = """
        SELECT  
            d.forename || ' ' || d.surname as piloto,
            COUNT(*) as podios
        FROM fato_resultado f
        JOIN dim_piloto d ON f.driverId = d.driverId
        WHERE f.position <= 3
        GROUP BY d.driverId
        ORDER BY podios DESC
        LIMIT 10;
    """
    
    df = read_dw(query)
    
    fig = px.bar(
        df,
        x="piloto",
        y="podios",
        title="Top 10 Pilotos por Pódios",
        text="podios",
        labels={"podios": "Número de Pódios", "piloto": "Piloto"},
    )
    fig.update_layout(
        plot_bgcolor="#1a1a2e",
        paper_bgcolor="#1a1a2e",
        font=dict(family="Century Gothic", size=14, color="#e0e0e0"),
        title_font=dict(family="Century Gothic", size=24, color="#e0e0e0"),
        title_x=0.5,
        xaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),      
            showgrid=False,
        ),
        yaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),
             gridcolor="#2a2a4a",       
            showgrid=True,
        )
    )
    fig.update_traces(
        textposition="outside",
        textfont=dict(color="#e0e0e0", size=14),
        hovertemplate="<b>%{x}</b><br>%{y}<extra></extra>"
    )
    fig.show()

# Análise 3: Top 10 Pilotos por Poles
def top_poles():
    query = """
        SELECT  
            d.forename || ' ' || d.surname as piloto,
            COUNT(*) as poles
        FROM fato_resultado f
        JOIN dim_piloto d ON f.driverId = d.driverId
        WHERE f.grid = 1
        GROUP BY d.driverId
        ORDER BY poles DESC
        LIMIT 10;
    """
    
    df = read_dw(query)
    
    fig = px.bar(
        df,
        x="piloto",
        y="poles",
        title="Top 10 Pilotos por Poles",
        text="poles",
        labels={"poles": "Número de Poles", "piloto": "Piloto"},
    )
    fig.update_layout(
        plot_bgcolor="#1a1a2e",
        paper_bgcolor="#1a1a2e",
        font=dict(family="Century Gothic", size=14, color="#e0e0e0"),
        title_font=dict(family="Century Gothic", size=24, color="#e0e0e0"),
        title_x=0.5,
        xaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),      
            showgrid=False,
        ),
        yaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),
             gridcolor="#2a2a4a",       
            showgrid=True,
        )
    )
    fig.update_traces(
        textposition="outside",
        textfont=dict(color="#e0e0e0", size=14),
        hovertemplate="<b>%{x}</b><br>%{y}<extra></extra>"
    )
    fig.show()

# Análise 4: Top 10 Pilotos por Voltas Rápidas
def top_volta_rapidas():
    query = """
        SELECT  
            d.forename || ' ' || d.surname as piloto,
            COUNT(*) as voltas_rapidas
        FROM fato_resultado f
        JOIN dim_piloto d ON f.driverId = d.driverId
        WHERE f.rank = 1
        GROUP BY d.driverId
        ORDER BY voltas_rapidas DESC
        LIMIT 10;
    """
    
    df = read_dw(query)
    
    fig = px.bar(
        df,
        x="piloto",
        y="voltas_rapidas",
        title="Top 10 Pilotos por Voltas Rápidas (2004-2024)",
        text="voltas_rapidas",
        labels={"voltas_rapidas": "Número de Voltas Rápidas", "piloto": "Piloto"},
    )
    fig.update_layout(
        plot_bgcolor="#1a1a2e",
        paper_bgcolor="#1a1a2e",
        font=dict(family="Century Gothic", size=14, color="#e0e0e0"),
        title_font=dict(family="Century Gothic", size=24, color="#e0e0e0"),
        title_x=0.5,
        xaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),      
            showgrid=False,
        ),
        yaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),
             gridcolor="#2a2a4a",       
            showgrid=True,
        )
    )
    fig.update_traces(
        textposition="outside",
        textfont=dict(color="#e0e0e0", size=14),
        hovertemplate="<b>%{x}</b><br>%{y}<extra></extra>"
    )
    fig.show()  

# Análise 5: Pilotos Dominantes por Era (Top 3 de cada era)    
def dominacao_era_piloto():
    query = """
        SELECT 
            e.eraName || ' (' || e.startYear || '-' || e.endYear || ')' as era,
            d.forename || ' ' || d.surname as piloto,
            COUNT(*) as vitorias
        FROM fato_resultado f
        JOIN dim_piloto d ON f.driverId = d.driverId
        JOIN dim_temporada t ON f.raceId = t.raceId
        JOIN dim_era e ON t.eraId = e.eraId
        WHERE f.position = 1
        GROUP BY e.eraId, d.driverId
        HAVING COUNT(*) >= (
            SELECT COUNT(*) 
            FROM fato_resultado f2
            JOIN dim_temporada t2 ON f2.raceId = t2.raceId
            WHERE f2.position = 1 AND t2.eraId = e.eraId
            GROUP BY f2.driverId
            ORDER BY COUNT(*) DESC
            LIMIT 1 OFFSET 2
        )
        ORDER BY e.eraId, vitorias ASC;
    """
    
    df = read_dw(query)
        
    df["label"] = df["piloto"] + " (" + df["vitorias"].astype(str) + ")"
    
    fig = px.bar(
        df,
        x="era",
        y="vitorias",
        color="piloto",
        barmode="stack",
        title="Pilotos Dominantes por Era",
        text="label",
        labels={"vitorias": "Vitórias", "era": "Era", "piloto": "Piloto"}
    )
    fig.update_layout(
        plot_bgcolor="#1a1a2e",
        paper_bgcolor="#1a1a2e",
        font=dict(family="Century Gothic", size=14, color="#e0e0e0"),
        title_font=dict(family="Century Gothic", size=24, color="#e0e0e0"),
        title_x=0.5,
        showlegend=False,
        xaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),      
            showgrid=False,
        ),
        yaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),
            gridcolor="#2a2a4a",       
            showgrid=True
        )
    )
    fig.update_traces(
        textposition="inside",
        textfont=dict(color="#2a2a4a", size=14),
        hovertemplate="<b>%{fullData.name}</b><br>Vitórias: %{y}<extra></extra>"
    )
    fig.show()

# Análise 6: Equipes Dominantes por Era (Top 3 de cada era)    
def dominacao_era_equipe():
    query = """
        SELECT
            e.eraId,
            e.eraName || ' (' || e.startYear || ' a ' || e.endYear || ')' as era,
            de.name as equipe,
            COUNT(*) as vitorias
        FROM fato_resultado f
        JOIN dim_equipe de ON f.constructorId  = de.constructorId 
        JOIN dim_temporada t ON f.raceId = t.raceId
        JOIN dim_era e ON t.eraId = e.eraId
        WHERE f.position = 1
        GROUP BY e.eraId, de.constructorId 
        HAVING COUNT(*) >= (
            SELECT COUNT(*) 
            FROM fato_resultado f2
            JOIN dim_temporada t2 ON f2.raceId = t2.raceId
            WHERE f2.position = 1 AND t2.eraId = e.eraId
            GROUP BY f2.constructorId
            ORDER BY COUNT(*) DESC
            LIMIT 1 OFFSET 2
        )
        ORDER BY e.eraId, vitorias DESC;
    """
    
    df = read_dw(query)
    df = df.sort_values(["eraId", "vitorias"], ascending=[True, True])
    df = df.drop(columns=["eraId"])

    df["label"] = df["equipe"] + " (" + df["vitorias"].astype(str) + ")"
    
    ordem = df["equipe"].unique().tolist()

    fig = px.bar(
        df,
        x="era",
        y="vitorias",
        color="equipe",
        barmode="stack",
        title="Equipes Dominantes por Era",
        text="label",
        category_orders={"equipe": ordem},
        labels={"vitorias": "Vitórias", "era": "Era", "equipe": "Equipe"}
    )
    fig.update_layout(
        plot_bgcolor="#1a1a2e",
        paper_bgcolor="#1a1a2e",
        font=dict(family="Century Gothic", size=14, color="#e0e0e0"),
        title_font=dict(family="Century Gothic", size=24, color="#e0e0e0"),
        title_x=0.5,
        showlegend=False,
        xaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),      
            showgrid=False,
        ),
        yaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),
            gridcolor="#2a2a4a",       
            showgrid=True
        )
    )
    fig.update_traces(
        textposition="inside",
        textfont=dict(color="#2a2a4a", size=14),
        hovertemplate="<b>%{fullData.name}</b><br>Vitórias: %{y}<extra></extra>"
    )
    fig.show()

# Análise 7: Aproveitamento dos Pilotos (Top 20 com pelo menos 50 corridas)
def aproveitamento_pilotos():
    query = """
        SELECT 
            d.forename || ' ' || d.surname as piloto,
            COUNT(*) as corridas,
            SUM(CASE WHEN f.position = 1 THEN 1 ELSE 0 END) as vitorias,
            ROUND(100.0 * SUM(CASE WHEN f.position = 1 THEN 1 ELSE 0 END) / COUNT(*), 1) as aproveitamento
        FROM fato_resultado f
        JOIN dim_piloto d ON f.driverId = d.driverId
        GROUP BY d.driverId
        HAVING corridas >= 50
        ORDER BY aproveitamento DESC
        LIMIT 20;
    """
    
    df = read_dw(query)
    
    fig = px.treemap(
        df,
        path=["piloto"],
        values="aproveitamento",
        color="aproveitamento",
        title="Aproveitamento dos Pilotos: Corridas vs Vitórias",
        color_continuous_scale=[
            [0, "#16213e"], 
            [1, "#aa0a04"]   
        ],
        labels={"aproveitamento": "Aproveitamento (%)"}
)
    fig.update_layout(
        plot_bgcolor="#1a1a2e",
        paper_bgcolor="#1a1a2e",
        font=dict(family="Century Gothic", size=14, color="#e0e0e0"),
        title_font=dict(family="Century Gothic", size=24, color="#e0e0e0"),
        title_x=0.5,
        showlegend=False
    )
    fig.update_traces(
        textinfo="label+value",
        texttemplate="%{label}<br>%{value}%",
        hovertemplate="<b>%{label}</b><br>Aproveitamento: %{value}%<extra></extra>",
        textfont=dict(color="#ffd700", size=20)
)
    fig.show()

# Análise 8: Linha do Tempo dos Hat-Tricks (Vitória, Pole e Volta Rápida na mesma corrida) - A partir de 2004
def hat_trick_timeline():
    query = """
        SELECT
            d.forename || ' ' || d.surname as piloto,
            t.year as ano,
            t.name as corrida
        FROM fato_resultado f
        JOIN dim_piloto d ON f.driverId = d.driverId
        JOIN dim_temporada t ON f.raceId = t.raceId
        WHERE f.grid = 1
        AND f.position = 1
        AND f.rank = 1
        AND t.year >= 2004
        ORDER BY t.year ASC;
    """
    
    df = read_dw(query)

    # Conta totais e ordena do maior pro menor
    totais = df.groupby("piloto")["ano"].count().reset_index()
    totais.columns = ["piloto", "total"]
    totais = totais.sort_values("total", ascending=True)
    totais["label"] = totais["piloto"] + " (" + totais["total"].astype(str) + ")"

    # Junta label com df original
    df = df.merge(totais[["piloto", "label"]], on="piloto")

    # Força ordem das categorias
    ordem_labels = totais["label"].tolist()
    df["label"] = pd.Categorical(df["label"], categories=ordem_labels, ordered=True)

    # Jitter com seed fixo
    np.random.seed(42)
    df["y_jitter"] = df["label"].cat.codes + 1 + np.random.uniform(-0.2, 0.2, len(df))

    fig = px.scatter(
        df,
        x="ano",
        y="y_jitter",
        color="label",
        hover_data=["corrida", "label", "y_jitter"],
        title="Hat-Tricks na História da F1 (2004-2024)",
        custom_data=["corrida", "label", "ano"],

    )
    fig.update_traces(
        marker=dict(size=16),
        textposition="top center",
        textfont=dict(color="#e0e0e0", size=11),
        hovertemplate="<b>%{customdata[1]}</b><br>%{customdata[0]}<br>%{customdata[2]}<extra></extra>"

    )
    fig.update_layout(
        plot_bgcolor="#1a1a2e",
        paper_bgcolor="#1a1a2e",
        font=dict(family="Century Gothic", size=14, color="#e0e0e0"),
        title_font=dict(family="Century Gothic", size=24, color="#e0e0e0"),
        title_x=0.5,
        showlegend=False,
        xaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),
            gridcolor="#2a2a4a",
            showgrid=True,
            tickmode="linear",
            tickvals=sorted(df["ano"].unique().tolist()),
            dtick=1
        ),
        yaxis=dict(
            title_font=dict(color="#e0e0e0"),
            tickfont=dict(color="#e0e0e0", size=14),
            gridcolor="#2a2a4a",
            showgrid=True,
            tickmode="array",
            tickvals=list(range(1, len(ordem_labels) + 1)),
            ticktext=ordem_labels,
        ),
    )
    fig.show()

# Análise 9: Mapa de Vitórias de Ayrton Senna pelo Mundo (Tamanho do marcador representa número de vitórias em cada circuito)
def mapa_vitorias_senna():
    query = """
        SELECT 
            c.name as circuito,
            c.country as pais,
            c.lat,
            c.lng,
            COUNT(*) as vitorias
        FROM fato_resultado f
        JOIN dim_temporada t ON f.raceId = t.raceId
        JOIN dim_circuito c ON t.circuitId = c.circuitId
        WHERE f.position = 1
        AND f.driverId = 102
        GROUP BY c.circuitId
        ORDER BY vitorias DESC;
    """
    
    df = read_dw(query)
    
    fig = px.scatter_geo(
        df,
        lat="lat",
        lon="lng",
        size="vitorias",
        hover_name="circuito",
        hover_data={"pais": True, "vitorias": True, "lat": False, "lng": False},
        title="Vitórias de Ayrton Senna pelo Mundo",
        size_max=30,
        color="vitorias",
        color_continuous_scale="Reds"
    )
    fig.update_layout(
        paper_bgcolor="#1a1a2e",
        font=dict(family="Century Gothic", size=14, color="#e0e0e0"),
        title_font=dict(family="Century Gothic", size=24, color="#e0e0e0"),
        title_x=0.5,
        geo=dict(
            bgcolor="#1a1a2e",
            landcolor="#5858db",
            oceancolor="#97bdeb",
            showocean=True,
            showland=True,
            showcountries=True,
            countrycolor="#5858db"
        )
    )
    fig.update_traces(
        mode="markers+text",
        text=df["vitorias"],
        textposition="middle center",
        textfont=dict(color="#1a1a2e", size=16),
        hovertemplate="<b>%{hovertext}</b><br>Vitórias: %{marker.size}<extra></extra>"
    )
    fig.show()


if __name__ == "__main__":
    top_vitorias()
    top_podios()
    top_poles()
    top_volta_rapidas()
    dominacao_era_piloto()
    dominacao_era_equipe()
    aproveitamento_pilotos()
    hat_trick_timeline()
    mapa_vitorias_senna()