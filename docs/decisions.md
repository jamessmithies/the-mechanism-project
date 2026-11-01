# Decisions

*As of October 2026. The Mechanism (TM) is evolving; this page describes key design decisions rather than every detail. The full code (including all design decisions) is kept in a private repository for security purposes.*

## A weak justification
I am keeping TM in service despite the system being complex and somewhat fragile. It is closer to a Heath Robinson machine than a refined product or platform, but I use it every week. Maintenance has settled into a monthly routine. It is designed and configured around my personal scholarly practices with no consideration for wider use. Its design and architecture might prove useful to people building AI-enabled research infrastructure but my intention was to create a tool to enable my own work, using as much local hardware and as many small and open models as possible. 

If I was forced to provide a single justification for TM's continued existence I would point to the balance between the contraption's closed universe of scholarly sources and the power of persistent agentic AI: the balance is difficult to achieve but compelling. My suspicion is that AI-enabled humanities research requires a radical narrowing to high quality sources tailored to the individual researcher, coupled with persistent agentic AI that can guide, critique, and learn alongside the researcher.  

This requires a lot more than straight-forward "chat with my pdfs" functionality, but significantly less than access to the entire World Wide Web. TM keeps the researcher firmly at the centre of epistemological and methodological decision-making but with access to the full range of their own sources (primary, secondary, RSS, social media) along with a consistent 'mentor and guide' and a range of configurable 'critical friends'. By keeping as much processing offline as possible and retaining detailed records in offline Markdown files I feel in control. I could continue to work on my monograph project even in the worst case scenario where access to frontier AI is entirely disabled. 

I particularly like using small and open weight models for some tasks, limiting information leakage to hyperscale AI vendors and reducing the environmental impact of my work. The mixture of deterministic and non-deterministic workflows is also valuable, using n8n and RSS for repeatable tasks that don't require agentic AI. Frontier AI services are only accessed intermittently by TM, for advanced text processing and occasional 1-1 discussion sessions and workshops with multiple AI models. Because core TM data only consists of Markdown files and a Zotero library, I could easily migrate my research to another platform if necessary. 

This portability and transparency extends to techncial aspects of the project too. I keep a record of architectural decisions in Markdown files in a private code repository, produced as a natural part of my software engineering process but also useful for auto-ethnography in the tradition of Science and Technology Studies (STS). The repository contains extensive documentation alongside Ansible playbooks that document as well as deploy infrastructure as code to TM. More than thirty architectural decisions are stored in the repository. Seven examples are listed below.

## 1. A closed universe of sources

Every external account is a throwaway, and the agent's source inputs are limited to my Zotero library, the RSS feeds I
follow, my own messages, and a few structured academic catalogues: PhilPapers, arXiv, Semantic Scholar, OpenAlex and Unpaywall. There is no arbitrary web
fetching, and no tool to support it.

**Why.** An autonomous agent with network access needs a bounded blast radius, especially on a home network, and my research needs to be protected from information leakage and unwanted activity by agents. Throwaway accounts make any compromise a matter of
rotating a key and restoring from backup.

**The cost.** The agent can't discover new sources on its own. That is treated as a feature: every
new source, from a book to an article or RSS feed, has to be approved by me. Browser automation is permanently rejected for the same reason. This constraint has turned into one of the system's best affordances. If I need an agent with access to the world I use a standard AI platform.

## 2. Local models for volume, frontier models for judgement

Work is facilitated by models appropriate to the task. A small model on the Jetson handles high-volume scoring and triage.
A larger model on the desktop GPU describes every passage and classifies new publications. Frontier
models, reached through an API, provide synthesis and tasks requiring reasoning depth. For structured
discussion sessions, the agent convenes one frontier model from each of three families (Anthropic,
Google and OpenAI) so the perspectives genuinely differ.

**Why.** Sending everything to a frontier model would be slow and expensive, and full texts would
leave my hardware. On the other hand, running everything locally would sacrifice quality in key areas.

**The cost.** Two tiers of local hardware to look after (inside and outside the VLAN), and a rule that model versions are pinned
exactly. Now that workflow bugs have been ironed out those constraints are not noticeable.

## 3. One key, one machine

Each credential lives on exactly one machine. Everything else reaches the service through a small
bridge that lets it use the service without ever seeing the key.

**Why.** A compromised agent can search the library, but not copy the key and use it elsewhere.

**The cost.** More small services to run, and a rule that no new credential-bearing service is
deployed until its boundary is defined. In practice I never notice the boundaries between the services; usage is seamless despite the agents being constrained.

## 4. The closed universe, enforced by the network

Every machine denies outbound traffic by default. The only way out to the web is a filtering
proxy on the cluster head, with a separate list of allowed destinations for each machine, and every
request it handles is logged. The feed reader is the one exception. Feeds can come from anywhere, so
it may request any destination, but only through the proxy.

**Why.** I have complete control over what sources agents have access to, and what problems they can introduce.

**The cost.** Each new source needs a deliberate addition. In practice I find I have all the sources I need so this is not an issue.

## 5. Allowing PDFs to leave the system

The original rule was that copyrighted full texts would never leave my own machines. In practice
the Zotero library was already storing every attached PDF on cloud servers, though, and keeping the
rule meant filing each book twice: once in the Zotero library, once in a folder on the desktop.

I decided that the Zotero library's cloud storage is a trusted channel. The desktop now fetches PDFs from the library
itself. Filing a book in my Zotero library is the only step needed to get it into TM.

**What didn't change.** Extraction, description and embedding still happen locally. No full text is
sent to a cloud model.

**Why it's here.** It shows what partial sovereignty looks like in practice: considered tradeoffs made on my own judgement and with awareness of the practical impact.

## 6. Moving triage off the Jetson

Each week the cluster harvests new records from PhilPapers, a large index of philosophy
publications, and a model sorts them for relevance to my research tracks. The plan was for the
small model on the Jetson to do this. It couldn't: the index returns every record *modified* that
week, often more than 80,000, and at the Jetson's pace one week's file took four days.

Speed wasn't the only problem. The 8-billion-parameter model marked about 0.4% of records as
relevant. The 32-billion-parameter model on the desktop marked about 21%. The small model was
quietly discarding papers I would have wanted. I relented and moved triage to my desktop computer off TM VLAN. The records the desktop marks as relevant
are stored in a PhilPapers collection of their own on the Jetson, which the agent can search alongside
the corpus.

**Why it's relevant.** It is the clearest case of finding a performance floor: this was a task the small model could run,
but not well enough. By moving up to a more powerful but still local machine, I compromised on system complexity but not data sovereignty.

## 7. Removing Google Scholar

The agent originally had five catalogues to search, including Google Scholar. Google Scholar was the
odd one out: it has no public API, so the tool scraped its pages, broke whenever Google rate-limited it,
and could hang for five to ten minutes. In September 2026 I removed the tool and closed the domain in
the outbound proxy. OpenAlex covers most of the humanities material it was there for. It had become more of an attack surface than a useful piece of functionality.

OpenLibrary led to different conclusions. In that case TM allows the agent to verify a book's details
from its ISBN, but only through a small bridge on the cluster head that makes fixed lookups. Allowing
the agent to reach OpenLibrary directly would have introduced similar issues to Google Scholar.

**Why it's relevant.** The closed universe is maintained, on a case by case basis balancing risk, terms of service restrictions, and functionality. 
