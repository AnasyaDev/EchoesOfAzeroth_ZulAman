import csv, subprocess, tempfile, urllib.request, os, sys
from pathlib import Path
ids = [int(x) for x in open(sys.argv[1]).read().strip().split(",") if x]
out = Path(sys.argv[2]); done = {}
if out.exists():
    for r in csv.reader(open(out)):
        if r and r[0].isdigit(): done[int(r[0])] = r[1]
with open(out, "a") as fh:
    w = csv.writer(fh)
    for fdid in ids:
        if fdid in done: continue
        try:
            with tempfile.TemporaryDirectory() as d:
                t = Path(d)/f"{fdid}.mp3"
                req = urllib.request.Request(f"https://wago.tools/api/casc/{fdid}?download", headers={"User-Agent":"EchoesMusicAudit/1.0"})
                with urllib.request.urlopen(req, timeout=120) as resp, open(t,"wb") as h: h.write(resp.read())
                dur = subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1",str(t)], text=True, env=dict(os.environ, LC_ALL="C")).strip()
                w.writerow([fdid, f"{round(float(dur),1):.1f}"]); fh.flush()
        except Exception as e:
            w.writerow([fdid, f"error:{e}"]); fh.flush()
print("done")
