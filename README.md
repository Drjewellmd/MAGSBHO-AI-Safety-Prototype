# MAGSBHO Prototype

## Governance-Constrained Multi-Agent AI Safety Prototype

This repository contains a Python prototype inspired by the **MAGSBHO (Multi-Agent Governance System for Behavioral Health)** framework.

---

## Purpose

The goal of this prototype is to demonstrate a simple, interpretable implementation of a governance-constrained multi-agent system for high-risk environments such as space missions and other isolated, confined, and extreme (I.C.E.) settings. This work explores governance-constrained multi-agent systems as a safety architecture aligned with emerging research in scalable oversight and human-in-the-loop AI.

---

## What the prototype includes

- **EVE**: wellness support agent for stress and emotional regulation  
- **KIRK**: ethical / cohesion agent for conflict and team stability  
- **SGG**: cognitive support agent for task load and clarity  
- **Governance Layer**: combines agent outputs and determines bounded action  

---

## Core Safety Concept

This prototype is built on a central AI safety principle:

**No single agent acts autonomously in a high-risk situation.**

Instead, a governance layer evaluates combined agent outputs and determines whether to:

- provide routine support  
- support and monitor  
- escalate to a human  

---

## EarthStar Protocol (“Do No Harm”)

The system follows a safety-first constraint model inspired by the EarthStar protocol:

- prioritize human safety and psychological stability  
- avoid harm, coercion, or overreach  
- enforce escalation in high-risk conditions  
- maintain transparency and bounded decision-making  

---

## MMAARS★ Non-Tokenized Training Concept

The prototype is conceptually aligned with a non-tokenized training approach:

- individualized contextual learning rather than generic token prediction  
- crew-specific behavioral adaptation  
- human-centered interaction constraints  
- prevention of unsafe generalization across contexts  

---

## Scenario Testing (Version 2)

The prototype was extended into a multi-scenario simulation runner to evaluate governance decisions under varying operational conditions.

### Features
- Multiple structured scenarios  
- Agent-level outputs (EVE, KIRK, SGG)  
- Governance decision logic  
- CSV export for analysis  

### Scenario Coverage
- High Stress + Conflict  
- Moderate Stress  
- Cognitive Overload  
- Low Risk  
- Repeated Mild Stress  
- High Conflict Only  
- High Stress Only  
- Borderline Mission Load  
- Team Drift Pattern  
- Operational Crisis  

### Output
Simulation results are exported to `magsbho_simulation_results.csv`, enabling structured evaluation of escalation behavior and bounded autonomy.

---

### Example Execution Output

See:
- `simulation_run_part1.png`
- `simulation_run_part2.png`
- `simulation_summary.png`

for full execution and summary results.

These results demonstrate early-stage validation of governance-constrained decision-making under varying operational conditions.

---

## Preliminary Simulation Insights

Initial scenario testing demonstrates that the governance layer consistently prioritizes safety by escalating in high-risk conditions.

### Key Observations
- High stress + conflict scenarios reliably triggered **ESCALATE_TO_HUMAN**  
- Cognitive overload conditions were correctly identified and escalated  
- Moderate and repeated issues resulted in **SUPPORT_AND_MONITOR**  
- Low-risk scenarios remained within **ROUTINE_SUPPORT**  

### Interpretation
These results suggest that the governance logic appropriately balances:

- safety-first escalation  
- avoidance of unnecessary intervention  
- bounded autonomy under lower-risk conditions  

This supports the core design principle that no single agent acts autonomously in high-risk situations.

### Limitations
This prototype uses simplified rule-based logic and simulated inputs; future work will incorporate probabilistic modeling, real-time data streams, and validation in in-person analog environments.

---
These findings support continued development and staged validation of governance-constrained multi-agent systems in high-risk environments.

## Future Work

Planned next steps to advance MAGSBHO toward research-grade validation include:
- expanding scenario coverage and stress-testing edge cases  
- integrating physiological and behavioral data streams  
- evaluating escalation accuracy against human expert judgment  
- extending toward clinically supervised architectures (QUARTET model)
- Future iterations will include human-labeled ground truth to evaluate escalation accuracy and false positive/false negative rates.
- Future work will incorporate uncertainty estimation to handle ambiguous or conflicting agent signals.
- Future work will incorporate temporal modeling to account for time-dependent dynamics, including the accumulation of repeated low-level stressors and trajectory-based changes in behavioral and cognitive states across mission duration.
- - incorporating temporal modeling to capture time-dependent dynamics, including accumulation of repeated stressors and trajectory-based behavioral changes  

## How to Run the Scenario Runner
```bash
py magsbho_scenario_runner.py
