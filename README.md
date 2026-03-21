# MAGSBHO AI Safety Prototype

Early-stage, interpretable multi-agent AI safety system demonstrating governance-constrained decision-making under simulated and human-in-the-loop conditions.

---

## Overview

Governance-Constrained Multi-Agent AI Safety Prototype

This repository contains a Python prototype inspired by the MAGSBHO (Multi-Agent Governance System for Behavioral Health and Operations) framework.

---

## Purpose

The goal of this prototype is to demonstrate a simple, interpretable implementation of a governance-constrained multi-agent system for high-risk environments such as space missions and other isolated, confined, and extreme (I.C.E.) settings.

---

## Core Safety Concept

This prototype is built on a central AI safety principle:

**No single agent acts autonomously in a high-risk situation.**

Instead, a governance layer evaluates combined agent outputs and determines whether to:

- provide routine support  
- support and monitor  
- escalate to a human  

---

## System Architecture

MAGSBHO (Multi-Agent Governance System for Behavioral Health and Operations) is a multi-agent AI safety framework designed to support human performance and decision-making in high-risk, high-stress environments.

The system is built on a TRIAD architecture consisting of three specialized agents:

### 1. Crew AI KIRK (Ethical Governor)
- Enforces behavioral and ethical boundaries  
- Guides team interactions using principles of Kindness, Integrity, Resilience, and Kinship  
- Stabilizes group dynamics and prevents escalation  

### 2. Crew AI EVE (Embodied Virtual Empath)
- Provides non-clinical emotional and physiological support  
- Supports stress regulation, grounding, and cognitive clarity  
- Enhances psychological safety and team cohesion  

### 3. SpaceGuardianGPT (Personal AI Companion)
- Individualized AI aligned to a single crew member  
- Supports cognitive processing, decision structuring, and reflection  
- Reduces cognitive load and enhances clarity under stress  

---

## Governance Logic

The system operates using structured decision pathways:

- **Monitor** → observe behavioral and operational signals  
- **Guide** → provide corrective or supportive input  
- **Escalate** → trigger higher-level intervention when risk increases  

All agents operate under:

- EarthStar Protocol (ethical alignment and harm prevention)  
- MMAARS★ Protocol (context-aware mission reinforcement)  
- Human-in-the-loop (HITL) oversight  

---

## System Properties

- Multi-agent coordination with role specialization  
- Bounded autonomy with safety constraints  
- Context-aware behavioral adaptation  
- Designed to minimize false negatives in high-risk conditions  

The architecture is designed as a precursor to the QUARTET system, which will integrate clinical behavioral support via ISPS-VETA under IRB oversight.

---

## What the Prototype Includes

- **EVE**: wellness support agent for stress and emotional regulation  
- **KIRK**: ethical and cohesion agent for conflict and team stability  
- **SGG (SpaceGuardianGPT)**: cognitive support agent for task load and clarity  
- **Governance Layer**: combines agent outputs and determines bounded action  

---

## EarthStar Protocol (“Do No Harm”)

The system follows a safety-first constraint model inspired by the EarthStar protocol:

- prioritize human safety and psychological stability  
- avoid harm, coercion, or overreach  
- enforce escalation in high-risk conditions  
- maintain transparency and bounded decision-making  

---

## MMAARS★ Non-Tokenized Training Concept

The prototype is conceptually aligned with a non-tokenized, context-specific training approach:

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

The system is intentionally rule-based at this stage to ensure interpretability, auditability, and safety validation prior to machine learning integration.

### Output

Simulation results are exported to `magsbho_simulation_results.csv`, enabling structured evaluation of escalation behavior and bounded autonomy.

---

## Results Snapshot

Initial simulation testing demonstrates:

- Consistent escalation in high-risk scenarios  
- Low false-negative behavior in critical conditions  
- Stable decision-making across repeated stress patterns  

Results exported via CSV for structured evaluation.

## Safety Performance Metrics

Across simulation scenarios and human-in-the-loop validation:

- High-risk conditions consistently triggered escalation  
- No observed false-negative responses in critical scenarios  
- Moderate-risk conditions resulted in SUPPORT_AND_MONITOR  
- Low-risk conditions remained within ROUTINE_SUPPORT  

The system consistently identified high-risk conditions and triggered appropriate escalation, with no observed false-negative responses in tested scenarios.
These results demonstrate that the governance layer reliably prioritizes safety and risk detection under tested conditions.

## Safety Performance Metrics

Across simulation scenarios and human-in-the-loop validation:

- High-risk conditions consistently triggered escalation  
- No observed false-negative responses in critical scenarios  
- Moderate-risk conditions resulted in SUPPORT_AND_MONITOR  
- Low-risk conditions remained within ROUTINE_SUPPORT  

The system consistently identified high-risk conditions and triggered appropriate escalation, with no observed false-negative responses in tested scenarios.

