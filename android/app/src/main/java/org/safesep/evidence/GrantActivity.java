package org.safesep.evidence;
import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
public final class GrantActivity extends Activity {
  @Override protected void onCreate(Bundle b){ super.onCreate(b);
    grantUriPermission("org.safesep.consumer",Uri.parse("content://org.safesep.evidence.synthetic/token"),Intent.FLAG_GRANT_READ_URI_PERMISSION);
    finish();
  }
}
