package com.example.smile.missingyou;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

public class CadastroCampanhaActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener, View.OnClickListener {

    private ViewHolder mViewHolder = new ViewHolder();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cadastro_campanha);

        getSupportActionBar().setTitle("Cadastro de Campanhas");

        Spinner spinner = (Spinner) findViewById(R.id.spinner_sexo);
        this.mViewHolder.spinnerSexo = spinner;
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.sexo, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        spinner = (Spinner) findViewById(R.id.spinner_olhos);
        this.mViewHolder.spinnerOlhos = spinner;
        adapter = ArrayAdapter.createFromResource(this, R.array.olhos, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        spinner = (Spinner) findViewById(R.id.spinner_raca);
        this.mViewHolder.spinnerRaca = spinner;
        adapter = ArrayAdapter.createFromResource(this, R.array.raca, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        spinner = (Spinner) findViewById(R.id.spinner_cabelo);
        this.mViewHolder.spinnerCabelo = spinner;
        adapter = ArrayAdapter.createFromResource(this, R.array.cabelo, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        this.mViewHolder.buttonCadastrarCampanha = (Button) findViewById(R.id.button_cadastrar_campanha);
        this.mViewHolder.editDataDesaparecimento = (EditText) findViewById(R.id.edit_data_desaparecimento);
        this.mViewHolder.editDataNascimento = (EditText) findViewById(R.id.edit_data_nascimento);
        this.mViewHolder.editBo = (EditText) findViewById(R.id.edit_numero_bo);
        this.mViewHolder.editNomeDesaparecido = (EditText) findViewById(R.id.edit_nome_desaparecido);
        this.mViewHolder.editLocalDesaparecimento = (EditText) findViewById(R.id.edit_local_desaparecimento);

        this.mViewHolder.buttonCadastrarCampanha.setOnClickListener(this);

    }

    private static class ViewHolder {
        Button buttonCadastrarCampanha;
        EditText editNomeDesaparecido;
        EditText editDataNascimento;
        EditText editDataDesaparecimento;
        EditText editLocalDesaparecimento;
        EditText editBo;
        Spinner spinnerOlhos;
        Spinner spinnerCabelo;
        Spinner spinnerSexo;
        Spinner spinnerRaca;
    }

    public void onItemSelected(AdapterView<?> parent, View view,
                               int pos, long id) {
        // An item was selected. You can retrieve the selected item using
        // parent.getItemAtPosition(pos)
    }

    public void onNothingSelected(AdapterView<?> parent) {
        // Another interface callback
    }

    @Override
    public void onClick(View view) {
        int id = view.getId();
        if (id == R.id.button_cadastrar_campanha) {

        }
    }


}
