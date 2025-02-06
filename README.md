# SGE_BLOC2

Aquesta connexió s'ha establert gràcies al mòdul psycopg2, que és una biblioteca de Python que permet connectar-se a bases de dades PostgreSQL. La connexió es crea utilitzant la funció psycopg2.connect(), que rep els paràmetres de connexió (usuari, contrasenya, base de dades, host i port).

Finalment, es mostra la connexió cridant la funció connection_db() i imprimint l'objecte de connexió. El que veiem a la sortida és la representació d'aquesta connexió, que inclou els detalls que hem menciona

![Connexio base dades](/Imagenes/Conectantbasedades.png/)

Per inserir la taula a PostgreSQL i les dades de Clients.csv a pgAdmin 4, cal crear primer crear la taula i amb la funció create_tables(), després carregar les dades del fitxer CSV a la taula.
Finalment, refresquem les taules a pgAdmin 4 per visualitzar la taula creada i els registres dels clients carregats.

**Per visualitzar la taula a la base de dades amb les dades Clients.csv a pgAdmin 4:**

Crear la taula a PostgreSQL amb l'estructura adequada.  
Carregar les dades del fitxer Clients.csv a la taula creada.  
Obrir pgAdmin 4, connectar-se a la base de dades i refrescar la vista de taules.  
Veure i els registres de clients carregats des del CSV utilitzant l'opció Veure/Editar dades.  

Així pots consultar les taules i veure les dades dins de pgAdmin 4.

![taula base dades](/Imagenes/Tabla.png/)

**Registre afegit**

![Ultim registre](/Imagenes/Ultimregistre.png)

**Mostra tots els registres** de forma horitzontal a una sola línea peró amb el return  
els mostra debaix de manera que a cada línia hi ha un camp.

![results_totals](/Imagenes/results_totals.png)

