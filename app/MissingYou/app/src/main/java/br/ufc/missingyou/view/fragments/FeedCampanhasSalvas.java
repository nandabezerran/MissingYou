package br.ufc.missingyou.view.fragments;


import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import br.ufc.missingyou.R;


/**
 * A simple {@link Fragment} subclass.
 */
public class FeedCampanhasSalvas extends Fragment {


    public FeedCampanhasSalvas() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_feed_campanhas_salvas, container, false);
    }

}
