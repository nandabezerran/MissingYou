package com.example.smile.missingyou;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.io.BufferedInputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import android.os.AsyncTask;



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
            URL url = null;
            try {
                url = new URL("http://52.67.179.63/missingYou/api/v1.0/selecionarUsuario/02");
            } catch (MalformedURLException e) {
                e.printStackTrace();
            }
            try {
                HttpURLConnection httpConn = (HttpURLConnection)url.openConnection();
                httpConn.setRequestMethod("GET");
                InputStream inputStream = httpConn.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = bufferedReader.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }


        }
        if (id==R.id.button_signup){
            Intent intent = new Intent(this, CadastroUsuarioActivity.class);
            startActivity(intent);
        }
    }
}
