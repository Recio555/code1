package hno.frutiapp

import android.annotation.SuppressLint
import android.app.Activity
import android.content.Context
import android.content.Intent
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.media.MediaPlayer
import android.os.Bundle
import android.provider.Telephony.Mms.Intents
import android.view.View
import android.view.inputmethod.InputMethodManager
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    lateinit var et_nommbre:EditText
    lateinit var personaje:ImageView
    lateinit var tv_bestScore:TextView
    lateinit var toggle: ActionBarDrawerToggle

    private lateinit var mp:MediaPlayer


    var aleatorio:Int = (Math.random() * 10).toInt()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        et_nommbre = findViewById(R.id.txt_nombre)
        personaje = findViewById(R.id.imageView_personaje)
        tv_bestScore = findViewById(R.id.textView_BestScore)
        supportActionBar?.setDisplayShowHomeEnabled(true)
        supportActionBar?.setIcon(R.mipmap.ic_launcher)
        var id:Int
        if (aleatorio == 0 || aleatorio == 10){
            id = getResources().getIdentifier("mango", "drawable", packageName)
            personaje.setImageResource(id)
        }else if (aleatorio == 1 || aleatorio == 9){
            id = getResources().getIdentifier("fresa", "drawable", packageName)
            personaje.setImageResource(id)
        } else if (aleatorio == 2 || aleatorio == 8){
            id = getResources().getIdentifier("manzana", "drawable", packageName)
            personaje.setImageResource(id)
        } else if (aleatorio == 3 || aleatorio == 7){
            id = getResources().getIdentifier("sandia", "drawable", packageName)
            personaje.setImageResource(id)
        } else if (aleatorio == 4 || aleatorio == 5 || aleatorio == 6){
            id = getResources().getIdentifier("uva", "drawable", packageName)
            personaje.setImageResource(id)
        }
        val admin = AdminSQLiteOpenHelper(this)
        val BD = admin.writableDatabase
        val consulta = BD.rawQuery(
           // "select * from puntaje where score = (select max(score) from puntaje)",null
            "SELECT * FROM puntaje WHERE score>=(SELECT MAX(score) FROM puntaje)", null)
        if (consulta.moveToFirst()){
            do {
                val temp_nombre:String = consulta.getString(0)
                val tem_score:String = consulta.getString(1)
                tv_bestScore.setText("Record: " + tem_score + " de " + temp_nombre)
            } while (consulta.moveToNext())
            consulta.close()
            BD.close()
        }else {
            BD.close()
        }
        mp = MediaPlayer.create(this,R.raw.alphabet_song)
        mp.start()
        mp.isLooping = true
    }
    fun Jugar(view: View) {
        var nombre:String = et_nommbre.text.toString()
        if (!nombre.equals("")){
            mp.stop()
            mp.release()
            val intent =  Intent(this,Main2Activity_Nivel1::class.java)
            intent.putExtra("jugador", nombre)
            startActivity(intent)
            finish()
        }else {
            Toast.makeText(this, "Primero debes escribir tu nombre", Toast.LENGTH_LONG).show()
            et_nommbre.requestFocus()
            val imm =  getSystemService(Context.INPUT_METHOD_SERVICE) as InputMethodManager
            imm.showSoftInput(et_nommbre,  InputMethodManager.SHOW_IMPLICIT)
        }
    }
    @SuppressLint("MissingSuperCall")
    override fun onBackPressed() {}
}
