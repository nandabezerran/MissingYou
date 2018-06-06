package br.ufc.missingyou.view.activitys;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import br.ufc.missingyou.R;


public class AjudarCampanhaActivity extends AppCompatActivity implements View.OnClickListener {
    private ViewHolder mViewHolder = new ViewHolder();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ajudar_campanha);

        getSupportActionBar().setTitle("Ajudar Campanha");

        this.mViewHolder.buttonViuPessoa = (Button) findViewById(R.id.button_viu_pessoa);
        this.mViewHolder.buttonDelegacia = (Button) findViewById(R.id.button_delegacia);
        this.mViewHolder.buttonEstaComPessoa = (Button) findViewById(R.id.button_esta_com_pessoa);

        this.mViewHolder.buttonViuPessoa.setOnClickListener(this);
        this.mViewHolder.buttonDelegacia.setOnClickListener(this);
        this.mViewHolder.buttonEstaComPessoa.setOnClickListener(this);

    }

    private static class ViewHolder {
        Button buttonViuPessoa;
        Button buttonDelegacia;
        Button buttonEstaComPessoa;
    }


    @Override
    public void onClick(View view) {
        int id = view.getId();
        if (id == R.id.button_esta_com_pessoa) {
            Intent intent = new Intent(this, AjudarEstaActivity.class);
            startActivity(intent);
        }
        if (id == R.id.button_viu_pessoa) {
            Intent intent = new Intent(this, AjudarViuActivity.class);
            startActivity(intent);
        }
        if (id == R.id.button_delegacia) {
            Intent intent = new Intent(this, AjudarDelegaciaActivity.class);
            startActivity(intent);

        }
    }
}
