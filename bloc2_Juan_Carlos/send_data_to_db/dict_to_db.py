
import psycopg2

def send_data_to_db(pos, data):
   print(data)
   conn = psycopg2.connect(
      database="the_bear",
      password="admin",
      user="admin",
      host="localhost",
      port="5432"
   )

   cur = conn.cursor()
   sql = "INSERT INTO Clientes (nombre_cliente, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños) VALUES (%s, %s, %s, %s, %s);"

   values = (data["nombre_cliente"][pos], data["dirección_cliente"][pos], data["teléfono_cliente"]
   [pos], data["correo_electrónico_cliente"][pos], data["fecha_cumpleaños"][pos])

   cur.execute(sql, values)
   conn.commit()

   cur.close()
   conn.close()

   return {"Message":"Data inserted"}
