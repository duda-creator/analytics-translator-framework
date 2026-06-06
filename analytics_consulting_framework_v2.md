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
| 1 | Map every place your team pulls numbers from — which systems, files, and shared drives | **Source-to-report lineage mapping** — document every data source, connection path, refresh dependency, and transformation between source systems and the dashboard |
| 2 | Find out how the numbers get updated — automatically, manually, or routinely fail without warning | **Refresh architecture assessment** — classify refresh mechanisms (scheduled, event-driven, manual), identify failure points, ownership, SLAs, and recovery procedures |
| 3 | List every key metric the business uses — where it's defined and who owns it | **Metric catalogue and business logic inventory** — document all measures, calculations, KPIs, filters, and business rules; identify ownership and duplication; establish a draft business glossary |
| 4 | Understand how teams use the dashboard, what questions they expect it to answer, and which decisions depend on it | **Usage and decision mapping** — identify user groups, report consumption patterns, and decision processes supported by the dashboard |
| 5 | Identify where users double-check results, export to Excel, or rely on alternative reports because they do not trust the dashboard | **Trust and adoption assessment** — evaluate data quality issues, reconciliation gaps, metric disputes, workarounds, and shadow reporting outside the dashboard |

#### Phase 02 — Define Target State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | What questions should the solution answer: separate what's happening, why it's happening, and what action is needed | **Analytics operating model design** — define required analytical layers (monitoring, diagnosis, prediction, action) and map them to user personas and decisions |
| 2 | How fresh does the data need to be? Monthly, weekly, daily, hourly, or near-real-time | **Refresh and latency requirements** — define target refresh frequency, data availability windows, and reporting SLAs by use case |
| 3 | Establish a small set of KPIs everyone can trust and use consistently | **Certified KPI framework** — identify critical business metrics, define calculation logic, ownership, and certification criteria |
| 4 | Agree what evidence users need before they're willing to make decisions from the data | **Trust and governance standards** — define lineage visibility, data quality controls, certification badges, ownership, and auditability requirements |
| 5 | Sketch how users will find answers before building anything technical | **Information architecture and wireframing** — design report structure, navigation, drill paths, and user journeys before model development begins |

#### Phase 03 — Gaps & Bottlenecks

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | The same KPI gives different answers depending on where you look | **Business logic fragmented across reports** — calculations exist in visuals, spreadsheets, and report layers instead of a governed semantic model |
| 2 | You can see today's number, but not whether things are improving or getting worse | **Limited analytical context** — model lacks time intelligence, trend analysis, and scenario comparison |
| 3 | The report is only as current as the person who remembers to update it | **Manual data acquisition dependency** — refresh process depends on human intervention, creating latency and operational risk |
| 4 | Teams spend more time debating numbers than acting on them | **Undefined metric ownership** — no accountable owner for business definitions, approval, and change management |
| 5 | The dashboard tells you what happened, but not why | **Insufficient analytical depth** — reporting supports monitoring but lacks drill-through, decomposition, and root-cause analysis capabilities |

#### Phase 04 — Solution Steps

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Stop spending time gathering data and start spending time using it | **Automate data ingestion and refresh pipelines** — eliminate manual extracts, schedule refreshes, and implement monitoring |
| 2 | Ensure every report, dashboard, and spreadsheet uses the same definitions | **Centralize business logic in the semantic model** — move calculations, KPIs, and business rules into a certified reusable layer |
| 3 | Make it easy to see what changed, by how much, and whether it matters | **Implement analytical time intelligence** — add period comparisons, trends, seasonality, rolling windows, and benchmarking measures |
| 4 | Move beyond "what happened" to "so what?" and "what should we do next?" | **Redesign for decision support** — structure reporting around Monitoring → Diagnosis → Action rather than static KPI display |
| 5 | Give users confidence that the numbers are accurate, explainable, and supported | **Establish trust mechanisms** — certify datasets, document metrics, expose lineage, and implement ownership and governance processes |

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
| 1 | List every place data lives — finance systems, customer systems, spreadsheets, and shared drives | **Source system inventory** — document system types (ERP, CRM, flat files, spreadsheets), connection protocols (ODBC, REST API, SFTP, manual export), and data ownership per source |
| 2 | Find the concepts that appear in multiple systems, like "customer" or "product", and check whether they mean the same thing everywhere | **Conformed dimension candidate assessment** — identify cross-source entities (customer, product, geography) and evaluate natural key alignment, naming conventions, and grain consistency |
| 3 | Find out how each team currently combines data from different sources and how much manual effort or rework it creates | **Ad-hoc integration pattern mapping** — document manual VLOOKUP or Power Query joins, shadow ETL processes, and intermediate flat files; estimate error rates and data loss risk |
| 4 | Find the reconciliation that causes the most arguments or wasted time — that is where we start | **Reconciliation hotspot prioritization** — identify the highest-friction reconciliation (the one consuming the most analyst time or producing the most disputes) and use it as the primary design anchor and ROI validation point |
| 5 | Check how complete and current each source actually is — missing values, outdated records, and broken links between systems | **Source-level data quality profiling** — assess completeness (null rates, coverage), timeliness (extraction lag, update frequency), consistency (referential integrity), and validity across each source |

