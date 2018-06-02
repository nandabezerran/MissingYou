package com.example.smile.missingyou;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class AjudarEstaActivity extends AppCompatActivity implements View.OnClickListener {

    private ViewHolder mViewHolder = new ViewHolder();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ajudar_esta);

        getSupportActionBar().setTitle("Ajudar Campanha");

        this.mViewHolder.editEsta = (EditText) findViewById(R.id.editText_esta);
        this.mViewHolder.buttonConfirmarEsta = (Button) findViewById(R.id.button_confirmar_esta);

        this.mViewHolder.buttonConfirmarEsta.setOnClickListener(this);

    }

    private static class ViewHolder {
        EditText editEsta;
        Button buttonConfirmarEsta;
    }

    @Override
    public void onClick(View view) {
        int id = view.getId();
        if (id == R.id.button_confirmar_esta) {

        }
    }
}
