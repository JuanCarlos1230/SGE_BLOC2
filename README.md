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

**Mostra tots els registres** de forma horitzontal en una sola línea.

![results_totals](/Imagenes/results_totals.png)

**A més de mostrar tots els registres dels clients, mostrem també només el registre del client número 5.**  
**És a dir, la informació de l'Alba.**  
**Mostrem el client 5 i no el 4 perquè comencem per 0.**

![Registre4=Client5](/Imagenes/Resgistre4.png)

A més de mostrar tots els registres dels clients, mostrem també només el registre del client número 5.  
És a dir, la informació de l'Alba.  
Mostrem el client 5 i no el 4 perquè comencem per 0.  
**Ara a més de mostrar aquesta informació especifiquem el camp que volem del client en aquest cas el correo**  
**electrónic de l'Alba.**  
**Mostrem el client 5 y no el 4 perque comencenm pero 0 i amb els camps pasa el mateix.**

![correo_electónic_Alba](/Imagenes/correo_Alba.png)

**Mostra les dades corresponents segons la entrada de results per exemple per results[9]**  
**mostra la informació del client numero 10 i si a més de possar [9] possem al costat [3] mostra la informació especifica**  
**del camp del client 10 i el camp 4 ja que comencem per 0.**  
**Aleshores tots els results amb un numero per exemple aixi: results[14] mostren tota la informació del registre de la fila del numero del client menys 1 peruqe comencem per 0 i els results como ara results[14] [1] mostran la fila 14 en aquest cas i el camp 1 pero no oblidem que comencem per 0 aixi que és la fila 15 i el camp 2.**  

![Resgistres_de_informació](/Imagenes/Registres_informacio.png)

**Això mostra tots els registres en ordre de manera imprimeix cada camp del registre i el seu valor**  
**en una sola linia és a dir sí el registre te 5 camps imprimeix 5 línies una per cada camp amb**  
**el seu valor corresponent.**
**Ja que li hem dit que el (nom es el primer camp [0] i el neixament és el cinque[4]) i els imprimeix en ordre**

![recuadre_text](/Imagenes/recuadre_text.png)
