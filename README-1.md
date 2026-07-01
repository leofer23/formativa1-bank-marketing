# Bank Marketing – Análisis Exploratorio e Inferencial
### MCDI501: Estadística Computacional para la Toma de Decisiones
**Magíster en Ciencia de Datos e Inteligencia Artificial – Universidad Andrés Bello**

---

## Integrantes
| Nombre | Rol |
|---|---|
| José Miguel Serrano | Integrante |
| Jesús Fernández Urbaneja | Integrante |
| Osvaldo Rodrigo Moncada Peralta | Integrante |
| Evelyn Andrea Andrade Cárdenas | Integrante |

**Docente:** Jean Paul Maidana González  
**Fecha:** 25/06/2026

---

## Descripción del proyecto

Análisis exploratorio e inferencial del dataset **Bank Marketing** (UCI ML Repository, ID 222).  
El dataset contiene información de campañas de marketing directo de un banco portugués (mayo 2008–noviembre 2010).  
**Objetivo:** identificar qué características del cliente y la campaña se asocian a mayor probabilidad de suscripción a un depósito a plazo.

- **Dataset:** `bank.csv` (versión reducida 10%, 4.521 registros × 17 variables, separador `;`)
- **Variable objetivo:** `y` — ¿suscribió depósito a plazo? (yes/no)
- **Tasa de conversión real:** 11.5% (521 de 4.521 clientes)

---

## Estructura del repositorio

```
formativa1-bank-marketing/
├── bank.csv                              # Dataset original (sep=';')
├── Sumativa_Fase2_BankMarketing.ipynb    # Notebook principal (Sumativa Fase 2)
├── Sumativa_Fase2_BankMarketing.pdf      # Informe técnico PDF (8 páginas)
├── Formativa1_BankMarketing_MCDI501.pdf  # Informe Formativa 1
└── README.md
```

---

## Cómo ejecutar el notebook

### Requisitos
```bash
pip install numpy pandas matplotlib seaborn scipy
```

### Ejecución
```bash
# Asegúrese de que bank.csv está en el mismo directorio que el notebook
jupyter notebook Sumativa_Fase2_BankMarketing.ipynb
```

> **Nota:** ejecutar todas las celdas en orden (Run All). El notebook genera automáticamente todas las figuras.

---

## Contenido del análisis (Sumativa Fase 2)

### 1. Calidad de datos
- 0 valores nulos · 0 duplicados
- Variables asimétricas (balance, duration, campaign, previous) se reportan por **mediana**
- `pdays = -1` codifica ausencia de contacto previo (82.0% de registros)
- `duration` **no se usa como predictor** (solo disponible al finalizar el contacto)

### 2. Estadística descriptiva (ID1.2)
- Medidas de tendencia central y dispersión para 6 variables numéricas
- Frecuencias absolutas y relativas para 9 variables categóricas
- Histogramas con mediana como referencia (variables asimétricas)
- Boxplots segmentados por variable objetivo

### 3. Análisis bivariado
- Matriz de correlaciones de Pearson
- Tasas de suscripción por 6 variables categóricas
- Gráficos de dispersión por resultado

### 4. Estimación puntual e IC al 95% (ID1.3)
- IC para medias: distribución **t de Student** (σ desconocida)
- IC para proporciones: método de **Wilson** (más robusto que aproximación normal)
- Parámetros estimados: μ(age), μ(balance), μ(duration), μ(campaign), π(y=yes), π(housing=yes), π(loan=yes), π(y=yes|cellular), π(y=yes|poutcome=success)

### 5. Pruebas de hipótesis (ID1.4)

| # | Prueba | Variables | Estadístico | p-valor | Efecto |
|---|---|---|---|---|---|
| 1 | Chi-cuadrado | poutcome vs y | χ²=386.88, gl=3 | <0.0001 | V=0.293 moderado |
| 2 | Chi-cuadrado | contact vs y | χ²=87.87, gl=2 | <0.0001 | V=0.139 pequeño |
| 3 | Mann-Whitney U | balance por y | U=1.190.770 | <0.0001 | d=0.061 pequeño |

- **Prueba 1:** poutcome=success → 64.3% de tasa de suscripción (vs 9.1% en unknown)
- **Prueba 2:** contact=unknown → solo 4.6% (vs ~14.5% en canales identificados)
- **Prueba 3:** No paramétrica (normalidad rechazada). Efecto pequeño; mediana yes=€710 vs no=€420

---

## Hallazgos principales

1. **poutcome=success** es el predictor más potente (64.3% vs 9.1%, V=0.293)
2. **contact=unknown** reduce drásticamente la conversión (4.6%) — registrar el canal es crítico
3. **balance** tiene diferencia significativa pero efecto pequeño (d=0.06) — leer por mediana
4. **duration** NO se usa como predictor (conocida solo al finalizar el contacto)
5. **Desbalance de clases** 88.5/11.5% — requiere tratamiento en modelado (SMOTE, class_weight)

---

## Dataset
- **Fuente:** UCI Machine Learning Repository — [Bank Marketing Dataset (ID 222)](https://archive.ics.uci.edu/dataset/222/bank+marketing)
- **Referencia:** Moro, S., Rita, P., & Cortez, P. (2014). A data-driven approach to predict the success of bank telemarketing. *Decision Support Systems, 62*, 22–31.
- **Licencia:** CC BY 4.0
