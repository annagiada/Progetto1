import DbFunctions as d

db = d.create_server_connection("localhost", "root", "")

d.create_database(db, "museo")

db = d.create_db_connection("localhost", "root", "", "museo")
create_artist="""

CREATE TABLE artist(

    id INT PRIMARY KEY,

    name VARCHAR(150),

    nationality VARCHAR(150),

    gender VARCHAR(150),

    birth YEAR,

    death YEAR

    )"""

create_opere_table = """

CREATE TABLE opere (

    id INT PRIMARY KEY,

    id_artista INT,

    titolo VARCHAR(50) NOT NULL,

    date DATE,

    medium INT,

    dimensioni INT,

    giorno_acquisizione DATE,

    credit VARCHAR(150),

    catalogo VARCHAR(150),

    dipartimento VARCHAR(150),

    classificazione VARCHAR(150),

    n_oggetto INT,

    diametro INT,

    circoferenza INT,

    altezza INT,

    lunghezza INT,

    ampiezza INT,

    profondità INT,

    peso INT,

    durata VARCHAR(150),

    FOREIGN KEY (id_artista) REFERENCES artist(id)

);

 """
d.execute_query(db, create_artist)

d.execute_query(db, create_opere_table)