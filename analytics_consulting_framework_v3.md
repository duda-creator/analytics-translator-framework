# Analytics Translator — Consulting Framework
**Marcin Duda · 2026**

> "You don't have a data problem. You have a last-mile analytics problem."

---

## Overview & Problem Statement

Most organisations have invested heavily in data infrastructure. The pipelines run. The warehouse is populated. The dashboards exist. And yet the business still doesn't trust the numbers, still can't answer the questions that matter, and still runs on spreadsheets, drowning in reconciliations.

That's not a data problem. That's a **last-mile analytics problem**: the gap between what your data infrastructure can do and what your business users actually get from it. It's the most consistently under-invested layer in analytics.

### Identity

**Full-stack analytics practitioner** specialising in semantic models, self-service analytics, and analytics enablement. Working at the intersection of business, data modelling, and decision-making — translating business concepts into trusted analytical products that people can actually use. Helping organisations turn fragmented reporting into scalable analytical capability, ensuring it reaches the people who need to make decisions with it.

### Specialisation

Designing the analytical layer that sits between data infrastructure and business decision-making. Work focuses on:

- Defining shared business metrics and terminology
- Building semantic models and analytical data products
- Designing decision-support experiences for executives, analysts, and operational teams
- Expanding self-service analytics capabilities
- Establishing trust through governance and analytical consistency
- Preparing data foundations for AI-enabled analytics

The goal: transform fragmented and dispersed data assets into decision-making capability.

### How I Work

**You know the business. I turn that knowledge into analytics.**
You are the domain expert. My job is to ask the questions that turn your business logic into a data model that actually reflects how your business works. That translation is a distinct skill from knowing your industry — and it's the one that's been missing.

**Fast, pragmatic, iterative**
Proof of Concept on real sample data first. Working prototype on full data second. Deployment and iterative enhancements third. Every stage produces something usable — no months-long requirements gathering before first value.

**Never a black box**
Documentation is built into the delivery rhythm, not deferred. A fixed, minimal artefact set ensures every solution remains explainable, ownable, and maintainable — by you, not by me. When definitions evolve, you change them. When logic shifts, you drive it. The solution adapts. No middleman required.

### What the Analytics Translator Does Differently

| What most BI delivery looks like | What I deliver |
|---|---|
| You got a dashboard, but you're still scrambling for an answer when your MD asks a question on Monday morning. | A semantic layer designed around the questions your business actually asks. |
| You exported it to Excel. Your colleagues did too. Now there are six versions of the truth. | One definition. One number. Every tool, every team, every time. |
| Reports designed around the data, not around the decisions. | KPIs built around how your business thinks — not how the data warehouse is structured. |
| Success was measured by go-live, not by business adoption. | I'm not done when it's built. I'm done when your people are using it. |

---

## Entry Point Framework

> Business users don't present their problems in analytical terms — they present them as the situation they're in. This framework meets them at their entry point and maps a clear path forward from there.

Each entry point follows the same four-phase structure: **Assess Current State → Define Target State → Gaps & Bottlenecks → Solution Steps**. Each phase is presented with both a Business Translation and an Analytics Translation.

---

### Entry Point 1 — Existing Dashboard

**Complexity:** Targeted · **Most common entry**

> *"Our dashboard is always out of date, nobody knows where the numbers come from, and it only tells us what happened — not what to do about it."*

#### Phase 01 — Assess Current State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | We pull numbers from all over the place — systems, files, shared drives. Nobody has a complete picture of what's where or what's authoritative. | **Source-to-report lineage mapping** — document every data source, connection path, refresh dependency, and transformation between source systems and the dashboard |
| 2 | Half our data updates are manual. When someone forgets or is out sick, we just don't have current numbers — and there's no warning when it fails. | **Refresh architecture assessment** — classify refresh mechanisms (scheduled, event-driven, manual), identify failure points, ownership, SLAs, and recovery procedures |
| 3 | Everyone has their own version of what our KPIs mean. There's no single place that says what they actually are or who owns them. | **Metric catalogue and business logic inventory** — document all measures, calculations, KPIs, filters, and business rules; identify ownership and duplication; establish a draft business glossary |
| 4 | Different teams use the dashboard for different things. I'm not sure it's actually answering the questions people need, or which decisions are supposed to depend on it. | **Usage and decision mapping** — identify user groups, report consumption patterns, and decision processes supported by the dashboard |
| 5 | People export to Excel to double-check the numbers before they present anything. That tells you everything about how much we trust the dashboard. | **Trust and adoption assessment** — evaluate data quality issues, reconciliation gaps, metric disputes, workarounds, and shadow reporting outside the dashboard |

#### Phase 02 — Define Target State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | I need to know what's happening, why it's happening, and what to do about it — not just a static snapshot of numbers. | **Analytics operating model design** — define required analytical layers (monitoring, diagnosis, prediction, action) and map them to user personas and decisions |
| 2 | By the time we see the numbers they're already outdated. I need data that's fresh enough to actually act on. | **Refresh and latency requirements** — define target refresh frequency, data availability windows, and reporting SLAs by use case |
| 3 | If we could agree on five KPIs everyone trusts and uses consistently, that would already change everything. | **Certified KPI framework** — identify critical business metrics, define calculation logic, ownership, and certification criteria |
| 4 | My team won't use the dashboard to make decisions until they're confident the numbers are right and they can explain where they come from. | **Trust and governance standards** — define lineage visibility, data quality controls, certification badges, ownership, and auditability requirements |
| 5 | Before any build starts, I want to see how the solution will actually work for the people using it — not just what it'll look like. | **Information architecture and wireframing** — design report structure, navigation, drill paths, and user journeys before model development begins |