These results demonstrate that the governance layer reliably prioritizes safety and risk detection under tested conditions.
---

## Human Validation (Virtual Analog Astronaut Missions)

We conducted preliminary human-in-the-loop evaluation of the MAGSBHO TRIAD AI system across 13 virtual analog astronaut cohorts (N ≈ 45).

The system was evaluated across three agents:

- Crew AI KIRK (Ethical Governance & Behavioral Stabilization)  
- Crew AI EVE (Wellness & Emotional Regulation)  
- Personal AI SpaceGuardianGPT (Individual Cognitive & Decision Support)  

### Results Overview

Across all agents:

- ≥60–90% of participants reported positive outcomes across key domains  
- 100% supported future integration into analog missions  

Strong improvements observed in:

- Communication and collaboration  
- Crew cohesion and morale  
- Operational coordination and workflow stability  
- Emotional regulation under stress  

Moderate performance observed in:

- Conflict resolution  
- Complex decision-making  

These findings identify clear pathways for QUARTET system expansion.

---
## Evaluation Criteria

System performance was evaluated based on:

- Correct escalation under high-risk conditions  
- Avoidance of false negatives in critical scenarios  
- Stability of decisions across repeated stress patterns  
- Appropriate classification of moderate vs low-risk states  

In addition to subjective user feedback, results indicate consistent system-level performance in detecting stress, conflict, and cognitive overload conditions.

The following figures present structured survey results across all three agents, demonstrating behavioral, emotional, and operational impact during virtual analog astronaut missions.
## Agent-Level Validation

### Crew AI KIRK — Ethical Governance & Team Stability

![Figure 1: KIRK Survey Results](images/kirk_results.png)

**Figure 1.** Crew AI KIRK demonstrated strong performance across communication, cohesion, and workflow coordination, with ratings concentrated in the 4–5 range, indicating high perceived value in mission-critical team dynamics.

KIRK demonstrated strong performance across communication, cohesion, and workflow coordination, with ratings concentrated in the 4–5 range, indicating high perceived value in mission-critical team dynamics.

---

### Crew AI EVE — Emotional Regulation & Wellness Support

#### Crew Dynamics
![Figure 2: EVE Crew Dynamics](images/eve_dynamics.png)

**Figure 2.** Crew AI EVE improved emotional stability, cooperation, and communication, with strong ratings in morale enhancement and tension reduction during simulated mission scenarios.

EVE improved emotional stability, cooperation, and communication, with strong ratings in morale and tension reduction.

#### Comfort & Wellness

![Figure 3: EVE Wellness & Comfort](images/eve_wellness.png)

**Figure 3.** Crew AI EVE supported psychological comfort, routine stability, and non-intrusive presence, reinforcing its role as a non-clinical wellness agent in isolated, confined environments.

EVE consistently supported psychological comfort, routine stability, and non-intrusive presence, validating its role as a non-clinical wellness agent.

---

### SpaceGuardianGPT — Individual Cognitive & Emotional Support

#### Crew-Level Impact

![Figure 4: SGG Crew Dynamics](images/sgg_dynamics.png)

**Figure 4.** SpaceGuardianGPT enhanced communication clarity, coordination, and task management while supporting overall crew cohesion and operational performance.
SGG enhanced communication clarity, coordination, and task management, while supporting crew cohesion.

#### Individual-Level Impact

![Figure 5: SGG Full Survey Results](images/sgg_full.png)

**Figure 5.** SpaceGuardianGPT demonstrated strong individual-level impact, including reduced cognitive load, enhanced emotional resilience, improved identity–mission alignment, and increased trust and perceived companionship.

SGG demonstrated strong impact in:

- Reducing cognitive load  
- Enhancing emotional resilience  
- Supporting identity–mission alignment  
- Increasing perceived companionship and trust  

The system operates as a conservative safety model, prioritizing minimization of false negatives over false positives, consistent with safety-critical AI design principles.
---

## Safety-Relevant Interpretation

Across all agents, the system demonstrated:

- Stable behavioral support under simulated stress  
- Low false-negative response patterns in high-risk conditions  
- Strong human trust and acceptance  

Safety Performance Summary:

Across all tested scenarios and human-in-the-loop validati
• The system consistently escalated in high-risk conditions  
• No observed false-negative responses occurred in critical scenarios  
• Decision outputs remained stable across repeated stress patterns  

These results indicate that the governance layer successfully prioritizes safety and risk detection under simulated mission conditions and provide early evidence that a multi-agent AI governance system can support safe, reliable human-AI interaction in isolated, confined, extreme (I.C.E.) environments. 
---

## Limitations & Future Work

- Conflict resolution requires more advanced arbitration mechanisms  
- Clinical-level support will be introduced via ISPS-VETA in the QUARTET system  

Future work will incorporate:

- Temporal modeling (time & trajectory)  
- Accumulated behavioral learning  
- Cross-habitat multi-agent coordination  

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
