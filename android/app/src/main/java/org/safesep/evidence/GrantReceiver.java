package org.safesep.evidence;
import android.content.BroadcastReceiver; import android.content.Context; import android.content.Intent; import android.net.Uri; import android.util.Log;
public final class GrantReceiver extends BroadcastReceiver {
  @Override public void onReceive(Context c,Intent i){
    Uri u=Uri.parse("content://org.safesep.evidence.synthetic/token");
    c.grantUriPermission("org.safesep.consumer",u,Intent.FLAG_GRANT_READ_URI_PERMISSION);
    Log.i("SAFESEP_EVIDENCE","{\"control\":\"grant_receiver\"}");
  }
}
