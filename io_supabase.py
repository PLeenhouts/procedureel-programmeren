import os
from supabase import create_client

SUPABASE_URL = "https://nihnfwgfjbxvhpzydmsi.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable_UrtwPC-nTqxru91e-Z242w_uKcigEL7"
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

def import_cijfer_overzicht():
    toetsen_rows = (supabase.table("toetsen").select("id, naam").order("id").execute().data)
    toetsen = [r["naam"] for r in toetsen_rows]
    toets_ids = [r["id"] for r in toetsen_rows]

    leerlingen_rows = (supabase.table("leerlingen").select("id, naam").order("id").execute().data)
    leerlingen = [r["naam"] for r in leerlingen_rows]
    leerling_ids = [r["id"] for r in leerlingen_rows]

    cijfers_rows = (supabase.table("cijfers").select("leerling_id, toets_id, cijfer").execute().data)

    cijfer_map = {(r["leerling_id"], r["toets_id"]): r["cijfer"] for r in cijfers_rows}

    cijfers = []
    for lid in leerling_ids:
        rij = []
        for tid in toets_ids:
            rij.append(cijfer_map.get((lid, tid), None))
        cijfers.append(rij)

    return toetsen, leerlingen, cijfers