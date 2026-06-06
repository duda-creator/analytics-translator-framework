# Marcin Duda · Analytics Translator
## Consulting Framework

> "You don't have a data problem. You have a last-mile analytics problem."

---

# Overview & Problem Statement

**Marcin Duda · Analytics Translator**

## You don't have a data problem. You have a last-mile analytics problem.

**I solve that.**

Most organisations have invested heavily in data infrastructure. The pipelines run. The warehouse is populated. The dashboards exist. And yet the business still doesn't trust the numbers, still can't answer the questions that matter, and still runs on spreadsheets, drowning in reconciliations.

That's not a data problem. That's a last-mile analytics problem: the gap between what your data infrastructure can do and what your business users actually get from it. It's the most consistently under-invested layer in analytics.

It's the space I specialize in.

---

**Marcin Duda — Analytics Translator**

Full-stack analytics practitioner specialising in semantic models, self-service analytics, and analytics enablement. I work at the intersection of business, data modelling, and decision-making, translating business concepts into trusted analytical products that people can actually use. I help organisations turn fragmented reporting into scalable analytical capability, ensuring it reaches the people who need to make decisions with it.

---

I specialise in designing the analytical layer that sits between data infrastructure and business decision-making.

My work focuses on creating governed semantic models, consistent business definitions, and self-service analytical experiences that allow users to explore data with confidence.

Rather than treating analytics as a reporting function, I treat it as an organisational capability. The objective is not simply to deliver dashboards, but to create trusted analytical products that scale across teams, reduce dependency on manual reporting, and support better decision-making.

This often involves:

- Defining shared business metrics and terminology
- Building semantic models and analytical data products
- Designing decision-support experiences for executives, analysts, and operational teams
- Expanding self-service analytics capabilities
- Establishing trust through governance and analytical consistency
- Preparing data foundations for AI-enabled analytics

The goal is straightforward: transform fragmented and dispersed data assets into decision-making capability.

---

## How I work

**You know the business. I turn that knowledge into analytics.**
You are the domain expert. My job is to ask the questions that turn your business logic into a data model that actually reflects how your business works. That translation is a distinct skill from knowing your industry — and it's the one that's been missing.

**Fast, pragmatic, iterative**
Proof of Concept on real sample data first. Working prototype on full data second. Deployment and iterative enhancements third. Every stage produces something usable — no months-long requirements gathering before first value.

**Never a black box**
Documentation is built into the delivery rhythm, not deferred. A fixed, minimal artefact set ensures every solution remains explainable, ownable, and maintainable — by you, not by me. When definitions evolve, you change them. When logic shifts, you drive it. The solution adapts. No middleman required.

---

## What the Analytics Translator does differently

**What most BI delivery looks like**

- You got a dashboard, but you're still scrambling for an answer when your MD asks a question on Monday morning.
- You exported it to Excel. Your colleagues did too. Now there are six versions of the truth.
- Reports designed around the data, not around the decisions.
- Success was measured by go-live, not by business adoption.

**What I deliver**

- A semantic layer designed around the questions your business actually asks.
- One definition. One number. Every tool, every team, every time.
- KPIs built around how your business thinks - not how the data warehouse is structured.
- I'm not done when it's built. I'm done when your people are using it.

---

# Entry Point Framework

**Where does your conversation start?**

Business users don't present their problems in analytical terms — they present them as the situation they're in. This framework meets them at their entry point and maps a clear path forward from there.

---

## 📊 Entry Point 1: Existing Dashboard

**Complexity: Targeted** | Most common entry

> *"Our dashboard is always out of date, nobody knows where the numbers come from, and it only tells us what happened — not what to do about it."*

### Phase 01 — Assess Current State
- Audit report sources — how many, which systems
- Identify refresh mechanism — manual, scheduled, broken
- Catalogue all metrics: where defined, by whom
- Document who uses it, what decisions it informs
- Score trust level: do users believe the numbers?

### Phase 02 — Define Target State
- Agree analytical layers: tracking / diagnosis / action
- Define minimum refresh frequency
- List 5–10 KPIs that must be certified and consistent
- Agree what "trusted" looks like — watermark, lineage
- Sketch report structure before touching the model

### Phase 03 — Gaps & Bottlenecks
- Metric logic lives in report, not shared model
- No time intelligence — only point-in-time snapshots
- Manual data pull blocks refresh frequency
- No single KPI owner → definitions drift
- Report shows status but no drill-to-cause