#### Phase 02 — Define Target State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Agree on the minimum set of shared definitions the business needs — which concepts (customer, product, geography, time) must mean the same thing everywhere | **Conformed dimension scope definition (Kimball)** — define canonical grain, surrogate key strategy, and SCD type per dimension |
| 2 | Agree upfront on the specific questions this integration must answer — those questions become the test of whether the solution is good enough | **Validated analytical question set design** — define analytical requirements as a validated question set and use it as integration-layer acceptance criteria; map each question to fact-dimension join paths |
| 3 | Decide how quickly data from each source needs to be reflected in reports — and make that an explicit commitment, not a vague expectation | **Subject-area refresh SLA specification** — define maximum acceptable latency from source transaction to analytical availability and document as data contract terms |
| 4 | Agree on who has the final say on what "customer" or "product" means — so when definitions change, everyone knows who decides | **Data ownership and decision-rights model** — assign a Data Owner per conformed dimension and business entity; document DRI accountability for definition changes in the Data Product Passport |
| 5 | Agree on how different teams will actually use the data — dashboards, spreadsheets, or custom tools — and design for those workflows from the start | **Persona-specific consumption interface architecture** — define consumption interfaces per user persona: semantic model with DirectQuery or Import for Power BI, XMLA endpoint for Excel Analysis Services, or REST API for custom UI |

#### Phase 03 — Gaps & Bottlenecks

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Each system has its own version of "customer" or "product" — they do not match, so cross-functional reporting turns into reconciliation debates | **No conformed dimensions** — each source maintains independent master data with no shared natural keys, no entity resolution, and no canonical grain |
| 2 | Combining data from different systems requires someone to manually stitch it together every time the analysis is needed | **No ELT or ETL pipeline** — cross-source joins are performed via ad-hoc Power Query or VLOOKUP with no lineage, no error handling, and no reproducibility |
| 3 | Different systems record data at different levels of detail — one shows individual transactions while another only shows rolled-up totals | **Misaligned fact grain across sources** — ERP at transaction level, CRM at account level, and flat files at monthly aggregate level, leaving no reconciliation path without grain transformation |
| 4 | Getting data out of source systems requires raising a request with IT — the business has no trusted self-service path | **No governed self-service access layer** — source system access is restricted to IT, with no semantic abstraction between raw data and business consumers |

