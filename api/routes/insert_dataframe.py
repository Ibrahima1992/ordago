import pandas as pd
import psycopg2

try:
    conn = psycopg2.connect(
        database="ordago",
        user="ordago",
        password="ordago",
        host="172.22.0.2",
        port="5432",
    )

    conn.autocommit = True

    cursor = conn.cursor()

    try:
        # Lecture du fichier de données
        df = pd.read_csv("api/ressources/Automobile_data.csv")
        # Remplacement par 0 de tous les enregistrements où le prix était à NAN ou non defini
        df["price"].fillna(0, inplace=True)
        # INSERTION DES DONNÉES DANS LA TABLE AUTOMOBILE DE LA BASE DE DONNÉES ORDAGO

        for row in df.itertuples():
            cursor.execute(
                f"""INSERT INTO automobile (index, company, body_style, wheel_base, length, engine_type, num_of_cylinders, horsepower, average_mileage, price) VALUES({row.index}, '{row.company}','{row.body_style}', {row.wheel_base}, {row.length}, '{row.engine_type}', '{row.num_of_cylinders}', {row.horsepower}, {row.average_mileage}, {row.price});"""
            )
    except:
        raise FileNotFoundError(
            "Fichier de données introuvable ou les données sont déjà présentes dans la base de données"
        )
    sql = "select * from automobile;"
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)
except:
    raise ConnectionRefusedError("erreur lors de la connexion à base de données")
finally:
    conn.close()