### Phase 04 — Solution Steps
- Automate data flow first: immediate visible win
- Migrate metric logic to certified model layer
- Add time intelligence: YoY, MoM, rolling 12
- Redesign layout: What → So What → Now What
- Certify model, document measures, add lineage

**⚠ Key bottlenecks**
- Manual refresh creates data staleness
- Metric logic embedded within individual dashboards
- No drill-through — can't go from summary to cause
- Trust deficit from past errors never addressed

**✓ Iterative target state**
- Automated daily (or more frequent) refresh
- All KPIs defined once in model, not in report
- Three-layer report structure operational
- Certified model with documented ownership

**Business questions this unlocks**
- Why does Finance get a different number than Business?
- Can I see this by region, product, and month?
- What does Revenue mean in this context?
- How do I know this is the right number?

> *"I don't just make your dashboard look better — I make it so your team can trust it, explore it, and act on it without asking IT for a new report every time."*

---

## 🗄️ Entry Point 2: Disconnected Data

**Complexity: Full Stack** | Full stack opportunity

> *"We have data in the ERP, the CRM, spreadsheets, and a shared drive. No one can ever get a consistent answer because everyone is pulling from a different place."*

### Phase 01 — Assess Current State
- Map all source systems: ERP, CRM, flat files, spreadsheets
- Identify shared dimensions: customer, product, country
- Document how each team currently joins data
- Identify the most painful reconciliation — anchor it
- Assess data quality per source: completeness, latency

### Phase 02 — Define Target State
- Define minimum set of conformed dimensions needed
- Agree primary analytical questions integration must answer
- Set data freshness targets per domain
- Identify who owns each entity definition going forward
- Agree on target consumption layer: Power BI, Excel, Custom UI

### Phase 03 — Gaps & Bottlenecks
- No shared reference data/dimensions across systems
- No integration layer — joins done manually in Excel
- Conflicting grain across sources
- IT controls source access — business can't self-serve

### Phase 04 — Solution Steps
- Build staging layer: extract each source cleanly
- Design conformed dimensions: customer, product, time
- Build fact tables at agreed grain per subject area
- Develop semantic model, shared KPIs, time intelligence
- Deploy governed self-service with RLS and certified metrics

**⚠ Key bottlenecks**
- No shared entity definitions across systems
- Manual join process = reconciliations factory
- Different data granularity across source systems
- No governed access path for business users

**✓ Iterative target state**
- Single version of every shared entity
- Automated integration pipeline with documented lineage
- Business users self-serve from one certified model
- Reconciliation meetings eliminated for covered domains

**Business questions this unlocks**
- Why does my revenue not match Finance?
- Can we combine CRM pipeline with ERP actuals?
- Who owns the customer dimension?
- How do we stop data living in five places?

> *"I can take your scattered data landscape and build a single connected model every function pulls from — so reconciliation meetings become unnecessary."*

---

## 🧮 Entry Point 3: Spreadsheet Dependency

**Complexity: Moderate** | Governance entry

> *"We have one spreadsheet that takes three hours every month to update, nobody else understands it, and we're terrified it's wrong."*

### Phase 01 — Assess Current State
- Identify the 3–5 most business-critical spreadsheets
- Map data inputs: where does each spreadsheet get data from?
- Document the logic: calculations, allocations, filters
- Identify maintenance responsibility: who owns and supports it?
- Assess downstream use: what decisions does it feed?

### Phase 02 — Define Target State
- Agree which processes must be automated first
- Define acceptable refresh cadence per process
- Identify what logic belongs in model vs spreadsheet
- Agree governance: documentation, ownership, version control
- Define change controls: who can make changes and how are they approved?

### Phase 03 — Gaps & Bottlenecks
- Data acquisition is manual — human is the bottleneck
- Critical logic lacks transparency and traceability
- No version control — changes invisible and irreversible
- Spreadsheet used as both ETL and reporting tool
- No data quality check before spreadsheet runs

### Phase 04 — Solution Steps
- Replace manual pulls with Power Query / pipeline
- Document and test all existing logic first
- Migrate metric calculations to shared model layer
- Retain Excel as a controlled consumption layer, not a logic owner
- Add version control, refresh schedule, named owner

**⚠ Key bottlenecks**
- Single person dependency on every critical file
- No automated data connection — all manual copy-paste
- Logic embedded in formulas nobody else understands
- No change control — errors introduced silently

