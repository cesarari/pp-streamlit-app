# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:30:52 2021

@author: cesar
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joblib
from PIL import Image
import time
from utilidades import *
import seaborn as sn





with st.sidebar:

    st.markdown("""<h1 style='text-align: left; color: black;'>
       Navegación
        </h1>""", unsafe_allow_html=True)




    my_button = st.sidebar.radio("Ir a la opcion", ('Presentación del modelo','Dimensión de contexto', 'Estrategias (Modelo)',
        'Dimensión de Gestión','Comentarios')) 

   
data=pd.read_csv("datos/datos_2018.csv",sep=',')
numeros = data['Numero'].values #numeros de las comunas:  ejemplo: Popular = 1, Altavista = 70
comunas = data['Comuna'].values #nombres de las comunas
df_comunas = data[['Numero','Comuna']]


if(my_button=='Presentación del modelo'):
    st.markdown("""<h1 style='text-align: left; color: blue;'>
        Cualificando la Participación
        </h1>""", unsafe_allow_html=True)
    st.text("")
    st.text("")
    st.text("")

    image = Image.open('imagenes/portada-app.png')
    st.image(image)    
    st.markdown("""<h3 style='text-align: left; color: black;'>
        Este es aplicación web contine un modelo de machine learning que explora la conexión 
        entre las inversiones de las distintas dependencias de presupuesto participativo o presupuesto ordinario
        y los componentes del índice de calidad de vida.  Esto
        con la intención de que se pueda reconocer la influencia de las variables unas sobre otras.
        </h3>""", unsafe_allow_html=True)

    st.markdown("""<h3 style='text-align: left; color: black;'>
        La aplicación tambén permite visualizar los montos actuales de las inversiones  en las
        dependencias y el estado de las componentes del índice de calidad de vida.  Esto permite identificar
        las necesidades y a dónde se está enfocando el presupuesto.  Esta opción se encuentra en el panel 
        izquierdo con la etiqueta:  Dimensión de contexto. 
        </h3>""", unsafe_allow_html=True)

    st.markdown("""<h3 style='text-align: left; color: black;'>
        En el panel izquierdo se encontrarán también otras opciones para analizar los datos de inversiones.
        </h3>""", unsafe_allow_html=True)





