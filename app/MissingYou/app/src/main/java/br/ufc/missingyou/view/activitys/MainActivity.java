package br.ufc.missingyou.view.activitys;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import br.ufc.missingyou.R;
import br.ufc.missingyou.view.dialogs.PopUpAjudaEnviada;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private ViewHolder mViewHolder = new ViewHolder();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        getSupportActionBar().setDisplayShowTitleEnabled(false);

        this.mViewHolder.buttonLogin = (Button) findViewById(R.id.button_login);
        this.mViewHolder.buttonCadastrese = (Button) findViewById(R.id.button_signup);
        this.mViewHolder.editEmailLogin = (EditText) findViewById(R.id.edit_email_login);
        this.mViewHolder.editSenhaLogin = (EditText) findViewById(R.id.edit_senha_login);

        this.mViewHolder.buttonLogin.setOnClickListener(this);
        this.mViewHolder.buttonCadastrese.setOnClickListener(this);

    }

    private static class ViewHolder {
        Button buttonLogin;
        Button buttonCadastrese;
        EditText editEmailLogin;
        EditText editSenhaLogin;
    }

    @Override
    public void onClick(View view) {
        int id = view.getId();
        if (id == R.id.button_login) {
            //adicionar aqui a intent pro feed
           // Intent intent = new Intent(this, NavBar.class);
            // startActivity(intent);
            Intent intent = new Intent(this, PopUpAjudaEnviada.class);
            startActivity(intent);
        }
        if (id==R.id.button_signup){
            Intent intent = new Intent(this, CadastroUsuarioActivity.class);
            startActivity(intent);
        }
    }
}
