package br.ufc.missingyou.view.fragments;


import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;

import br.ufc.missingyou.R;


/**
 * A simple {@link Fragment} subclass.
 */
public class QuadroCampanhasCadastradas extends Fragment implements AdapterView.OnItemSelectedListener, View.OnClickListener {


    public QuadroCampanhasCadastradas() {
        // Required empty public constructor
    }
    private ViewHolder mViewHolder = new ViewHolder();

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View rootview = inflater.inflate(R.layout.fragment_quadro_campanhas_cadastradas, container, false);
        this.mViewHolder.nomeDesaparecido = (EditText) rootview.findViewById(R.id.nomePessoa);
        this.mViewHolder.localDesaparecimento = (EditText) rootview.findViewById(R.id.local_desaparecimento);
        this.mViewHolder.dataDesaparecimento = (EditText) rootview.findViewById(R.id.data_desaparecimento);
        this.mViewHolder.dataNascimentoDesaparecido = (EditText) rootview.findViewById(R.id.data_nascimento);
        this.mViewHolder.cabeloDesaparecido = (EditText) rootview.findViewById(R.id.cabelo);
        this.mViewHolder.olhosDesaparecido = (EditText) rootview.findViewById(R.id.olho);
        this.mViewHolder.racaDesaparecido = (EditText) rootview.findViewById(R.id.raca);
        this.mViewHolder.sexoDesaparecido = (EditText) rootview.findViewById(R.id.genero);
        this.mViewHolder.foto = (ImageView) rootview.findViewById(R.id.foto_desaparecido);

        this.mViewHolder.alterarDados = (Button) rootview.findViewById(R.id.alterarDados);
        this.mViewHolder.gerarFolder = (Button) rootview.findViewById(R.id.gerarFolder);
        this.mViewHolder.notificacoes = (Button) rootview.findViewById(R.id.notificacoes);

        this.mViewHolder.alterarDados.setOnClickListener(this);
        this.mViewHolder.gerarFolder.setOnClickListener(this);
        this.mViewHolder.notificacoes.setOnClickListener(this);
        return inflater.inflate(R.layout.fragment_quadro_campanhas_cadastradas, container, false);
    }

    private static class ViewHolder {
        ImageView foto;
        Button alterarDados;
        Button notificacoes;
        Button gerarFolder;
        EditText nomeDesaparecido;
        EditText dataNascimentoDesaparecido;
        EditText dataDesaparecimento;
        EditText olhosDesaparecido;
        EditText cabeloDesaparecido;
        EditText sexoDesaparecido;
        EditText racaDesaparecido;
        EditText localDesaparecimento;
    }

    @Override
    public void onClick(View v) {
        int id = v.getId();
        if(id == R.id.alterarDados) {
            //logica do botao aqui
        } else if (id == R.id.gerarFolder){
            //logica do botao aqui
        } else if (id == R.id.notificacoes){
            //logica do botao aqui
        }
    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {

    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }
}
