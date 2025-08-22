from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__) 

def insertar_mascota(tipo, nombre):
    conn = sqlite3.connect("personajesSqlite.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO mascotas(tipo, nombre) VALUES (?,?)
        """,(tipo, nombre)
    )
    id_mascota = cursor.lastrowid
    conn.commit()
    conn.close()
    return id_mascota
    #print(f"Nombre: {nombre} y Mascota: {tipo} fueron agregados a la base de datos")

#🔧 Paso 2: Insertar mascota y personaje vinculado
def insertar_perosonaje_relacionado(nombre,edad,color,mascota_id):
    conn = sqlite3.connect("personajesSqlite.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO personajes(nombre, edad, color_favorito, mascota_id) VALUES(?,?,?,?)
        """, (nombre, edad, color, mascota_id)
    )
    conn.commit()
    conn.close()
    print(f"Nombre: {nombre} vinculado a mascota ID {mascota_id}")

# Ruta GET: Mostrar todos los personajes
@app.route("/personajesSql", methods=["GET"])
def get_personaje():
    conn = sqlite3.connect("personajesSql.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT p.nombre, p.edad, p.color_favorita, m.tipo, m.nombre 
        FROM peronajes p 
        JOIN mascotas m ON p.mascota_id = m.id 
        """
    )
    resultado = cursor.fetchall()
    conn.close()
    personajes = [
        {
            "nombre": r[0],
            "edad": r[1],
            "color_favorito": r[2],
            "mascota": {"tipo": r[3], "nombre": r[4]}
        }for r in resultado
    ]
    return jsonify(personajes)

@app.route("/personajesSql", methods=["POST"])
def post_personaje():
    data = request.json
    mascota_id = insertar_mascota(data["mascota"]["tipo"], data["mascota"]["nombre"])
    insertar_perosonaje_relacionado(data["nombre"], data["edad"], data["color_favorito"], mascota_id)
    return jsonify({"mensaje": "Persoanje creado"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0, port=10000)

#🧠 Habilidades que estás desarrollando:
#Nivel	Habilidad
#🧠 110%	Creación de API RESTful
#🧠 115%	Comunicación entre frontend y backend
#🧠 120%	Preparación para autenticación, seguridad y despliegue

#¡Vamos a construir tu primera API real con rutas completas, ISC! 🚀
#Ya que tienes tu base de datos con relaciones entre tablas, 
#ahora vamos a integrar rutas PUT, DELETE y búsqueda por nombre en tu API Flask. 
#Esto te lleva al nivel 115%, y te prepara para despliegue, autenticación 
#y conexión con frontends.

#🧱 Ruta GET /personajes/<nombre> – Buscar personaje por nombre
@app.route("/personajesSql/<nombre>", methods=["GET"])
def get_personajes(nombre):
    conn = sqlite3.connect("personajesSql.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT p.nombre, p.edad, p.color_favorito, m.tipo, m.nombre 
        FROM personas p
        JOIN mascotas m ON p.mascota_id = m.id 
        WHERE LOWER(nombre) = ?
        """, (nombre,)
    )
    resultado = cursor.fetchall()
    conn.close()
    if resultado:
        personaje =[
            {
                "nombre": resultado[0],
                "edad": resultado[1],
                "color_favorito": resultado[2],
                "mascota": {"tipo": resultado[3], "nombre": resultado[4]} 
            }
        ]
        return jsonify(personaje)
    else:
        return jsonify({"error": "Personaje no encontrado"})

@app.route("/personajesSql/<nombre>", methods=["PUT"])
def put_personajes(nombre):
    data = request.json
    nuevo_color = data.get("color_favorito")
    conn = sqlite3.connect("personajesSql")
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE personajes 
        SET nuevo_color = ?
        WHERE LOWER(nombre) = (?)
        """,(nuevo_color, nombre)
    )
    conn.commit()
    conn.close()

    return jsonify({"mensaje": f"Color Favorito de {nombre} actualizado a {nuevo_color}"})

@app.route("/personajesSql/<nombre>", methods=["DELETE"])
def delete_persoanjes(nombre):
    conn = sqlite3.connect("persoanjesSql.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM personajes
        WHERE LOWER(nombre) = LOWER(?)
        """,(nombre,)
    )
    conn.commit()
    conn.close()
    return jsonify({"mensaje": f"Personaje {nombre} eliminado"})

#🧠 Habilidades que estás desarrollando:

#Nivel	Habilidad
#🧠 115%	Manejo completo de rutas REST
#🧠 120%	Edición y eliminación vía HTTP
#🧠 125%	Preparación para autenticación, despliegue y seguridad

#🛠️ Solución paso a paso: Instalar Git en Windows
#🔧 Paso 1: Descargar Git
#Ve al sitio oficial: 👉 https://git-scm.com/download/win

#La descarga debería comenzar automáticamente. Si no, elige la versión para Windows manualmente.

#🔧 Paso 2: Instalar Git
#Ejecuta el instalador descargado.

#Acepta los términos y deja la mayoría de las opciones por defecto.

#Asegúrate de que la opción “Git from the command line and also from 3rd-party software” esté seleccionada. Esto garantiza que Git se agregue al PATH del sistema.

#🔧 Paso 3: Verifica la instalación
#Después de instalar, abre una nueva terminal (puede ser PowerShell o CMD) y escribe:

#bash
#git --version
#✅ Si ves algo como git version 2.42.0, ¡todo está listo!

#🧠 Habilidades que estás desarrollando:
#Nivel	Habilidad
#🧠 120%	Instalación y configuración de herramientas
#🧠 125%	Control de versiones con Git
#🧠 130%	Preparación para despliegue en GitHub y Render
