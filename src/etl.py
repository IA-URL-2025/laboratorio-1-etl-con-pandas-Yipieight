import pandas as pd

def run_etl():

    df = pd.read_csv("data/citas_clinica.csv")
    
    df["paciente"] = df["paciente"].str.title() 
    df["especialidad"] = df["especialidad"].str.upper() 
    
    df["fecha_cita"] = pd.to_datetime(df["fecha_cita"], errors="coerce")
    df = df.dropna(subset=["fecha_cita"])
    
    df = df[df["estado"] == "CONFIRMADA"]
    df = df[df["costo"] > 0]
    
    df["telefono"] = df["telefono"].fillna("NO REGISTRA")
    
    df["fecha_cita"] = df["fecha_cita"].dt.strftime("%Y-%m-%d")
    
    df.to_csv("data/output.csv", index=False)


if __name__ == "__main__":
    run_etl()
