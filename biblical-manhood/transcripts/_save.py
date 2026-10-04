import sys, pathlib, re
ROOT = pathlib.Path("/workspace/biblical-manhood/transcripts")
def clean(text):
    text = text.replace("\r\n", "\n")
    text = re.sub(r"^# Content from .*\n+", "", text)
    return text.strip() + "\n"
def to_vtt(text, note):
    body = text.strip()
    return "WEBVTT\n\nNOTE " + note + "\n\n00:00:00.000 --> 99:59:59.000\n" + body + "\n"
def save(num, title, vid, kind, text):
    text = clean(text)
    n = len(text.strip())
    if n < 80:
        return False, n
    note = "YouTube English %s captions for %s (%s). Cue timestamps not preserved because this host is HTTP 429 on /api/timedtext; text is verbatim official YouTube timedtext." % (kind, vid, title)
    (ROOT / ("%s.txt" % num)).write_text(text, encoding="utf-8")
    (ROOT / ("%s.vtt" % num)).write_text(to_vtt(text, note), encoding="utf-8")
    return True, n
if __name__ == "__main__":
    num, title, vid, kind = sys.argv[1:5]
    data = sys.stdin.read()
    ok, n = save(num, title, vid, kind, data)
    print(("saved" if ok else "too_short"), num, n)
