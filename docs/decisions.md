# Decisions

*As of October 2026.*

The Mechanism keeps a record of its architectural decisions: what was decided, why, and what it
cost. More than thirty exist. These ten show the reasoning best, including the ones that were
reversed. A decision that didn't survive contact with use is as informative as one that did.

## 1. A closed universe, permanently

Every external account is a throwaway, and the agent's inputs are fixed: my library, the feeds I
follow, my own messages, and a few structured academic catalogues. There is no arbitrary web
fetching, and no tool for it.

**Why.** An autonomous agent with network access needs a bounded blast radius, but a home research
cluster doesn't warrant enterprise defences. Throwaway accounts make any compromise a matter of
rotating a key and restoring from backup.

**The cost.** The agent can't discover new sources on its own. That is treated as a feature: every
new channel has to come past me first. Browser automation stays off the table for the same reason.

## 2. Local models for volume, frontier models for judgement

Work is split by what it needs. A small model on the Jetson handles high-volume scoring and triage.
A larger model on the desktop GPU describes every passage and classifies new publications. Frontier
models, reached through an API, do synthesis and anything that needs reasoning depth. For structured
discussion sessions, the agent convenes one frontier model from each of three families (Anthropic,
Google and OpenAI) so the perspectives genuinely differ, not just the parameters.

**Why.** Sending everything to a frontier model would be slow and expensive, and full texts would
leave my hardware. Running everything locally would sacrifice quality where it matters most.

**The cost.** Two tiers of local hardware to look after, and a rule that model versions are pinned
exactly. A model that changes underneath the system, with nothing recording what ran, makes old
transcripts useless as evidence.

## 3. One key, one machine

Each credential lives on exactly one machine. Everything else reaches the service through a small
bridge that lets it use the service without ever seeing the key.

**Why.** A compromised agent should be able to search the library, but not walk off with the
library's key and use it from somewhere else.

**The cost.** More small services to run, and a rule that no new credential-bearing service is
deployed until its boundary is defined.

## 4. The closed universe, enforced by the network

For its first months, the closed universe was a promise kept by configuration. Any process could
open an outbound connection. Then the agent, following an instruction inside one of its own skill
files, downloaded and installed a program from the internet. No control fired, because none
existed at that layer.

Now every machine denies outbound traffic by default. The only way out to the web is a filtering
proxy on the cluster head, with a separate list of allowed destinations for each machine, and every
request it handles is logged.

**Why.** A boundary that depends on every component behaving is not a boundary.

**The cost.** Each new legitimate destination needs a deliberate addition, and installing software
has its own authenticated route that the agent's machine can't use.

## 5. Giving up "PDFs never leave my hardware"

The original rule was that copyrighted full texts would never leave my own machines. In practice
the reference library was already storing every attached PDF on its own servers, and keeping the
rule meant filing each book twice: once in the library, once in a folder on the desktop.

I decided the library's storage is a trusted channel. The desktop now fetches PDFs from the library
itself, and filing a book once is the only manual step.

**What didn't change.** Extraction, description and embedding still happen locally. No full text is
sent to a cloud model.

**Why it's here.** It shows what partial sovereignty looks like in practice: a line drawn on purpose,
where keeping data local stopped being worth its cost.

## 6. The library's rules are the system's rules

The pipeline was originally built outward from what its scripts happened to do. That made the
supported ways of using the library an accident of implementation history. Works filed in two
tracks appeared in only one. Trashed items stayed in the corpus. Filing into a sub-collection
silently ingested nothing.

The decision reversed the direction: whatever Zotero allows is what the pipeline must handle,
whether that's filing in several places, moving between tracks, trashing, or editing notes. As I
put it at the time: *"The system needs to trust that I use Zotero intentionally, not create
artificial drift warnings and system barriers based on inadequate requirements."*

**The cost.** Much more work in the pipeline, and a growing written record of exactly which library
actions are safe.

## 7. Rigour by consequence

Two principles pulled against each other. One: this is a working research cluster, not a product,
so don't over-build. The other came from the incident record. Re-ingesting duplicated the corpus,
a fuzzy matcher stamped 1,169 passages of one volume with another volume's details, the annotation
collection sat 40% complete, and backups turned out not to restore. Every one of those failures was
silent, and several would have surfaced years later as a wrong citation in a book.

The resolution sorts every requirement by what its failure would cost:

- **Provable:** anything that could silently corrupt or lose research content, or produce a wrong
  citation. It needs an executable test and must fail closed.
- **Observable and recoverable:** failures you would see and could fix without loss. Monitoring is
  enough.
- **Fix when it breaks:** cosmetic or self-correcting problems.

**Why.** It puts the effort where silent failure would do lasting damage, and nowhere else.

## 8. Rollback over forensics

For a home cluster on throwaway accounts, investigating a compromise costs more than rotating
credentials and restoring from backup. So rollback is the primary defence: daily local backups,
weekly encrypted offsite ones.

**What testing found.** The first serious audit showed the claim wasn't true for the corpus. The
local backup copied a live database and produced torn copies. The offsite backup had quietly done
nothing for weeks because it exceeded its size limit and still reported success. And neither kept
older generations. All three are fixed, and the lesson stayed: a backup is a claim until it has
been restored.

## 9. Trying Notion, and leaving it the next day

I added Notion as a structured writing surface alongside Obsidian, with a schema designed with the
agent: chapters linked to bibliography entries and sources. Within a day it had three structural
problems. Renaming anything in Notion silently broke the agent's writes. A routine redeploy wiped the
stored links between the schema and the live databases. And the two copies of the schema needed a
discipline nobody would sustain.

I decommissioned it. Obsidian is the only writing surface again.

**Why it's here.** Five hours of migration was the price of finding out. That is what building on
real use is for: the system pushed back quickly, and the cheap answer was to leave.

## 10. Letting the agent edit its own instructions

The agent's skills are the instructions it loads and trusts. They're also where it records what it
learns about how the cluster actually behaves. A writable skill is the one place where a manipulated
agent could plant something it would obey later.

Locking them was tried. The skills became read-only, and the agent submitted proposed changes to a
review queue. It worked as designed, and was withdrawn the same day, because I said plainly I wouldn't
read the queue. An unread queue doesn't make learning safe; it stops learning and leaves machinery
to maintain.

So the agent edits its own skills, and every change comes back into version control as a diff I
can see.

**Why.** The agent regularly finds things in its instructions that are wrong, and it is often the
only party in a position to notice. Visibility was chosen over prevention because it's the control
that will actually be exercised.