**✓ Iterative target state**
- Automated data feed replaces manual extraction
- Core metric logic in versioned, certified model
- Excel retained as analysis surface — not data processor
- Named owner, documented logic, scheduled refresh

> *"I can take your critical spreadsheets and rebuild the underlying logic properly — so the business process keeps running without the fragility and the key-person risk."*

---

## 🤖 Entry Point 4: AI / Copilot Pressure

**Complexity: Moderate** | Emerging urgency

> *"Leadership wants us to use AI tools on our data but when we ask Copilot a question about revenue we get a different number every time."*

### Phase 01 — Assess Current State
- Test what AI tools return for 3–5 core business questions
- Identify why answers are inconsistent: model quality, labelling?
- Audit semantic model: measure descriptions, table names
- Assess data quality in the layer AI is querying
- Identify which use cases business actually wants AI to answer

### Phase 02 — Define Target State
- Define 5–10 questions AI must answer consistently
- Agree what "AI-ready" means: certified model, documented measures
- Identify pilot use case — narrow scope, high visibility
- Set accuracy benchmark per question
- Agree governance: who validates AI outputs?

### Phase 03 — Gaps & Bottlenecks
- Measures have no descriptions — AI can't interpret intent
- Tables named technically, not semantically
- No single certified model: AI queries conflicting sources
- Time intelligence missing: AI can't handle period comparisons
- No validation process for AI outputs

### Phase 04 — Solution Steps
- Audit and rename all tables, columns, measures to plain English
- Write measure descriptions for every certified KPI
- Build or remediate time intelligence layer in model
- Connect AI tool to certified model only — not raw data
- Establish validation workflow: spot-check AI outputs

**⚠ Key bottlenecks**
- AI queries ambiguous or unlabelled model objects
- No single certified model — AI picks inconsistent sources
- Time intelligence absent — no period comparisons
- No human validation step for AI outputs

**✓ Iterative target state**
- All measures described in plain business language
- AI connected exclusively to certified semantic model
- Time intelligence fully operational
- Pilot producing consistent, validated outputs

> *"Your AI tools are only as good as the data model underneath them. I build the foundation that makes your AI investment actually work - instead of confidently giving you the wrong answer."*

---

## 📈 Entry Point 5: No Analytics Capability (Greenfield)

**Complexity: Full Stack** | Greenfield opportunity

> *"We spend two days before every board meeting manually pulling numbers from three systems. There's no consistency and leadership always challenges the figures."*

### Phase 01 — Assess Current State
- Run structured discovery: what questions are asked every week?
- Identify data sources that exist and their accessibility
- Map current reporting process end-to-end
- Identify highest-pain analytical gap
- Assess analytical competency: what tools users can use comfortably?

### Phase 02 — Define Target State
- Prioritise top 10–15 business questions as design brief
- Define minimum viable reporting layer for immediate value
- Sequence iterative delivery
- Set clear success metrics (adoption, usage, decision impact)
- Define the end-state self-service vision, with explicit scope boundaries

### Phase 03 — Gaps & Bottlenecks
- No data extraction layer: no governed access to source data
- No platform chosen: technology decisions blocking delivery
- No metric definitions: nobody has agreed what KPIs mean
- No internal capability: every change requires external support
- No governance: no owner, no refresh, no trust process

### Phase 04 — Solution Steps
- Phase 1: Extract top 3 sources, minimal schema, core dashboard
- Phase 2: Add time intelligence, dimensions, hierarchies
- Phase 3: Extend model, enable self-service layer, certify metrics
- Phase 4: Train key users, document model, establish governance
- Each phase produces something usable — not a big-bang project

**⚠ Key bottlenecks**
- No governed access to source data
- No agreed metric definitions to build from
- Risk of "big bang" approach — nothing for 12 months
- No internal capability to maintain what's built

**✓ Iterative target state**
- Phase 1 live within 4–6 weeks: 3 sources, core KPIs
- Metrics defined and certified before reporting goes live
- Self-service layer operational by Phase 3
- Internal champion identified and enabled

> *"I can take you from manual spreadsheet chaos to a working analytics layer in a focused engagement — starting with the questions that matter most, not a two-year platform project."*

---

## ❓ Entry Point 6: The Translation Failure

**Complexity: Diagnostic** | Business-IT disconnect

> *"Our last dashboard looked great in the demo. Three months after go-live, everyone was back in Excel. The business never trusted the numbers enough to stop checking them manually. We don't have the appetite to go through that again."*

