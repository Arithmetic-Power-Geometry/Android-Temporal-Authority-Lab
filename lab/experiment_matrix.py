"""Generate a safe synthetic test matrix; execution is intentionally external."""
from lab.contracts import CONTRACTS

TRANSITIONS=("activity_finish","profile_lock","process_death","reboot","explicit_revoke")

def matrix():
    rows=[]
    for name,c in CONTRACTS.items():
      for t in TRANSITIONS:
        rows.append({"contract":name,"capability":c.capability,"transition":t,
                     "synthetic_data_only":True,"expected_old_after":c.expected_after_transition})
    return rows

if __name__=="__main__":
    rows=matrix()
    print({"cases":len(rows),"synthetic_only":all(r["synthetic_data_only"] for r in rows)})
