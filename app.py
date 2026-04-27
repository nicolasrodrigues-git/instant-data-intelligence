import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ─── CONFIG ─────────────────────────────────────────────────────
st.set_page_config(
    page_title="Instant Data Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── VISUAL IDENTITY ────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }

.stApp {
    background: linear-gradient(160deg, #e8f0fe 0%, #f0f4ff 40%, #dce8fd 70%, #eaf1ff 100%) !important;
    min-height: 100vh;
}

[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.55) !important;
    backdrop-filter: blur(24px) !important;
    -webkit-backdrop-filter: blur(24px) !important;
    border-right: 1px solid rgba(99,146,255,0.18) !important;
}
[data-testid="stSidebar"] * { color: #2d3a5e !important; }

#MainMenu, footer, header { visibility: hidden; }

[data-testid="collapsedControl"] { display: block !important; visibility: visible !important; }
section[data-testid="stSidebar"] { display: flex !important; visibility: visible !important; width: 21rem !important; }

[data-testid="metric-container"] {
    background: rgba(255,255,255,0.65) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid rgba(99,146,255,0.2) !important;
    border-radius: 16px !important;
    padding: 20px !important;
    box-shadow: 0 4px 24px rgba(60,100,220,0.08), inset 0 1px 0 rgba(255,255,255,0.8) !important;
    text-align: center !important;
}
[data-testid="metric-container"] label {
    color: #7b93c8 !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #1a2f6e !important;
    font-size: 28px !important;
    font-weight: 700 !important;
}

.stButton > button {
    background: rgba(255,255,255,0.6) !important;
    color: #2546a0 !important;
    border: 1px solid rgba(99,146,255,0.35) !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 10px 20px !important;
    backdrop-filter: blur(10px) !important;
    transition: all .2s !important;
}
.stButton > button:hover {
    background: rgba(255,255,255,0.85) !important;
    border-color: rgba(99,146,255,0.6) !important;
}

.stDownloadButton > button {
    background: rgba(255,255,255,0.5) !important;
    color: #2546a0 !important;
    border: 1px solid rgba(99,146,255,0.3) !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    backdrop-filter: blur(10px) !important;
    transition: all .2s !important;
    width: 100% !important;
}
.stDownloadButton > button:hover { background: rgba(255,255,255,0.8) !important; }

[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.4) !important;
    border: 1.5px dashed rgba(99,146,255,0.4) !important;
    border-radius: 12px !important;
    padding: 4px !important;
}
[data-testid="stFileUploader"] * { color: #3a55a0 !important; }

.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.5) !important;
    border-radius: 12px !important;
    padding: 4px !important;
    border: 1px solid rgba(99,146,255,0.18) !important;
    backdrop-filter: blur(10px) !important;
    gap: 2px !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: 8px !important;
    color: #7b93c8 !important;
    font-weight: 500 !important;
    font-size: 13px !important;
    padding: 8px 18px !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(99,146,255,0.18) !important;
    color: #1a2f6e !important;
    font-weight: 600 !important;
}

.streamlit-expanderHeader {
    background: rgba(255,255,255,0.55) !important;
    border: 1px solid rgba(99,146,255,0.18) !important;
    border-radius: 10px !important;
    color: #2d3a5e !important;
    font-weight: 500 !important;
}

[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    border: 1px solid rgba(99,146,255,0.15) !important;
    overflow: hidden !important;
}

[data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,0.55) !important;
    border: 1px solid rgba(99,146,255,0.25) !important;
    border-radius: 8px !important;
    color: #1a2f6e !important;
}
[data-testid="stSelectbox"] label {
    color: #7b93c8 !important;
    font-size: 12px !important;
    font-weight: 500 !important;
}

.stSuccess {
    background: rgba(74,222,128,0.12) !important;
    border: 1px solid rgba(74,222,128,0.35) !important;
    border-radius: 10px !important;
}
.stAlert { border-radius: 10px !important; }