#### Phase 04 — Solution Steps

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Create a reliable, automated connection to each source so data flows into one place consistently | **Build staging layer** — source-aligned extraction with no business logic applied, preserving raw schemas and supporting full and incremental loads under documented extraction contracts |
| 2 | Establish one agreed definition for shared business concepts like customer, product, and date | **Design conformed dimensions (Kimball)** — implement surrogate key generation, SCD Type 1 or 2 handling, canonical attribute sets, and natural key mapping across source systems |
| 3 | Structure the data at the right level of detail for each business question so teams can analyze consistently | **Build fact tables at validated grain** — model subject-area facts (e.g. transaction, order-line, or daily-position) with additive measures, foreign key integrity to conformed dimensions, and degenerate dimensions where needed |
| 4 | Build the shared analytical layer on top with consistent KPI definitions, period comparisons, and a trusted model for reporting | **Build certified semantic model** — implement SSAS Tabular or Power BI dataset with star schema foundation, certified KPI DAX layer, and marked date table with complete time intelligence coverage |
| 5 | Open up self-service access so each team sees the data relevant to them and can analyze without relying on ad-hoc extracts | **Deploy governed self-service layer** — configure Row Level Security by domain and persona, enable Power BI dataset certification, and enforce workspace access controls aligned to data ownership |

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
| 1 | Find the spreadsheets the business could not function without — the ones that feed board packs, financial close, or operational decisions | **Shadow IT audit** — identify business-critical spreadsheets by downstream decision impact, refresh frequency, and risk tier (single point of failure, key-person dependency, regulatory touch) |
| 2 | Follow the data backwards — find out where each spreadsheet gets its numbers from, how they arrive, and how many manual steps are involved | **Data lineage trace per file** — document source systems, extraction method (manual export, ODBC connection, copy-paste), intermediate files, and transformation steps applied pre-load |
| 3 | Write down exactly how the numbers are calculated — every formula, every allocation rule, every assumption baked in — so the logic exists somewhere outside the file itself | **Embedded business logic reverse-engineering** — document formula chains, allocation rules, conditional filters, and hardcoded assumptions; flag volatile functions, circular references, and undocumented constants |
| 4 | Find out who looks after it — and whether anyone else could step in if that person was unavailable | **Key-person dependency assessment** — identify sole maintainer, document tribal knowledge not captured in the file, and evaluate succession risk if that person is unavailable |
| 5 | Understand what this spreadsheet feeds into — which reports, decisions, or processes would break if it was wrong or unavailable | **Downstream consumer and workflow mapping** — identify reports, dashboards, or processes dependent on file output and assess impact propagation if the file produces incorrect results |

#### Phase 02 — Define Target State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Agree on which processes to fix first — prioritize by how often they run, how many people depend on them, and how long they take to maintain | **Automation candidate prioritization by risk score** — weight by refresh frequency, downstream dependency count, manual effort per cycle, and error detection lag |
| 2 | Decide how frequently each process needs to run — and make that a requirement, not a best effort | **Process-level data freshness SLA definition** — set maximum acceptable latency between source change and spreadsheet output and document as baseline pipeline design requirements |
| 3 | Separate stable, repeatable calculations that should be centralized from flexible analysis Excel is good at — so each layer does the job it is suited for | **Business logic layer classification** — map certified metric definitions and aggregations to semantic model layer, while keeping ad-hoc analysis, scenario modeling, and user-controlled parameters in Excel consumption layer |
| 4 | Agree on the basics: who owns each file, how changes get recorded, and where documentation lives — so no single person holds all the knowledge | **Governance framework definition** — define file versioning policy, named owner per file, documentation standard (inline comments, data dictionary), and change log requirements |
| 5 | Agree on who can change the logic — and what must happen before a change goes live — so errors cannot be introduced silently | **Change management process establishment** — define change initiator roles, peer review requirements, UAT sign-off, rollback procedure, and consumer notification on logic changes |

#### Phase 03 — Gaps & Bottlenecks

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Every refresh depends on someone doing it manually — if they are unavailable, the numbers go stale, and there is no record of what loaded or when | **No automated data pipeline** — acquisition relies on manual export or copy-paste with no scheduled extraction, no error handling, and no audit trail of what loaded and when |
| 2 | Nobody outside the file owner can explain how numbers are calculated — the logic is invisible and cannot be checked or challenged | **Business logic trapped in opaque formula chains** — no inline documentation, no separation of inputs from calculations, and no unit tests; logic is non-reproducible outside the file |
| 3 | When something changes or breaks, there is no record of what was altered, when, or by whom — and no way to roll back | **No version control system** — no Git, no enforced SharePoint versioning, and no change log; modifications overwrite prior state with no rollback path and no audit trail |
| 4 | The same file is doing three jobs at once: collecting data, calculating numbers, and presenting results — changing one part risks breaking all three | **No separation of concerns** — one workbook handles extraction, transformation, business logic, and presentation, creating brittle coupling and poor testability |
| 5 | There is nothing to catch bad input data before it reaches final numbers — errors only surface when someone spots them in the output | **No data validation layer** — no input schema checks, no range or threshold controls, and no row-count reconciliation against source; bad data propagates silently to output |

