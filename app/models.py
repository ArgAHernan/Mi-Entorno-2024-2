from app.database import get_db
from datetime import datetime 

class Maquinaria:

    #contructor
    def __init__(self,maquinaria_id=None,brand=None,name=None,model=None,release_date=None,banner=None):
        self.maquinaria_id = maquinaria_id
        self.brand = brand
        self.name = name
        self.model = model
        self.release_date = release_date
        self.banner = banner

    def serialize(self):
        return {
            'maquinaria_id':self.maquinaria_id,
            'brand':self.brand,
            'name':self.name,
            'model':self.model,
            'release_date':self.release_date.strftime('%Y-%m-%d'), 
            'banner':self.banner,
        }

    @staticmethod
    def get_all():
        #logica de buscar en la base todas las peliculas
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM productos"
        cursor.execute(query)
        #obtengo resultados
        rows = cursor.fetchall()
        maquinaria = [Maquinaria(maquinaria_id=row[0],brand=row[1], name=row[2], model=row[3], release_date=row[4], banner=row[5]) for row in rows]
        #cerramos el cursor
        cursor.close()
        return maquinaria

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.maquinaria_id:
            cursor.execute("""
                UPDATE Maquinaria< SET brand = %s, name = %s, model= %s, release_date = %s, banner = %s
                WHERE maquinaria_id = %s
            """, (self.brand, self.name , self.model, self.release_date, self.banner, self.maquinaria_id))
        else:
            cursor.execute("""
                INSERT INTO Maquinaria (brand, name, model, release_date, banner) VALUES (%s, %s, %s, %s)
            """, (self.brand, self.name, self.model, self.release_date, self.banner))
            #voy a obtener el último id generado
            self.maquinaria_id = cursor.lastrowid
        db.commit() #confirmar la accion
        cursor.close()

    @staticmethod
    def get_by_id(id_maquinaria):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE maquinaria_id = %s", (id_maquinaria,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Maquinaria(brand=row[0], name=row[1], model=row[2], release_date=row[3], banner=row[4])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE maquinaria_id = %s", (self.maquinaria_id,))
        db.commit()
        cursor.close()