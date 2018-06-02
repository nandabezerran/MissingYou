package com.example.smile.missingyou;

import android.app.Activity;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.DisplayMetrics;
import android.view.View;
import android.widget.Button;

public class PopUpCPF extends Activity implements View.OnClickListener {

    private ViewHolder mViewHolder = new ViewHolder();
    @Override
    protected void onCreate( Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.popup_cpf);

        DisplayMetrics dm = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(dm);

        this.mViewHolder.buttonOk = (Button) findViewById(R.id.button_ok);

        this.mViewHolder.buttonOk.setOnClickListener(this);

        int width = dm.widthPixels;
        int height = dm.heightPixels;

        getWindow().setLayout((int)(width*.8), (int)(height*.2));
    }
    private static class ViewHolder {
        Button buttonOk;
    }

    @Override
    public void onClick(View view) {
        int id = view.getId();
        if (id == R.id.button_ok) {
            finish();
        }
    }
}
