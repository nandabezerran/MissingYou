package br.ufc.missingyou.adapters;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.support.v4.app.FragmentActivity;
import android.support.v7.widget.CardView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.List;

import br.ufc.missingyou.R;
import br.ufc.missingyou.model.Quadro;
import br.ufc.missingyou.view.activitys.FeedQuadroDetailsActivity;

public class CustomListAdapter extends BaseAdapter {

    Activity context;
    LayoutInflater inflater;
    List<Quadro> feedItems;


    public CustomListAdapter(FragmentActivity activity, List<Quadro> quadros) {
        this.context = activity;
        this.feedItems = quadros;
    }

    @Override
    public int getCount() {
        return feedItems.size();
    }

    @Override
    public Object getItem(int position) {
        return feedItems.get(position);
    }

    @Override
    public long getItemId(int position) {
        return feedItems.indexOf(getItem(position));
    }


    private class ViewHolder{
        ImageView fotos;
        TextView nome;
        TextView data_desaparecimento;
        TextView local_desaparecimento;
        CardView card;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {

        ViewHolder holder = null;

        if(inflater == null){
            inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        }

        if (convertView == null) {
            convertView = inflater.inflate(R.layout.list_row, null);

        }

        holder = new ViewHolder();

        holder.fotos = (ImageView) convertView.findViewById(R.id.foto_desaparecido);
        holder.nome = (TextView) convertView.findViewById(R.id.nomes);
        holder.data_desaparecimento = (TextView) convertView.findViewById(R.id.datas_desaparecimento);
        holder.local_desaparecimento = (TextView) convertView.findViewById(R.id.locais_desaparecimento);
        holder.card = convertView.findViewById(R.id.card_view);

        final Quadro row_pos = feedItems.get(position);

        holder.fotos.setImageResource(row_pos.getFoto_id());
        holder.nome.setText(row_pos.getNome());
        holder.data_desaparecimento.setText(row_pos.getData_desaparecimento());
        holder.local_desaparecimento.setText(row_pos.getLocal_desaparecimento());

        holder.card.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent = new Intent(context, FeedQuadroDetailsActivity.class);

                intent.putExtra("quadro", row_pos);

                context.startActivity(intent);

            }
        });


        return convertView;
    }

}
