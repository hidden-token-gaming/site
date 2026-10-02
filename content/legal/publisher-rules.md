# Publisher rules

Every game HTG plays comes with its publisher's rules, and they apply on top of
[ours](../policy/rules.md). This page summarises the rules that matter to a community: what gets
an account, a server or HTG itself into trouble, and what happens if it does. Each rule links to its
source. All sources were checked on **2026-10-02**; dates in a row are the source's own.

This is a summary, not legal advice, and it is **pending legal review**. Where the publisher's text
and this page differ, the publisher's text wins. Quotes are copied from the source; anything we
could not confirm on an official page is marked *unverified*.

## At a glance

| Publisher | Game | The rule that hurts most | What HTG does |
|---|---|---|---|
| Valve | Counter-Strike 2 | Inventory, skin, knife or rank spoofing on a server: the server tokens are disabled for good | No item or inventory plugins on any HTG server, ever |
| Bulkhead / Team17 | WARDOGS | Joining an XP-farming server for more than a few minutes: permanent ban | No farming setups; HTG server settings stay stock-legal |
| Microsoft / Rare | Sea of Thieves | Game content on a paid or selling page; using the Sea of Thieves logo | Required notice on the site; no logos; no SoT content behind any payment |
| Cloud Imperium Games | Star Citizen | Any donation, fundraising or paywall tied to Star Citizen | Fan-site notice on every SC page; nothing paid touches SC |
| KRAFTON | PUBG: BATTLEGROUNDS | Charging for, or rewarding supporters with, features built on PUBG API data | Required trademark notice; API-derived features free for everyone |

## Valve: Counter-Strike 2 and Steam