if(my_button=='Dimensión de contexto'):

    st.markdown("""<h4 style='text-align: left; color: black;'>
        Aquí se puede explorar el estado de las componentes del
        índice de calidad de vida.  Así se pueden identificar las
        principales necesidades de la comuna de interes.
        Para esto, seleccione el número de la comuna en la barra izquierda.
        Si no conoce el número de la comuna de interes, consultelo en tabla 
        que aparece en el panel izquierdo.
        </h4>""", unsafe_allow_html=True)


    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    
  
    df_ind=pd.read_csv('datos/datos_2018_Indices_limpios.csv',sep=',')
    df_inv=pd.read_csv('datos/datos_2018_InversionesPP_per_capita_limpios.csv',sep=',')
    df_vot=pd.read_csv('datos/votos_2018_limpios.csv',sep=',')

    with st.sidebar:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        num_comuna=st.number_input(label="Número de la comuna de interes",
            format="%d",help='Ingrese el número de la cumuna.  Puede consultarlo en la tabla de abajo',value=1,max_value=90,
            min_value=1)

        image = Image.open('imagenes/comunas.png')
        st.image(image,width=200)    


       
  
    #seleccionamos una comuna en particular
    index = np.where(numeros==num_comuna)

    row=df_ind.iloc[index[0][0],3:]

    cols=row.keys()
    values=row.values

    indices = np.argsort(values)

    col1,col2=st.beta_columns(2)
    with col1:

        st.write(""" #####        Con esta gráfica podemos identificar las principales necesidades de la comuna""")
        st.text("")
        st.text("")

        fig,ax=plt.subplots(1,1,figsize=(7,9))
        plt.title('Componentes del indice de calidad de vida',fontsize=20)

        plt.barh(range(len(indices)), values[indices], color='b', align='center')
        plt.yticks(range(len(indices)), [cols[i] for i in indices])
        plt.xlabel('Valor del indice',fontsize=18)
        st.pyplot(fig)

    
    row=df_inv.iloc[index[0][0],3:]

    cols=row.keys()
    values=row.values

    indices = np.argsort(values)

    with col2:

        st.write(""" ##### Con esta gráfica podemos ver en que dependencias se ha invertido más en PP""")
        #st.markdown("""<h3 style='text-align: center; color: black;'>
        #    Con esta grafica podemos ver en que dependencias se ha invertido mas
        #    </h3>""", unsafe_allow_html=True)
        st.text("")
        st.text("")

   

        fig,ax=plt.subplots(1,1,figsize=(7,9))
        plt.title('Inversiones per capita por dependencia',fontsize=20)

        plt.barh(range(len(indices)), values[indices], color='r', align='center')
        plt.yticks(range(len(indices)), [cols[i] for i in indices])
        plt.xlabel('Inversion per capita (en pesos)',fontsize=18)
        st.pyplot(fig)





    row=df_vot.iloc[index[0][0],3:]

    cols=row.keys()
    values=row.values

    indices = np.argsort(values)

    with col1:
        st.text("")
        st.text("")
        st.text("")

        st.write(""" ##### Con esta gráfica podemos ver por cuales dependencias se vota más en PP""")
        #st.markdown("""<h3 style='text-align: center; color: black;'>
        #    Con esta grafica podemos ver en que dependencias se ha invertido mas
        #    </h3>""", unsafe_allow_html=True)
        st.text("")

   

        fig,ax=plt.subplots(1,1,figsize=(7,9))
        plt.title('Votos por dependencia',fontsize=20)

        plt.barh(range(len(indices)), values[indices], color='g', align='center')
        plt.yticks(range(len(indices)), [cols[i] for i in indices])
        plt.xlabel('Total de votos',fontsize=18)
        st.pyplot(fig)
    





    


 

    
    
    




