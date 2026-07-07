import nbformat
path = "S2/Sumativa_Fase3_Remuestreo_Simulacion.ipynb"
nb = nbformat.read(path, as_version=4)
for cell in nb.cells:
    if 'pd.read_csv("bank.csv"' in cell.source:
        cell.source = cell.source.replace(
            'df = pd.read_csv("bank.csv", sep=";")',
            'df = pd.read_csv("../S1/bank.csv", sep=";")  # ruta actualizada tras reorganizar en S1/S2'
        )
        print("Celda corregida.")
nbformat.write(nb, path)
print("Guardado OK.")
