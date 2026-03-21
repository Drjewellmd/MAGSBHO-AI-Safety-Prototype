# MAGSBHO Prototype

Early-stage AI safety prototype demonstrating governance-constrained multi-agent decision-making under simulated mission conditions.

## Governance-Constrained Multi-Agent AI Safety Prototype

This repository contains a Python prototype inspired by the **MAGSBHO (Multi-Agent Governance System for Behavioral Health and Operations)** framework.

---

## Purpose

The goal of this prototype is to demonstrate a simple, interpretable implementation of a governance-constrained multi-agent system for high-risk environments such as space missions and other isolated, confined, and extreme (I.C.E.) settings.

---

## What the Prototype Includes

- **EVE**: wellness support agent for stress and emotional regulation  
- **KIRK**: ethical and cohesion agent for conflict and team stability  
- **SGG (SpaceGuardianGPT)**: cognitive support agent for task load and clarity  
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

### Method

The system uses rule-based decision logic to enable transparent evaluation of governance behavior prior to machine learning integration.

### Output

Simulation results are exported to `magsbho_simulation_results.csv`, enabling structured evaluation of escalation behavior and bounded autonomy.

---

## Example Execution Output

Example Scenario:

Scenario: High Stress + Conflict  
EVE: HIGH_SUPPORT | KIRK: ESCALATE_CONFLICT | SGG: MONITOR  
Decision: ESCALATE_TO_HUMAN  

Full outputs are available in:

- `simulation_run_part1.png`  
- `simulation_run_part2.png`  
- `simulation_summary.png`  

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

## Results Snapshot

Initial simulation testing demonstrates:

- Consistent escalation in high-risk scenarios  
- Low false-negative behavior in critical conditions  
- Stable decision-making across repeated stress patterns  

Results exported via CSV for structured evaluation.

---

## Why This Matters

AI systems deployed in high-risk environments must operate safely under uncertainty, incomplete information, and human stress.

This prototype demonstrates how governance-based architectures can:

- enforce safety constraints  
- maintain interpretability  
- support reliable decision-making in mission-critical environments  

including space missions, healthcare systems, and autonomous operations.

---

## Future Work

Planned next steps include:

- expanding scenario coverage and stress-testing edge cases  
- incorporating temporal modeling (time, accumulation, trajectory of behavioral states)  
- integrating physiological and behavioral data streams  
- evaluating escalation accuracy against human expert judgment  
- transitioning from virtual simulations to in-person analog astronaut missions  
- extending toward clinically supervised architectures (QUARTET model)  

---

## Run the Scenario Runner

```bash
py magsbho_scenario_runner.py
