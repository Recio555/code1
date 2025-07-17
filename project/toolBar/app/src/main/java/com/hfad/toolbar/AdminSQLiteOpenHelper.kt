package com.hfad.toolbar

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

}