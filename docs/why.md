# Why build it this way

## The method

The Mechanism is an exercise in critical technical practice. I could have designed an AI research
system on cloud infrastructure, where the machines and the network are out of reach behind someone
else's interface. Instead I built it from what I already had: an existing desktop and a disused
Raspberry Pi 4 cluster. Working directly with the physical machines and the network meant meeting
the possibilities and trade-offs of AI for humanities and social science research first-hand,
rather than inheriting decisions a vendor had already made.

The architecture shows it. It grew around what was available, and its oddities record what the
hardware could and could not do. Three spare nodes sit powered off. Work moved to the desktop when
the small inference board took four days to process one week's batch. Where the found hardware ran
out, I added a few pieces: two Raspberry Pi 5s and an NVIDIA Jetson Orin Nano for local inference.
Each addition marks a limit the build reached.

## A prototype for thinking with

Building it locally was also a way to understand what AI could do for humanities and social science
research at all. When I started, there was no established model for that: no settled picture of how
AI might fit into a full research workflow, from finding and triaging new work, through reading and
annotation, to retrieval and writing. The question had to be explored, not looked up.

A physical prototype made that exploration easier. Each idea could be tried on real machines against
a real library, and the result kept, changed or discarded. Its scope could grow one piece at a time,
from feed triage to a searchable corpus to an agent working across the whole workflow. Concept
development done online, through diagrams, hosted services and other people's interfaces, would have
been less tactile, and I suspect less productive. Here the ideas had to run before they counted.

## What it is not

It is not faster or simpler than renting, and efficiency was never the point. Rented infrastructure
arrives with its trade-offs already made and hidden behind an invoice. Owned hardware pushes back,
and the pushback is the evidence.

On cost, though, it compares better than it might seem. The found hardware cost nothing new, the
additions were modest and were funded by my ANU Futures Scheme award (2024–2026), and the cluster draws about 37 watts, under A$10 a month in electricity.
Renting the equivalent, a server for the always-on services plus a GPU on demand for the heavy
batches, costs several times that every month. I plan to run The Mechanism for at least five years.
Spread over that span, the purchases, the electricity and an allowance for replacement parts come to
a little over A$40 a month. Renting a server for the always-on services alone would cost A$40–80 a month,
before any GPU time. That sum leaves out the time
spent building it, which was the point.

Nor is it sealed off. Synthesis, the step where a frontier model reads retrieved passages and
writes, goes to a commercial model through an API, and the reference library syncs through a cloud
service. The Mechanism is local where locality teaches something or protects something, and it
rents where it doesn't. It says so.

## What emerged along the way

These benefits weren't the reasons for building it. They're findings.

- **Always-on work.** Triage of new publications, feed scoring and annotation harvesting turned out
  to run on a different rhythm from conversation with a frontier model. That is continuous,
  low-stakes, high-volume work, a distinct kind of AI use that only became visible once the
  infrastructure was there to run it.
- **Finding the floor.** The cluster made it possible to find the lower limits of useful AI by
  working upward from the bottom. A small 8-billion-parameter model on the Jetson handled a task
  until the task outgrew it. Then a 32-billion-parameter model on the desktop took over, and a
  frontier model was used only for what neither could manage. Model scale becomes something to
  study directly: which research tasks need a frontier model, and how much runs well on far less.
- **Full texts stay on my own hardware.** Whole books and articles are extracted, chunked,
  described by a local model, embedded and indexed on machines I own. None of that runs through a
  frontier model or a cloud service. A frontier model sees only the handful of passages a search
  returns when it answers a question, never the book. The PDFs themselves sync through my reference
  manager's storage, so this isn't total data sovereignty. It is partial and negotiated, and the
  degree is the interesting part: where keeping data local was cheap, where it was expensive, and
  where I gave it up deliberately.
- **Constraints as evidence.** Collections that existed but couldn't be searched. Annotations
  produced and never ingested. Jobs that outgrew the hardware they started on. Each shows where the
  apparatus resists, and surfacing that resistance is the purpose of critical technical practice.
