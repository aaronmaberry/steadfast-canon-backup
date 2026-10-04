# Biblical Manhood (One Mission Men) — access notes

Probed 2026-08-27. Nothing was published, purchased, or transcribed into chat.
Organization: Planning Center org `499515` (One Mission Bible Church, Leander, TX).
Channel: [One Mission Men](https://onemissionbible.churchcenter.com/channels/27610) (id `27610`).

## Bottom line

| Question | Answer |
| --- | --- |
| Is catalog public? | **Yes.** 24 episodes, titles, dates, speakers, series. |
| Is video public? | **Playable without a Church Center login.** Hosted as **unlisted YouTube** embeds on `@onemissionbible`. oEmbed succeeds; videos are **not** in the channel’s public RSS. |
| Media host | **YouTube** (`library_streaming_service: youtube`). No Vimeo, Mux, m3u8, Boxcast, or Resi on this channel. |
| Audio / podcast | **None.** `enabled_formats.audio=false`, `podcast=false`, `podcast_feed_url=null`, `library_audio_url=null`. |
| Captions / transcripts | **Not recovered.** Church Center has no caption/transcript objects. YouTube timedtext was **HTTP 429** here; player/watch pages bot-gated. Do not assume captions exist. |
| Sermon notes | **Yes, public JSON.** Fill-in-the-blank outlines for sessions 01–22 via `/publishing/v2/episodes/{id}/note_template`. Sessions 23–24: 404 (no template). Saved under `notes/`, not `transcripts/`. |
| Login required? | Not for catalog, video playback via YouTube URL, or note templates. Anonymous org Bearer is enough for the Church Center Publishing JSON. |

## What worked

### 1. Public HTML (JS-rendered)

Church Center is a React Router **SPA** (`ssr:false`). `curl` of page URLs returns a ~6468-byte hydration shell — **not** episode content. Ignore `/workspace/biblical-manhood/raw/{id}.html`.

A JS-executing fetch of the channel/episode list **does** return titles:

- Channel: https://onemissionbible.churchcenter.com/channels/27610
- Episode index: https://onemissionbible.churchcenter.com/channels/27610/episodes
- **Working episode URL:** `https://onemissionbible.churchcenter.com/episodes/{id}`  
  Nested `.../channels/27610/episodes/{id}` 404s (route is `/episodes/:episodeId`, not nested).

### 2. Session bootstrap (unauthenticated)

These same-origin JSON endpoints work **without login**:

```
GET  https://onemissionbible.churchcenter.com/sessions/check
     -> AnonymousPerson

POST https://onemissionbible.churchcenter.com/sessions/tokens
     Accept: application/json
     -> { data: { type: "Bearer", attributes: { token: "ort_...", expires_at }, 
          relationships: { organization: { data: { id: "499515" } } } } }
```

Token type is an **organization Bearer** (`ort_…`), ~2 hour TTL. Authorization header format used by the SPA: `Bearer <token>`. Do not treat this as a secret; any visitor can mint one. Do not persist live tokens.

### 3. Church Center Publishing JSON (the real catalog/media API)

**Working host:** `https://api.churchcenter.com`  
Headers: `Accept: application/json`, `Authorization: Bearer <ort_token>`, `X-PCO-API-Version: 2024-03-25`

Confirmed 200s:

| Path | Result |
| --- | --- |
| `/publishing/v2/channels/27610` | Channel “One Mission Men”; `enabled_formats.on_demand_video=true`, `sermon_notes=true`, audio/podcast/live false |
| `/publishing/v2/channels/27610/episodes?per_page=100&include=series,speakerships,speakerships.speaker` | All **24** episodes + YouTube `library_video_url` |
| `/publishing/v2/channels/27610/series` | Fall 2025 (`81067`), Spring 2026 (`81068`) |
| `/publishing/v2/channels/27610/speakers` | Tim Hawks (`186234652`), Cindy Hawks (`186496657`) |
| `/publishing/v2/episodes/{id}?include=channel,series,speakerships.speaker,episode_resources,note_template` | Per-episode media + notes |
| `/publishing/v2/episodes/{id}/note_template` | Outline HTML (01–22) |
| `/publishing/v2/episodes/{id}/episode_resources` | Empty array (sampled) |

Each episode has:

- `library_streaming_service`: `"youtube"`
- `library_video_url`: `https://www.youtube.com/embed/{id}?rel=0`
- `library_video_embed_code`: iframe
- `library_video_thumbnail_url`: `https://img.youtube.com/vi/{id}/maxresdefault.jpg`
- `church_center_url`: `/episodes/{id}`
- no `video_url` / live stream (on-demand library only)

JS bundles (`Episode-DZaN9JJU.js`, `queries-BgMR0Pci.js`) call these same `/publishing/v2/...` paths. They also reference Vimeo/YouTube **player** scripts as generic embed hosts; this series only uses YouTube. No GraphQL. No `m3u8` / Mux / caption API strings for this app surface.

### 4. YouTube (playable media)

All 24 oEmbed lookups succeeded (`author_name`: One Mission Bible Church, `author_url`: https://www.youtube.com/@onemissionbible).

Public channel RSS `https://www.youtube.com/feeds/videos.xml?channel_id=UCRag0ZnjkQAA06JqZMGxCng` lists Sunday sermons, **not** these Biblical Manhood IDs → treat as **unlisted but world-playable** with the URL.

No separate Vimeo/podcast mirrors found on the public web. Hawks newsletter ([hawksonmission.curated.co](https://hawksonmission.curated.co/)) mentions “One Mission Bible Church Men’s Biblical Manhood Study — Semester Review” but does not host the series.

## What is gated / did not work

| Endpoint | Result |
| --- | --- |
| `https://onemissionbible.churchcenter.com/channels/27610[.json|/episodes.json]` and `Accept: application/json` | SPA HTML shell (~6.5KB), not JSON |
| Remix `?_data=` / `?_routes=` variants | Same SPA HTML (client-side SPA, no SSR data) |
| `https://onemissionbible.churchcenter.com/publishing/v2/...` | 404 SPA HTML (API is not same-origin) |
| `https://api.onemissionbible.churchcenter.com/...` | TLS SAN mismatch (`*.churchcenter.com` does not cover three-level names); `-k` then 502 |
| `https://api.planningcenteronline.com/publishing/v2/...` | **401** without a PCO developer PAT/OAuth (official API is gated) |
| `https://api.planningcenteronline.com/media/v1/` and `media/v2/` | **404** JSON “Not Found” — those product prefixes do not exist |
| GraphQL | None referenced in the Church Center JS bundles |
| YouTube `/api/timedtext` | **429** Sorry page from this IP |
| YouTube watch HTML / innertube `player` | Bot wall (`LOGIN_REQUIRED` / “video unavailable”) from this datacenter |
| Church Center `audio_download` | N/A — no sermon audio file (`source: default`, empty name) |
| Sessions 23–24 `note_template` | HTTP 404 |

## JS bundle notes

HTML modulepreload list (on `onemissionbible.churchcenter.com`):

- `/assets/client/assets/manifest-d825a424.js`
- `entry.client-PierW_Yh.js`, `vendor-CPMdfHCh.js`, `root-DmccKtbu.js`, …

API client in `vendor-CPMdfHCh.js`:

- Origin helper `Mx("api")` → `https://api.<host>`  
  On the church subdomain that yields the broken `api.onemissionbible.churchcenter.com`. In practice the working public API is **`https://api.churchcenter.com`** with the org Bearer.
- Token mint: `POST /sessions/tokens` (same origin as the SPA).
- Publishing includes used by the episode page: `channel,episode_times,episode_resources,person_episode_progress,series,note_template,speakerships.speaker`.

Grep hits for `vimeo` / `youtube` are generic embed players, not this series’ host. No `transcript`, `caption`, `.vtt`, `.srt`, `m3u8`, or `mux` usage on the episode path.

## Series shape

Two published series:

1. **Biblical Manhood - Fall 2025** (series `81067`) — Sep 12 – Nov 14, 2025 — 10 episodes  
2. **Biblical Manhood - Spring 2026** (series `81068`) — Jan 23 – Apr 29, 2026 — 14 episodes (API `episodes_count` 15 includes the extra spring session count as stored)

Speakers: Tim Hawks for 23 sessions; **Cindy Hawks for session 16** (“25 Ways to be a Servant Leader”, 2026-02-25 CT, YouTube `apJIZ8QYT_E`).

## Caption / transcript decision

- Did **not** fabricate transcripts.
- Did **not** save anything under `transcripts/` except a README explaining the gap.
- Outlines (not speech-to-text) are in `/workspace/biblical-manhood/notes/{nn}-{slug}.md` for sessions 01–22.

A browser session on a residential IP could re-check YouTube captions (`watch` page `captionTracks` or timedtext). This environment cannot.

## Files written

- `/workspace/biblical-manhood/access-notes.md` (this file)
- `/workspace/biblical-manhood/catalog.json` (24 episodes)
- `/workspace/biblical-manhood/notes/*.md` (22 outlines)
- `/workspace/biblical-manhood/transcripts/README.md`
- `/workspace/biblical-manhood/api-probes/` (raw JSON from working endpoints; JS copies under `js/`)