#### Phase 03 — Gaps & Bottlenecks

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Revenue looks different depending on which report you pull it from. Nobody agrees which one is right. | **Business logic fragmented across reports** — calculations exist in visuals, spreadsheets, and report layers instead of a governed semantic model |
| 2 | I can see today's number, but I have no idea if we're trending in the right direction or heading for a problem. | **Limited analytical context** — model lacks time intelligence, trend analysis, and scenario comparison |
| 3 | When that one person is on holiday, the data just stops. Nobody else knows how to update it. | **Manual data acquisition dependency** — refresh process depends on human intervention, creating latency and operational risk |
| 4 | We waste half the meeting arguing about which number is right instead of deciding what to do about it. | **Undefined metric ownership** — no accountable owner for business definitions, approval, and change management |
| 5 | I can see what happened, but the dashboard gives me no way to understand why — or what I should do next. | **Insufficient analytical depth** — reporting supports monitoring but lacks drill-through, decomposition, and root-cause analysis capabilities |

#### Phase 04 — Solution Steps

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | I want my team spending time on analysis and decisions — not chasing down the right numbers every morning. | **Automate data ingestion and refresh pipelines** — eliminate manual extracts, schedule refreshes, and implement monitoring |
| 2 | No matter where I look — dashboard, report, spreadsheet — I want to see the same number with the same definition behind it. | **Centralize business logic in the semantic model** — move calculations, KPIs, and business rules into a certified reusable layer |
| 3 | I need to know not just what the number is, but how it's moved — and whether that movement actually matters. | **Implement analytical time intelligence** — add period comparisons, trends, seasonality, rolling windows, and benchmarking measures |
| 4 | The dashboard shouldn't just tell me what happened. It should help me understand what to do about it. | **Redesign for decision support** — structure reporting around Monitoring → Diagnosis → Action rather than static KPI display |
| 5 | When someone challenges a number in a meeting, I need to be able to say exactly where it comes from and why it's right. | **Establish trust mechanisms** — certify datasets, document metrics, expose lineage, and implement ownership and governance processes |

**Key bottlenecks:** Manual refresh creates data staleness · Metric logic embedded within individual dashboards · No drill-through — can't go from summary to cause · Trust deficit from past errors never addressed

**Iterative target state:** Automated daily (or more frequent) refresh · All KPIs defined once in model, not in report · Three-layer report structure operational · Certified model with documented ownership

**Business questions this unlocks:** Why does Finance get a different number than Business? · Can I see this by region, product, and month? · What does Revenue mean in this context? · How do I know this is the right number?

> *"I don't just make your dashboard look better — I make it so your team can trust it, explore it, and act on it without asking IT for a new report every time."*

---

### Entry Point 2 — Disconnected Data (Silos)

**Complexity:** Full Stack · **Full stack opportunity**

> *"We have data in the ERP, the CRM, spreadsheets, and a shared drive. No one can ever get a consistent answer because everyone is pulling from a different place."*

#### Phase 01 — Assess Current State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | We have data in the ERP, the CRM, spreadsheets, SharePoint, and probably places I've forgotten about. Nobody has a complete picture. | **Source system inventory** — document system types (ERP, CRM, flat files, spreadsheets), connection protocols (ODBC, REST API, SFTP, manual export), and data ownership per source |
| 2 | Customer in the CRM doesn't mean the same thing as customer in the ERP. We've just learned to live with that — and it causes problems constantly. | **Conformed dimension candidate assessment** — identify cross-source entities (customer, product, geography) and evaluate natural key alignment, naming conventions, and grain consistency |
| 3 | Every cross-functional report requires someone to manually stitch together data from four different places. It takes days and it's never quite right. | **Ad-hoc integration pattern mapping** — document manual VLOOKUP or Power Query joins, shadow ETL processes, and intermediate flat files; estimate error rates and data loss risk |
| 4 | Finance and Operations can never agree on revenue. Every month we spend days in reconciliation meetings that go nowhere. | **Reconciliation hotspot prioritization** — identify the highest-friction reconciliation (the one consuming the most analyst time or producing the most disputes) and use it as the primary design anchor and ROI validation point |
| 5 | Some of our source systems are clean, others are a mess of gaps and outdated records. We don't have a clear picture of how bad it actually is. | **Source-level data quality profiling** — assess completeness (null rates, coverage), timeliness (extraction lag, update frequency), consistency (referential integrity), and validity across each source |

#### Phase 02 — Define Target State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | We need to agree on what "customer", "product", and "region" mean once — so every team is working from the same baseline. | **Conformed dimension scope definition (Kimball)** — define canonical grain, surrogate key strategy, and SCD type per dimension |
| 2 | Before we build anything, I want to agree on exactly which questions this needs to answer. That's how we'll know if it worked. | **Validated analytical question set design** — define analytical requirements as a validated question set and use it as integration-layer acceptance criteria; map each question to fact-dimension join paths |
| 3 | I need to know exactly how current the data is — not approximately. And I need that to be a commitment, not a best effort. | **Subject-area refresh SLA specification** — define maximum acceptable latency from source transaction to analytical availability and document as data contract terms |
| 4 | When the definition of "customer" changes — and it will — I need someone who has the final say and makes sure everyone else knows. | **Data ownership and decision-rights model** — assign a Data Owner per conformed dimension and business entity; document DRI accountability for definition changes in the Data Product Passport |
| 5 | Finance will use it in Excel, Operations wants a dashboard, and the dev team wants an API. We need all of those to work from the same data. | **Persona-specific consumption interface architecture** — define consumption interfaces per user persona: semantic model with DirectQuery or Import for Power BI, XMLA endpoint for Excel Analysis Services, or REST API for custom UI |

