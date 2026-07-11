# Bank Marketing – Proyecto Integrado MCDI501
### Magíster en Ciencia de Datos e Inteligencia Artificial – Universidad Andrés Bello
**MCDI501: Estadística Computacional para la Toma de Decisiones**

---

## Integrantes
| Nombre | Rol |
|---|---|
| José Miguel Serrano | Integrante |
| Jesús Fernández Urbaneja | Integrante |
| Osvaldo Rodrigo Moncada Peralta | Integrante |
| Evelyn Andrea Andrade Cárdenas | Integrante |

**Docente:** Jean Paul Maidana González | **Fecha:** 25/06/2026

---

## Descripción del proyecto

Análisis completo del dataset **Bank Marketing** (UCI ML Repository, ID 222) siguiendo la progresión **S1 → S2 → S3**:

- **Objetivo:** predecir qué clientes suscribirán un depósito a plazo en campañas de marketing telefónico
- **Dataset:** `bank.csv` · 4.521 registros × 17 variables · tasa de conversión: 11.5%
- **Variable objetivo:** `y` (yes/no)

---

## Estructura del repositorio

```
formativa1-bank-marketing/
├── S1/
│   ├── bank.csv
│   └── Sumativa_Fase2_BankMarketing.ipynb    # S1: EDA + Inferencia
├── S2/
│   ├── Sumativa_Fase3_Remuestreo_Simulacion.ipynb  # S2: Bootstrap + Monte Carlo
│   └── resultados_validados.csv
├── S3/
│   └── S3_Sumativa3_BankMarketing.ipynb      # S3: Imputación + Regresión Logística
├── informes/
│   ├── Sumativa_Fase2_BankMarketing.pdf
│   └── S3_Informe_Final_BankMarketing.pdf
├── .gitignore
└── README.md
```

---

## Cómo ejecutar

```bash
pip install numpy pandas matplotlib seaborn scipy scikit-learn
```

Ejecutar en orden: S1 → S2 → S3. S3 lee `S1/bank.csv` y `S2/resultados_validados.csv`.

---

## Progresión S1 → S2 → S3

| Fase | Contenido | Aporte a la siguiente |
|---|---|---|
| **S1** | EDA, IC Wilson, pruebas hipótesis | poutcome (V=0.293), contact (V=0.139) como predictores clave; duration excluida |
| **S2** | Bootstrap 10k, Monte Carlo, jackknife | poutcome estable IC=[0.247,0.338]; +276 suscriptores/500 llamadas priorizando poutcome=success |
| **S3** | Imputación regresión, logística 3 modelos, bootstrap coeficientes | AUC=0.68, Recall=0.67; contact y previous los coeficientes más estables |

---

## Resultados principales S3

| Modelo | AUC | F1 | Recall |
|---|---|---|---|
| M1 S1/S2 informado (seleccionado) | 0.6776 | 0.2889 | 0.6667 |
| M2 L2-Ridge | 0.6767 | 0.2782 | 0.6474 |
| M3 L1-Lasso | 0.6762 | 0.2748 | 0.6474 |

**Coeficientes estables (bootstrap):** contact (OR=0.65), previous (OR=1.48), campaign (OR=0.77), housing (OR=0.79), loan (OR=0.79)

**Imputación pdays:** MNAR, imputación por regresión (E3) seleccionada — preserva correlaciones de S2 y mantiene n=4.521.

---

## Recomendaciones de negocio

1. Priorizar clientes con **poutcome=success** (64.3% de tasa de conversión)
2. **Registrar el canal de contacto** — unknown reduce la tasa a 4.6%
3. No persistir con muchos contactos: cada uno adicional reduce odds 23% (OR=0.77)
4. Historial previo positivo aumenta odds 48% (OR=1.48)

---

**Fuente dataset:** [UCI ML Repository – Bank Marketing (ID 222)](https://archive.ics.uci.edu/dataset/222/bank+marketing) · Licencia CC BY 4.0
