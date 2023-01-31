# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 23:15:45 2022
@author: Maloa
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
import psycopg2
import re
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
warnings.warn('InsecureRequestWarning')
warnings.warn('Do not show this message')


BD=[]

NombreDeBaseDatos = "LINKS_GRUPOS.xlsx"
dfgrupos = pd.read_excel(NombreDeBaseDatos, sheet_name='Hoja1', engine='openpyxl')
tamaño_dfgrupos =dfgrupos.shape
links = dfgrupos["LINKS"]
ident = dfgrupos["ID"]

for j in range(0,5): #len(links)
    
    x=ident[j]
    link=links[j]
    
    try:
        print("link numero ",j,"'",links[j],"'") 
        r = requests.get(links[j], verify=False)
        soup = BeautifulSoup(r.text, 'lxml')
        
        NomGrupo = soup.find("span", class_='celdaEncabezado')
        NombreGrupo = NomGrupo.text
        
        #Filtrar todas las tablas
        table = soup.find_all('table')
        
        
        dfconsolidado = pd.DataFrame()
        dfconsolidado["Nombre del Grupo"] = [NombreGrupo]
        
        
        json ='{"Grupo":{"Nombre":"'+NombreGrupo+'","DatosBasicos":{'
        datos = pd.read_html(str(table))[0]
        for i in range(10):
            json=json+'"'+str(datos[0][i+1])+'":"'+str(datos[1][i+1])+'",'
    
        json = json[:-1]+'},'
        
        for i in range (1,85,1):
          print("---------------------. ",i)
          if (i==4 or i==26 or i==45 or i==46 or i==50 or i==76 or i==80):
              pass
          elif(i<13):
              A = pd.read_html(str(table))[i]
              json = json+'"'+A[0][0]+'":{'
              for i in range(len(A)):
                  A[0][i]=A[0][i].replace('"'," ")
                  A[0][i]=A[0][i].replace("'"," ")
                  A[0][i]=re.sub('\W+',' ',A[0][i]).strip()
                  json=json+'"'+str(i)+'":"'+str(A[0][i])+'",'
              json = json[:-1]+'},'
          else:
              A = pd.read_html(str(table))[i]
              json = json+'"'+A[0][0]+'":{'
              for i in range(len(A)):
                  A[1][i]=A[1][i].replace('"'," ")
                  A[1][i]=A[1][i].replace("'"," ")
                  A[1][i]=re.sub('\W+',' ',A[1][i]).strip()
                  json=json+'"'+str(i)+'":"'+str(A[1][i])+'",'
              json = json[:-1]+'},'  
        
        json = json[:-1]+'}}'
        BD.append(json)
        
        
    except:
        pass
    try:
        
        
        ####    BASES DE DATOS ###
        
        conn=psycopg2.connect(
            host="localhost",
            user="postgres",
            password="Piraka7895123",
            database="postgres",
            port="5432"
        )
        
        cur = conn.cursor()
        
        #cur.execute("INSERT INTO ctei (id,grupos) VALUES ("+str(x)+",'"+  json +"')")
        #cur.execute("INSERT INTO mc (id,link,info) VALUES ("+str(x)+", wwwwww ,'"+  json +"')")
        cur.execute("insert into mc (id,info,link) values ("+str(x)+",'"+json+"','"+str(link)+"')")
        
        conn.commit()
        cur.close()
        conn.close()
       
        
    except:
        
        print("Error en ", j)

# READ JSON ONLINE https://jsoneditoronline.org/#left=local.tuzohe&right=local.moyefe