| Rule | Consequence | Source |
|---|---|---|
| Servers must not "falsify the contents of a player's profile or inventory": no temporary skins, knives or gloves a player doesn't own, no fake skill groups, profile ranks or coins, and no "custom models and/or weapon skins that do not exist" in the game. | Valve "permanently disabled Game Server Login Tokens" of operators who did this, and "the Steam user that generated the tokens is now also permanently restricted from creating new GSLTs". New tokens then need a new Steam account with a new qualifying phone number. | [Game Server Operation Guidelines](https://blog.counter-strike.net/server_guidelines/) |
| Allowed: stock weapons from a mod, letting players use items they own in a new way, and custom scoreboards. | — | [Game Server Operation Guidelines](https://blog.counter-strike.net/server_guidelines/), FAQ 3–5 |
| A server token (GSLT) needs a Steam account that owns CS2, has a qualifying phone, and isn't banned, locked or limited. "Do not distribute game server login tokens to third parties." | "If your game server accounts are banned for any reason, you may be restricted from playing the associated games." | [Steam Game Server Account Management](https://steamcommunity.com/dev/managegameservers) |
| The dedicated server may be used "for the purpose of hosting online multiplayer games of Valve products", at the operator's own cost. Content and services may not be exploited "for any commercial purpose" except as the agreement allows. | Account termination under the agreement | [Steam Subscriber Agreement](https://store.steampowered.com/subscriber_agreement/) §2.E, §2.G |
| Steam Web API: only fetch a user's data when that user asks; post a privacy policy saying what is stored and where; keep the API key secret; at most 100,000 calls a day; never present the data as endorsed by or affiliated with Valve or Steam. | API access ends | [Steam Web API Terms of Use](https://steamcommunity.com/dev/apiterms) §2, §5 |

**Notes.** The server guidelines were written for CS:GO (2015–2016). Valve has not published a
CS2-specific version, so they are treated as current. Valve's own pages don't confirm the claim,
repeated by hosting companies, that a spoofing ban also bans every other token on the account or
the phone number outright (*unverified*). We plan for the worst case anyway. Valve has no published
rule on paid VIP or reserved slots; HTG doesn't sell them (see [supporters](#supporters-and-money)).

**What HTG does:** CS2 servers run from a dedicated HTG Steam account whose phone is used for
nothing else, so a ban can't reach anyone's personal account. HTG's server images will refuse
inventory and skin plugins, and there is no `!ws`, `!knife` or `!gloves` on any server HTG runs or
uses.

## Bulkhead and Team17: WARDOGS

WARDOGS is developed by Bulkhead and published by Team17. Community servers are run by approved
hosting partners; HTG rents one.

| Rule | Consequence | Source |
|---|---|---|
| **XP farming.** "We track every server you enter, and we are also very aware of which servers are XP farming servers." | "If your account is tracked as joining one of these servers for more than a few minutes, we will ban your account permanently." | [Patch 0.11 notes](https://store.steampowered.com/news/app/1867240/view/1843481262698449) (2026-09-12) |
| **Cash and XP exploits**, and real-money trading. | Cash and XP reset to 0 and a timed ban; "players now risk being permanently banned without warning". | [Patch 0.11 notes](https://store.steampowered.com/news/app/1867240/view/1843481262698449); [Update 0.1.2](https://store.steampowered.com/news/app/1867240/view/1845383656376490) (2026-09-30) |
| **Exploit tutorials**: content that teaches how to abuse a system without reporting it counts as advertising cheats. | Permanent ban | [Patch 0.11 notes](https://store.steampowered.com/news/app/1867240/view/1843481262698449) |
| "Win trading, deliberate throwing, boosting, and playing to farm rewards rather than to play the game." | Suspension or ban. A Bulkhead ban "blocks you from all online play, including on community servers". Only permanent bans can be appealed, to <appeal@bulkhead.com>. | [Security & Enforcement policy](https://www.wardogs.com/enforcement) (2026-09-07) |
| **Servers** used to break these rules. | "We may also remove a server from the browser, or withdraw our services from it." | [Security & Enforcement policy](https://www.wardogs.com/enforcement) |
| **Community servers** are allowed only through tools or hosts Team17 or Bulkhead authorise or approve. Private servers, emulators and proxies are not. | Breach of the EULA | [WARDOGS EULA](https://www.wardogs.com/eula), §5.2(n) and Addendum §3 |
| No "commercial exploitation of our Services without our prior written consent, including by performing services for another user … in exchange for payment". | Breach of the EULA | [WARDOGS EULA](https://www.wardogs.com/eula), §5.2(q) |
| Server names must sort alphabetically regardless of special characters, with no double spaces. | Enforced by the server browser | [Patch 0.11 notes](https://store.steampowered.com/news/app/1867240/view/1843481262698449) |

**Notes.** Server admins "set their own rules and can kick or ban players from their own servers",
and those bans are theirs alone. Bulkhead doesn't review them. No official table of allowed server
settings is published (*unverified* beyond the patch notes). Bulkhead publishes no fan-content
policy or required notice; the EULA forbids suggesting any affiliation or endorsement.

**Approved hosts.** At launch (2026-09-08) Bulkhead named three approved hosting partners:
QONZER, BisectHosting and xREALM. The current [server hub](https://www.wardogs.com/serverhub)
lists only BisectHosting and xREALM (checked 2026-10-02), but QONZER is still an approved host
(owner confirmation, 2026-10-02). HTG's server is at QONZER.

**What HTG does:** the HTG server runs with no farming setups and nothing that makes XP or cash
easier to earn than in normal play. Rule 5 of [our rules](../policy/rules.md) makes farming a
permanent ban here too. Nothing on the HTG server is sold.

## Microsoft and Rare: Sea of Thieves

| Rule | Consequence | Source |
|---|---|---|
| Anything shared that uses Sea of Thieves content must carry Microsoft's notice and a link to the rules ([notices](notices.md#sea-of-thieves)). | Microsoft may require you "to stop distributing your Item right away". | [Game Content Usage Rules](https://www.xbox.com/en-US/developers/rules) |
| No selling or earning from game content, including ads in it. It may not be posted "on a site that requires subscription or other fees to view the Item, or … on a page you use to sell other items or services". Optional donation requests are allowed. | Permission revoked "at any time and for any reason" | [Game Content Usage Rules](https://www.xbox.com/en-US/developers/rules) |
| No logos from the game in your own logos, and no use of the game's name that makes it look official. Rare: never use the Reaper's Mark skull; the name may appear only as a secondary part of a title. | Permission revoked | [Game Content Usage Rules](https://www.xbox.com/en-US/developers/rules); [Sea of Thieves Limited Commercial Usage Guidelines](https://www.seaofthieves.com/commercial-use-guidelines) |
| "We have zero tolerance … to any form of in-game hacking or cheating." Teaming or boosting in competitive modes, harassment, repeated stream sniping, and data-mined content are also against the code. | Warnings and suspensions up to permanent termination; 12 points is a permanent removal, and egregious offences can earn 12 at once. Ban evasion with alt accounts terminates every account. | [Sea of Thieves Code of Conduct](https://www.seaofthieves.com/code-of-conduct) |
| Third-party tools are against the code. Crosshair overlays are not a bannable offence (at your own risk); ReShade-style visual mods are bannable; game files must not be tampered with. | Enforcement under the code | [Enforcement Policy Updates](https://support.seaofthieves.com/articles/24643308439314) (2026-04-09) |
| Xbox: don't share or sell accounts, don't charge players to help them through a game, don't send repeated unwanted invites, don't share another player's information "more broadly than they've agreed to". | Strikes for six months; suspensions; a permanent suspension forfeits game licences and account balances | [Xbox Community Standards](https://www.xbox.com/en-US/legal/community-standards) |
| Microsoft services: no "impermissible scraping", no "automating inauthentic activity", and Xbox services "are only for your personal and noncommercial use". | Account closure | [Microsoft Services Agreement](https://www.microsoft.com/en-us/servicesagreement) (effective 2026-09-30) |

**Notes.** Rare's own code of conduct doesn't mention server hopping or the Hourglass by name, and no
official page addresses map tools, automation or the website's login cookie (*unverified*). Treat
them as third-party tools: don't. Custom Seas has no published rules on entry fees or prizes; the
general rules above apply.

**What HTG does:** the site carries the Microsoft notice; HTG's logo uses no Sea of Thieves art;
crew-ups are organised by people, never by automated friend or party requests. Members' gamertags
are shared only with the crews they sign up for.

## Cloud Imperium Games: Star Citizen

| Rule | Consequence | Source |
|---|---|---|
| Every fan site, org domain or social page shows CIG's fan-site notice, "open, obvious" and no smaller than other notices, and links to the official site ([notices](notices.md#star-citizen)). | Not "in keeping with our Fan site policy"; CIG reserves "all rights in law and equity" | [Fankit and Fandom FAQ](https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793) |
| **No commercial use of RSI content**: "for profit, side business, gig, advertising, clout, fundraising, donations, investment, paywalls, games of any kind etc." No licences are offered. | Use is prohibited | [Fankit and Fandom FAQ](https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793) |
| A fan site that charges for access, or earns advertising or sponsor revenue, may not use RSI fan-site content or marks. No merchandise. | Licence terminated; "further civil or criminal legal action" for unauthorised use | [RSI Terms of Service](https://robertsspaceindustries.com/en/tos) §XIII.B, §XIII.D |
| No "Star Citizen", "Roberts Space Industries", "Cloud Imperium", "Turbulent" or "Squadron 42", or in-game company names, in a site's domain. Nothing may look official. | Not a permitted fan use | [Fankit and Fandom FAQ](https://support.robertsspaceindustries.com/hc/en-us/articles/360006895793) |
| No cheats, macros, bots or unauthorised third-party software; no software that reads game memory; no client modification; no exploiting bugs for advantage. | Warnings, suspension, account termination with no refund | [RSI Terms of Service](https://robertsspaceindustries.com/en/tos) §IV, §XVIII; [EULA](https://robertsspaceindustries.com/en/eula) §I |
| No "bots, spiders, scrapers" for "data scraping or harvesting, scraping or harvesting information about other users". | As above | [RSI Terms of Service](https://robertsspaceindustries.com/en/tos) §IV |
| No real-money trading of in-game items or services ("power-leveling"), and no selling or sharing accounts. | As above | [RSI Terms of Service](https://robertsspaceindustries.com/en/tos) §III, §IV |

**Notes.** The full Fan Kit Agreement sits behind an RSI login, so this page summarises the public
FAQ and Terms of Service. CIG has no published position on handle verification by a code in the RSI
bio, which fan tools use (*unverified*).

**What HTG does:** the notice appears on every Star Citizen page and in the Star Citizen channels.
No supporter perk, donation ask or paid feature touches Star Citizen, and HTG's domain and logo use
no CIG marks. RSI pages are only read when a member asks to link their own handle.

## KRAFTON: PUBG: BATTLEGROUNDS

| Rule | Consequence | Source |
|---|---|---|
| Anything that shows the PUBG trademark carries PUBG's trademark notice ([notices](notices.md#pubg-battlegrounds)). No PUBG logo without written consent, nothing that implies sponsorship or endorsement, no merchandise. | "Any use of a Trademark in violation of these guidelines will automatically terminate any license to the Trademarks." | [PUBG Developer API Terms](https://developer.pubg.com/tos), Trademark Guidelines |
| **No charging for features built on PUBG API data.** "You may not charge money for exclusive access to features that are based, in whole or in part, on data gained from the PUBG API." | API key revoked; email blacklisted | [PUBG Developer API Terms](https://developer.pubg.com/tos), Monetization Policy |
| **No crowdfunding rewards.** Donations are allowed, but donors "cannot be granted any special benefits from doing so". | As above | [PUBG Developer API Terms](https://developer.pubg.com/tos), Monetization Policy |
| No reselling the data, no player-count estimates, nothing misleading; the API key stays on the server, never in a browser. | "Your API key being revoked" | [Developer FAQ](https://developer.pubg.com/faq); [API keys](https://documentation.pubg.com/en/api-keys.html) |
| No unauthorised programs or hardware, client or `ini` changes, exploits, or teaming that the mode doesn't allow, including in custom games. Cash transactions, even via custom-game names, are banned. | Up to a permanent ban and a hardware ban; legal action for those who make or sell cheats | [Rules of Conduct](https://pubg.com/en/clause/rules_of_conduct) Articles 5–7 |
| "You are not allowed to generate any profit using the game service without prior approval from KRAFTON." No gambling content. | Account suspension | [Rules of Conduct](https://pubg.com/en/clause/rules_of_conduct) Article 4; [Terms of Service](https://pubg.com/en/clause/term_of_service) §3 |
| Fan content: donations and ordinary site ads are fine; content with game IP may not sit behind a paid subscription. | Content removal, account bans, legal action | [Content Creation Guideline](https://pubg.com/en/clause/content_creation_guideline) §2–3 |

**Notes.** KRAFTON publishes no rules for community tournaments on PC. Read together, the profit and
gambling rules mean any paid entry or prize event needs KRAFTON's written approval first.

**What HTG does:** PUBG stats and boards built from the API are free for every member, and no
supporter tier changes what they show. The API key never leaves the server, and the PUBG logo isn't
used.

## Supporters and money

HTG plans a supporter programme (Patreon) to pay for infrastructure. The rules above shape it:

| Publisher | What it allows | What it rules out |
|---|---|---|
| Valve | Nothing specific to supporters | Item or inventory perks of any kind; commercial use of Steam content |
| Bulkhead / Team17 | Creator income from streams and videos | Paid services inside the game or on the server without written consent |
| Microsoft / Rare | Optional donation requests | Game content on a paid page or a page that sells anything |
| CIG | Nothing | Donations, fundraising or paywalls tied to Star Citizen content |
| KRAFTON | Donations without benefits; ordinary ads | Paid or supporter-only API-derived features |

So supporter perks stay **community-wide and game-neutral** (roles, a site badge, name colour), and
supporter pages carry no game art, logos or game-specific content. Questions for counsel before
launch (plan decision D5):

1. Can a supporter page on a site that also hosts Star Citizen and Sea of Thieves content sit under
   the same domain, or does it need to be kept separate?
2. Does event priority for supporters count as a "special benefit" under KRAFTON's crowdfunding rule
   when the event is a PUBG custom match?
3. Are reserved CS2 server slots for supporters "commercial purpose" under the Steam Subscriber
   Agreement? (Off by default until answered.)

## Keeping this current

Staff re-check every source at the start of each season, and whenever a publisher posts new terms.
Update the date on the changed section and note the change in the
[site changelog](https://github.com/hidden-token-gaming/site/blob/main/CHANGELOG.md).
