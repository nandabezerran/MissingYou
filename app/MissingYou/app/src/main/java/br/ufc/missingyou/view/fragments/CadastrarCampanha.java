package br.ufc.missingyou.view.fragments;


import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

import br.ufc.missingyou.R;


/**
 * A simple {@link Fragment} subclass.
 */
public class CadastrarCampanha extends Fragment implements AdapterView.OnItemSelectedListener, View.OnClickListener{


    public CadastrarCampanha() {}

    private ViewHolder mViewHolder = new ViewHolder();

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View rootview = inflater.inflate(R.layout.fragment_cadastrar_campanha, container, false);


        EditText editar = (EditText) rootview.findViewById(R.id.edit_data_desaparecimento);

        Spinner spinner = (Spinner) rootview.findViewById(R.id.spinner_sexo);
        this.mViewHolder.spinnerSexo = spinner;
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this.getActivity(), R.array.sexo, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        spinner = (Spinner) rootview.findViewById(R.id.spinner_olhos);
        this.mViewHolder.spinnerOlhos = spinner;
        adapter = ArrayAdapter.createFromResource(this.getActivity(), R.array.olhos, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        spinner = (Spinner) rootview.findViewById(R.id.spinner_raca);
        this.mViewHolder.spinnerRaca = spinner;
        adapter = ArrayAdapter.createFromResource(this.getActivity(), R.array.raca, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        spinner = (Spinner) rootview.findViewById(R.id.spinner_cabelo);
        this.mViewHolder.spinnerCabelo = spinner;
        adapter = ArrayAdapter.createFromResource(this.getActivity(), R.array.cabelo, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        this.mViewHolder.buttonCadastrarCampanha = (Button) rootview.findViewById(R.id.button_cadastrar_campanha);
        this.mViewHolder.editDataDesaparecimento = (EditText) rootview.findViewById(R.id.edit_data_desaparecimento);
        this.mViewHolder.editDataNascimento = (EditText) rootview.findViewById(R.id.edit_data_nascimento);
        this.mViewHolder.editBo = (EditText) rootview.findViewById(R.id.edit_numero_bo);
        this.mViewHolder.editNomeDesaparecido = (EditText) rootview.findViewById(R.id.edit_nome_desaparecido);
        this.mViewHolder.editLocalDesaparecimento = (EditText) rootview.findViewById(R.id.edit_local_desaparecimento);

        this.mViewHolder.buttonCadastrarCampanha.setOnClickListener(this);

        return inflater.inflate(R.layout.fragment_cadastrar_campanha, container, false);
    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {

    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

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

    @Override
    public void onClick(View view) {
        int id = view.getId();
        if(id == R.id.button_cadastrar_campanha) {
            //logica do botao aqui
        }
    }
}
