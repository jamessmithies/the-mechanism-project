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

## What it is not

It is not cheaper, faster or simpler than renting. A cloud GPU would do the heavy work for roughly
the same money, and a small virtual server would run the always-on services. The point was never
efficiency. Rented infrastructure arrives with its trade-offs already made and hidden behind an
invoice. Owned hardware pushes back, and the pushback is the evidence.

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
- **Models of different sizes.** A small model on the Jetson, a larger one on the desktop and a
  frontier model through an API. Model scale becomes something to study directly: which research
  tasks need a frontier model, and which don't.
- **A degree of data sovereignty.** Partial and negotiated, not absolute. The interesting thing is
  the degree: where keeping data local was cheap, where it was expensive, and where I gave it up
  deliberately.
- **Constraints as evidence.** Collections that existed but couldn't be searched. Annotations
  produced and never ingested. Jobs that outgrew the hardware they started on. Each shows where the
  apparatus resists, and surfacing that resistance is the purpose of critical technical practice.