#### Phase 03 — Gaps & Bottlenecks

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Every system has its own definition of "customer". The moment you try to cross-reference anything, you end up in a reconciliation debate. | **No conformed dimensions** — each source maintains independent master data with no shared natural keys, no entity resolution, and no canonical grain |
| 2 | Every time someone needs a cross-functional report, a person has to manually join the data. There's no automated, repeatable way to do it. | **No ELT or ETL pipeline** — cross-source joins are performed via ad-hoc Power Query or VLOOKUP with no lineage, no error handling, and no reproducibility |
| 3 | Our CRM shows account-level totals but our ERP has transaction-level detail. You can't compare them without a spreadsheet and a lot of assumptions. | **Misaligned fact grain across sources** — ERP at transaction level, CRM at account level, and flat files at monthly aggregate level, leaving no reconciliation path without grain transformation |
| 4 | Every time we need data from a system, we have to log a request with IT. By the time it arrives, the moment for the decision has passed. | **No governed self-service access layer** — source system access is restricted to IT, with no semantic abstraction between raw data and business consumers |

#### Phase 04 — Solution Steps

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | I want data from every system flowing into one place automatically, without anyone having to do it manually. | **Build staging layer** — source-aligned extraction with no business logic applied, preserving raw schemas and supporting full and incremental loads under documented extraction contracts |
| 2 | There should be one definition of "customer", one definition of "product", and everyone should use it — no exceptions. | **Design conformed dimensions (Kimball)** — implement surrogate key generation, SCD Type 1 or 2 handling, canonical attribute sets, and natural key mapping across source systems |
| 3 | I need to be able to drill from a summary to a transaction without hitting a wall because the systems work at different levels of detail. | **Build fact tables at validated grain** — model subject-area facts (e.g. transaction, order-line, or daily-position) with additive measures, foreign key integrity to conformed dimensions, and degenerate dimensions where needed |
| 4 | Every team should pull from the same analytical layer — not their own copy of the data with their own formulas on top. | **Build certified semantic model** — implement SSAS Tabular or Power BI dataset with star schema foundation, certified KPI DAX layer, and marked date table with complete time intelligence coverage |
| 5 | Each team should be able to answer their own questions without depending on someone else to pull the data for them. | **Deploy governed self-service layer** — configure Row Level Security by domain and persona, enable Power BI dataset certification, and enforce workspace access controls aligned to data ownership |

**Key bottlenecks:** No shared entity definitions across systems · Manual join process = reconciliations factory · Different data granularity across source systems · No governed access path for business users

**Iterative target state:** Single version of every shared entity · Automated integration pipeline with documented lineage · Business users self-serve from one certified model · Reconciliation meetings eliminated for covered domains

**Business questions this unlocks:** Why does my revenue not match Finance? · Can we combine CRM pipeline with ERP actuals? · Who owns the customer dimension? · How do we stop data living in five places?

> *"I can take your scattered data landscape and build a single connected model every function pulls from — so reconciliation meetings become unnecessary."*

---

### Entry Point 3 — Spreadsheet Dependency

**Complexity:** Moderate · **Governance entry**

> *"We have one spreadsheet that takes three hours every month to update, nobody else understands it, and we're terrified it's wrong."*

#### Phase 01 — Assess Current State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | We have spreadsheets that feed the board pack every month. If one of them breaks, we can't close the books. | **Shadow IT audit** — identify business-critical spreadsheets by downstream decision impact, refresh frequency, and risk tier (single point of failure, key-person dependency, regulatory touch) |
| 2 | The numbers get into the spreadsheet somehow — exports, copy-paste, manual entry. I couldn't tell you exactly how many steps it takes. | **Data lineage trace per file** — document source systems, extraction method (manual export, ODBC connection, copy-paste), intermediate files, and transformation steps applied pre-load |
| 3 | The logic is all in the formulas. Nobody has ever written down what it actually does — it's just something you learn by sitting with the person who built it. | **Embedded business logic reverse-engineering** — document formula chains, allocation rules, conditional filters, and hardcoded assumptions; flag volatile functions, circular references, and undocumented constants |
| 4 | One person built it and one person maintains it. If they're not available, we have a problem. Nobody else understands it well enough to step in. | **Key-person dependency assessment** — identify sole maintainer, document tribal knowledge not captured in the file, and evaluate succession risk if that person is unavailable |
| 5 | I don't know how many downstream processes depend on this spreadsheet. If it were wrong, I'm not sure we'd catch it until the board pack went out. | **Downstream consumer and workflow mapping** — identify reports, dashboards, or processes dependent on file output and assess impact propagation if the file produces incorrect results |

#### Phase 02 — Define Target State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | I want to fix the ones that cause the most pain first — the monthly processes that take three hours and only one person knows how to run. | **Automation candidate prioritization by risk score** — weight by refresh frequency, downstream dependency count, manual effort per cycle, and error detection lag |
| 2 | Some of these need to run daily, some monthly. I need that to be a guaranteed delivery, not something that depends on someone remembering. | **Process-level data freshness SLA definition** — set maximum acceptable latency between source change and spreadsheet output and document as baseline pipeline design requirements |
| 3 | I want to keep Excel for the flexible analysis and scenarios it's actually good for — not as the home of every critical calculation. | **Business logic layer classification** — map certified metric definitions and aggregations to semantic model layer, while keeping ad-hoc analysis, scenario modeling, and user-controlled parameters in Excel consumption layer |
| 4 | Someone needs to own each file formally. Right now it's whoever built it — and if that person leaves, we lose everything. | **Governance framework definition** — define file versioning policy, named owner per file, documentation standard (inline comments, data dictionary), and change log requirements |
| 5 | Changes go into these files with no approval process. Someone edits a formula and nobody else knows until something downstream breaks. | **Change management process establishment** — define change initiator roles, peer review requirements, UAT sign-off, rollback procedure, and consumer notification on logic changes |