### Phase 01 — Assess Their State
- "Walk me through how you get your key numbers each week"
- "What question do you most wish you could answer but can't?"
- "When was the last time a number was challenged in a meeting?"
- Check whether insights lead to clear action, not just explanation

### Phase 02 — Define Target (Together)
- Reframe from "what report do you want" to "what decision?"
- Establish they own the metric definitions — you translate them
- Agree on 3 questions analytics should answer that currently can't

### Phase 03 — Surface Real Gaps
- Probe the metric: "Is revenue gross or net? Before rebates?"
- Test the data: "Would ERP revenue match your spreadsheet?"
- Test ownership: "Who would you call if the number was wrong?"

### Phase 04 — Reposition & Propose
- Translate findings into one of the other entry point frameworks
- Propose a focused diagnostic engagement — not a full solution
- Output: a shared problem statement, not a quote
- Make explicit: "You own the business rules, I own the translation"

**⚠ Key bottlenecks**
- The people who defined the requirements weren't the people who felt the problem — so the brief was wrong before the build started
- Everyone described their piece of the process, nobody described the whole — leaving the biggest inefficiencies invisible and unaddressed
- The build fixed what was asked for, not what was actually broken — and what was actually broken was often one step upstream or downstream
- Developers optimised the current state rather than questioning whether the current state was worth keeping

**✓ Iterative target state**
- Requirements gathered across the full stakeholder map — not just the loudest voice in the room — so the brief reflects the actual problem, not the presented one
- End-to-end process walkthrough before any build begins — because the highest-value improvement is rarely where the conversation started
- Every request assessed against the full workflow: what feeds it, what follows it, and what breaks if it changes
- Current state treated as a reference point, not a starting point — the question is always what the business needs, not what the system already does

> *"I'm not the domain expert — you are. My job is to ask the questions that turn your business knowledge into a data model that actually reflects how your business works. That's a different skill from knowing your industry."*

---

# Delivery Methodology

**Four stages, six artefacts, every engagement**

The same cadence applies regardless of entry point. The content of each stage differs by complexity. Documentation is built into the rhythm — not deferred to the end. Nothing becomes a black box.

---

## Delivery Cadence

### Stage 01 — Discover
**Timing: 1–5 days**

Structured conversations using entry-point diagnostic questions. No tools yet — understand the problem, not the solution.

**Output:** Current state in business language. Top 3 gaps. Target state as answerable questions. Proposed scope.

### Stage 02 — POC
**Timing: 1–2 weeks**

Real but sampled data. Core model skeleton and 1–2 most important KPIs. Clickable prototype for business validation.

**Output:** Working prototype. First draft Metric Dictionary and Data Map. Business confirms model reflects their logic.

### Stage 03 — Build
**Timing: 1–8 weeks**

Full data, complete model, key reports. Delivered in sub-releases — not a single handover. Model Specification produced.

**Output:** Production model. Complete reporting layer. Model Specification. First Handover Guide. Data Product Passport.

### Stage 04 — Embed
**Timing: Ongoing**

Iterative enhancements. Additional reports and analytical capabilities. Documentation evolves with model.

**Output:** Enhanced model iterations. Updated artefacts. Trained users. Versioned metric changes communicated to consumers.

---

## The Fixed Artefact Set

### Artefact 01 — Discovery Summary
**Produced: end of Discover stage**

One page. Current state in business language — not technical architecture. Top three gaps. Target state as a set of business questions the solution will be able to answer. The scoping contract.

### Artefact 02 — Metric Dictionary
**Built: POC stage · Maintained: forever**

Plain English name, business definition (words not DAX), origin type (upstream/domain/hybrid), owner, exclusions, date logic, version. Business users certify this. Eliminates the Finance vs Operations problem.

### Artefact 03 — Data Map
**Produced: POC · Updated: Build stage**

Business-readable flow from source system through transformation to report surface. Not a technical ERD. Answers "where does this number come from?" without a developer. Anti-black-box document.

### Artefact 04 — Model Specification
**Produced: start of Build stage**

Translates Metric Dictionary and Data Map into what needs to be built: fact tables, dimensions, key measures, time intelligence requirements, refresh schedule, RLS needs. Technical handoff that a business-literate reader can follow.

### Artefact 05 — Handover Guide
**Produced: end of every iteration**

