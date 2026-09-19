package org.safesep.evidence;

import android.content.ContentProvider;
import android.content.ContentValues;
import android.database.Cursor;
import android.net.Uri;
import android.os.ParcelFileDescriptor;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.nio.charset.StandardCharsets;

/** Synthetic read-only provider used only for owned-emulator authority tests. */
public final class SyntheticProvider extends ContentProvider {
    public static final String AUTHORITY = "org.safesep.evidence.synthetic";
    @Override public boolean onCreate() { return true; }
    @Override public String getType(Uri uri) { return "text/plain"; }
    @Override public Cursor query(Uri u,String[] p,String s,String[] a,String sort){ return null; }
    @Override public Uri insert(Uri u, ContentValues v){ throw new UnsupportedOperationException(); }
    @Override public int delete(Uri u,String s,String[] a){ throw new UnsupportedOperationException(); }
    @Override public int update(Uri u,ContentValues v,String s,String[] a){ throw new UnsupportedOperationException(); }

    @Override public ParcelFileDescriptor openFile(Uri uri, String mode) throws FileNotFoundException {
        if (!"/token".equals(uri.getPath()) || !"r".equals(mode)) throw new FileNotFoundException();
        try {
            ParcelFileDescriptor[] pipe = ParcelFileDescriptor.createPipe();
            new Thread(() -> {
                try (FileOutputStream out = new FileOutputStream(pipe[1].getFileDescriptor())) {
                    out.write("synthetic-authority-evidence".getBytes(StandardCharsets.UTF_8));
                } catch (Exception ignored) {}
                try { pipe[1].close(); } catch (Exception ignored) {}
            }).start();
            return pipe[0];
        } catch (Exception e) {
            throw new FileNotFoundException(e.toString());
        }
    }
}
