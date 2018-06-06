package br.ufc.missingyou.view.activitys;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import br.ufc.missingyou.R;

public class CadastroUsuarioActivity extends AppCompatActivity implements View.OnClickListener{

    private ViewHolder mViewHolder = new ViewHolder();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cadastro_usuario);

        getSupportActionBar().setDisplayShowTitleEnabled(false);

        this.mViewHolder.buttonCadastrarUsuario = (Button) findViewById(R.id.button_cadastrar_usuario);
        this.mViewHolder.editEmailUsuario = (EditText) findViewById(R.id.edit_email_usuario);
        this.mViewHolder.editSenhaUsuario = (EditText) findViewById(R.id.edit_senha_usuario);
        this.mViewHolder.editNomeUsuario = (EditText) findViewById(R.id.edit_nome_usuario);

        this.mViewHolder.buttonCadastrarUsuario.setOnClickListener(this);

    }

    private static class ViewHolder {
        Button buttonCadastrarUsuario;
        EditText editNomeUsuario;
        EditText editEmailUsuario;
        EditText editSenhaUsuario;
    }

    @Override
    public void onClick(View view) {
        int id = view.getId();
        if (id == R.id.button_cadastrar_usuario) {
            Intent intent = new Intent(this, GuiaActivity.class);
            startActivity(intent);
        }
    }
}
