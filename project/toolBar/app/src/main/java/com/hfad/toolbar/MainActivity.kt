package com.hfad.toolbar

import android.content.ContentValues
import android.os.Bundle
import android.view.View
import android.widget.Spinner
import android.widget.TextView
import android.widget.Toast
import android.widget.Toolbar
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {

    lateinit var nombre_jugador: TextView
    lateinit var vidas: TextView
    lateinit var nextDeposito: TextView
    lateinit var lista: TextView
    lateinit var mensualSemanal: Spinner
    lateinit var  bestScore: TextView
    var score:Int = 0
    lateinit var admin:AdminSQLiteOpenHelper

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        nombre_jugador = findViewById(R.id.deposito)
        vidas = findViewById(R.id.fecha)
        nextDeposito = findViewById(R.id.nextDeposito)
        lista = findViewById(R.id.lista)
        mensualSemanal = findViewById(R.id.capitalizar)
        bestScore= findViewById(R.id.totalBalance)

        admin = AdminSQLiteOpenHelper(this)
    }


    fun Comparar(view: View) {
        score++
       // admin.agregarDatos(nombre_jugador.text.toString(), nextDeposito.text.toString().toInt())
      //  Toast.makeText(this, "Guardados", Toast.LENGTH_SHORT).show()
        val db = admin.writableDatabase
        val query = "SELECT * FROM puntaje WHERE score = (SELECT MAX(score) FROM puntaje)"
        val cursor = db.rawQuery(query, null)
        if (cursor.moveToFirst()) {
            do {
                val temp_nombre:String = cursor.getString(0).toString()
                val tem_score:Int = cursor.getString(1).toInt()
                var bestScore:Int = tem_score.toInt()
                lista.setText("Record: " + tem_score + " de " + temp_nombre)
                vidas.setText(score.toString())
                if(score > bestScore.toInt()){
                    Toast.makeText(this, "EJECUTANDO EL IF", Toast.LENGTH_SHORT).show()
                    val db = admin.writableDatabase
                    val modificacion = ContentValues()
                    modificacion.put("nomre", nombre_jugador.toString())
                    modificacion.put("score", score)
                    vidas.setText(nombre_jugador.text.toString()+" : "+ score)
                    db.update("puntaje", modificacion,"score" + bestScore,null)
                    db.close()
                }else{
                    val datos = ContentValues()
                    datos.put("nombre", nombre_jugador.text.toString())
                    datos.put("score", score)
                    val db = admin.writableDatabase
                    db.insert("puntaje", null,datos)
                    db.close()
                }

            } while (cursor.moveToNext())
        }
        cursor.close()
        db.close()


    }


}