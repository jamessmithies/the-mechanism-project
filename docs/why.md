# Why TM was built this way

## The method

The Mechanism (TM) is an exercise in critical technical practice. I could have designed an AI research
system on cloud infrastructure, where the machines and the network are out of reach behind someone
else's interface. Instead I built it from what I already had: an existing desktop and a disused
Raspberry Pi 4 cluster. Working directly with the physical machines and the network meant meeting
the possibilities and trade-offs of AI for humanities and social science research first-hand,
rather than inheriting decisions a vendor had already made.

The architecture demonstrates this. It grew around what was available, and its oddities record what the
hardware could and could not do. Three spare nodes sit powered off, for possible future expansion. Work moved to the desktop when
the small inference board took four days to process one week's batch. Where the found hardware ran
out, I added a few pieces: two Raspberry Pi 5s and an NVIDIA Jetson Orin Nano for local inference.

## A prototype for thinking with

Building TM locally was also a way to understand what AI could do for humanities and social science
research at all. When I started, there was no established model for that: no settled picture of how
AI might fit into a full research workflow, from finding and triaging new work, through reading and
annotation, to retrieval and writing. Cloud AI services I experiemtned with felt limited and lacking in an understanding of what humanities research workflows consist of.

A physical prototype made that exploration easier. Each idea could be tried on real machines against
a real library, and the result kept, changed or discarded. Its scope could grow one piece at a time,
from feed triage to a searchable corpus to an agent working across the whole workflow. Concept
development done online, through diagrams, hosted services, and cloud infrastructure interfaces, would have
been less tactile, and I suspect less productive. 

## What it is not

TM is not faster or simpler than renting, but efficiency was never the point. Rented infrastructure
has a wide range of trade-offs, from data soveriegnty to higher monthly costs, and issues with long-term sustainability. Using recycled hardware I own means I have complete control and can choose to keep it going for as long as the hardware keeps running, upgrading components along the way if they fail or if I need more power.

On cost, though, TM fares quite well. The project is funded by my ANU Futures
Scheme award (2024–2026). The found hardware cost nothing (the Pi cluster was funded by King's Colelge London when I worked there), the additional purchases were modest, and the
cluster only draws about 37 watts, under A$10 a month in electricity. My System 76 Thelio draws significantly more power but is my daily driver PC and only processes TM jobs occassionally.
Renting the equivalent (a server for the always-on services plus a GPU on demand for the heavy
batches) would costs several times that every month. I plan to run TM for at least five years, but have an upcycled ThinkPad x230 laptop pushing 15 years old: pushing hardware beyond its shelf-life is a personal hobby.
Spread over five years, the purchases, the electricity, and an allowance for replacement parts amount to
a little over A$40 a month. Renting a server for the always-on services alone would cost A$40–80 a month,
before any GPU time. That sum leaves out evenings spent building the system, but the knowledge and research potential easily balances out those labour costs.

TM is not a fully closed system, either. Synthesis, the step where a frontier model reads retrieved passages and
writes, goes to a commercial model through an API, and the reference library syncs through a cloud
service. TM is primarily local but bursts out to hyperscale infrastructure to provide access to frontier AI when needed. If local models provide enough capability one day I can easily configure TM as a fully offline system.


