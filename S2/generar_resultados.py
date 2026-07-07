import pandas as pd

resultados_validados = pd.DataFrame({
    "parametro": [
        "media_age",
        "media_balance",
        "media_campaign",
        "mediana_balance",
        "mediana_duration",
        "cohen_d_duration",
        "cramer_v_poutcome"
    ],
    "estimacion": [
        41.170,
        1422.658,
        2.794,
        444.0,
        185.0,
        1.3711,
        0.2925
    ],
    "ic_bootstrap_low": [
        40.720,
        1355.130,
        2.696,
        420.0,
        179.0,
        1.2318,
        0.2472
    ],
    "ic_bootstrap_high": [
        41.620,
        1493.870,
        2.897,
        474.0,
        192.0,
        1.5165,
        0.3381
    ],
    "metodo": [
        "bootstrap percentil",
        "bootstrap percentil",
        "bootstrap percentil",
        "bootstrap percentil",
        "bootstrap percentil",
        "bootstrap percentil (por grupo)",
        "bootstrap percentil (remuestreo de filas)"
    ],
    "estabilidad": [
        "robusto",
        "robusto",
        "robusto",
        "robusto",
        "robusto",
        "robusto",
        "robusto - efecto mas fuerte del estudio"
    ]
})

resultados_validados.to_csv("S2/resultados_validados.csv", index=False)
print("Archivo generado: S2/resultados_validados.csv")
print(resultados_validados)
