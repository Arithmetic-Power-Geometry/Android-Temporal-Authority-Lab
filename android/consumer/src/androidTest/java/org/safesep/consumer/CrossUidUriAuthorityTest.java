package org.safesep.consumer;

import static org.junit.Assert.*;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Build;
import android.util.Log;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import androidx.test.platform.app.InstrumentationRegistry;
import java.io.InputStream;
import org.junit.Test;
import org.junit.runner.RunWith;

@RunWith(AndroidJUnit4.class)
public class CrossUidUriAuthorityTest {
  private static final String TAG="SAFESEP_EVIDENCE";
  private static final Uri URI=Uri.parse("content://org.safesep.evidence.synthetic/token");

  private boolean canRead(Context c){
    try(InputStream in=c.getContentResolver().openInputStream(URI)){
      return in!=null && in.read()>=0;
    }catch(Exception e){ return false; }
  }
  private void invoke(Context c,String cls) throws Exception{
    Intent i=new Intent().setComponent(new ComponentName("org.safesep.evidence",cls))
      .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
    c.startActivity(i);
    Thread.sleep(500);
  }

  @Test public void crossUidExplicitRevokeInvalidatesAndRegrantRestores() throws Exception {
    Context consumer=InstrumentationRegistry.getInstrumentation().getTargetContext();
    assertEquals("org.safesep.consumer",consumer.getPackageName());

    invoke(consumer,"org.safesep.evidence.GrantActivity");
    boolean before=canRead(consumer);
    invoke(consumer,"org.safesep.evidence.RevokeActivity");
    boolean afterRevoke=canRead(consumer);
    invoke(consumer,"org.safesep.evidence.GrantActivity");
    boolean afterRegrant=canRead(consumer);
    invoke(consumer,"org.safesep.evidence.RevokeActivity");

    Log.i(TAG,"{\"case\":\"cross_uid_uri_explicit_revoke\",\"sdk\":"+Build.VERSION.SDK_INT+
      ",\"before\":"+before+",\"after_revoke\":"+afterRevoke+",\"after_regrant\":"+afterRegrant+"}");

    assertTrue("fixed grant must enable cross-UID synthetic read",before);
    assertFalse("explicit revoke must remove cross-UID synthetic read authority",afterRevoke);
    assertTrue("fresh grant must restore cross-UID synthetic read authority",afterRegrant);
  }
}