#### Phase 04 — Solution Steps

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Automate the data feed so the file updates itself — removing the manual step and person dependency | **Replace manual extraction with automated pipeline** — implement Power Query M with parameterized source connections, or Dataflow Gen2 or ADF for enterprise scale, and configure scheduled refresh with failure alerting |
| 2 | Write down and verify every calculation before changing anything — so there is a clear record of logic and a way to confirm nothing breaks | **Reverse-engineer and unit-test logic before migration** — build a test dataset with known outputs, document formulas and allocations as functional specification, and use as regression baseline during transition |
| 3 | Move core calculations out of spreadsheets into a shared governed layer — so logic is maintained once and spreadsheets become display surfaces | **Migrate certified metric logic to semantic model layer** — use Power BI shared dataset, SSAS Tabular, or dbt to remove formula duplication and establish a single source of truth for shared KPIs |
| 4 | Keep Excel for what it does best — flexible analysis and scenario exploration — not as the home of business-critical calculations | **Reconfigure Excel as thin consumption layer** — connect Excel to semantic model through XMLA endpoint or Analyze in Excel, keep business logic in model, and limit Excel to ad-hoc analysis and scenario inputs |
| 5 | Give every critical file a named owner, automatic update schedule, and change history — so it is maintainable, auditable, and not tied to one person | **Operationalize spreadsheet assets** — implement version control (SharePoint versioning or Git for structured workbooks), enforce scheduled refresh SLA, assign named DRI, and document in Data Product Passport |

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
| 1 | Ask the AI the questions your business actually needs answered — and document what it returns, including when answers contradict each other | **AI output benchmarking** — run a fixed set of natural language queries against the current data layer and document responses, inconsistency rates, and failure modes (hallucination, wrong measure resolution, incorrect filter context) |
| 2 | Understand why the AI keeps giving different answers — whether it is guessing what "revenue" means, querying the wrong source, or misreading period terms like "last quarter" | **Root-cause AI inconsistency analysis** — distinguish between ambiguous measure names (NL resolution failure), missing measure descriptions (intent inference failure), multiple datasets queried (source ambiguity), and absent time intelligence (period resolution failure) |
| 3 | Check whether the model is labeled so AI can understand it — clear names, plain-English descriptions, and no technical shorthand | **Semantic model AI-readiness audit** — assess measure description coverage, semantic naming quality for tables and columns, synonym definitions, and Q&A linguistic schema completeness |
| 4 | Check the quality of data AI is using — gaps, inconsistencies, or uncertified sources will produce unreliable answers | **Queried data layer profiling** — evaluate null rates on key dimensions, referential integrity, grain consistency, and certified versus uncertified datasets within AI-accessible scope |
| 5 | Be specific about which business questions AI should answer first — narrowing scope is what makes a pilot succeed | **AI use case taxonomy definition** — classify target queries by type (aggregation, trend, ranking, diagnostic, predictive) and assess feasibility against current model capabilities |

#### Phase 02 — Define Target State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Agree the exact questions AI must answer reliably — these become the test of whether implementation works | **AI acceptance criteria as fixed question set** — pair each benchmark question with an expected answer validated against the certified semantic model and use this as a regression test suite |
| 2 | Define what "ready for AI" means in practice — not just connected tooling, but correct and consistent answers to core questions | **AI-readiness checklist definition** — require complete measure descriptions, semantic naming standards, certified dataset as sole AI source, populated Q&A linguistic schema, and operational time intelligence layer |
| 3 | Pick one narrow, visible question first — prove success before expanding scope | **Pilot use case selection by feasibility-impact matrix** — prioritize a single subject area, up to five certified measures, clear success metric, and existing model coverage; avoid multi-domain complexity in pilot |
| 4 | Agree what "correct" means per question — exact values for some, acceptable ranges for others | **Accuracy threshold definition per query type** — require exact match for aggregation queries and tolerance bands for trend queries with documented acceptable variance |
| 5 | Agree who checks AI answers and how often — before outputs are used in decision-making | **AI output governance framework** — define validation DRI per subject area, spot-check sampling frequency, escalation path for anomalies, and integration with model certification cycle |

