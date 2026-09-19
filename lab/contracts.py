"""Conservative contracts derived from public Android documentation.

These are benchmark hypotheses, not claims that every transition revokes every
capability. A platform experiment must bind a transition to the relevant documented
contract before a mismatch is meaningful.
"""
from lab.semantics_oracle import Contract,Lifetime

CONTRACTS={
 "temporary_uri_activity_lifetime":Contract(
   "temporary_uri",Lifetime.ACTIVITY,False,
   "Activity docs: URI access granted for an Activity remains until that Activity finishes."),
 "persistable_uri_until_explicit_revoke":Contract(
   "persistable_uri",Lifetime.EXPLICIT_REVOCATION,True,
   "Intent docs: persistable URI permission may persist across reboot until explicitly revoked."),
 "private_profile_execution_while_locked":Contract(
   "profile_execution",Lifetime.PROFILE_AVAILABLE,False,
   "Android Private Space docs: locking stops the private profile and its apps."),
 "pending_intent_creator_authority":Contract(
   "pending_intent",Lifetime.CREATOR_DEFINED,True,
   "PendingIntent is delegated execution as creator; persistence alone is not treated as anomaly.")
}