One page per report or model component. Answers: "How do I navigate this?", "How do I know the data is current?", "What do I do if something looks wrong?" Replaces implicit knowledge. Updated every iteration.

### Artefact 06 — Data Product Passport *(Data Mesh)*
**Produced: Build stage · gate before Embed**

Product name/version, owning domain, covered subject areas, consumption interfaces, refresh SLA, data quality indicators, metric ownership summary, known limitations. Front page of the product in the data catalogue.

---

# Common Layer

**Present in every entry point. Complexity varies — the need does not.**

Six components appear in every engagement regardless of entry point. The shape, governance formality, and technical depth differ by complexity. The requirement to address them does not disappear.

---

## The Six Common Components

**🧊 Semantic / Data Model**
Every solution requires at least a minimal data model — from a single Power BI dataset to a full SSAS Tabular enterprise model. The grain, shape, and governance formality differ; the need does not.

**📐 Metric Definition**
Every engagement surfaces at least one metric defined differently in different places. Agreeing and encoding the canonical definition is always a deliverable, regardless of entry point.

**📅 Date / Time Intelligence**
A shared, governed date table with consistent period logic (YoY, MTD, rolling) is required in every delivery that produces business reporting. It is almost always missing or inconsistent in the current state.

**🔄 Refresh & Pipeline**
Every current state has a data freshness problem — manual, broken, or non-existent automation. The complexity of the fix ranges from a scheduled Power Query refresh to a full ELT pipeline.

**🛡️ Trust & Governance**
Users do not trust what they cannot verify. Every delivery must address certification, data lineage visibility, and documented ownership — or adoption will not follow, regardless of technical quality.

**🎓 User Enablement**
Handing over a model or dashboard without structured enablement produces low adoption. Every delivery includes at minimum a navigation guide and a short structured handover session.

---

## How Common Layer Complexity Scales by Entry Point

| Component | Dashboard | Disconnected | Spreadsheet | AI Ready | Greenfield | Translation |
|---|---|---|---|---|---|---|
| Data model complexity | Low | Full | Moderate | Moderate | Full | Diagnostic only |
| Pipeline / ETL work | Low | Full | Moderate | Low | Full | Diagnostic only |
| Metric definition work | Moderate | Full | Moderate | Full | Full | Full |
| Time intelligence | Moderate | Moderate | Low | Moderate | Moderate | Diagnostic only |
| Governance formality | Moderate | Full | Moderate | Moderate | Full | Diagnostic only |
| User enablement | Low | Moderate | Low | Moderate | Full | Moderate |

*Key: Low = Targeted · Moderate = Moderate · Full = Full depth · Diagnostic only = no build work*

---

# Metric Ownership Model

**Not all metrics are owned the same way**

The reconciliation path runs in opposite directions depending on metric origin type. Conflating these in documentation is one of the most common causes of the Finance vs Operations problem at the metric level.

---

## The Three Origin Types

### ⬇️ Upstream-Certified
**Calculated and owned externally**

Delivered via a feed or report from a system or function outside this domain. The domain is a *consumer*, not an owner. Examples: LCR ratio from regulatory system, RWA from credit risk engine, intercompany funding rates from central TMS.

> **Reconciliation direction:** YOUR model → upstream system. If they differ, the upstream is right until proven otherwise.

### 🔧 Domain-Derived
**Defined and calculated within this domain**

Built from source field values the domain controls or has direct access to. The domain *is* the owner. Examples: Net FTP from internal spread calculation, liquidity buffer utilisation from position data, concentration of funding by counterparty.

> **Reconciliation direction:** downstream consumers → YOUR model. This model is the golden source. Defend it with the Metric Dictionary.

### ⚗️ Upstream + Domain-Adjusted (Hybrid)
**The most dangerous — looks certified but isn't**

Starts as an upstream figure but has a local adjustment applied (management overlay, different perimeter, entity exclusion). Consumers assume it matches the upstream — it doesn't, by design. Must be flagged explicitly.

> **Document both:** upstream source AND adjustment logic. State explicitly: "Will not match upstream. Expected variance: [desc]."

---

## Metric Dictionary — Structure & Sample

