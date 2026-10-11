# Privacy policy

> **Draft, pending legal review.** Not yet in effect. Items in *[brackets]* are open questions for
> counsel.

**Last updated:** 2026-10-11

Hidden Token Gaming ("HTG", "we") is a gaming community for adults. This policy explains what
information about you HTG handles, why, who else sees it, how long we keep it and what you can ask
us to do with it.

HTG is run by **MKZ Systems LLC**, a Texas limited liability company, which decides how your
information is used (the "controller"). Contact: [privacy@hiddentoken.com](mailto:privacy@hiddentoken.com).
*[Interim, pending legal review: whether a postal address is needed.]*

## The short version

- **We collect as little as we can.** Today that is what Discord already shows to everyone in the
  server, the account you create if you sign in on app.hiddentoken.com, and the match stats and
  moderation records of the War Dogs server HTG runs.
- **We never sell your information,** and we don't show ads or use trackers.
- **Your name on leaderboards is opt-in.** The War Dogs server HTG runs counts everyone who plays
  on it, and the boards show each player under a made-up pseudonym unless they link their Steam
  account and choose to show their name.
- **You can ask** to see, correct or delete what we hold, at any time.

## What this policy covers

| Service | Status |
|---|---|
| The website, hiddentoken.com | Live |
| The HTG Discord server and the HTG Bot | Live |
| Game servers HTG runs or rents (today one War Dogs server) | Live |
| Support tickets and appeals | Live |
| app.hiddentoken.com: your HTG account, signing in with Discord and linking your Steam account | Live |
| app.hiddentoken.com: War Dogs stats, leaderboards and member profiles | **Live** since 2026-10-10 |
| app.hiddentoken.com: moderating HTG's game servers, from the web and from Discord | **Live** since 2026-10-10 |
| Seeding calls for the War Dogs server, and the time seeders spend on it | **Live** since 2026-10-10 |
| Muster: squad-ups and seeding nights at app.hiddentoken.com/muster and from the HTG Bot | **Live** since 2026-10-10 |
| Presence: who is playing now, in #whos-playing | **Live** since 2026-10-11 |
| Session recaps after HTG events (Wardogs Wednesdays) | **Live** since 2026-10-11 |
| app.hiddentoken.com: stats for other games and further linked identities (Xbox, Star Citizen, PUBG) | **Planned.** Covered here so you know in advance; we will update this policy before it launches |
| Supporters (Patreon) | **Planned** |

Discord, Steam, Xbox, Roberts Space Industries, KRAFTON, Patreon and the game publishers have
their own privacy policies for what they collect. This policy covers only what HTG does.

## What we collect today

### The website