#### Phase 03 — Gaps & Bottlenecks

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | AI does not know what the business means by "Revenue" — without definitions it guesses | **Near-zero measure description coverage** — NL engines rely on descriptions and synonyms for intent resolution; without them they fall back to ambiguous name matching |
| 2 | Data is labeled in developer shorthand — abbreviations and codes AI can easily misread | **Technical naming conventions in model metadata** — snake_case, system prefixes, and abbreviated codes reduce NL resolution quality and increase hallucination risk |
| 3 | AI can pick from several overlapping sources unpredictably, so the same question can return different answers | **Multiple conflicting datasets exposed to AI** — no single certified authoritative model, causing non-deterministic source selection |
| 4 | Ask about period comparisons and AI either fails or returns unreliable results because time logic is missing | **No marked date table or time intelligence measures** — AI cannot resolve natural period language without CALCULATE-based measures and a configured date table |
| 5 | There is no process to verify whether AI answers are correct before they reach decision-makers | **No output validation layer** — responses are not reconciled against certified values; no sampling framework, anomaly detection, or assigned DRI |

#### Phase 04 — Solution Steps

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Relabel everything in plain business language so AI understands the same vocabulary your team uses | **Apply semantic naming conventions across model** — rename tables, columns, and measures to business-readable terms; populate Q&A linguistic schema with synonyms and common query phrasing |
| 2 | Write plain-English definitions for each key metric so AI knows exactly which number to return | **Author measure descriptions for certified metrics** — document business definition, grain, inclusions or exclusions, and date logic in plain English to support intent resolution |
| 3 | Add reliable period comparison capability so AI can answer time-based questions accurately, not just return snapshots | **Implement time intelligence layer** — mark date table, build YoY, QoQ, MTD, YTD, and rolling-window measures, validate against fiscal calendar, and register period synonyms in Q&A schema |
| 4 | Point AI only at trusted certified data so answers come from the same numbers your team already relies on | **Restrict AI data scope to certified semantic model** — remove raw dataset or warehouse access and configure Copilot or Fabric AI to query endorsed dataset only as a contract boundary |
| 5 | Set up recurring checks so AI answers are verified against certified numbers before they influence decisions | **Implement output validation protocol** — assign DRI per subject area, define weekly sampling cadence, configure variance anomaly alerts, and fold checks into model certification review |

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
| 1 | Talk to the people who need answers — find out what they ask every week, what they can't currently answer, and where reporting is slowing decisions down | **Conduct requirements elicitation using structured discovery interviews** — capture recurring analytical questions, report consumers, decision frequency, and current workaround patterns |
| 2 | Find out what data exists and whether it's actually reachable — some systems connect easily, others only through manual extracts | **Source system discovery** — catalogue available systems (ERP, CRM, HRIS, flat files), assess connection feasibility (API availability, ODBC/JDBC, export-only, manual), and identify data ownership |
| 3 | Walk through exactly how reports are produced today — every manual step, every handoff, and where delays or errors get introduced | **Process archaeology** — document the current-state reporting workflow end-to-end: source extraction steps, manual transformation logic, file handoffs, consolidation points, and rework loops |
| 4 | Find the one question or process that causes the most pain — the one that wastes the most time or blocks the most important decisions | **Prioritise analytical gaps by business impact score** — weight by decision frequency, stakeholder seniority, manual effort displaced, and revenue or risk exposure; use as anchor for MVP scope |
| 5 | Understand how comfortable different users are with data tools — so what gets built matches how people actually work | **Assess user analytical maturity by persona** — distinguish power users (comfortable with calculated fields, custom visuals), standard consumers (filter and slice only), and executive viewers |

#### Phase 02 — Define Target State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Agree on the specific questions this needs to answer — and make those the test of whether each stage has worked | **Convert question inventory to a model design brief** — map each question to required dimensions, measures, and grain; use as acceptance criteria for each delivery phase |
| 2 | Agree on the smallest version that still gives you something genuinely useful — weeks to first value, not months | **Define MVP scope** — minimum subject area coverage, minimum KPI set, and minimum sources required to answer the top 3–5 priority questions; design for iterative extension |
| 3 | Agree on a delivery sequence where each stage builds on the last — so you're never waiting on a single big launch that keeps slipping | **Define phased delivery roadmap** — sequence releases by dependency order, validate each phase against acceptance criteria before proceeding |
| 4 | Agree upfront on how you'll know it's working — time saved, people using it, decisions actually informed by it | **Define success KPIs per delivery phase** — active users, query volume, manual reporting hours displaced; instrument usage telemetry from day one |
| 5 | Agree on what the finished solution looks like — and equally what it won't cover — so expectations are set before the build starts | **Define target state architecture** — semantic model scope, self-service tier design by user persona, governance model, and explicit out-of-scope boundaries to prevent scope creep |

