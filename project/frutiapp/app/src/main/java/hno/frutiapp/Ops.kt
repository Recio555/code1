package hno.frutiapp

import android.media.MediaPlayer
import android.view.View
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView

class Ops(val tv_score: TextView, val iv_vidas: ImageView) {
    lateinit var mp: MediaPlayer
    lateinit var mp_great:MediaPlayer
    lateinit var mp_bad:MediaPlayer
    var score:Int = 0
    var numAleatorio_uno:Int = 0
    var numAleatorio_dos:Int = 0
    var resultado:Int = 0
    var vidas:Int = 3
    var numero = arrayOf("cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve")

    fun Clear(et_respuestas:EditText): String {
        val valor: String =  et_respuestas.text.toString()
        et_respuestas.text.clear()
        return valor
    }
    fun Aleatorio(id: Int){
        if(score <= 1000000){
            numAleatorio_uno = (Math.random() * 10).toInt()
            numAleatorio_dos = (Math.random() * 10 ).toInt()
            resultado = numAleatorio_uno * numAleatorio_dos
            if (resultado <= 9) {
                for (i: Int in 0 until numero.size) {
                    if (numAleatorio_uno == i){
                      //  iv_Auno.setImageResource(id)
                    }
                    if (numAleatorio_dos == i){
                      // iv_Ados.setImageResource(id)
                    }
                }
            }

        }
    }



}