The site sets **no cookies** and runs **no analytics, ads or trackers**, and no other company
collects information about your activity across websites through it. It is hosted on Cloudflare,
which processes your IP address and request details to deliver the site and protect it from
attacks, as HTG's processor under [Cloudflare's privacy policy](https://www.cloudflare.com/privacypolicy/).
If Cloudflare ever has to challenge a suspicious request, it may set a short-lived security cookie
that is strictly necessary for that check ([Cloudflare cookies](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/)).

### Discord

When you join the HTG Discord server, HTG staff and the bots in the server can see what Discord
shows to server staff: your username and ID, avatar, roles, when you joined, your onboarding
answers (games, platform, region and pings), and what you post in the server. Discord stores all
of it under [Discord's privacy policy](https://discord.com/privacy).

HTG keeps its own copies of only:

- **moderation records:** for every warning, timeout, kick or ban, your Discord user ID and
  username, the rule, what happened, the staff member, and the date. They sit in a private staff
  channel and are used to apply the [moderation ladder](../policy/moderation.md) and handle
  appeals;
- **server audits:** a weekly snapshot of the server's structure and its numbers: how many
  members it has, in total and per role, how many joined in the past week, and how many messages
  were posted in each channel in the past week and by how many people. To count those, the HTG
  Bot sees which account posted each message, and keeps only the totals. Audits name no members
  and hold no member IDs or message content. They're used to manage the server's structure and to see
  whether the community is growing. Staff and ticket channels aren't counted.

Anything the HTG Bot or HTG's apps get from Discord is used only for the HTG features described
here. It is never sold, never shared beyond the providers below, never used to profile you, and
deleted when it's no longer needed or when you ask.

### Support tickets and appeals

- **Tickets** opened in `#support` are handled by a third-party bot, Ticket Tool. When a ticket
  closes, its transcript is posted to a private staff channel in HTG's Discord server. Ticket Tool
  doesn't keep a copy ([Ticket Tool FAQ](https://docs.tickettool.xyz/debugging/faqs)).
- **Ban appeals** are sent by email to [appeals@hiddentoken.com](mailto:appeals@hiddentoken.com), hosted by Proton in Switzerland.
  We use what you send only to decide your appeal.

### Your HTG account (app.hiddentoken.com)

You don't need an account to be a member; it exists so HTG can tie game stats, sessions and
recognition to you later, and only if you choose to link things. If you sign in:

- **Signing in with Discord** gives HTG your Discord user ID, your username and display name, and
  your avatar. We store those three and read nothing else from Discord (the sign-in asks Discord
  for your identity only, not your email, connections or servers).
- **Linking Steam** proves which Steam account is yours through Steam's sign-in; HTG stores your
  SteamID and, from Steam's public profile data (the Steam Web API), your persona name and avatar.
  We read no achievements or play history yet; that is planned below. You can unlink Steam at
  any time on your account page.
- **Staying signed in** uses one cookie on app.hiddentoken.com that identifies your session and
  nothing else (Muster's pages add their own, below). It is strictly necessary for the account to work, carries no tracking, and lasts
  30 days or until you log out. "Log out everywhere" ends every session you have.
- **A log of sign-ins, links and unlinks** with their dates, kept so you and HTG can see what
  happened to your account. HTG does not store the IP address or browser you sign in from. To
  protect the site from abuse, the number of requests from an address is counted briefly in
  memory and never written down.

The profile details are refreshed each time you sign in or link, so what the account page shows
is what Discord or Steam currently shows.

### Game servers: War Dogs

HTG's War Dogs server is run by our host (QONZER) under Bulkhead's licence, and both handle
connection data under their own policies. HTG reads the server through its admin interface, and
this applies to **everyone who plays on it**, whether or not they are an HTG member:

- **Who's on, live.** Every 15 seconds HTG reads the match and the player list: in-game name,
  SteamID, team, kills, deaths and ping. Members signed in to app.hiddentoken.com see who is on;
  the in-game names and ping aren't saved.
- **Match stats.** From those reads HTG records each match (the map and when it started and ended)
  and, for each player in it, their SteamID, team, kills, deaths and time on the server. That is
  what the leaderboards count.
- **Player counts and scores.** HTG also records how many players were on, minute by minute, and
  each match's team scores. These are counts only: nothing in them says who was playing.
- **Session recaps.** After an HTG event such as Wardogs Wednesday, the HTG Bot posts a recap in the
  game's channel, with a page on app.hiddentoken.com: peak players, the matches with their scores,
  and the top five by kills, under the same pseudonyms as the leaderboards. Nothing new is
  collected for a recap; it is read from the match stats above.
- **The kill feed.** The server also sends HTG each kill as it happens, with the SteamIDs of the
  player who made it and the player who was hit. HTG stores each batch as it arrives for 30 days,
  so it can turn them into more detailed stats (planned), then deletes it.
- **No connection IPs.** The War Dogs server doesn't give HTG players' IP addresses.

**How you appear.** A leaderboard shows each player under a **pseudonym**: two words generated from
their SteamID with a secret key, so it can't be worked back to the Steam account. Your name
replaces it only if you link your Steam account on app.hiddentoken.com and turn on "show my name on
leaderboards" on your profile; it's off until you do, and you can turn it off again. Your profile
(your totals and recent matches) is visible to you and HTG's owner, and to everyone only if you
show your name.

**Moderation on the server.** When staff kick, ban or message a player, from app.hiddentoken.com or
from Discord, HTG records it in a moderation log: the date, the staff member, the action, the
player's SteamID, the reason or message, and the result. The log can't be edited or deleted, so
every action stays accountable, and a copy is posted in a private staff channel in Discord. A ban
also goes on HTG's ban list for the server (SteamID, reason, date, and the date it's lifted).

**Seeding calls.** War Dogs matches start at 20 players, so when the server is under that at the
times HTG sets, the HTG Bot pings the members who chose the `@WD Seeder` role, at most once every
two hours. While a call is open, HTG records how long each player is on the server, by their
SteamID, as **seeding time**: one record per player per call, kept like match stats (below), so
seeders can be recognised. If you don't choose the role, you are never pinged; anyone on the
server during a call is counted, as for match stats.

### Muster: squad-ups and seeding nights

Muster is how members get together for a game: a **squad-up** (whoever wants to play on HTG's War
Dogs server now or at a set time) or a **seeding night**. You create or join one at
app.hiddentoken.com/muster or with the HTG Bot's `/squad` and `/seed` commands in Discord. HTG
keeps, by your Discord user ID:

- **The sessions you host:** the game and activity, when it starts, and the note you wrote;
- **Your seat in each session you join:** the role, and whether you were interested, confirmed,
  attended or didn't show (the host marks attendance);
- **Your attendance as participation:** when the host marks you attended, the session and how long
  it ran are added to your participation on app.hiddentoken.com, kept like match stats (below).

A session and who is in it are visible to members signed in to app.hiddentoken.com, and to anyone
who can see the Discord channel where its card is posted. Upcoming sessions with a start time are
also listed publicly, on hiddentoken.com/events and Muster's calendar, with only the game, the
activity, the time and how many seats are taken: never who hosts, who signed up, or the host's note. When a session has a start time, the HTG Bot also lists it as a Discord event; marking yourself interested in that
event signs you up in Muster, and Discord shows the event's interested list under its own policy.
Muster's pages sign you in through your HTG account. They set their own cookies on
app.hiddentoken.com/muster, all strictly necessary and none for tracking: one that keeps you
signed in to Muster for up to an hour or until you sign out of it, one that lasts only while a
sign-in is under way, and one that carries a single confirmation message to the next page.

## What we will collect when app.hiddentoken.com launches (planned)

This section describes the design. It takes effect only when these features launch, and we will
update it and announce the change first.

- **Further linked game identities, only the ones you choose to link** (Discord sign-in and
  Steam linking are live; see above):
  - **Steam achievements:** with your permission we read your public achievements for the games
    HTG plays;
  - **Xbox:** your Xbox user ID and gamertag, read from your Discord connections with your
    permission;
  - **Star Citizen:** your RSI handle, proved by a one-time code you place in your RSI bio;
  - **PUBG:** your PUBG account ID and name, proved by a custom-match challenge;
  - **Patreon:** your supporter tier and status. Payments happen at Patreon; we never see card
    details. Patreon controls your membership data, and HTG uses what Patreon shares only to give
    you your supporter perks, under Patreon's
    [Creator Privacy Promise](https://support.patreon.com/hc/en-us/articles/360026912432-Data-Processing-Agreement-Creator-Privacy-Promise).
- **Game activity for other games.** Events from HTG-run servers and official game APIs, such as
  matches played, kills, deaths, scores and time played, kept as War Dogs stats are (above).
  Counter-Strike 2 server logs also record the IP address you connect from. *[Whether to keep IPs at all, and for how long, is
  a question for counsel; the default is to drop them at ingestion except where needed for ban
  enforcement.]*
- **Gamertags and game names in Muster sessions.** For games where you add each other in game
  (Sea of Thieves, Star Citizen, PUBG), your linked gamertag or game name is shown to the members of
  a session you join.
- **"Who's playing now" (presence).** If you share your activity on Discord, Discord tells the HTG
  Bot what you're doing. The bot keeps only the name of the game you're playing, and only in memory
  while you're online, so it can count how many members are playing each game. The count is shown in
  #whos-playing and never names anyone. HTG doesn't write down who was playing or keep any history
  of anyone's activity. Everything else Discord sends, such as music or a custom status, is
  ignored. If you don't share your activity on Discord, the bot sees nothing.
**Before you link anything, HTG shows no name.** Servers HTG runs record stats for everyone who
plays. Until you link and choose to show your name, those stats appear only under a generated
pseudonym that can't be traced back to your game account.

## Where it comes from

- **From you:** what you post, your onboarding answers, tickets, appeals, and the accounts you
  choose to link.
- **From Discord:** your Discord profile and roles in the HTG server.
- **From game servers HTG runs or rents:** your in-game name, SteamID and match activity, from
  the server's admin interface and its kill feed (War Dogs gives no IP addresses; HTG-run
  Counter-Strike 2 servers will log your connection IP, planned).
- **From services you link:** Discord (your user ID, name and avatar when you sign in) and Steam
  (your SteamID, persona name and avatar when you link). Planned: Steam achievements, Xbox via
  your Discord connections, your public RSI citizen page, the PUBG API, and Patreon.

**Do you have to give it?** A Discord account is needed to join the community. Linking game
accounts, sharing activity and supporting are optional; without them, the features that depend on
them won't work for you.

## Why we use it

| Purpose | Information | Legal basis, where the law asks for one *[for counsel]* |
|---|---|---|
| Run the community: Discord roles, events, crew-ups, game servers | Discord profile, onboarding answers, session signups, linked identities | Providing the service you joined (contract) |
| Keep everyone safe: moderation, bans, cheating and ban-evasion checks | Moderation log, ban lists, SteamIDs, connection IPs from HTG servers (planned) | Our and members' legitimate interest in a safe, fair community |
| Stats and leaderboards for everyone who plays on HTG's servers, under pseudonyms | Match stats and the kill feed, by SteamID | Legitimate interest in running fair, competitive servers *[for counsel: players who aren't HTG members]* |
| Showing your name and profile on the leaderboards | Your linked Steam account and your choice | Your consent: the switch on your profile, which you can turn off |
| Seeding calls | The seeding role, and each player's time on the server during a call, by SteamID | Legitimate interest in getting matches started; the seeding role is your choice |
| Who's playing now (planned) | Live Discord activity, counted, not stored | Legitimate interest in getting members together; sharing your activity is your choice |
| Supporter perks | Patreon tier and status | Providing the perks (contract) |
| Answer support requests and appeals | What you send us | Legitimate interest; contract |
| Manage the server and see whether the community is growing | Server audits: totals only, no names, IDs or message content | Legitimate interest in running the community |

We don't use your information for advertising, we don't sell or rent it, and we don't use it to
build profiles beyond what is described here. We don't make automated decisions with legal or
similarly significant effects on you. Bans are decided by people.

## Who else sees it

- **Other members** see what you post in Discord, the sessions you join, and anything you make
  public on the app. On the leaderboards they see your stats under your pseudonym, or under your
  name if you chose to show it, and your profile only if you show your name.
- **Service providers** process it for us, under their own terms:

  | Provider | What for | Where |
  |---|---|---|
  | Discord | The community server, the HTG Bot, sign-in to app.hiddentoken.com | United States |
  | Steam | Linking your Steam account to your HTG account; your persona name and avatar through the Steam Web API | United States |
  | HTG's own server | app.hiddentoken.com: your account, linked identities, sign-in sessions, game stats, seeding time, the kill feed, the moderation log and Muster | United States |
  | Cloudflare | Website hosting, DNS, security | Global network |
  | Proton | Email for appeals | Switzerland |
  | QONZER | The War Dogs server | United States |
  | [Ticket Tool](https://tickettool.xyz/privacy-policy) | Support tickets in Discord | Transcripts stay in HTG's Discord |
  | [Wick](https://wickbot.com/legal/privacy) | Anti-raid protection in Discord | *[not published]* |
  | DigitalOcean | HTG's own game servers (planned) | United States |
  | Patreon | Supporter membership (planned) | United States |

- **Game publishers,** when we report cheating or abuse on their games, receive the evidence and
  the game account involved.
- **Authorities,** when the law requires it, or to protect someone from serious harm.

## Where it is stored

HTG's own records are stored in the **United States**. Appeal emails are stored in Switzerland
(Proton). The website is served from Cloudflare's global network. If you live outside the United
States, your information is transferred there. *[Transfer safeguards to confirm with counsel.]*

## How long we keep it

| Information | How long |
|---|---|
| Server audits | Kept; they hold only totals, nothing about any one member |
| Moderation records | While they count toward the ladder, and for as long as a ban lasts. *[Period after a ban ends: for counsel]* |
| Ticket transcripts (in HTG's staff channel) and appeal emails | *[Proposed: 12 months after the ticket or appeal closes, then deleted]* |
| Your HTG account and linked identities | Until you delete them or unlink |
| Sign-in sessions | 30 days, or until you log out |
| The log of sign-ins, links and unlinks | With the account |
| Per-match game stats (by SteamID) | **13 months**. After that, each player's matches are added up into monthly totals, still by SteamID, which keep the season and all-time leaderboards correct and stay until the player asks us to erase them *[period and the monthly totals pending legal review]* |
| Pseudonyms | Until the player asks us to erase their stats |
| Seeding time and attendance (participation) | Like per-match stats: **13 months**, then monthly totals until the player asks us to erase them *[pending legal review, as above]* |
| Muster sessions and the seats in them | **13 months** after the session ends, then deleted with every seat in it *[pending legal review]* |
| Player counts by the minute, and each match's team scores | Kept; they hold only counts and scores, nothing about any one player |
| What members are playing (presence) | Not kept: held in the HTG Bot's memory only while you're online, to count it |
| The War Dogs kill feed, as received | 30 days |
| The moderation log for HTG's game servers | Kept; it can't be edited or deleted *[how long after a ban ends: for counsel]* |
| Ban lists for HTG's game servers | While the ban stands; a lifted ban stays in the moderation log |
| Players' in-game names and ping | Not kept: read live, never saved |
| Who is playing which game now (planned) | Not kept: counted live, never saved |
| Connection IPs from HTG-run Counter-Strike 2 servers (planned) | *[Proposed: not kept, except with a ban record]* |
| Patreon tier and status (planned) | While you are a supporter, then 30 days |

## Your choices and rights

You can:

- **see** what HTG holds about you and get a copy of it;
- **correct** it;
- **delete** it. We remove your account and linked identities, and erase your game stats: your
  SteamID is replaced with a random token in every match, monthly total, seeding and attendance
  record and stored kill-feed batch, and your pseudonym is deleted, so match totals and
  leaderboards stay correct but show "Deleted player" and no longer point to you. In Muster we
  delete the sessions you hosted and your seats in other sessions. We may keep a ban record and the moderation log where we
  need them to enforce a ban *[for counsel]*. **You don't need to be an HTG member:** anyone who
  has played on HTG's War Dogs server can ask, with their SteamID *[how we confirm a non-member
  owns that SteamID: for counsel]*;
- **unlink** a game account at any time on your account page (your account keeps at least one
  signed-in identity, so the last one is removed by deleting the account); take your name off the
  leaderboards at any time with the switch on your profile;
- **withdraw consent** to your name on the leaderboards by turning the switch off or unlinking;
- **object** to how we use your information, or ask us to restrict it;
- **complain** to your local data protection authority, if you have one.

Ask in a `#support` ticket or by email to [privacy@hiddentoken.com](mailto:privacy@hiddentoken.com). We'll confirm it's really you
through your Discord account, and answer within 30 days.

**Do Not Track:** the site doesn't track you, so there is nothing for a Do Not Track signal to
switch off.

## Age

HTG is for adults only. You must be 18 or older to join (rule 1 of the
[server rules](../policy/rules.md)). If we learn that a member is under 18, we remove them and
delete what we hold about them, except what we need to stop them rejoining before they turn 18.

## Security

Access to HTG's systems and records is limited to the staff who need it. HTG's own data stores
are encrypted at rest, secrets are encrypted, and HTG's bot runs with the fewest permissions it
needs. No system is perfectly secure. If a breach
affects your information, we will tell you and any authority we must notify, as the law requires.

## Changes

We will post changes here and update the date at the top. If a change matters, such as a new kind
of information or a new use for it, we will announce it in Discord before it takes effect.