| Metric Name | Origin | Business Definition | Owner / Golden Source | Date Logic | Exclusions | Version |
|---|---|---|---|---|---|---|
| LCR Ratio | UPSTREAM | Liquidity Coverage Ratio as reported by the regulatory system. HQLA ÷ Net Cash Outflows over 30-day stress period. | Regulatory Reporting System · Risk function | Reporting date (T) | None — use as received | v1.0 |
| Net FTP Spread | DOMAIN | Difference between the internal transfer price rate assigned to a product and the actual cost of funds for that tenor, expressed in basis points. | Treasury Analytics model · Treasury team | Trade origination date | Excludes intercompany trades flagged IC=Y | v2.1 |
| Liquidity Buffer (Mgmt) | HYBRID | Regulatory HQLA pool with management adjustments: excludes pledged assets not available for same-day monetisation and adds uncommitted but operationally available reserves. | Base: Regulatory System · Adjustment: Treasury team | End of business day | Pledged assets, restricted reserves | v1.3 |
| Funding Concentration | DOMAIN | Top-10 counterparty funding as % of total wholesale funding. Identifies single-name concentration risk in the funding base. | Treasury Analytics model · Treasury team | As-at date (snap) | Retail deposits excluded; intragroup excluded | v1.0 |

---

## Why this distinction is the anti-black-box mechanism

Most BI deliveries treat all numbers as equally opaque — users don't know where they come from, who owns them, or what to do when they're challenged. Making ownership and reconciliation paths visible — and differentiating them by origin type — is the structural mechanism that converts a model from a black box into a governed data product. When a number is challenged in a board meeting, the owner, the golden source, and the reconciliation path are all documented. The conversation moves from "which number is right?" to "which definition are we applying, and why?"

---

# Data Mesh Alignment

**Additive framing, not architectural replacement**

Data mesh is an ownership and governance principle, not a technology pattern. The delivery methodology and technical architecture remain intact. What changes is how ownership, interfaces, and governance are framed around them.

---

## Core Data Mesh Principles — How They Map

### Principle 1 — Domain Ownership of Data
The domain that best understands the data owns it end-to-end — pipeline, quality, SLAs, and versioning. In the delivery methodology this shifts the Discover question: "Who currently owns the data between source and consumption — and is that the right team?" The answer shapes whether you're enabling a central IT function or a domain-owned product.

### Principle 2 — Data as a Product
Data has a defined interface, named consumers, quality SLAs, and a published specification — just like software. The semantic model is not a BI layer; it is the queryable interface of the data product. The Data Product Passport (Artefact 06) is the published specification. Versioning discipline in the Metric Dictionary makes it behave like a software API.

### Principle 3 — Self-Serve Data Platform
Consumers connect to the product's interface without needing to understand the warehouse underneath. The certified semantic model — with named measures, described dimensions, and documented RLS — is that interface. AI tools connect here too, which is why the AI entry point is directly improved by data mesh discipline.

### Principle 4 — Federated Computational Governance
Global standards, local ownership. The Metric Ownership Model (upstream/domain/hybrid classification) is the governance instrument that makes this operational. Conformed metrics (like a shared date table or agreed entity definitions) are the global standards. Domain-derived metric definitions are local ownership in action.

---

## What Changes in the Methodology — Additive Only

| Stage / Artefact | Change Type | What Changes | What Stays the Same |
|---|---|---|---|
| Discover stage | ADD | Add ownership question: "Who owns this data between source and consumption — and is that right?" | All other diagnostic questions unchanged |
| POC stage | REFRAME | Mock data / sample data used explicitly as contract validation — does the model produce correct outputs against known inputs? | POC scope, timing, and deliverable unchanged |
| Build stage | GATE | Data contract formalised as delivery gate before publishing. Nothing goes to self-service until contract is agreed. | Build sequence, model architecture unchanged |
| Metric Dictionary | ADD | Version column + "last changed" field on every measure entry. Downstream consumers notified on definition change. | All existing fields unchanged |
| Embed stage | REFRAME | Every measure change is a version increment. Consumer notification is part of the iteration process, not optional. | Iteration cadence, enhancement process unchanged |
| Artefact 06 (new) | ADD | Data Product Passport produced at Build stage. Contains metric ownership summary, consumption interfaces, SLA, known limitations. | Artefacts 01–05 unchanged in purpose and format |

---

*© 2026 Marcin Duda. All rights reserved. This framework, its structure, terminology, and content are the intellectual property of Marcin Duda. No part may be reproduced, distributed, or used in derivative works without prior written permission.*

*Last-Mile Analytics Framework · Entry Point Model · Delivery Methodology · Metric Ownership Model · Data Mesh Alignment · Common Layer Architecture*