if(my_button=='Estrategias (Modelo)'):
    st.write("""
 
         
         """   
         )

    st.markdown("""<h4 style='text-align: left; color: black;'>
        Este es un modelo de Machine Learning que explora la conexión
        entre las inversiones en las distintas dependencias de presupuesto ordinario y
        los componentes del índice de calidad de vida.
        En el panel izquierdo puedes escoger una componente del índice de calidad de vida que quieras analizar.
        El modelo toma la componente que hayas escogido y la clasifica como perteneciente a un nivel 1, 2 ó 3,
        que corresponde a bajo, medio o alto respectivamente (gráfica roja).  El modelo también muestra en la gráfica azul cuáles dependencias fueron
        más importantes a la hora de hacer esta clasificación y una gráfica de correlaciones (a la derecha) entre las inversiones y el valor del índice 
        escogido. 
        </h4>""", unsafe_allow_html=True)

    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    col1,col2=st.beta_columns([4,3])

    my_button2 = st.sidebar.radio("Escoge un índice para analizar",("Ind Escolaridad","Ind Entorno de la vivienda","Ind Servicios publicos","Ind Medio ambiente",
           "Ind Desescolarizacion","Ind Movilidad","Ind Capital fisico","Ind Participacion","Ind Libertad y seguridad",
           "Ind Vulnerabilidad","Ind Salud","Ind Trabajo","Ind Recreacion","Ind Percepcion calidad de vida",
           "Ind Ingreso per-capita"))
    
    df = load_dataframe(my_button2)
    features=df.drop(columns=[my_button2]).columns


    yy=df[my_button2]
    m=yy.mean()
    s=yy.std()


    def f(row,m,s):
        if row[my_button2] < m:
            val = 1
        else:
            val = 2
        return val

    df[my_button2] = df.apply(f,args=(m,s), axis=1)
    

    with col2:
        corrMatrix = df.corr() #matriz de correlaciones
        x = corrMatrix[[my_button2]]
        fig,ax=plt.subplots(1,1,figsize=(1,6))
        plt.title('Correlaciones con el %s'%my_button2,fontsize=15)
        sn.heatmap(x, annot=True,cmap='coolwarm')
        st.pyplot(fig)


    
    nombres_modelos= ["escolaridad","vivienda","servicios","ambiente",
           "desescolarizacion","movilidad","capital_fisico","participacion","seguridad",
           "vulnerabilidad","salud","trabajo","recreacion","calidad_de_vida",
           "ingreso"]


    with col1:

        #con esta funcion escojemos el nombre del modelo de acuerdo al nombre del indice
        def func(indice):
            return {
            "Ind Escolaridad": nombres_modelos[0],
            "Ind Entorno de la vivienda": nombres_modelos[1],
            "Ind Servicios publicos": nombres_modelos[2],
            "Ind Medio ambiente": nombres_modelos[3],
            "Ind Desescolarizacion": nombres_modelos[4],
            "Ind Movilidad": nombres_modelos[5],
            "Ind Capital fisico": nombres_modelos[6],
            "Ind Participacion": nombres_modelos[7],
            "Ind Libertad y seguridad": nombres_modelos[8],
            "Ind Vulnerabilidad": nombres_modelos[9],
            "Ind Salud": nombres_modelos[10],
            "Ind Trabajo": nombres_modelos[11],
            "Ind Recreacion": nombres_modelos[12],
            "Ind Percepcion calidad de vida": nombres_modelos[13],
            "Ind Ingreso per-capita": nombres_modelos[14]
            
        }.get(indice,nombres_modelos[0])


        modelo='./modelos_3_niveles/'+func((my_button2))+'.joblib'
        loaded_clf = joblib.load(modelo)
    

 



        importances = loaded_clf.feature_importances_
        indices = np.argsort(importances)

        fig2,ax2=plt.subplots(1,1,figsize=(7,9))
        plt.rcParams["figure.figsize"] = (7, 9)
        plt.title('Importancia de variables para el %s'%my_button2,fontsize=20)

        plt.barh(range(len(indices)), importances[indices], color='b', align='edge')
        plt.yticks(range(len(indices)), [features[i] for i in indices])
        plt.xlabel('Importancia relativa')
        xtics=[0,0.05,0.1,0.15]
        ax2.set_xticks(xtics)
        st.pyplot(fig2)




    with st.sidebar:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        num_comuna=st.number_input(label="Número de la comuna de interés",
            format="%d",help='Número de la comuna entre 1 y 80',value=10,max_value=80,
            min_value=1)


        index = np.where(numeros==num_comuna)


        attrib = []
        st.text("")
        st.text("")
        st.text("")


    with col1:
         
          df_dependencias=pd.read_csv('principales_dependencias_3_niveles/'+func((my_button2))+'.csv',sep=',')




       
          dep0=df_dependencias['dependencia0'].values
          dep1=df_dependencias['dependencia1'].values
          dep2=df_dependencias['dependencia2'].values
          lista = [dep0[0],dep1[0],dep2[0]]

   
          
          x_train3 = df[lista].values
          y_train3 = df.iloc[:,0]


          df_tmp = df[lista]

          row=df_tmp.iloc[index[0][0],:]

          cols=row.keys()

   

          from sklearn.preprocessing import StandardScaler
          scaler = StandardScaler().fit(x_train3)


          # load, no need to initialize the loaded_rf
          loaded_clf2 = joblib.load("./modelos_3_dependencias_3_niveles/"+func((my_button2))+".joblib")
    
          #y3 = y_train3[index[0][0]]
          
          #st.write(y_train3)


          df_tmp=df.loc[index[0][0],lista]

          st.text("")
          st.text("")
          st.text("")


          st.write("#### Predicción del índice a partir de las inversion per capita por dependencia")
          for i in range(len(cols)):
            name=cols[i]

            var=st.number_input(label=name,format="%d",value=int(df_tmp[name]),max_value=int(4*df_tmp[name].max()),min_value=0)
            attrib.append(var)

          

          x_test = df_tmp.values.reshape(1,-1)

          for i in range(len(cols)):
            x_test[0][i]=attrib[i]
   

    
          y1 = loaded_clf2.predict(x_test)

          st.text("")    
          st.text("") 
          st.text("") 
          st.text("")    
          st.text("")
         
          st.write("### El nivel del %s predicho para la comuna %d es =   %d "%(my_button2,num_comuna,y1))
  
          fig,ax=plt.subplots(1,1,figsize=(3,0.1))
          plt.xlim(0,3)
    
          xtics=[1,2,3]
          ax.set_xticks(xtics)
    
          ax.set_yticks([])
          plt.barh(1, y1, color='b', align='center')

          st.pyplot(fig)

    
    x_train2 = df.iloc[:,1:].values
    y_train2 = df.iloc[:,0]
    
    y = y_train2[index[0][0]]
  





    st.text("")    
    st.text("") 
    st.text("") 
    st.text("")    
    st.text("") 
    st.text("") 



    
