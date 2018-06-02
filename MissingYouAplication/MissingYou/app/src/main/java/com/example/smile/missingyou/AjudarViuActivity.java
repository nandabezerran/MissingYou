package com.example.smile.missingyou;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class AjudarViuActivity extends AppCompatActivity implements View.OnClickListener {
    private ViewHolder mViewHolder = new ViewHolder();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ajudar_viu);

        getSupportActionBar().setTitle("Ajudar Campanha");

        this.mViewHolder.editViu = (EditText) findViewById(R.id.editText_viu);
        this.mViewHolder.buttonConfirmarViu = (Button) findViewById(R.id.button_confirmar_viu);

        this.mViewHolder.buttonConfirmarViu.setOnClickListener(this);

    }



    private static class ViewHolder {
        EditText editViu;
        Button buttonConfirmarViu;
    }

    @Override
    public void onClick(View view) {
        int id = view.getId();
        if (id == R.id.button_confirmar_delegacia) {

        }
    }
}
