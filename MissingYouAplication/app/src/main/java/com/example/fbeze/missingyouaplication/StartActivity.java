package com.example.fbeze.missingyouaplication;

        import android.app.Activity;
        import android.content.Intent;
        import android.os.Bundle;
import android.widget.TextView;

import com.amazonaws.mobile.auth.core.IdentityManager;
import com.amazonaws.mobile.auth.core.IdentityProvider;
import com.amazonaws.mobile.auth.core.SignInResultHandler;
import com.amazonaws.mobile.auth.ui.AuthUIConfiguration;
import com.amazonaws.mobile.auth.ui.SignInActivity;

public class StartActivity extends Activity {



    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        AWSProvider.initialize(getApplicationContext());

        //setContentView(R.layout.activity_main);

        final IdentityManager identityManager = AWSProvider.getInstance().getIdentityManager();
        // Set up the callbacks to handle the authentication response
        identityManager.login(this, new SignInResultHandler() {
            @Override
            public void onSuccess(Activity activity, IdentityProvider identityProvider) {

                // Go to the main activity
                final Intent intent = new Intent(activity, WallActivity.class)
                        .setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
                activity.startActivity(intent);
                activity.finish();
            }

            @Override
            public void onIntermediateProviderCancel(Activity callingActivity, IdentityProvider provider) {

            }

            @Override
            public void onIntermediateProviderError(Activity callingActivity, IdentityProvider provider, Exception ex) {

            }

            @Override
            public boolean onCancel(Activity activity) {
                return false;
            }
        });

        // Start the authentication UI
        AuthUIConfiguration config = new AuthUIConfiguration.Builder()
                .userPools(true)
                .build();
        SignInActivity.startSignInActivity(this, config);
        StartActivity.this.finish();

    }
}