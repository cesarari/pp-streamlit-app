import pandas as pd
df1=pd.read_csv("datos/julio/Datos-completos-2016-2020-ordinario.csv",sep=',')

#reemplazamos los nan por 0
df1 = df1.fillna(0)


cols= df1.columns

for col in cols:
    #convertimos las columans a numeros.  A veces vienen como strings 
    df1[col] = df1[col].astype(float)
    

#ahora dividimos las columnas de inversion por la poblacion
df1.iloc[:,17:]  = df1.iloc[:,17:].div(df1.Poblacion, axis=0) 



def load_dataframe(name):


    #diferentes posiblidades para escoger el dataframe:

    #aqui escogemos solo un indice y eliminamos los otros del dataframe

    #ingreso per capita
    df_ingreso   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida"])



    #percepcion de la calidad de vida
    df_cal_vida   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion",
                            "Ind Ingreso per-capita"])


    #recreacion
    df_recre   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])


    #trabajo
    df_trabajo   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])


    #salud
    df_salud   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])


    #vulnerabilidad
    df_vuln   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])


    #libertada y seguridad
    df_segur   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])


    #participacion
    df_part   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])



    #indice de capital fisico
    df_cap_fis   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])

    #indice de movilidad    
    df_mov   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])
    #indice de desescolarizacion
    df_desesc   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                            "Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])


    #medio ambiente
    df_medio   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Servicios publicos",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])

    #servicios publicos
    df_serv   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Escolaridad","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])
    #entorno de la vivienda
    df_vivi   = df1.drop(columns=["Poblacion","IMCV","Ind Escolaridad","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])
    #escolaridad
    df_esc   = df1.drop(columns=["Poblacion","IMCV","Ind Entorno de la vivienda","Ind Servicios publicos","Ind Medio ambiente",
                             "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
                            "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
                            "Ind Ingreso per-capita"])

    
    def func(name):
            return {
            "Ind Escolaridad": df_esc,
            "Ind Entorno de la vivienda": df_vivi,
            "Ind Servicios publicos": df_serv,
            "Ind Medio ambiente": df_medio,
            "Ind Desescolarizacion": df_desesc,
            "Ind Movilidad": df_mov,
            "Ind Capital fisico": df_cap_fis,
            "Ind Participacion": df_part,
            "Ind Libertad y seguridad": df_segur,
            "Ind Vulnerabilidad": df_vuln,
            "Ind Salud": df_salud,
            "Ind Trabajo": df_trabajo,
            "Ind Recreacion": df_recre,
            "Ind Percepcion calidad de vida": df_cal_vida,
            "Ind Ingreso per-capita": df_ingreso
            
            }.get(name,df_esc)

    return func(name)