#### Phase 03 — Gaps & Bottlenecks

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | Every time you need numbers, someone has to manually pull them from each system separately — and the process is different each time, which is why the results never quite match | **No ELT pipeline or governed extraction layer** — source systems accessible only through manual export; no staging environment, no extraction contracts, no schema documentation |
| 2 | You've been waiting for a technology decision that doesn't need to happen before you start — the debate about which tools to use is what's keeping you stuck | **No agreed analytics platform or toolchain** — absence of decisions on warehouse, semantic layer, and consumption tool is creating delivery paralysis; platform selection should be timeboxed and driven by use-case requirements |
| 3 | Leadership challenges the figures every board meeting because there's no agreed definition — Revenue means something different to Finance than it does to Sales | **No Metric Dictionary or Business Glossary** — KPI definitions undocumented; conflicting definitions risk being encoded into the model from day one |
| 4 | When this is built, you need someone internally who can own and update it — without that person, you'll be dependent on outside help for every small change | **No internal analytics capability** — no owned semantic model, no trained power users, no knowledge transfer plan; every change requires external resourcing |
| 5 | Unless ownership is established from day one, you'll be back in the same position in 12 months — numbers nobody fully trusts, maintained by nobody, updated only when someone remembers | **No governance framework** — no named data owner, no refresh SLA, no certification or change process; without these, user trust will not develop regardless of technical quality |

#### Phase 04 — Solution Steps

| Phase | Business Translation | Analytics Translation |
|---|---|---|
| Phase 1 | Within 4–6 weeks, you stop spending two days before every board meeting — your core numbers are automated, consistent, and ready before you ask for them | Build extraction layer for top 3 source systems, minimal staging schema, core fact and dimension tables at agreed grain, certified semantic model with 3–5 KPIs, and first report validated against acceptance criteria |
| Phase 2 | You can now answer the follow-up questions without going back to source systems — trends over time, breakdowns by team or product, and the ability to drill into what's behind a number | Implement time intelligence layer, extend dimension model with additional attributes, hierarchies, and SCD handling, and validate against extended acceptance criteria |
| Phase 3 | Your team stops asking for new reports — they can explore the data themselves, and every number they use has a certified, agreed definition behind it | Extend semantic model to additional subject areas, configure self-service layer with RLS by user persona, apply certified endorsement, and complete Metric Dictionary for all published measures |
| Phase 4 | The solution is yours — your team knows how to use it, someone owns it, and it can evolve without bringing in outside help every time something changes | Deliver structured enablement by user tier, publish Data Product Passport and Handover Guide, assign DRI per subject area, and operationalise change management process |

**Key bottlenecks:** No governed access to source data · No agreed metric definitions to build from · Risk of "big bang" approach — nothing for 12 months · No internal capability to maintain what's built

**Iterative target state:** Phase 1 live within 4–6 weeks: 3 sources, core KPIs · Metrics defined and certified before reporting goes live · Self-service layer operational by Phase 3 · Internal champion identified and enabled

> *"I can take you from manual spreadsheet chaos to a working analytics layer in a focused engagement — starting with the questions that matter most, not a two-year platform project."*

---

### Entry Point 6 — The Translation Failure

**Complexity:** Diagnostic · **Business-IT disconnect**

> *"Our last dashboard looked great in the demo. Three months after go-live, everyone was back in Excel. The business never trusted the numbers enough to stop checking them manually. We don't have the appetite to go through that again."*

#### Phase 01 — Assess Their State

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | You're asked to walk through your actual weekly reporting process — not what it's supposed to look like, but what actually happens — because that gap is usually where the real problem lives | **Current-state process mapping via elicitation** — establish end-to-end data acquisition workflow, identify manual touchpoints, and surface undocumented transformation steps the stakeholder has normalised |
| 2 | "What question do you most wish you could answer but can't?" — that usually surfaces requirements the previous project never captured, because the people writing the brief never thought to ask it | **Analytical capability gap identification** — surface unmet decision-support requirements not captured in formal requirements documentation; often reveals actual scope vs presented scope |
| 3 | "When was the last time a number was challenged in a meeting?" — that question locates the exact moment trust broke down, and whether it was ever properly acknowledged or just quietly absorbed | **Trust deficit assessment** — identify the most recent analytical failure event; root-cause as data quality, metric definition, or stakeholder credibility gap; use as a proxy for the depth of the trust problem |
| 4 | Find out whether the current numbers are actually driving decisions — or just describing situations nobody knows how to act on — because a dashboard that only explains is one people eventually stop opening | **Decision-action linkage audit** — assess whether analytical outputs are connected to specific decisions or consumed as information only; distinguish descriptive from prescriptive reporting maturity |