#### Phase 03 — Gaps & Bottlenecks

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Every month someone has to sit down and manually update this thing. If they're on holiday or sick, it just doesn't happen — and there's no record of what loaded or when. | **No automated data pipeline** — acquisition relies on manual export or copy-paste with no scheduled extraction, no error handling, and no audit trail of what loaded and when |
| 2 | Only the person who built it can explain how the numbers are calculated. Ask anyone else and they'll shrug. | **Business logic trapped in opaque formula chains** — no inline documentation, no separation of inputs from calculations, and no unit tests; logic is non-reproducible outside the file |
| 3 | If a number looks wrong, we have no way of knowing what changed or when. There's no history, no rollback — just "who touched this last?" | **No version control system** — no Git, no enforced SharePoint versioning, and no change log; modifications overwrite prior state with no rollback path and no audit trail |
| 4 | The file does everything — pulls the data, calculates the numbers, and formats the output. Touch anything and you risk breaking the whole thing. | **No separation of concerns** — one workbook handles extraction, transformation, business logic, and presentation, creating brittle coupling and poor testability |
| 5 | Bad data goes in and we don't find out until someone spots something wrong in the output — usually in a meeting. | **No data validation layer** — no input schema checks, no range or threshold controls, and no row-count reconciliation against source; bad data propagates silently to output |

#### Phase 04 — Solution Steps

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | I want the file to update itself. No manual steps, no person dependency — it should just work. | **Replace manual extraction with automated pipeline** — implement Power Query M with parameterized source connections, or Dataflow Gen2 or ADF for enterprise scale, and configure scheduled refresh with failure alerting |
| 2 | Before we change anything, I need to know exactly what the current logic is — so we can verify the new version gives the same answers. | **Reverse-engineer and unit-test logic before migration** — build a test dataset with known outputs, document formulas and allocations as functional specification, and use as regression baseline during transition |
| 3 | The core calculations shouldn't live in a spreadsheet. They should live somewhere central that everyone draws from. | **Migrate certified metric logic to semantic model layer** — use Power BI shared dataset, SSAS Tabular, or dbt to remove formula duplication and establish a single source of truth for shared KPIs |
| 4 | Excel is great for analysis and modelling scenarios. It shouldn't be the system of record for calculations that feed the board. | **Reconfigure Excel as thin consumption layer** — connect Excel to semantic model through XMLA endpoint or Analyze in Excel, keep business logic in model, and limit Excel to ad-hoc analysis and scenario inputs |
| 5 | Every critical file should have a named owner, an automatic update schedule, and a change history — maintained properly and not tied to one person. | **Operationalize spreadsheet assets** — implement version control (SharePoint versioning or Git for structured workbooks), enforce scheduled refresh SLA, assign named DRI, and document in Data Product Passport |

**Key bottlenecks:** Single person dependency on every critical file · No automated data connection — all manual copy-paste · Logic embedded in formulas nobody else understands · No change control — errors introduced silently

**Iterative target state:** Automated data feed replaces manual extraction · Core metric logic in versioned, certified model · Excel retained as analysis surface — not data processor · Named owner, documented logic, scheduled refresh

> *"I can take your critical spreadsheets and rebuild the underlying logic properly — so the business process keeps running without the fragility and the key-person risk."*

---

### Entry Point 4 — AI / Copilot Pressure

**Complexity:** Moderate · **Emerging urgency**

> *"Leadership wants us to use AI tools on our data but when we ask Copilot a question about revenue we get a different number every time."*

#### Phase 01 — Assess Current State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | We've been asking Copilot our standard questions and getting different answers every time. Sometimes it's completely wrong and there's no way to know which answer to trust. | **AI output benchmarking** — run a fixed set of natural language queries against the current data layer and document responses, inconsistency rates, and failure modes (hallucination, wrong measure resolution, incorrect filter context) |
| 2 | I can't tell if it's using the wrong data source, misunderstanding the question, or just making things up. There's nothing to reason against. | **Root-cause AI inconsistency analysis** — distinguish between ambiguous measure names (NL resolution failure), missing measure descriptions (intent inference failure), multiple datasets queried (source ambiguity), and absent time intelligence (period resolution failure) |
| 3 | Our data model was built by developers. The column names are abbreviations and codes that make sense to IT, not to a business user — or an AI. | **Semantic model AI-readiness audit** — assess measure description coverage, semantic naming quality for tables and columns, synonym definitions, and Q&A linguistic schema completeness |
| 4 | If AI is pulling from uncertified sources with gaps and inconsistencies, we'll never get reliable answers — no matter how good the AI is. | **Queried data layer profiling** — evaluate null rates on key dimensions, referential integrity, grain consistency, and certified versus uncertified datasets within AI-accessible scope |
| 5 | Leadership wants AI working on everything. I need to push back and pick two or three questions we can actually prove work before we expand scope. | **AI use case taxonomy definition** — classify target queries by type (aggregation, trend, ranking, diagnostic, predictive) and assess feasibility against current model capabilities |

#### Phase 02 — Define Target State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | I want a short list of questions that AI should be able to answer correctly, every time. That's how we'll know if this is actually working. | **AI acceptance criteria as fixed question set** — pair each benchmark question with an expected answer validated against the certified semantic model and use this as a regression test suite |
| 2 | Being "AI-ready" isn't just having Copilot connected. It means getting the same correct answer every time I ask the same question. | **AI-readiness checklist definition** — require complete measure descriptions, semantic naming standards, certified dataset as sole AI source, populated Q&A linguistic schema, and operational time intelligence layer |
| 3 | I want to prove this works on one question before we roll it out to the whole business and set expectations we can't deliver on. | **Pilot use case selection by feasibility-impact matrix** — prioritize a single subject area, up to five certified measures, clear success metric, and existing model coverage; avoid multi-domain complexity in pilot |
| 4 | For some questions I need an exact match. For trend questions I need to know what an acceptable margin of error looks like. | **Accuracy threshold definition per query type** — require exact match for aggregation queries and tolerance bands for trend queries with documented acceptable variance |
| 5 | Someone needs to be checking AI answers before they reach decision-makers. I'm not comfortable just letting it run unsupervised. | **AI output governance framework** — define validation DRI per subject area, spot-check sampling frequency, escalation path for anomalies, and integration with model certification cycle |

