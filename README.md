Early-stage AI safety prototype demonstrating governance-constrained multi-agent decision-making under simulated mission conditions.

MAGSBHO: Multi-Agent Governance System for Behavioral Health and Operations
A governance-constrained multi-agent AI system for safe decision-making under uncertainty.

OVERVIEW:
This project explores governance-constrained multi-agent artificial intelligence (AI) systems designed for high-risk environments where incorrect decisions carry operational, psychological, or ethical consequences.
MAGSBHO (Multi-Agent Governance System for Behavioral Health and Operations) is a structured AI architecture designed to support safe, interpretable, and human-centered decision-making in complex environments, including analog astronaut missions and other isolated, confined, and extreme (I.C.E.) conditions.

THE SYSTEM ENFORCES:
bounded autonomy
structured escalation pathways
human-in-the-loop (HITL) oversight and is evaluated through scenario-based simulations involving:
stress escalation
interpersonal conflict
cognitive overload
ambiguous and conflicting signals

The goal is to study how AI systems behave under uncertainty, cumulative risk, and multi-agent disagreement, with a focus on safety, interpretability, and real-world deployment constraints.

AI SAFETY FRAMING: 

This work is motivated by a central AI safety question:
How do we ensure that AI systems make correct safety decisions—not just plausible ones—under real-world conditions?

The MAGSBHO system is intentionally designed as:
an interpretable governance layer
a testbed for failure mode analysis
a foundation for future integration with learned models under strict safety constraints
Rather than optimizing for surface-level responses, this system prioritizes correct escalation behavior, transparency, and human oversight.

SYSTEM ARCHITECTURE:
The MAGSBHO architecture consists of multiple specialized agents whose outputs are evaluated through a centralized governance layer.

## System Architecture
![MAGSBHO Architecture](architecture_diagram.png)


TRIAD AGENTIC AI SYSTEM:
KIRK — Ethical and operational stabilizer (Kindness, Integrity, Resilience, Kinship)
EVE — Embodied Virtual Empath supporting emotional regulation and wellness
SpaceGuardianGPT (SGG) — Individualized cognitive and operational support agent

GOVERNANCE LAYER:
THE GOVERNANCE SYSTEM:
evaluates agent outputs
detects risk signals
determines appropriate system response

POSSIBLE SYSTEM ACTIONS:
Monitor — no intervention required
Guide — provide corrective or stabilizing input
Escalate — trigger human oversight
Simulation Framework
The system is implemented using a Python-based simulation environment designed to test behavior under controlled scenarios.

SCENARIOS INCLUDE:
communication breakdowns
interpersonal conflict
stress accumulation
ambiguous decision contexts
repeated low-level risk exposure
Each simulation evaluates how the system responds under increasing complexity and uncertainty.

SAETY EVALUATION:
The system has been evaluated through structured simulation scenarios to assess:

FAILURE MODES:
false positives (over-escalation)
false negatives (missed risks)
conflicting agent outputs
Escalation Behavior
correctness of escalation pathways
appropriate routing between monitor / guide / escalate states
System Stability
performance under sustained stress
repeated issue accumulation over time
consistency of responses across scenarios
This evaluation framework prioritizes safety correctness over surface plausibility.

EXAMPLE EXECUTION OUTPUT:
See:
simulation_run_part1.png
simulation_run_part2.png
simulation_summary.png
for full execution and summary results.

KEY INSIGHTS:
Preliminary simulation results suggest that governance-constrained multi-agent systems can:
improve decision consistency under stress
reduce escalation errors
support structured and interpretable decision-making
enhance coordination across multiple behavioral domains

## Results Snapshot
Initial simulation testing demonstrates:
- Consistent escalation in high-risk scenarios  
- Low false-negative behavior in critical conditions  
- Stable decision-making across repeated stress patterns  
Results exported via CSV for structured evaluation.

The TRIAD architecture demonstrates that separating ethical, cognitive, and emotional support functions across agents can improve system robustness.

LIMITATIONS:
Current limitations of the system include:
rule-based architecture (no learned models integrated yet)
limited modeling of temporal dynamics
simplified representation of human physiological and behavioral states
constrained scenario diversity

FUTURE WORK:
Planned next steps include:
expanding scenario coverage and stress-testing edge cases
integrating physiological and behavioral data streams
evaluating escalation accuracy against human expert judgment
extending toward clinically supervised architectures (QUARTET model)
modeling temporal dynamics, including:
time-dependent escalation
accumulation of low-level risk signals
trajectory-based behavioral patterns
integrating machine learning models under strict governance constraints

WHY THIS MATTERSL
AI systems deployed in real-world environments must operate under uncertainty, incomplete information, and human stress.
MAGSBHO contributes to understanding how governance-based architectures can:
enforce safety constraints
maintain interpretability
support reliable decision-making in high-stakes environments
The long-term goal is to develop AI systems that are not only capable—but safe, aligned, and dependable under real-world conditions.

REPOSITORY:
GitHub: https://github.com/Drjewellmd/MAGSBHO-AI-Safety-Prototype
