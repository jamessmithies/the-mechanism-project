# Decisions

*As of October 2026.*

The Mechanism keeps a record of its architectural decisions: what was decided, why, and its impact. More than thirty exist. These six show some key examples.

## 1. A closed universe, permanently

Every external account is a throwaway, and the agent's inputs are fixed: my library, the feeds I
follow, my own messages, and a few structured academic catalogues. There is no arbitrary web
fetching, and no tool for it.

**Why.** An autonomous agent with network access needs a bounded blast radius, but a home research
cluster doesn't warrant enterprise defences. Throwaway accounts make any compromise a matter of
rotating a key and restoring from backup.

**The cost.** The agent can't discover new sources on its own. That is treated as a feature: every
new channel has to be approved by me. Browser automation is permanently rejected for the same reason. This constraint has turned into one of the system's best affordances. If I need an agent with access to the world I use a standard AI service.

## 2. Local models for volume, frontier models for judgement

Work is facilitated by models appropriate to the task. A small model on the Jetson handles high-volume scoring and triage.
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

**Why.** A compromised agent can search the library, but not walk off with the
library's key and use it from somewhere else.

**The cost.** More small services to run, and a rule that no new credential-bearing service is
deployed until its boundary is defined. In practice I never notice the boundaries between the services; usage is seamless despite the agents being constrained.

## 4. The closed universe, enforced by the network

Every machine denies outbound traffic by default. The only way out to the web is a filtering
proxy on the cluster head, with a separate list of allowed destinations for each machine, and every
request it handles is logged.

**Why.** I have complete control over what sources agents have access to, and what problems they can introduce.

**The cost.** Each new source needs a deliberate addition. In practice I find I have all the sources I need so this is not an issue.

## 5. Giving up "PDFs never leave my hardware"

The original rule was that copyrighted full texts would never leave my own machines. In practice
the reference library was already storing every attached PDF on its own servers, and keeping the
rule meant filing each book twice: once in the Zotero library, once in a folder on the desktop.

I decided the Zotero library's cloud storage is a trusted channel. The desktop now fetches PDFs from the library
itself, and filing a book once is the only manual step.

**What didn't change.** Extraction, description and embedding still happen locally. No full text is
sent to a cloud model.

**Why it's here.** It shows what partial sovereignty looks like in practice: considered tradeoffs made on my own judgement and with full understanding of the practical impact.

## 6. Moving triage off the Jetson

Each week the cluster harvests new records from PhilPapers, a large index of philosophy
publications, and a model sorts them for relevance to my research tracks. The plan was for the
small model on the Jetson to do this. It couldn't: the index returns every record *modified* that
week, often more than 80,000, and at the Jetson's pace one week's file took four days.

Speed wasn't the only problem. The 8-billion-parameter model marked about 0.4% of records as
relevant. The 32-billion-parameter model on the desktop marked about 21%. The small model was
quietly discarding papers I would have wanted.

Triage moved permanently to the desktop, which now skips records it has already seen.

**Why it's here.** It is the clearest case of finding a performance floor: this was a task the small model could run,
but not well enough. By moving up to a more powerful but still local machine, I compromised on system complexity but not data sovereignty.
