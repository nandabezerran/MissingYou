package br.ufc.missingyou.adapters;

import android.content.Context;
import android.support.annotation.NonNull;
import android.support.v4.view.PagerAdapter;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import br.ufc.missingyou.R;


public class ImageAdapter extends PagerAdapter {
    private Context mContext;
    private int[] mImageIds = new int []{R.drawable.guiacadastro, R.drawable.guiaajuda, R.drawable.guiafeed,
            R.drawable.guiainformacao, R.drawable.guiasalvar, R.drawable.guiafolder, R.drawable.guiamapa };

    public ImageAdapter(Context context){
        mContext = context;
    }

    @Override
    public int getCount() {
        return mImageIds.length;
    }

    @Override
    public boolean isViewFromObject(@NonNull View view, @NonNull Object object) {
        return view == object;
    }

    @NonNull
    @Override
    public Object instantiateItem(@NonNull ViewGroup container, int position) {
        ImageView imageView = new ImageView(mContext);
        imageView.setScaleType(ImageView.ScaleType.CENTER_CROP);
        imageView.setImageResource(mImageIds[position]);
        imageView.setAdjustViewBounds(true);
        container.addView(imageView, 0);
        return imageView;
    }

    @Override
    public void destroyItem(@NonNull ViewGroup container, int position, @NonNull Object object) {
        container.removeView((ImageView)object);
    }
}

