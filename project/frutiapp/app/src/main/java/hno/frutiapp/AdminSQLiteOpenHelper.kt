package hno.frutiapp

import android.annotation.SuppressLint
import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper

class  AdminSQLiteOpenHelper(context: Context): SQLiteOpenHelper(context,"BD.db",null, 1) {

    override fun onCreate(BD: SQLiteDatabase?) {
        BD!!.execSQL("CREATE TABLE puntaje"+"(nombre TEXT,score INTEGER)")
    }


    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        val ordenBorado = "DROP TABLE IF EXISTS puntaje"
        db!!.execSQL(ordenBorado)
        onCreate(db)
    }
    fun agregarDatos(nombre:String, score:Int){
        val datos = ContentValues()
        datos.put("nombre", nombre)
        datos.put("score", score)
        val db = this.writableDatabase
        db.insert("puntaje", null,datos)
        db.close()
    }
    fun Update(score: Int,nombre_jugador:String){
        val BD = this.writableDatabase
        val consulta = BD.rawQuery(
            // "select * from puntaje where score = (select max(score) from puntaje)",null
            "SELECT * FROM puntaje WHERE score = (SELECT MAX(score) FROM puntaje)", null)
        if (consulta.moveToFirst()){
            do {
                val temp_nombre:String = consulta.getString(0)
                val tem_score:String = consulta.getString(1)
                var bestScore:Int = tem_score.toString().toInt()
                if(score > bestScore){
                    val modificacion = ContentValues()
                    modificacion.put("nombre", nombre_jugador)
                    modificacion.put("score", score)
                    BD.update("puntaje", modificacion,"score = " + bestScore,null)
                    BD.close()
                }
            } while (consulta.moveToNext())
            consulta.close()
            BD.close()
        }else {
            val insertar = ContentValues()
            insertar.put("nombre", nombre_jugador)
            insertar.put("score", score)
            BD.insert("puntaje", null, insertar)
            BD.close()
        }
    }
}

