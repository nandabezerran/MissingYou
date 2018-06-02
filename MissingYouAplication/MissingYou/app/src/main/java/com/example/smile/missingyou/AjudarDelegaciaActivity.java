package com.example.smile.missingyou;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.support.v7.app.AppCompatActivity;
import android.widget.Button;
import android.widget.EditText;

public class AjudarDelegaciaActivity  extends AppCompatActivity implements View.OnClickListener{

    private ViewHolder mViewHolder = new ViewHolder();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ajudar_delegacia);

        getSupportActionBar().setTitle("Ajudar Campanha");

        this.mViewHolder.editDelegacia = (EditText) findViewById(R.id.editText_delegacia);
        this.mViewHolder.buttonConfirmarDelegacia = (Button) findViewById(R.id.button_confirmar_delegacia);

        this.mViewHolder.buttonConfirmarDelegacia.setOnClickListener(this);

    }



    private static class ViewHolder {
        EditText editDelegacia;
        Button buttonConfirmarDelegacia;
    }

    @Override
    public void onClick(View view) {
        int id = view.getId();
        if (id == R.id.button_confirmar_delegacia) {

        }
    }
}
