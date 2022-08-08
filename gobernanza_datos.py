#!/usr/bin/env python

import pandas as pd

# TODO: xlsx to csv file
def xlsx_to_csv(xlsx):
    # TODO: Leer excel
    df = pd.read_excel(xlsx, header=None)
    df = df.drop(labels=(0))
    # TODO: Borrar datos en caso de encriptacion
#    df.drop(labels=[5, 6, 7, 8], axis=0, inplace=True)
    ubi = "./in/documento_original.csv"
    df.to_csv(ubi, header=None, sep=',', index=False)
    return ubi

def create_codes(column):
    codes = []
    df = pd.DataFrame(columns=['Identifier', 'Code_ID'])
    for i in range(10001, 10001 + len(column)):
        codes.append(str(i))
    df['Identifier'] = column
    df['Code_ID'] = codes
    return df

def df_asingcodes(file):
    # TODO: Leer csv
    df = pd.read_csv(file)
    # TODO: Extraer columna de documento
    sr_id = df.iloc[:, 4]
    # TODO: Obtener documentos unicos de cada documento
    id_uniq = pd.Series(sr_id.unique()).values
    # TODO: Crear codigo para cada documento
    df_codes = create_codes(id_uniq)
    # TODO: Unir documentos con su respectivo codigo
    df_final = pd.merge(df, df_codes, how='left', left_on=df.columns[4], right_on='Identifier')
    # TODO: Eliminar columnas de identidades
#    df_final = df_final.drop(columns=df.columns[4:5])
    # TODO: Informe con confidencialidad de datos
    df_final.to_csv('./out/documento_protegido.csv', index=False)
    return df_final