#### Phase 03 — Gaps & Bottlenecks

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | We ask it about Revenue and it returns a number, but we have no idea which revenue it's using or what rules it applied. | **Near-zero measure description coverage** — NL engines rely on descriptions and synonyms for intent resolution; without them they fall back to ambiguous name matching |
| 2 | The model is full of codes and abbreviations that only developers understand. AI reads those the same way a new analyst would — wrongly. | **Technical naming conventions in model metadata** — snake_case, system prefixes, and abbreviated codes reduce NL resolution quality and increase hallucination risk |
| 3 | There are multiple datasets it can query. Sometimes it picks one, sometimes another. That's why the same question gives different answers. | **Multiple conflicting datasets exposed to AI** — no single certified authoritative model, causing non-deterministic source selection |
| 4 | Ask it anything about last quarter or year-on-year and it either fails or returns something that's clearly wrong. | **No marked date table or time intelligence measures** — AI cannot resolve natural period language without CALCULATE-based measures and a configured date table |
| 5 | An answer that sounds confident gets used in a meeting. Nobody checks it against anything first. That's how errors reach the board. | **No output validation layer** — responses are not reconciled against certified values; no sampling framework, anomaly detection, or assigned DRI |

#### Phase 04 — Solution Steps

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | The model needs to speak the same language we do — not developer shorthand that means nothing to a business user. | **Apply semantic naming conventions across model** — rename tables, columns, and measures to business-readable terms; populate Q&A linguistic schema with synonyms and common query phrasing |
| 2 | Every key metric needs a definition that's clear enough that when AI reads it, it knows exactly which number to return. | **Author measure descriptions for certified metrics** — document business definition, grain, inclusions or exclusions, and date logic in plain English to support intent resolution |
| 3 | "Show me last quarter versus the same period last year" is a basic question. I need AI to answer it reliably, not just give me a snapshot. | **Implement time intelligence layer** — mark date table, build YoY, QoQ, MTD, YTD, and rolling-window measures, validate against fiscal calendar, and register period synonyms in Q&A schema |
| 4 | AI should only be able to query the data my team already trusts and relies on. Not everything in the warehouse — just the certified layer. | **Restrict AI data scope to certified semantic model** — remove raw dataset or warehouse access and configure Copilot or Fabric AI to query endorsed dataset only as a contract boundary |
| 5 | I need a regular process where someone checks AI outputs against the numbers we know are right — before those outputs end up in a board report. | **Implement output validation protocol** — assign DRI per subject area, define weekly sampling cadence, configure variance anomaly alerts, and fold checks into model certification review |

**Key bottlenecks:** AI queries ambiguous or unlabelled model objects · No single certified model — AI picks inconsistent sources · Time intelligence absent — no period comparisons · No human validation step for AI outputs

**Iterative target state:** All measures described in plain business language · AI connected exclusively to certified semantic model · Time intelligence fully operational · Pilot producing consistent, validated outputs

> *"Your AI tools are only as good as the data model underneath them. I build the foundation that makes your AI investment actually work — instead of confidently giving you the wrong answer."*

---

### Entry Point 5 — No Analytics Capability (Greenfield)

**Complexity:** Full Stack · **Greenfield opportunity**

> *"We spend two days before every board meeting manually pulling numbers from three systems. There's no consistency and leadership always challenges the figures."*

#### Phase 01 — Assess Current State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Every week the same questions come up that nobody can answer quickly. We're slowing down decisions because we can't get to the numbers fast enough. | **Conduct requirements elicitation using structured discovery interviews** — capture recurring analytical questions, report consumers, decision frequency, and current workaround patterns |
| 2 | We have an ERP, a CRM, and a dozen spreadsheets. I have no idea which ones could actually feed an analytics layer and which ones are export-only. | **Source system discovery** — catalogue available systems (ERP, CRM, HRIS, flat files), assess connection feasibility (API availability, ODBC/JDBC, export-only, manual), and identify data ownership |
| 3 | Our reports are produced by someone manually pulling from three systems and combining them in Excel. It takes two days and it's different every time. | **Process archaeology** — document the current-state reporting workflow end-to-end: source extraction steps, manual transformation logic, file handoffs, consolidation points, and rework loops |
| 4 | The board pack preparation is the worst. Two days of manual work, constant last-minute corrections, and leadership still challenges the figures every time. | **Prioritise analytical gaps by business impact score** — weight by decision frequency, stakeholder seniority, manual effort displaced, and revenue or risk exposure; use as anchor for MVP scope |
| 5 | Some of my team will dig into data and build their own views. Others just want a clean report they can open and read. I need both to work. | **Assess user analytical maturity by persona** — distinguish power users (comfortable with calculated fields, custom visuals), standard consumers (filter and slice only), and executive viewers |

#### Phase 02 — Define Target State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Before we build anything, I want to agree on the questions this needs to answer. That's how I'll know each stage has delivered what I paid for. | **Convert question inventory to a model design brief** — map each question to required dimensions, measures, and grain; use as acceptance criteria for each delivery phase |
| 2 | I don't want to wait 12 months to see results. Give me something genuinely useful in weeks, even if it's small. | **Define MVP scope** — minimum subject area coverage, minimum KPI set, and minimum sources required to answer the top 3–5 priority questions; design for iterative extension |
| 3 | I've been through the single big launch that keeps slipping. I want a sequence of stages where each one adds something real. | **Define phased delivery roadmap** — sequence releases by dependency order, validate each phase against acceptance criteria before proceeding |
| 4 | I want to agree upfront on how we measure success — not just go-live, but actual adoption and time saved. | **Define success KPIs per delivery phase** — active users, query volume, manual reporting hours displaced; instrument usage telemetry from day one |
| 5 | I need to know what's in scope and what isn't — so I'm not expecting something in six months that was never part of the plan. | **Define target state architecture** — semantic model scope, self-service tier design by user persona, governance model, and explicit out-of-scope boundaries to prevent scope creep |

