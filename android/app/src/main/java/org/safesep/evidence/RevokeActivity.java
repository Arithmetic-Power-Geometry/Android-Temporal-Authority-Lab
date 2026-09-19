package org.safesep.evidence;
import android.app.Activity; import android.content.Intent; import android.net.Uri; import android.os.Bundle; import android.util.Log;
public final class RevokeActivity extends Activity {
  @Override protected void onCreate(Bundle b){ super.onCreate(b);
    Uri u=Uri.parse("content://org.safesep.evidence.synthetic/token");
    revokeUriPermission("org.safesep.consumer",u,Intent.FLAG_GRANT_READ_URI_PERMISSION);
    Log.i("SAFESEP_EVIDENCE","{\"control\":\"revoke\",\"consumer\":\"org.safesep.consumer\"}");
    finish();
  }
}
