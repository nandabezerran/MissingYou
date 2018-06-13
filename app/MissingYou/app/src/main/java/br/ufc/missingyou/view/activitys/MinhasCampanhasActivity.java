package br.ufc.missingyou.view.activitys;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;

import br.ufc.missingyou.R;
import br.ufc.missingyou.view.fragments.MinhasCampanhas;

public class MinhasCampanhasActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_minhas_campanhas);

        getSupportActionBar().setTitle("Minhas Campanhas Cadastradas");

        MinhasCampanhas feed = new MinhasCampanhas();
        getSupportFragmentManager().beginTransaction().add(R.id.container, feed).commit();
    }
}
