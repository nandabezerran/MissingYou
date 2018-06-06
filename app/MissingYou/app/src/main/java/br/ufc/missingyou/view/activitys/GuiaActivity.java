package br.ufc.missingyou.view.activitys;

import android.content.Intent;
import android.os.Bundle;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import br.ufc.missingyou.R;
import br.ufc.missingyou.adapters.ImageAdapter;


public class GuiaActivity extends AppCompatActivity implements View.OnClickListener{

    private ViewHolder mViewHolder = new ViewHolder();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_guia);
        getSupportActionBar().setTitle("Guia");
        ViewPager viewPager = findViewById(R.id.viewPager);
        ImageAdapter adapter = new ImageAdapter(this);
        viewPager.setAdapter(adapter);
        getSupportActionBar().setDisplayShowTitleEnabled(false);
        getSupportActionBar().setDisplayShowHomeEnabled(true);
        getSupportActionBar().setIcon(R.mipmap.ic_launcher);

        this.mViewHolder.buttonPular= (Button) findViewById(R.id.button_pular);

        this.mViewHolder.buttonPular.setOnClickListener(this);
    }

    private static class ViewHolder {
        Button buttonPular;
    }

    @Override
    public void onClick(View view) {

        int id = view.getId();

        if (id == R.id.button_pular) {
            Intent intent = new Intent(this, CadastroUsuarioActivity.class);
            startActivity(intent);
        }

    }
}