if(my_button=='Comentarios'):

    st.markdown('<h3>Puedes dejarnos tu comentario</h3>', unsafe_allow_html=True)

    col1,col2=st.beta_columns(2)



    df = pd.read_csv('comentarios.csv')

    with col1:
        name=st.text_input("nombre")
        mail=st.text_input("email")

    comment=st.text_input("comentario")
    clickSubmit = st.button('Enviar')
    
    if clickSubmit == True and name and mail and comment :

        d = {'nombre': name, 
            'email': mail,
            'comentario': comment}

        

        st.markdown('<h3>¡Gracias por tu comentario!</h3>', unsafe_allow_html=True)
        df=df.append(pd.DataFrame(d,index=[0]))

        open('comentarios.csv', 'w').write(df.to_csv())

    elif clickSubmit and not ( name or mail or comment) :
        st.markdown('<h3>Por favor llena los campos</h3>', unsafe_allow_html=True)




if(my_button=='Dimensión de Gestión'):
    
    st.markdown("""<h4 style='text-align: left; color: black;'>
    El índice de gestión mide la relación que existe entre las necesidades de cada territorio y las 
    inversiones en líneas estratégicas del PDL.    
        </h4>""", unsafe_allow_html=True)


    st.text("")    
    st.text("") 
    st.text("") 
    st.text("")    
    st.text("") 
    st.text("") 


    col1,col2=st.beta_columns([3,4])

    with col2:

        df=pd.read_csv("datos/julio/Datos-gestion.csv",sep=',')
        comunas = df['Comuna'].values
        calificacion =  df['Calificacion'].values
        indice = df['Indice'].values
        valores_indices=['Baja','Media-baja','Media-alta','Alta']
 
        fig,ax=plt.subplots(1,1,figsize=(7,9))
        #plt.figure(figsize=(7,9))
        plt.title('Indice de Gestion')

        plt.barh(range(len(comunas)),indice, color='b', align='center')
        plt.yticks(range(len(indice)), [comunas[i] for i in range(len(indice)) ])
        plt.xticks(range(len(valores_indices)), [valores_indices[i] for i in range(len(valores_indices)) ])
        plt.xlabel('Indice')
        st.pyplot(fig)

    with col1:

        st.markdown("""<h5 style='text-align: left; color: black;'>
        Este índice tiene 4 posibles niveles:  Bajo, medio-bajo, medio-alto y alto.
        Para calcular el nivel del índice se miran cuáles son las 3 líneas del PDL que reciben mayor
        inversión y también cuáles son las necesidades más apremiantes de la comuna, de acuerdo a la 
        encuesta de calidad de vida.  Si las líneas de mayor inversión convuerdan con las necesidades más
        apremiantes de la comuna, se tiene un índice de gestión alto.  Si ninguna línea de inversión concuerda
        con las necesidades más apremiantes de la comuna se tiene un índice de gestión bajo.    
        </h5>""", unsafe_allow_html=True)
        


    
    
    



