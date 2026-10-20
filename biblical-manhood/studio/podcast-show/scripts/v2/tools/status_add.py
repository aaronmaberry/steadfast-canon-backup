#!/usr/bin/env python3
"""Record a finished script in STATUS.md: progress row (from the checker), next pointer, ledger line.
Usage: status_add.py FILE NEXT "ledger text"   (ledger "-" = refresh row only) """
import os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
path, nxt, ledger = sys.argv[1], sys.argv[2], sys.argv[3]
out = subprocess.run([sys.executable, os.path.join(HERE, "check_script.py"), path], capture_output=True, text=True).stdout
ep = os.path.basename(path)[:4]
w = re.search(r"Spoken words: (\d+) \(about (\d\d:\d\d)", out)
ws = re.search(r"WES: \d+ lines, \d+ words \((\d+)%\)", out); js = re.search(r"JONATHON: \d+ lines, \d+ words \((\d+)%\)", out)
res = "PASS" if "PASS" in out.splitlines()[-1] else "FAIL"
st = open(os.path.join(ROOT, "STATUS.md")).read()
row = f"| {ep} | {os.path.basename(path)} | done | {int(w.group(1)):,} | {w.group(2)} | {ws.group(1)}/{js.group(1)} | {res} |"
st = re.sub(r"^\| " + ep + r" \|.*\n", "", st, flags=re.M)
st = re.sub(r"(\n\nNext: )[^\n]*", "\n" + row + r"\1" + nxt + ".", st, count=1)
if ledger != "-": st = st.replace("\n<!-- ledger-end -->", f"\n- {ep}: {ledger}\n<!-- ledger-end -->", 1)
open(os.path.join(ROOT, "STATUS.md"), "w").write(st)
print(row)