#### Phase 03 — Gaps & Bottlenecks

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Every time we need numbers for a meeting, someone manually pulls from three systems and stitches it together. The results are never quite consistent. | **No ELT pipeline or governed extraction layer** — source systems accessible only through manual export; no staging environment, no extraction contracts, no schema documentation |
| 2 | We've been stuck in a tooling debate for months. Every time we try to start, someone says we need to decide on the platform first. | **No agreed analytics platform or toolchain** — absence of decisions on warehouse, semantic layer, and consumption tool is creating delivery paralysis; platform selection should be timeboxed and driven by use-case requirements |
| 3 | Every board meeting, leadership challenges the figures. Revenue means something different to Finance than it does to Sales and nobody has ever resolved it. | **No Metric Dictionary or Business Glossary** — KPI definitions undocumented; conflicting definitions risk being encoded into the model from day one |
| 4 | I don't want to need a consultant every time I need to update a metric definition. Someone on my team needs to own this and be able to maintain it. | **No internal analytics capability** — no owned semantic model, no trained power users, no knowledge transfer plan; every change requires external resourcing |
| 5 | I've seen this happen before — a project delivers something, nobody owns it, and in 12 months we're back where we started. | **No governance framework** — no named data owner, no refresh SLA, no certification or change process; without these, user trust will not develop regardless of technical quality |

#### Phase 04 — Solution Steps

| Phase | Business Translation | Analytics Translation |
|---|---|---|
| Phase 1 | Within six weeks, I want to stop spending two days before every board meeting pulling numbers manually. The core figures should be ready before I ask for them. | Build extraction layer for top 3 source systems, minimal staging schema, core fact and dimension tables at agreed grain, certified semantic model with 3–5 KPIs, and first report validated against acceptance criteria |
| Phase 2 | When leadership asks a follow-up in the meeting, I want to be able to answer it in the room — not say "I'll get back to you". | Implement time intelligence layer, extend dimension model with additional attributes, hierarchies, and SCD handling, and validate against extended acceptance criteria |
| Phase 3 | I want my team to be able to answer their own questions without coming to me or IT every time they need a different cut of the data. | Extend semantic model to additional subject areas, configure self-service layer with RLS by user persona, apply certified endorsement, and complete Metric Dictionary for all published measures |
| Phase 4 | By the end, I want my team to own this completely — able to update it, extend it, and maintain it without bringing in outside help. | Deliver structured enablement by user tier, publish Data Product Passport and Handover Guide, assign DRI per subject area, and operationalise change management process |

**Key bottlenecks:** No governed access to source data · No agreed metric definitions to build from · Risk of "big bang" approach — nothing for 12 months · No internal capability to maintain what's built

**Iterative target state:** Phase 1 live within 4–6 weeks: 3 sources, core KPIs · Metrics defined and certified before reporting goes live · Self-service layer operational by Phase 3 · Internal champion identified and enabled

> *"I can take you from manual spreadsheet chaos to a working analytics layer in a focused engagement — starting with the questions that matter most, not a two-year platform project."*

---

### Entry Point 6 — The Translation Failure

**Complexity:** Diagnostic · **Business-IT disconnect**

> *"Our last dashboard looked great in the demo. Three months after go-live, everyone was back in Excel. The business never trusted the numbers enough to stop checking them manually. We don't have the appetite to go through that again."*

#### Phase 01 — Assess Current State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | I can tell you what our reporting process is supposed to look like. What I struggle to describe is what it actually looks like week to week — because the gap between those two things is where the real problem lives. | **Current-state process mapping via elicitation** — establish end-to-end data acquisition workflow, identify manual touchpoints, and surface undocumented transformation steps the stakeholder has normalised |
| 2 | The last project didn't ask us the right questions. There are things I wish we could answer that nobody ever thought to include in the brief. | **Analytical capability gap identification** — surface unmet decision-support requirements not captured in formal requirements documentation; often reveals actual scope vs presented scope |
| 3 | Numbers get challenged in every meeting. At some point trust broke down and we never properly addressed it — we just kept presenting and apologising. | **Trust deficit assessment** — identify the most recent analytical failure event; root-cause as data quality, metric definition, or stakeholder credibility gap; use as a proxy for the depth of the trust problem |
| 4 | We have reports. I'm not sure they're actually changing any decisions. People open them, look at them, and then act on instinct anyway. | **Decision-action linkage audit** — assess whether analytical outputs are connected to specific decisions or consumed as information only; distinguish descriptive from prescriptive reporting maturity |

#### Phase 02 — Define Target (Together)

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Last time we spent months specifying what the dashboard should look like. This time I want to start with what decisions I'm actually trying to make — that single shift changes everything that follows. | **Requirements decomposition** — shift elicitation from output specification (report format, requested KPIs) to decision decomposition (decision type, frequency, owner, data inputs required, acceptable latency) |
| 2 | If a number gets challenged, I need to be able to say who owns that definition and why it's calculated the way it is. | **Metric ownership assignment** — establish DRI accountability for business rule definition per KPI; document in Metric Dictionary; position the analytical layer as translation medium, not definition authority |
| 3 | Give me three questions. If our engagement can answer those reliably, it will have been worth it. | **Acceptance criteria definition** — establish a minimum viable question set as functional requirements; each question maps to a specific decision, data source, and metric definition; use as scope anchor and delivery gate |

#### Phase 03 — Surface Real Gaps

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | I just assumed everyone meant the same thing by Revenue. Once you ask the second question — gross or net? before rebates? — you realise nobody ever actually agreed. | **Metric definition decomposition** — test whether the KPI is sufficiently specified for unambiguous implementation: grain, inclusions, exclusions, date logic, and edge-case treatment |
| 2 | If I pull revenue from the ERP and from the spreadsheet we use for management reporting, they won't match. They never do. That's the problem we need to solve before any dashboard gets built. | **Source-of-truth reconciliation test** — assess whether primary data sources would produce the same output for the same question; identify the existence and depth of data trust gaps without running a formal reconciliation |
| 3 | If this number turned out to be wrong, I honestly don't know who to call. There's no one who formally owns it. | **Data ownership and escalation path assessment** — identify whether a DRI exists per metric, whether a documented resolution process exists for data quality issues, and whether the stakeholder has an accountable counterpart |

