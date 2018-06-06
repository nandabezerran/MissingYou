package br.ufc.missingyou.view.fragments;


import android.content.res.TypedArray;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ListView;

import java.util.ArrayList;
import java.util.List;

import br.ufc.missingyou.R;
import br.ufc.missingyou.adapters.CustomListAdapter;
import br.ufc.missingyou.model.Quadro;


public class MinhasCampanhas extends Fragment {

    String[] nomes;
    TypedArray fotos;
    String[] locais_desaparecimento;
    String[] data_desaparecimentos;

    List<Quadro> quadros;
    ListView listView;


    public MinhasCampanhas() {
        // Required empty public constructor
    }


    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        quadros = new ArrayList<Quadro>();

        nomes = getResources().getStringArray(R.array.Nomes);
        locais_desaparecimento = getResources().getStringArray(R.array.locais);
        data_desaparecimentos = getResources().getStringArray(R.array.datas);
        fotos = getResources().obtainTypedArray(R.array.fotos);

        for(int i = 0; i < 2; i++){
            Quadro quadro = new Quadro(fotos.getResourceId(i, -1), nomes[i], locais_desaparecimento[i], data_desaparecimentos[i]);
            quadros.add(quadro);
        }

        View view = inflater.inflate(R.layout.fragment_feed, container, false);
        //nao sei se ta certo DUVIDA
        listView = (ListView) view.findViewById(R.id.list);
        CustomListAdapter adapter = new CustomListAdapter(getActivity(), quadros);
        listView.setAdapter(adapter);
        // Inflate the layout for this fragment
        return view;
    }

}
