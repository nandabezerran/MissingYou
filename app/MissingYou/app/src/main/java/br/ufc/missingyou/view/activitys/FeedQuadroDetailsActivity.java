package br.ufc.missingyou.view.activitys;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.widget.TextView;

import br.ufc.missingyou.R;
import br.ufc.missingyou.model.Quadro;

public class FeedQuadroDetailsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_feed_quadro_details);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        Quadro quadro = (Quadro) getIntent().getSerializableExtra("quadro");
        TextView nome = (TextView) findViewById(R.id.nome);
        nome.setText(quadro.getNome());

    }


    @Override
    public boolean onOptionsItemSelected(MenuItem item) {

        switch (item.getItemId()){
            case android.R.id.home:  finish();
        }


        return super.onOptionsItemSelected(item);
    }
}
