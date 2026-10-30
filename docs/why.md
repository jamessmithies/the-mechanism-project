# Why TM was built this way

## The method

The Mechanism (TM) is an exercise in critical technical practice. I could have designed an AI research
system on cloud infrastructure, where the machines and the network are out of reach behind someone
else's interface, or signed up to a commercial research platform. Instead I built it from what I already had: an existing desktop and a disused
Raspberry Pi 4 cluster. Working directly with the physical machines and the network allowed me to explore the possibilities and trade-offs of AI for humanities and social science research first-hand,
rather than experimenting with services designed by vendors.

The architecture demonstrates this. It grew around what was available, with several design decisions (especially related to security) emerging by happy coincidence rather than foresight or planning. Three spare nodes sit powered off, for possible future expansion. I resisted incorporating my desktop PC into the system for as long as possible but relented when the small inference board took four days to process one week's batch. Where the found hardware ran out, I added a few pieces: two Raspberry Pi 5s and an NVIDIA Jetson Orin Nano for local inference.

## A prototype for thinking with

Building TM locally was also a way to understand what AI could do for humanities and social science
research at all. When I started, there was no established model for AI enabled research beyond some 'chat to my documents' services. There is still no settled picture of how
AI might fit into a full research workflow, from finding and triaging new work, through reading and
annotation, to retrieval and writing. Cloud AI services I experimented with felt limited and lacking in an understanding of what humanities research workflows consist of.

A physical prototype made that exploration easier. Each idea could be tried on real machines against
a real library, and the result retained, changed, or discarded. The system's scope grow one component and one service at a time,
from feed triage to a searchable corpus to an agent working across the whole workflow. Concept
development undertaken online, through wireframe diagrams, hosted services, and cloud infrastructure interfaces, would have
been less tactile, and I suspect less productive. 

## What it is not

TM is not faster or simpler than using cloud infrastructure or an AI research platform, but efficiency was never the point. Rented infrastructure and digital platforms have a wide range of trade-offs, from limited configuration options, to problems with data soveriegnty, higher monthly costs, and issues with long-term sustainability. Using recycled hardware means I have complete control and can choose to keep it going for as long as the hardware keeps running, upgrading components along the way if they fail or if I need more power.

TM has turned out to be quite cost effective. The project is funded by my ANU Futures
Scheme award (2024–2026). The found hardware cost nothing (the Pi cluster was funded by King's College London when I worked there and was sitting in pieces after my migration to Australia), the additional purchases were modest. The cluster only draws about 37 watts, under A$10 a month in electricity. My System 76 Thelio draws significantly more power but is my daily driver PC and only processes TM jobs occassionally. I am currently spending ~A$10 a month for frontier AI tokens. The hardware purchases, the electricity, and an allowance for replacement parts amount to a little over A$40 a month over five years. I plan to run the system for at least that long. I have an upcycled ThinkPad x230 laptop pushing 15 years old: maintaining hardware beyond its shelf-life is a personal hobby. Renting the equivalent (a server for the always-on services plus a GPU on demand for the heavy batches) would cost A$40–80 a month in perpetuity. 

It is worth emphasising that TM is not a fully closed system. Synthesis, the processing step where a frontier model is used to read retrieved passages and write abstracts, goes to a commercial model through an API, and the Zotero reference library syncs to Zotero cloud storage. Frontier AI tokens (accessed via Open Router) are used for intensive reasoning and critique when needed. If local models provide enough capability one day I will configure TM as a fully offline system but until then commerical AI is used for burst out capability.


