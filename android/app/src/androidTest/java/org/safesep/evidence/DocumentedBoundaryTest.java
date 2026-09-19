package org.safesep.evidence;

import static org.junit.Assert.*;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.Build;
import android.util.Log;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import androidx.test.platform.app.InstrumentationRegistry;
import org.junit.Test;
import org.junit.runner.RunWith;

/**
 * Defensive platform-baseline tests.
 *
 * These tests exercise only this package on an owned/emulated device. They do
 * not target third-party apps, credentials, user data, or exported components.
 * Their purpose is to prove that the evidence pipeline can distinguish a
 * documented cross-version security boundary from an anomaly.
 */
@RunWith(AndroidJUnit4.class)
public class DocumentedBoundaryTest {
    private static final String TAG = "SAFESEP_EVIDENCE";

    @Test
    public void immutablePendingIntentIgnoresFillInMutation() throws Exception {
        Context c = InstrumentationRegistry.getInstrumentation().getTargetContext();
        Intent base = new Intent("org.safesep.BASELINE").setPackage(c.getPackageName());
        PendingIntent pi = PendingIntent.getBroadcast(c, 101, base,
                PendingIntent.FLAG_IMMUTABLE | PendingIntent.FLAG_CANCEL_CURRENT);
        assertNotNull(pi);
        Log.i(TAG, "{\"case\":\"immutable_baseline\",\"sdk\":" + Build.VERSION.SDK_INT +
                ",\"result\":\"created\"}");
        pi.cancel();
    }

    @Test
    public void mutableImplicitCreationMatchesDocumentedApiBoundary() {
        Context c = InstrumentationRegistry.getInstrumentation().getTargetContext();
        boolean threw = false;
        try {
            Intent implicit = new Intent("org.safesep.SYNTHETIC_ONLY");
            PendingIntent pi = PendingIntent.getBroadcast(c, 102, implicit,
                    PendingIntent.FLAG_MUTABLE | PendingIntent.FLAG_CANCEL_CURRENT);
            if (pi != null) pi.cancel();
        } catch (IllegalArgumentException expected) {
            threw = true;
        }
        Log.i(TAG, "{\"case\":\"mutable_implicit_creation\",\"sdk\":" + Build.VERSION.SDK_INT +
                ",\"illegal_argument\":" + threw + "}");
        if (Build.VERSION.SDK_INT >= 34) assertTrue(threw);
        else assertFalse(threw);
    }
}
