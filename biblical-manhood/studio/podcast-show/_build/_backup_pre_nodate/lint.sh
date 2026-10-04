#!/usr/bin/env bash
# usage: lint.sh file...
rc=0
for f in "$@"; do
  echo "== $f"
  rg -n "—|–" "$f" && { echo "  FAIL em/en dash"; rc=1; }
  rg -n "[“”‘’]" "$f" && { echo "  FAIL curly quotes"; rc=1; }
  rg -n -i "\b(additionally|crucial|delve|enduring|enhance|fostering|garner|interplay|intricate|landscape|pivotal|showcase|tapestry|testament|underscore|vibrant|serves as)\b" "$f" && { echo "  FAIL banned words"; rc=1; }
  rg -n -i "not just .{1,40} but " "$f" && echo "  WARN not-just-but"
  rg -n "\b(Anthony|Desmond|Calvin|Darnell|Barry|Horace|Rafael|Felix|Benny|Julian|Clarence|Chester|Boyd|Dewey|Manny|Silas|Warren|Tyrone|Vern|Tobias|Zeke|Sal|Woody|Stan|Dwight|Tadeo|Booker|Eli|Tomás|Walt|Roy|Marcus|Bernard|Gus|Jasper|Mario|Wade|Milo|Monty|Morris|Nolan|Otis|Owen|Carl|Ira)\b" "$f" && { echo "  FAIL banned story names"; rc=1; }
  rg -n -i "robert lewis|modern-day knight|men's fraternity|authentic manhood|fellowship bible|tim hawks|one mission" "$f" && { echo "  FAIL banned source names"; rc=1; }
  # Disclosure (SHOW-BIBLE section 13, locked 2026-10-03): exactly one credits line, Wes, after [CLOSING MUSIC 3s] and [CREDITS],
  # as the last spoken line of the script. Every other AI mention fails.
  dc=$(python3 _build/credits.py --check "$f"); [ -n "$dc" ] && { echo "  FAIL credits: $dc"; rc=1; }
  python3 _build/credits.py --strip "$f" | rg -n -i "\\bAI\\b|A\\.I\\.|AI-generated|made with AI|artificial intelligence|synthetic|composites? drawn|are characters|PENDING AARON" && { echo "  FAIL AI mention outside the credits slot (SHOW-BIBLE section 13)"; rc=1; }
  rg -q "DRAFT Walk Steadfast open" "$f" && echo "  WARN open is a DRAFT pending Aaron (SHOW-BIBLE section 5)"
  rg -q "Walk Steadfast open (written for|for) E" "$f" || echo "  WARN legacy intro (no entry in _build/intros_data.py yet, SHOW-BIBLE section 5)"
  rg -n -i "\b(uh|um|umm|uhh)\b" "$f" && { echo "  FAIL filler"; rc=1; }
  rg -n -i "^#.*go first|title.*go first" "$f" && { echo "  FAIL Go First as title"; rc=1; }
  rg -n -i "front step|leather notebook|napkin|deleted text" "$f" && { echo "  FAIL training images"; rc=1; }
  rg -n -i "\\\$[0-9]" "$f" | rg -v "^.*(PROD|NOTE)" && echo "  WARN price mention"
  rg -n -i "(book.s coming|it.s coming at walksteadfast|and it.s coming\. walksteadfast|comes out this week|is coming at walksteadfast|\(coming\)|training when it.s out)" "$f" >/dev/null && echo "  WARN future-tense plug wording (SHOW-BIBLE section 8a, see _build/tense_sweep.py)"
  body=$(python3 -c "import sys;s=open('$f').read();print(s.split('## Script',1)[-1].split('\n## Shorts',1)[0])")
  e=$(printf '%s' "$body" | rg -o "[a-z,]\.\.\. ?[a-z]" | wc -l); echo "  mid-line ellipses: $e (max 4)"; [ "$e" -gt 4 ] && rc=1
  p=$(printf '%s' "$body" | rg -o "\[pause [12]s\]" | wc -l); echo "  long pauses: $p (max 3)"; [ "$p" -gt 3 ] && rc=1
  bt=$(printf '%s' "$body" | rg -o "\(beat\)" | wc -l); bmax=10; case "$f" in *field-notes*) bmax=9;; esac
  echo "  beats: $bt (max $bmax)"; [ "$bt" -gt "$bmax" ] && echo "  WARN beat budget (round 5)"
  w=$(rg "^(WES|JONATHON):" "$f" | sed -E 's/^(WES|JONATHON): //; s/\([^)]*\)//g; s/\[[^]]*\]//g' | wc -w); echo "  spoken words: $w"
  ww=$(rg "^WES:" "$f" | sed -E 's/^WES: //; s/\([^)]*\)//g; s/\[[^]]*\]//g' | wc -w); echo "  Wes words: $ww"
  n1112=$(rg -o -i "^(WES|JONATHON):.*" "$f" | rg -o -i "\b(eleven|twelve)\b" | wc -l); echo "  INFO eleven/twelve spoken: $n1112 (round 7 number check)"
done
echo "== open system (all intros in _build/intros_data.py)"
python3 _build/intro_lint.py | sed "s/^/  /" | rg "FAIL|WARN|intros " ; python3 _build/intro_lint.py | rg -q "^FAIL" && rc=1
exit $rc