#### Phase 04 — Reposition & Propose

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | I don't want to start a full project without understanding what the actual problem is. A diagnostic first — so we both agree on what we're solving before any money is committed. | **Diagnostic classification** — map discovery findings to the appropriate entry point framework; document presenting problem, root cause hypothesis, and recommended starting sequence |
| 2 | I've had expensive projects fail before. I want to see proof of direction before I commit to anything large. | **Scoped engagement proposal** — define a time-boxed diagnostic phase (discovery + POC) before committing to full build, with scope defined by the question set rather than a feature list |
| 3 | I want something written down that describes the problem in my language — not technical jargon — that we've both agreed on before anything gets built. | **Discovery artefact** — produce a jointly authored problem statement capturing current state in business language, root cause hypothesis, the three agreed questions, and proposed success criteria |
| 4 | I need to know exactly what's my job in this engagement and what's yours. I own the business definitions — what does that mean in practice? | **Engagement model definition** — formalise the division of responsibility: business owns metric definitions, business rules, and acceptance criteria; consultant owns translation into model and delivery structure |

**Key bottlenecks:**
- The people who defined the requirements weren't the people who felt the problem — so the brief was wrong before the build started
- Everyone described their piece of the process, nobody described the whole — leaving the biggest inefficiencies invisible and unaddressed
- The build fixed what was asked for, not what was actually broken — and what was actually broken was often one step upstream or downstream
- Developers optimised the current state rather than questioning whether the current state was worth keeping

**Iterative target state:**
- Requirements gathered across the full stakeholder map — not just the loudest voice in the room — so the brief reflects the actual problem, not the presented one
- End-to-end process walkthrough before any build begins — because the highest-value improvement is rarely where our conversation started
- Every request assessed against the full workflow: what feeds it, what follows it, and what breaks if it changes
- Current state treated as a reference point, not a starting point — the question is always what the business needs, not what the system already does

> *"I'm not the domain expert — you are. My job is to ask the questions that turn your business knowledge into a data model that actually reflects how your business works. That's a different skill from knowing your industry."*

---

## Delivery Methodology

> "Four stages, six artefacts, every engagement. The same cadence applies regardless of entry point. The content of each stage differs by complexity. Documentation is built into the rhythm — not deferred to the end. Nothing becomes a black box."

### Delivery Cadence

| Stage | Timing | Description | Output |
|---|---|---|---|
| **01 · Discover** | 1–5 days | Structured conversations using entry-point diagnostic questions. No tools yet — understand the problem, not the solution. | Current state in business language. Top 3 gaps. Target state as answerable questions. Proposed scope. |
| **02 · POC** | 1–2 weeks | Real but sampled data. Core model skeleton and 1–2 most important KPIs. Clickable prototype for business validation. | Working prototype. First draft Metric Dictionary and Data Map. Business confirms model reflects their logic. |
| **03 · Build** | 1–8 weeks | Full data, complete model, key reports. Delivered in sub-releases — not a single handover. Model Specification produced. | Production model. Complete reporting layer. Model Specification. First Handover Guide. Data Product Passport. |
| **04 · Embed** | Ongoing | Iterative enhancements. Additional reports and analytical capabilities. Documentation evolves with model. | Enhanced model iterations. Updated artefacts. Trained users. Versioned metric changes communicated to consumers. |

### The Fixed Artefact Set

| # | Artefact | When Produced | Description |
|---|---|---|---|
| **01** | **Discovery Summary** | End of Discover stage | One page. Current state in business language — not technical architecture. Top three gaps. Target state as a set of business questions the solution will be able to answer. The scoping contract. |
| **02** | **Metric Dictionary** | Built at POC · Maintained forever | Plain English name, business definition (words not DAX), origin type (upstream/domain/hybrid), owner, exclusions, date logic, version. Business users certify this. Eliminates the Finance vs Operations problem. |
| **03** | **Data Map** | Produced at POC · Updated at Build | Business-readable flow from source system through transformation to report surface. Not a technical ERD. Answers "where does this number come from?" without a developer. Anti-black-box document. |
| **04** | **Model Specification** | Produced at start of Build | Translates Metric Dictionary and Data Map into what needs to be built: fact tables, dimensions, key measures, time intelligence requirements, refresh schedule, RLS needs. Technical handoff that a business-literate reader can follow. |
| **05** | **Handover Guide** | Produced at end of every iteration | One page per report or model component. Answers: "How do I navigate this?", "How do I know the data is current?", "What do I do if something looks wrong?" Replaces implicit knowledge. Updated every iteration. |
| **06** | **Data Product Passport** | Produced at Build · gate before Embed | Product name/version, owning domain, covered subject areas, consumption interfaces, refresh SLA, data quality indicators, metric ownership summary, known limitations. Front page of the product in the data catalogue. |

---

## Common Layer

> "Six components appear in every engagement regardless of entry point. The shape, governance formality, and technical depth differ by complexity. The requirement to address them does not disappear."

| Component | Description |
|---|---|
| 🧊 **Semantic / Data Model** | Every solution requires at least a minimal data model — from a single Power BI dataset to a full SSAS Tabular enterprise model. The grain, shape, and governance formality differ; the need does not. |
| 📐 **Metric Definition** | Every engagement surfaces at least one metric defined differently in different places. Agreeing and encoding the canonical definition is always a deliverable, regardless of entry point. |
| 📅 **Date / Time Intelligence** | A shared, governed date table with consistent period logic (YoY, MTD, rolling) is required in every delivery that produces business reporting. It is almost always missing or inconsistent in the current state. |
| 🔄 **Refresh & Pipeline** | Every current state has a data freshness problem — manual, broken, or non-existent automation. The complexity of the fix ranges from a scheduled Power Query refresh to a full ELT pipeline. |
| 🛡️ **Trust & Governance** | Users do not trust what they cannot verify. Every delivery must address certification, data lineage visibility, and documented ownership — or adoption will not follow, regardless of technical quality. |
| 🎓 **User Enablement** | Handing over a model or dashboard without structured enablement produces low adoption. Every delivery includes at minimum a navigation guide and a short structured handover session. |

