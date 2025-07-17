package hno.frutiapp

import android.content.ContentValues
import android.content.Intent
import android.media.MediaPlayer
import android.os.Bundle
import android.view.View
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class Main2Activity_Nivel2 : AppCompatActivity() {
    lateinit var ver: TextView
    lateinit var tv_score: TextView
    lateinit var tv_nombre: TextView
    lateinit var iv_vidas: ImageView
    lateinit var iv_Auno: ImageView
    lateinit var  iv_Ados: ImageView
    lateinit var et_respuestas:EditText
    lateinit var mp: MediaPlayer
    lateinit var mp_great: MediaPlayer
    lateinit var mp_bad: MediaPlayer
    var score:Int = 0
    var numAleatorio_uno:Int = 0
    var numAleatorio_dos:Int = 0
    var resultado:Int = 0
    var vidas:Int = 3
    lateinit var string_score: String
    lateinit var string_vidas: String
    lateinit var nombre_jugador:String
    var numero = arrayOf("cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2_nivel2)

        Toast.makeText(this,"Nivel 2 - Sumas moderadas", Toast.LENGTH_LONG).show()
        tv_score = findViewById(R.id.textView_score)
        tv_nombre = findViewById(R.id.textView_nombre)
        iv_Auno = findViewById(R.id.imageView_NumUno)
        iv_Ados = findViewById(R.id.imageView_NumDos)
        et_respuestas = findViewById(R.id.editText_resultado)
        iv_vidas = findViewById(R.id.imageView_vidas)
        nombre_jugador = intent.getStringExtra("jugador").toString()
        tv_nombre.setText("Jugador : " + nombre_jugador)
        supportActionBar?.setDisplayShowHomeEnabled(true)
        supportActionBar?.setIcon(R.mipmap.ic_launcher)
        supportActionBar?.setDisplayUseLogoEnabled(true);
        mp = MediaPlayer.create(this,R.raw.goats)
        mp.start()
        mp.isLooping = true
        mp_great = MediaPlayer.create(this, R.raw.wonderful)
        mp_bad = MediaPlayer.create(this,R.raw.bad)
        NumeroAleatorio()
    }
    fun Comparar(view: View) {
        var ops = Ops(tv_score, iv_vidas)
        var respuesta:String = ops.Clear(et_respuestas)
        val db = AdminSQLiteOpenHelper(this)
        if (respuesta.isNotBlank()) {
            val respuesta_jagador: Int = respuesta.toInt()
            if (resultado == respuesta_jagador) {
                score++
                mp_great.start()
                tv_score.setText("Score  : " + score.toString())
                ops.Clear(et_respuestas)
                db.Update(score,nombre_jugador)
            } else {
                mp_bad.start()
                vidas--
                db.Update(score,nombre_jugador)
                when (vidas) {
                    3 -> {
                        iv_vidas.setImageResource(R.drawable.tresvidas)
                    }

                    2 -> {
                        Toast.makeText(this, "Te quedan 2 manzanas", Toast.LENGTH_LONG).show()
                        iv_vidas.setImageResource(R.drawable.dosvidas)
                    }

                    1 -> {
                        Toast.makeText(this, "Te queda 1 manzana", Toast.LENGTH_LONG).show()
                        iv_vidas.setImageResource(R.drawable.unavida)
                    }

                    0 -> {
                        Toast.makeText(this, "Has perdido todas tus manzanas", Toast.LENGTH_LONG)
                            .show()
                        val intent = Intent(this, MainActivity::class.java)
                        startActivity(intent)
                        finish()
                        mp.stop()
                        mp.release()
                    }
                }
                ops.Clear(et_respuestas)
            }
            NumeroAleatorio()
        } else {
            Toast.makeText(this, "Escribe tu respuetas", Toast.LENGTH_LONG).show()
        }
    }
    private fun BaseDeDatos() {
        val admin = AdminSQLiteOpenHelper(this)
        val BD = admin.writableDatabase
        val consulta = BD.rawQuery(
            // "select * from puntaje where score = (select max(score) from puntaje)",null
            "SELECT * FROM puntaje WHERE score = (SELECT MAX(score) FROM puntaje)", null)
        if (consulta.moveToFirst()){
            do {
                val temp_nombre:String = consulta.getString(0)
                val tem_score:String = consulta.getString(1)
                var bestScore:Int = tem_score.toString().toInt()
                var nombre_consultado:String = temp_nombre
                if(score > bestScore){
                    val modificacion = ContentValues()
                    modificacion.put("nombre", nombre_jugador)
                    modificacion.put("score", score)
                    try {
                        BD.update("puntaje", modificacion,"score = " + bestScore,null)
                        BD.close()
                    } catch (e: InterruptedException) {
                        finish()
                    }
                }else{
                    if(nombre_jugador != nombre_consultado ){
                        val insertar = ContentValues()
                        insertar.put("nombre", nombre_jugador)
                        insertar.put("score", score)
                        BD.insert("puntaje", null, insertar)
                        BD.close()
                    }
                }
            } while (consulta.moveToNext())
            consulta.close()
            BD.close()

        }else {
            BD.close()
        }
    }

    public  fun NumeroAleatorio(){
        if(score <= 19){
            numAleatorio_uno = (Math.random() * 10).toInt()
            numAleatorio_dos = (Math.random() * 10 ).toInt()
            resultado = numAleatorio_uno + numAleatorio_dos
            if (resultado <= 9) {
                for (i: Int in 0 until numero.size) {
                    var id = resources.getIdentifier(numero[i], "drawable", packageName)
                    if (numAleatorio_uno == i){
                        iv_Auno.setImageResource(id)
                    }
                    if (numAleatorio_dos == i){
                        iv_Ados.setImageResource(id)
                    }
                }
            }else{
                NumeroAleatorio()
            }

        }else{
            val intent =  Intent(this,Main2Activity_Nivel3::class.java)
            string_score = score.toString()
            string_vidas = vidas.toString()
            intent.putExtra("jugador", nombre_jugador)
            intent.putExtra("score", string_score)
            intent.putExtra("vidas", string_vidas)

            startActivity(intent)
            finish()
            mp.stop()
            mp.release()
        }
    }
}