#### Phase 02 — Define Target (Together)

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | The previous project started with "what should the dashboard show?" — this one starts with "what decisions are you trying to make?" — that single shift changes everything that follows | **Requirements decomposition** — shift elicitation from output specification (report format, requested KPIs) to decision decomposition (decision type, frequency, owner, data inputs required, acceptable latency) |
| 2 | Before any number is built, agree who owns what it means — the business defines the rules, the analyst encodes them — so when a number is challenged there's no ambiguity about where to go | **Metric ownership assignment** — establish DRI accountability for business rule definition per KPI; document in Metric Dictionary; position the analytical layer as translation medium, not definition authority |
| 3 | Agree on three specific questions this engagement must be able to answer — not a wish list — three questions that, if answered reliably, would genuinely change how decisions get made | **Acceptance criteria definition** — establish a minimum viable question set as functional requirements; each question maps to a specific decision, data source, and metric definition; use as scope anchor and delivery gate |

#### Phase 03 — Surface Real Gaps

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | "Is revenue gross or net? Before rebates?" — the moment you ask the second question, you find out whether Revenue is a shared definition or a word everyone has assumed means the same thing | **Metric definition decomposition** — test whether the KPI is sufficiently specified for unambiguous implementation: grain, inclusions, exclusions, date logic, and edge-case treatment |
| 2 | Ask whether the ERP and the spreadsheet would give you the same revenue figure — because if two sources your team already uses can't agree, that's the problem to solve before any dashboard is built | **Source-of-truth reconciliation test** — assess whether primary data sources would produce the same output for the same question; identify the existence and depth of data trust gaps without running a formal reconciliation |
| 3 | "Who would you call if this number was wrong?" — that question almost always produces a pause, and the pause is the answer: either someone owns the number, or nobody does | **Data ownership and escalation path assessment** — identify whether a DRI exists per metric, whether a documented resolution process exists for data quality issues, and whether the stakeholder has an accountable counterpart |

#### Phase 04 — Reposition & Propose

| # | Business Translation | Analytics Translation |
|---|---|---|
| 1 | By the end of the diagnostic engagement, you and the consultant have a shared name for the actual problem and a clear point of entry for solving it | **Diagnostic classification** — map discovery findings to the appropriate entry point framework; document presenting problem, root cause hypothesis, and recommended starting sequence |
| 2 | What you walk away with is not a quote for a project — it's a proposal for a short, bounded diagnostic that proves direction before major investment | **Scoped engagement proposal** — define a time-boxed diagnostic phase (discovery + POC) before committing to full build, with scope defined by the question set rather than a feature list |
| 3 | You leave with a written statement describing your problem in your own language — agreed by both sides before any delivery starts | **Discovery artefact** — produce a jointly authored problem statement capturing current state in business language, root cause hypothesis, the three agreed questions, and proposed success criteria |
| 4 | Before anything is built, the working relationship is made explicit: you define what the numbers mean, and the consultant translates that into an analytical solution | **Engagement model definition** — formalise the division of responsibility: business owns metric definitions, business rules, and acceptance criteria; consultant owns translation into model and delivery structure |

**Key bottlenecks:**
- The people who defined the requirements weren't the people who felt the problem — so the brief was wrong before the build started
- Everyone described their piece of the process, nobody described the whole — leaving the biggest inefficiencies invisible and unaddressed
- The build fixed what was asked for, not what was actually broken — and what was actually broken was often one step upstream or downstream
- Developers optimised the current state rather than questioning whether the current state was worth keeping

**Iterative target state:**
- Requirements gathered across the full stakeholder map — not just the loudest voice in the room — so the brief reflects the actual problem, not the presented one
- End-to-end process walkthrough before any build begins — because the highest-value improvement is rarely where the conversation started
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