### Common Layer Complexity by Entry Point

| Component | Dashboard | Disconnected | Spreadsheet | AI Ready | Greenfield | Translation |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Data model complexity | Low | High | Medium | Medium | High | Diagnostic only |
| Pipeline / ETL work | Low | High | Medium | Low | High | Diagnostic only |
| Metric definition work | Medium | High | Medium | High | High | High |
| Time intelligence | Medium | Medium | Low | Medium | Medium | Diagnostic only |
| Governance formality | Medium | High | Medium | Medium | High | Diagnostic only |
| User enablement | Low | Medium | Low | Medium | High | Medium |

*Low = Targeted · Medium = Moderate · High = Full depth · Diagnostic only = No build, assessment only*

---

## Metric Ownership Model

> "The reconciliation path runs in opposite directions depending on metric origin type. Conflating these in documentation is one of the most common causes of the Finance vs Operations problem at the metric level."

### The Three Origin Types

#### ⬇️ Upstream-Certified
**Calculated and owned externally**

Delivered via a feed or report from a system or function outside this domain. The domain is a *consumer*, not an owner. Examples: LCR ratio from regulatory system, RWA from credit risk engine, intercompany funding rates from central TMS.

> **Reconciliation direction:** YOUR model → upstream system. If they differ, the upstream is right until proven otherwise.

#### 🔧 Domain-Derived
**Defined and calculated within this domain**

Built from source field values the domain controls or has direct access to. The domain *is* the owner. Examples: Net FTP from internal spread calculation, liquidity buffer utilisation from position data, concentration of funding by counterparty.

> **Reconciliation direction:** downstream consumers → YOUR model. This model is the golden source. Defend it with the Metric Dictionary.

#### ⚗️ Upstream + Domain-Adjusted (Hybrid)
**The most dangerous — looks certified but isn't**

Starts as an upstream figure but has a local adjustment applied (management overlay, different perimeter, entity exclusion). Consumers assume it matches the upstream — it doesn't, by design. Must be flagged explicitly.

> **Document both:** upstream source AND adjustment logic. State explicitly: "Will not match upstream. Expected variance: [description]."

### Metric Dictionary — Structure & Sample

| Metric Name | Origin | Business Definition | Owner / Golden Source | Date Logic | Exclusions | Version |
|---|---|---|---|---|---|---|
| LCR Ratio | UPSTREAM | Liquidity Coverage Ratio as reported by the regulatory system. HQLA ÷ Net Cash Outflows over 30-day stress period. | Regulatory Reporting System · Risk function | Reporting date (T) | None — use as received | v1.0 |
| Net FTP Spread | DOMAIN | Difference between the internal transfer price rate assigned to a product and the actual cost of funds for that tenor, expressed in basis points. | Treasury Analytics model · Treasury team | Trade origination date | Excludes intercompany trades flagged IC=Y | v2.1 |
| Liquidity Buffer (Mgmt) | HYBRID | Regulatory HQLA pool with management adjustments: excludes pledged assets not available for same-day monetisation and adds uncommitted but operationally available reserves. | Base: Regulatory System · Adjustment: Treasury team | End of business day | Pledged assets, restricted reserves | v1.3 |
| Funding Concentration | DOMAIN | Top-10 counterparty funding as % of total wholesale funding. Identifies single-name concentration risk in the funding base. | Treasury Analytics model · Treasury team | As-at date (snap) | Retail deposits excluded; intragroup excluded | v1.0 |

### Why This Distinction Is the Anti-Black-Box Mechanism

Most BI deliveries treat all numbers as equally opaque — users don't know where they come from, who owns them, or what to do when they're challenged. Making ownership and reconciliation paths visible — and differentiating them by origin type — is the structural mechanism that converts a model from a black box into a governed data product.

When a number is challenged in a board meeting, the owner, the golden source, and the reconciliation path are all documented. The conversation moves from *"which number is right?"* to *"which definition are we applying, and why?"*

---

## Data Mesh Alignment

> "Data mesh is an ownership and governance principle, not a technology pattern. The delivery methodology and technical architecture remain intact. What changes is how ownership, interfaces, and governance are framed around them. Additive framing, not architectural replacement."

### Core Data Mesh Principles — How They Map

**Principle 1 · Domain Ownership of Data**
The domain that best understands the data owns it end-to-end — pipeline, quality, SLAs, and versioning. In the delivery methodology this shifts the Discover question: "Who currently owns the data between source and consumption — and is that the right team?" The answer shapes whether you're enabling a central IT function or a domain-owned product.

**Principle 2 · Data as a Product**
Data has a defined interface, named consumers, quality SLAs, and a published specification — just like software. The semantic model is not a BI layer; it is the queryable interface of the data product. The Data Product Passport (Artefact 06) is the published specification. Versioning discipline in the Metric Dictionary makes it behave like a software API.

**Principle 3 · Self-Serve Data Platform**
Consumers connect to the product's interface without needing to understand the warehouse underneath. The certified semantic model — with named measures, described dimensions, and documented RLS — is that interface. AI tools connect here too, which is why the AI entry point is directly improved by data mesh discipline.

**Principle 4 · Federated Computational Governance**
Global standards, local ownership. The Metric Ownership Model (upstream/domain/hybrid classification) is the governance instrument that makes this operational. Conformed metrics (like a shared date table or agreed entity definitions) are the global standards. Domain-derived metric definitions are local ownership in action.

### What Changes in the Methodology — Additive Only

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
