# Podcast distribution: hosts, costs, recommendation

Internal. Researched 2026-10-02. **Nothing is signed up or paid for.** All prices come from the vendors' pages or from third-party price checks dated Sep 2026, as cited, and should be rechecked on the day Aaron buys. Sources are listed in `research/_notes-raw.md` and the dossier.

## How the pieces fit

- **YouTube (video).** Upload the full video episodes directly in YouTube Studio. It's free. Put them in a playlist and set that playlist as a podcast in YouTube Studio, so they show up under YouTube's Podcasts and in YouTube Music.
  - Don't use YouTube's RSS ingestion for this show. RSS ingestion is for audio-first shows: YouTube builds static-image videos from the show art and uploads every new feed episode. Using it would put a duplicate, picture-less copy of each episode on the channel (YouTube Help 13525207).
- **Apple Podcasts and Spotify (audio, optionally video).**
  - Both read a podcast RSS feed that a hosting company makes.
  - Submitting to Apple Podcasts Connect is free. It needs an Apple Account, an RSS feed with at least one episode and the required tags, and square 3000x3000 cover art (JPG or PNG, RGB).
  - Spotify submission is free too.
  - Video on Apple: since Feb 2026, Apple plays video podcasts through HLS from participating hosting companies. The launch partners were Acast, ART19, Omny Studio and SiriusXM/Simplecast, with others joining. Buzzsprout says its Audio + Video plan adds video distribution to Apple Podcasts.
  - Video on Spotify: Spotify for Creators accepts video uploads and plays them on Spotify. Other apps get the audio through the RSS feed.

## Hosting options

| Host | Price (as listed) | What fits our show | Pros | Cons |
|---|---|---|---|---|
| **Spotify for Creators** | Free | Free hosting plus an RSS feed. Video episodes play on Spotify. | $0. Video on Spotify natively. Simple. Spotify monetization programs live here. | Video stays on Spotify only. Apple gets audio only. Thinner analytics and portability than the paid hosts. Ties the show to one platform's tool. |
| **Buzzsprout** | Free plan (2 h/month, episodes hosted 90 days). Audio: $18/mo or $180/yr (6 h/month). **Audio + Video: $30/mo or $300/yr** (video to Apple Podcasts). Overage $2-4/h on monthly plans. Archive plan $5/mo. | Our upload is about 3.5 h/month at two a week (4.3 main episodes at about 35 min, plus 4.3 Field Notes at about 14 min). That fits the 6 h plan. | The easiest tool in the field. Strong help docs. Video to Apple. IAB-certified stats. Magic Mastering and Cohost AI add-ons ($60/yr each, optional). | Priced by upload hours. Annual plans can't buy overage; you upgrade instead. The free plan deletes episodes after 90 days, so it's useless for a real show. |
| **Transistor** | Starter $19/mo (about $15.20/mo annual), 20K downloads/month. Professional $49 (100K, adds YouTube auto-posting per reviewers). Business $99. 14-day trial, no free plan. | Unlimited shows on one account, which suits a later Steadfast audio devotional or a training feed. | Priced by downloads, not upload hours. Unlimited shows. Private podcasts (useful for a paid training audio feed later). | Starts at $19 with no free tier. YouTube auto-posting needs the $49 tier, and we don't want it anyway. |
| **Captivate** | Personal $19/mo or $204/yr (30K downloads). Professional $49. Business $99. 30-day trial. | Strong growth tools: links pages, CTAs, guest management. | Generous trial. Built-in marketing pages. | Same price floor as Transistor. More features than we need at launch. |
| **RSS.com** | Free plan (unlimited episodes). Paid from about $15/mo billed annually (per RSS.com's own comparison). | Audio-to-video conversion for YouTube (not needed). Apple Podcasts Subscriptions support. | A real free tier with unlimited episodes. Cheap paid tier. | Smaller ecosystem. The audio-to-video feature duplicates what we upload ourselves. |

Where people listen (Buzzsprout platform data): Apple Podcasts 34.8% of downloads, Spotify 25.7%, web browser 8.8%; 81% on mobile. Those figures are audio only. YouTube is the largest podcast service overall (YouTube Blog, Feb 2025).

## Recommendation

1. **YouTube:** direct upload, free. This is the main home of the show.
2. **Audio feed:** **Buzzsprout Audio + Video, $300 a year billed annually.** Of the hosts we compared, it's the cheapest one that also puts the video on Apple Podcasts. Its 6 hours a month covers two episodes a week with room to spare, and it's the easiest one for Aaron to run without help.
3. **Spotify:** submit the Buzzsprout feed to Spotify (free). Also claim the show in Spotify for Creators, so Aaron controls the page and sees the stats.

**$0 alternative.** Spotify for Creators as the host, plus YouTube direct. This works at launch and costs nothing. The trade-offs: no video on Apple, lighter analytics, and moving hosts later needs a redirect (all the major hosts support it). If Aaron wants to spend nothing until the show proves itself, take this path and move to Buzzsprout after the first season.

**Either way, before any spend:** Aaron approves the plan and the dollar amount. Nothing gets signed up.

## Launch checklist (no action until Aaron says)

- [ ] Final show name and a trademark check
- [ ] Cover art, 3000x3000 square, navy, gold and bone. Readable at 55 px. The show name only, no episode number.
- [ ] Show description (about 150 words), category Religion & Spirituality > Christianity, secondary Society & Culture > Relationships. The explicit flag is off.
- [ ] Owner email (a Steadfast address, not personal)
- [ ] Trailer episode (60-90 s, cut from E001) published first, so the feed exists for Apple review
- [ ] Apple Podcasts Connect submission (review can take a few days)
- [ ] Spotify submission
- [ ] YouTube podcast playlist created and marked as a podcast
- [ ] Episode naming on the feed: "Ep. 1: The Man You Keep Saying You'll Be" (feed titles may include the number; YouTube titles put it at the end)
- [ ] Show notes in the reading-narrative format (`READING-NARRATIVE-FORMAT.md`), plus chapters

## Release timing

- Tuesday 5:00 AM CT for main episodes and Friday 5:00 AM CT for Field Notes, the same minute on YouTube and in the feed, so the drive-time listener has it before work.
- Shorts start the day after each main episode, one a day (see `production/PRODUCTION-SPEC.md`).
