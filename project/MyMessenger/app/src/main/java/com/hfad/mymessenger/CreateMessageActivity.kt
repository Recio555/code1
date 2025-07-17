package com.hfad.mymessenger

import android.os.Bundle
import android.view.View
import androidx.appcompat.app.AppCompatActivity

class CreateMessageActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_create_message)

    }

    fun onSendMessage(view: View) {}
}