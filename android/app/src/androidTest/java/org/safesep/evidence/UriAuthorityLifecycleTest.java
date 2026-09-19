package org.safesep.evidence;

import static org.junit.Assert.*;
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

/** Controlled cross-package URI grant/revoke calibration. */
@RunWith(AndroidJUnit4.class)
public class UriAuthorityLifecycleTest {
    private static final String TAG="SAFESEP_EVIDENCE";
    private static final Uri URI=Uri.parse("content://org.safesep.evidence.synthetic/token");

    private boolean canRead(Context c) {
        try (InputStream in=c.getContentResolver().openInputStream(URI)) {
            return in != null && in.read() >= 0;
        } catch (Exception e) {
            return false;
        }
    }

    @Test public void explicitRevokeInvalidatesOldGrantAndFreshRegrantRestoresIt() {
        Context owner=InstrumentationRegistry.getInstrumentation().getTargetContext();
        Context probe=InstrumentationRegistry.getInstrumentation().getContext();
        String probePackage=probe.getPackageName();

        owner.grantUriPermission(probePackage, URI, Intent.FLAG_GRANT_READ_URI_PERMISSION);
        boolean before=canRead(probe);

        owner.revokeUriPermission(probePackage, URI, Intent.FLAG_GRANT_READ_URI_PERMISSION);
        boolean afterRevoke=canRead(probe);

        owner.grantUriPermission(probePackage, URI, Intent.FLAG_GRANT_READ_URI_PERMISSION);
        boolean afterRegrant=canRead(probe);
        owner.revokeUriPermission(probePackage, URI, Intent.FLAG_GRANT_READ_URI_PERMISSION);

        Log.i(TAG, "{\"case\":\"uri_explicit_revoke\",\"sdk\":" + Build.VERSION.SDK_INT +
                ",\"before\":" + before + ",\"after_revoke\":" + afterRevoke +
                ",\"after_regrant\":" + afterRegrant + "}");

        assertTrue("grant must enable synthetic read", before);
        assertFalse("explicit revoke must remove synthetic read authority", afterRevoke);
        assertTrue("fresh re-grant must restore synthetic read authority", afterRegrant);
    }
}
