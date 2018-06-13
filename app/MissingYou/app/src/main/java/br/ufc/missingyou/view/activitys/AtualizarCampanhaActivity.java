package br.ufc.missingyou.view.activitys;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

import br.ufc.missingyou.R;

public class AtualizarCampanhaActivity extends AppCompatActivity {

    private ViewHolder mViewHolder = new ViewHolder();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_atualizar_campanha);

        getSupportActionBar().setTitle("Atualizar Campanha");

        // spinner sexo
        Spinner spinner = (Spinner) findViewById(R.id.spinner_sexo_atualizar);
        this.mViewHolder.spinner_Sexo = spinner;
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.sexo, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        // spinner olhos
        spinner = (Spinner) findViewById(R.id.spinner_olhos_atualizar);
        this.mViewHolder.spinner_olhos = spinner;
        adapter = ArrayAdapter.createFromResource(this, R.array.olhos, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);


        // spinner raca
        spinner = (Spinner) findViewById(R.id.spinner_raca_atualizar);
        this.mViewHolder.spinner_raca = spinner;
        adapter = ArrayAdapter.createFromResource(this, R.array.raca, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        // spinner cabelo
        spinner = (Spinner) findViewById(R.id.spinner_cabelo_atualizar);
        this.mViewHolder.spinner_cabelo = spinner;
        adapter = ArrayAdapter.createFromResource(this, R.array.cabelo, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);



    }
    private static  class ViewHolder{
        Spinner spinner_cabelo;
        Spinner spinner_olhos;
        Spinner spinner_raca;
        Spinner spinner_Sexo;
    }

    public void onItemSelected(AdapterView<?> parent, View view,
                               int pos, long id) {
        // An item was selected. You can retrieve the selected item using
        // parent.getItemAtPosition(pos)
    }

    public void onNothingSelected(AdapterView<?> parent) {
        // Another interface callback
    }

    public void onClick(View view) {

    }

}