h1, h2, h3 { color: #1a2f6e !important; }
.stMarkdown p { color: #4a5e8a !important; }
</style>
""", unsafe_allow_html=True)

PLOTLY_THEME = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(255,255,255,0.3)",
    font=dict(family="Inter", color="#4a5e8a", size=12),
    margin=dict(l=20, r=20, t=40, b=20),
    colorway=["#3b6ef5", "#60a5fa", "#34d399", "#f472b6", "#fbbf24", "#a78bfa"],
)

# ─── SECURITY CONSTANTS ─────────────────────────────────────────
MAX_FILE_SIZE_MB = 50
MAX_ROWS = 500_000
FORMULA_PREFIXES = ('=', '+', '-', '@')

# ─── HELPERS ────────────────────────────────────────────────────

def sanitize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    [SECURITY] Escapa fórmulas CSV injection em colunas de texto.
    Células que iniciam com =, +, -, @ são prefixadas com ' para
    evitar execução automática em Excel/LibreOffice ao abrir o export.
    """
    def _clean(val):
        if isinstance(val, str) and val.startswith(FORMULA_PREFIXES):
            return "'" + val
        return val

    sanitized = df.copy()
    for col in sanitized.select_dtypes(include="object").columns:
        sanitized[col] = sanitized[col].map(_clean)
    return sanitized


@st.cache_data(ttl=300)
def classify_columns(df):
    numeric, categorical, date, id_like, text_free = [], [], [], [], []
    for col in df.columns:
        s = df[col].dropna()
        if s.empty:
            continue
        if s.dtype == object:
            parsed = pd.to_datetime(s.astype(str), errors="coerce")
            if parsed.notna().mean() > 0.7:
                date.append(col)
                continue
        if pd.api.types.is_numeric_dtype(s):
            if s.nunique() == len(s):
                id_like.append(col)
            else:
                numeric.append(col)
        elif s.dtype == object:
            if s.nunique() <= 30:
                categorical.append(col)
            else:
                text_free.append(col)
    return dict(numeric=numeric, categorical=categorical,
                date=date, id_like=id_like, text_free=text_free)


@st.cache_data(ttl=300)
def quality_report(df):
    return dict(
        total=len(df),
        null_cols=df.isnull().sum()[lambda x: x > 0].to_dict(),
        dupes=int(df.duplicated().sum())
    )


@st.cache_data(ttl=300)
def generate_advanced_insights(df, cols):
    insights = {}
    num_cols = cols["numeric"]
    cat_cols = cols["categorical"]
    date_cols = cols["date"]

    if num_cols:
        insights["most_variable"] = df[num_cols].var().idxmax()

    outliers = {}
    for col in num_cols[:3]:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        outliers[col] = len(df[(df[col] < q1 - 1.5*iqr) | (df[col] > q3 + 1.5*iqr)])
    insights["outliers"] = outliers

    if date_cols and num_cols:
        main_metric = df[num_cols].sum().idxmax()
        df_sorted = df.sort_values(date_cols[0])
        first = df_sorted[main_metric].iloc[0]
        last = df_sorted[main_metric].iloc[-1]
        if first != 0:
            insights["growth"] = round(((last - first) / first) * 100, 2)

    if len(num_cols) >= 2:
        corr = df[num_cols].corr()
        corr_unstack = corr.where(~np.eye(len(corr), dtype=bool)).unstack().dropna()
        if not corr_unstack.empty:
            insights["top_correlation"] = corr_unstack.abs().idxmax()

    if cat_cols and num_cols:
        cat, val = cat_cols[0], num_cols[0]
        insights["top_category"] = df.groupby(cat)[val].sum().idxmax()

    return insights


@st.cache_data(ttl=600)
def generate_sample_csv():
    import random, datetime
    random.seed(42)
    rows = []
    start = datetime.date(2024, 1, 1)
    regions = ["Sul", "Norte", "Sudeste", "Nordeste", "Centro-Oeste"]
    categories = ["SaaS", "E-commerce", "Servicos", "Consultoria"]
    for i in range(120):
        d = start + datetime.timedelta(days=i * 3)
        rows.append({
            "data": d.strftime("%Y-%m-%d"),
            "regiao": random.choice(regions),
            "categoria": random.choice(categories),
            "receita": round(random.uniform(800, 15000), 2),
            "clientes": random.randint(5, 120),
            "nps": random.randint(30, 95),
            "custo": round(random.uniform(200, 5000), 2),
        })
    return pd.DataFrame(rows).to_csv(index=False).encode("utf-8")


# ─── SIDEBAR ────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding:16px 0 28px;text-align:center'>
      <div style='font-size:26px;font-weight:700;color:#1a2f6e;letter-spacing:-0.02em'>
        📊 Instant Data Intelligence
      </div>
      <div style='font-size:12px;color:#7b93c8;margin-top:4px'>
        Instant Data Intelligence
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size:11px;font-weight:600;color:#7b93c8;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:8px;text-align:center'>Upload do arquivo</p>", unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "Arquivo",
        type=["csv", "xlsx", "xls"],
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.download_button(
        label="⬇  Baixar arquivo de exemplo",
        data=generate_sample_csv(),
        file_name="sample_datamvp.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.markdown("""
    <br>
    <div style='background:rgba(235,242,255,0.7);border:1px solid rgba(99,146,255,0.2);
                border-radius:10px;padding:12px;text-align:center;'>
      <p style='font-size:11px;color:#7b93c8;margin:0;line-height:1.6'>
        Dados processados localmente.<br>Nenhuma informacao armazenada.
      </p>
    </div>
    <br>
    <div style='text-align:center;padding-top:12px;border-top:1px solid rgba(99,146,255,0.15)'>
      <p style='font-size:11px;color:#7b93c8;margin:0 0 6px'>Dashboard customizado?</p>
      <a href='https://www.upwork.com/freelancers/~01eaec31a2c10dea5f?viewMode=1'
         target='_blank'
         style='font-size:13px;color:#3b6ef5;font-weight:600;text-decoration:none'>
        Entre em contato no Upwork
      </a>
    </div>
    """, unsafe_allow_html=True)


# ─── LOAD DATA ──────────────────────────────────────────────────
df = None

if uploaded is not None:
    # [SECURITY] Limite de tamanho em bytes
    if uploaded.size > MAX_FILE_SIZE_MB * 1024 * 1024:
        st.error(f"Arquivo muito grande (limite: {MAX_FILE_SIZE_MB}MB).")
        st.stop()

    with st.spinner("Processando dados..."):
        try:
            if uploaded.name.endswith(".csv"):
                df = pd.read_csv(uploaded)
            else:
                df = pd.read_excel(uploaded, engine="openpyxl")
        except Exception:
            st.error("Nao foi possivel ler o arquivo. Verifique se o formato e valido (CSV, XLS ou XLSX).")
            st.stop()

    # [SECURITY] Limite de linhas — proteção contra arquivos gigantes / zip bombs
    if df is not None and len(df) > MAX_ROWS:
        st.error(f"Arquivo com mais de {MAX_ROWS:,} linhas não é suportado. Reduza o dataset e tente novamente.")
        st.stop()

if df is not None and df.empty:
    st.warning("O arquivo carregado esta vazio. Envie um arquivo com dados.")
    st.stop()


# ─── HEADER ─────────────────────────────────────────────────────
st.markdown("""
<div style='padding:32px 0 16px;text-align:center'>
  <h1 style='color:#1a2f6e;font-size:38px;font-weight:700;margin:0;letter-spacing:-0.03em'>
    Instant Data Intelligence
  </h1>
  <p style='color:#7b93c8;font-size:15px;margin-top:10px;max-width:480px;
            margin-left:auto;margin-right:auto;line-height:1.6;font-weight:500'>
    Instant Data Intelligence &nbsp;·&nbsp; Upload → Analyze → Insight
  </p>
</div>
""", unsafe_allow_html=True)

# ─── EMPTY STATE ────────────────────────────────────────────────
if df is None:
    st.markdown("""
    <div style='background:rgba(255,255,255,0.55);
                backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
                border:1.5px dashed rgba(99,146,255,0.35);border-radius:20px;
                padding:80px 40px;text-align:center;margin:16px 0;
                box-shadow:0 4px 24px rgba(60,100,220,0.07),inset 0 1px 0 rgba(255,255,255,0.9)'>
      <div style='font-size:52px;margin-bottom:20px'>📂</div>
      <h2 style='color:#1a2f6e;font-weight:700;margin:0 0 10px;font-size:22px'>
        Nenhum arquivo carregado
      </h2>
      <p style='color:#7b93c8;font-size:14px;max-width:380px;margin:0 auto;line-height:1.7'>
        Use o painel lateral para fazer upload do seu CSV ou Excel.<br>
        Sem arquivo? Baixe o <strong style='color:#3b6ef5'>arquivo de exemplo</strong>.
      </p>
      <div style='margin-top:20px;font-size:13px;color:#6b85c8'>
        Formatos suportados: CSV, XLS, XLSX
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()


# ─── PROCESSAMENTO ──────────────────────────────────────────────
cols = classify_columns(df)
qr = quality_report(df)
insights = generate_advanced_insights(df, cols)
null_cols_series = pd.Series(qr["null_cols"])

num_cols = cols["numeric"]
cat_cols = cols["categorical"]
date_cols = cols["date"]


# ─── METRICS ────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Linhas", f"{qr['total']:,}")
m2.metric("Colunas", f"{len(df.columns)}")
m3.metric("Duplicatas", f"{qr['dupes']}")
if "growth" in insights:
    m4.metric("Crescimento", f"{insights['growth']}%")
else:
    m4.metric("Colunas numericas", f"{len(num_cols)}")

st.markdown("<br>", unsafe_allow_html=True)

# ─── QUALITY ────────────────────────────────────────────────────
if null_cols_series.empty:
    st.success("Dados limpos — nenhum valor nulo encontrado.")
else:
    with st.expander(f"Aviso: {len(null_cols_series)} coluna(s) com valores nulos"):
        null_df = null_cols_series.reset_index()
        null_df.columns = ["Coluna", "Nulos"]
        null_df["% do total"] = (null_df["Nulos"] / qr["total"] * 100).round(1).astype(str) + "%"
        st.dataframe(null_df, use_container_width=True, hide_index=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── INSIGHTS CARD ──────────────────────────────────────────────
st.markdown("""
<div style='background:rgba(255,255,255,0.55);backdrop-filter:blur(16px);
            -webkit-backdrop-filter:blur(16px);
            border:1px solid rgba(99,146,255,0.2);border-radius:16px;
            padding:20px 28px;margin-bottom:24px;
            box-shadow:0 4px 24px rgba(60,100,220,0.06),inset 0 1px 0 rgba(255,255,255,0.9)'>
  <p style='font-size:11px;font-weight:600;color:#7b93c8;text-transform:uppercase;
            letter-spacing:0.08em;margin:0 0 16px;text-align:center'>
    Insights Automaticos
  </p>
""", unsafe_allow_html=True)

i1, i2, i3 = st.columns(3)

if "most_variable" in insights:
    i1.metric("Mais volatil", insights["most_variable"])

if "top_category" in insights:
    i2.metric("Top categoria", str(insights["top_category"]))

if "top_correlation" in insights:
    col1, col2 = insights["top_correlation"]
    i3.metric("Top correlacao", f"{col1} × {col2}")

st.markdown("</div>", unsafe_allow_html=True)


# ─── CHARTS ─────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["Tendencias", "Distribuicoes", "Correlacoes", "Dados Brutos"])

with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    if not num_cols:
        st.info("Nenhuma coluna numerica detectada.")
    else:
        c1, c2 = st.columns([2, 1])
        with c1:
            if date_cols:
                y_sel = st.selectbox("Metrica (eixo Y)", num_cols, key="t_y")
                x_col = date_cols[0]
                agg = df.groupby(x_col)[y_sel].sum().reset_index()
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=agg[x_col], y=agg[y_sel],
                    mode="lines", fill="tozeroy",
                    line=dict(color="#3b6ef5", width=2.5),
                    fillcolor="rgba(59,110,245,0.1)",
                    name=y_sel,
                ))
                fig.update_layout(
                    title=f"{y_sel} ao longo do tempo",
                    xaxis=dict(showgrid=False, color="#7b93c8", linecolor="rgba(99,146,255,0.2)"),
                    yaxis=dict(showgrid=True, gridcolor="rgba(99,146,255,0.12)", color="#7b93c8"),
                    **PLOTLY_THEME
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                y_sel = st.selectbox("Metrica", num_cols, key="t_y2")
                fig = px.histogram(df, x=y_sel, nbins=30,
                                   title=f"Distribuicao de {y_sel}",
                                   color_discrete_sequence=["#3b6ef5"])
                fig.update_layout(**PLOTLY_THEME)
                st.plotly_chart(fig, use_container_width=True)

        with c2:
            if cat_cols and num_cols:
                cat_sel = st.selectbox("Categoria", cat_cols, key="t_cat")
                val_sel = st.selectbox("Valor", num_cols, key="t_val")
                agg2 = df.groupby(cat_sel)[val_sel].sum().reset_index().sort_values(val_sel, ascending=True).tail(8)
                fig2 = px.bar(agg2, x=val_sel, y=cat_sel, orientation="h",
                              title=f"{val_sel} por {cat_sel}",
                              color=val_sel,
                              color_continuous_scale=["rgba(59,110,245,0.2)", "#3b6ef5"])
                fig2.update_layout(**PLOTLY_THEME, showlegend=False, coloraxis_showscale=False)
                fig2.update_traces(marker_line_width=0)
                st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    if not num_cols and not cat_cols:
        st.info("Nenhuma coluna adequada para distribuicao.")
    else:
        c1, c2 = st.columns(2)
        with c1:
            if num_cols:
                sel = st.selectbox("Coluna numerica", num_cols, key="d1")
                fig = px.box(df, y=sel, title=f"Box plot - {sel}",
                             color_discrete_sequence=["#3b6ef5"])
                fig.update_layout(**PLOTLY_THEME)
                fig.update_traces(marker_color="#3b6ef5", line_color="#60a5fa")
                st.plotly_chart(fig, use_container_width=True)
        with c2:
            if cat_cols:
                sel2 = st.selectbox("Coluna categorica", cat_cols, key="d2")
                vc = df[sel2].value_counts().reset_index()
                vc.columns = [sel2, "count"]
                fig2 = px.pie(vc, names=sel2, values="count",
                              title=f"Proporcao - {sel2}",
                              color_discrete_sequence=["#3b6ef5","#60a5fa","#34d399","#f472b6","#fbbf24","#a78bfa"])
                fig2.update_layout(**PLOTLY_THEME)
                fig2.update_traces(textposition="inside", textinfo="percent+label")
                st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    if len(num_cols) < 2:
        st.info("Precisa de ao menos 2 colunas numericas para correlacao.")
    else:
        corr = df[num_cols].corr()
        fig = px.imshow(corr, text_auto=".2f", title="Mapa de Correlacao",
                        color_continuous_scale=["#eef2ff", "#3b6ef5"],
                        zmin=-1, zmax=1)
        fig.update_layout(**PLOTLY_THEME)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        cc1, cc2, cc3 = st.columns(3)
        x_s = cc1.selectbox("Eixo X", num_cols, key="sc_x")
        y_s = cc2.selectbox("Eixo Y", num_cols, index=min(1, len(num_cols)-1), key="sc_y")
        c_s = cc3.selectbox("Cor (opcional)", ["nenhuma"] + cat_cols, key="sc_c")
        fig2 = px.scatter(df, x=x_s, y=y_s,
                          color=None if c_s == "nenhuma" else c_s,
                          title=f"{x_s} x {y_s}",
                          color_discrete_sequence=["#3b6ef5","#60a5fa","#34d399","#f472b6","#fbbf24"],
                          opacity=0.7)
        fig2.update_layout(**PLOTLY_THEME)
        st.plotly_chart(fig2, use_container_width=True)

with tab4:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:600;color:#1a2f6e;text-align:center'>Previa - primeiras 100 linhas</p>", unsafe_allow_html=True)
    st.dataframe(df.head(100), use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("Estatisticas descritivas"):
        if num_cols:
            st.dataframe(df[num_cols].describe().round(2), use_container_width=True)

    # [SECURITY] CSV export sanitizado contra formula injection
    csv_export = sanitize_dataframe(df).to_csv(index=False).encode("utf-8")
    st.download_button(
        "Exportar dados tratados (CSV)",
        data=csv_export,
        file_name="datamvp_export.csv",
        mime="text/csv"
    )

# ─── FOOTER ─────────────────────────────────────────────────────
st.markdown("""
<br>
<div style='border-top:1px solid rgba(99,146,255,0.18);padding-top:20px;text-align:center'>
  <span style='font-size:12px;color:#7b93c8'>
    Instant Data Intelligence · Dados processados localmente ·&nbsp;
    <a href='https://www.upwork.com/freelancers/~01eaec31a2c10dea5f?viewMode=1'
       target='_blank'
       style='color:#3b6ef5;font-weight:600;text-decoration:none'>
      Solicitar dashboard customizado
    </a>
  </span>
</div>
""", unsafe_allow_html=True)