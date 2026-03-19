# MAGSBHO Prototype

## Governance-Constrained Multi-Agent AI Safety Prototype

This repository contains a simple Python prototype inspired by the **MAGSBHO (Multi-Agent Governance System for Behavioral Health)** framework.

### Purpose
The goal of this prototype is to demonstrate a small, interpretable part of a governance-constrained multi-agent system for high-risk environments.

### What the prototype includes
- **EVE**: wellness support agent for stress and emotional regulation
- **KIRK**: ethical / cohesion agent for conflict and team stability
- **SGG**: cognitive support agent for task load and confusion
- **Governance Layer**: combines agent outputs and determines bounded action

### Core safety concept
This prototype is designed around a simple AI safety principle:

**No single agent acts autonomously in a high-risk situation.**  
Instead, a governance layer evaluates the combined outputs and decides whether to:
- provide routine support
- support and monitor
- escalate to a human

### Example output
The current demo mission case simulates:
- elevated stress
- team conflict
- cognitive overload
- repeated issue pattern
### Example Run Output

Below is a sample output from running the prototype:

![MAGSBHO Output](output_screenshot.png)

This leads to a governance decision of:

`ESCALATE_TO_HUMAN`

### Run the code
```bash
py magsbho_prototype.py
