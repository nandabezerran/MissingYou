package br.ufc.missingyou.view.activitys;

import android.support.v4.app.FragmentActivity;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.ListFragment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import android.content.res.TypedArray;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;

import java.util.ArrayList;
import java.util.List;
import android.view.Menu;
import android.widget.ListView;

import br.ufc.missingyou.R;
import br.ufc.missingyou.view.fragments.Feed;


public class FeedActivity extends AppCompatActivity {

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        getSupportActionBar().setTitle("Missing You");



        Feed feed = new Feed();
        getSupportFragmentManager().beginTransaction().add(R.id.container, feed).commit();

    }
}
