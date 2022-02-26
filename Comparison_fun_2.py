#====Librerias usadas==========================================================
# Manejo de datos
#import pandas as pd
#multiples data frames
#from pathlib import Path
#libreria para manejar opciones del sistema
import os
#==Funciones auxiliares========================================================
def match_name(file,loc_result,energy=False):
    if os.path.exists(loc_result)==False:
               os.mkdir(loc_result)
    if type(file)==str:
        loc_origen=loc_result+file.split('/')[1]
    else:
        loc_origen=loc_result+file[0].split('/')[1]
    if os.path.exists(loc_origen)==False:
               os.mkdir(loc_origen)
    if energy==2:
        type_energy=['H','M','L']
        n_folder=[]
        for j in range(3):
            Loc_final=loc_origen+'/'+type_energy[j]
            if os.path.exists(Loc_final)==False:
               os.mkdir(Loc_final)
            if type(file)==str:
                Folder=Loc_final+'/match_'+file.split('/')[2].replace('.csv','')
                names=file.split('/')[2].replace('.csv','')
                n_folder.append(Folder)
            else:
                Folder,names=list_file(file,Loc_final+'/')
                n_folder=n_folder+Folder
    else:
        if type(file)==str:
            n_folder=loc_origen+'/match_'+file.split('/')[2].replace('.csv','')
            names=file.split('/')[2].replace('.csv','')
        else:
            n_folder,names=list_file(file,loc_origen+'/')
    return n_folder

def list_file(file,loc_result):
    n_folder=[];names=[]
    for i in range(len(file)):
        list_file=file[i].split('/')[2]
        list_file=list_file.replace('.csv','')
        names.append(list_file)
        list_file=('match_'+list_file)                            
        n_folder.append(loc_result+list_file)
    return n_folder,names

def select_match(file_exp,file_theo):
    list_match=[]
    for i in range(len(file_exp)):
        name=file_exp[i].split('/')[1]
        origen=name.split('_')[1]
        origen=origen.replace('.csv','')
        for k in range(len(file_theo)):
            if origen in file_theo[k]:
                list_match.append([file_theo[k],file_exp[i],name.replace('.csv',''),origen])
                break
    return list_match

def file(file_exp,file_theo):
    list_match=[]
    for i in range(len(file_exp)):
        name=file_exp[i].split('/')[1]
        origen=name.split('_')[1]
        origen=origen.replace('.csv','')
        for k in range(len(file_theo)):
            if origen in file_theo[k]:
                list_match.append([file_theo[k],file_exp[i],name.replace('.csv',''),origen])
                break
    return list_match