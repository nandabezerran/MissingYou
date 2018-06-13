package com.example.smile.missingyou;

import android.content.Intent;
import android.os.StrictMode;
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

    private String serverAddress = "http://52.67.179.63/missingYou/api/v1.0/";
    private String loginRequest = "validarLogin/%1$s/%2$s";


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

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);

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
                String password = mViewHolder.editSenhaLogin.getText().toString();
                String email = mViewHolder.editEmailLogin.getText().toString();
                url = new URL(serverAddress + String.format(loginRequest, password, email));
            } catch (MalformedURLException e) {
                e.printStackTrace();
            }
            try {
                assert url != null;
                HttpURLConnection httpConn = (HttpURLConnection)url.openConnection();
                httpConn.setRequestMethod("GET");
                httpConn.connect();
                InputStream inputStream = httpConn.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                String line = bufferedReader.readLine();
                System.out.println(line);
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
