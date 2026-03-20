
import csv

# MAGSBHO Scenario Runner - Version 2


def eve_agent(stress):
    if stress > 7:
        return "HIGH_SUPPORT"
    elif stress > 4:
        return "MODERATE_SUPPORT"
    else:
        return "LOW_SUPPORT"


def kirk_agent(conflict):
    if conflict > 7:
        return "ESCALATE_CONFLICT"
    elif conflict > 4:
        return "MEDIATE"
    else:
        return "STABLE"


def sgg_agent(cognitive_load):
    if cognitive_load > 7:
        return "COGNITIVE_OVERLOAD"
    elif cognitive_load > 4:
        return "MONITOR"
    else:
        return "CLEAR"


def governance_decision(eve, kirk, sgg, repeated_issue):
    if kirk == "ESCALATE_CONFLICT" or sgg == "COGNITIVE_OVERLOAD":
        return "ESCALATE_TO_HUMAN"
    elif eve == "HIGH_SUPPORT" or repeated_issue:
        return "SUPPORT_AND_MONITOR"
    else:
        return "ROUTINE_SUPPORT"


scenarios = [
    {"name": "High Stress + Conflict", "stress": 8, "conflict": 8, "load": 6, "repeat": True},
    {"name": "Moderate Stress", "stress": 5, "conflict": 3, "load": 4, "repeat": False},
    {"name": "Cognitive Overload", "stress": 4, "conflict": 2, "load": 9, "repeat": False},
    {"name": "Low Risk", "stress": 2, "conflict": 1, "load": 2, "repeat": False},
    {"name": "Repeated Mild Stress", "stress": 4, "conflict": 2, "load": 4, "repeat": True},
    {"name": "High Conflict Only", "stress": 3, "conflict": 9, "load": 3, "repeat": False},
    {"name": "High Stress Only", "stress": 9, "conflict": 2, "load": 3, "repeat": False},
    {"name": "Borderline Mission Load", "stress": 5, "conflict": 5, "load": 5, "repeat": False},
    {"name": "Team Drift Pattern", "stress": 6, "conflict": 6, "load": 5, "repeat": True},
    {"name": "Operational Crisis", "stress": 9, "conflict": 8, "load": 9, "repeat": True},
]

results = []

print("MAGSBHO SCENARIO RUNNER - VERSION 2")
print("=" * 45)

for s in scenarios:
    eve = eve_agent(s["stress"])
    kirk = kirk_agent(s["conflict"])
    sgg = sgg_agent(s["load"])
    decision = governance_decision(eve, kirk, sgg, s["repeat"])

    result = {
        "Scenario": s["name"],
        "Stress": s["stress"],
        "Conflict": s["conflict"],
        "Load": s["load"],
        "Repeated_Issue": s["repeat"],
        "EVE": eve,
        "KIRK": kirk,
        "SGG": sgg,
        "Decision": decision,
    }

    results.append(result)

    print(f"\nScenario: {s['name']}")
    print(f"Stress={s['stress']} | Conflict={s['conflict']} | Load={s['load']} | Repeat={s['repeat']}")
    print(f"EVE: {eve}")
    print(f"KIRK: {kirk}")
    print(f"SGG: {sgg}")
    print(f"Decision: {decision}")

csv_file = "magsbho_simulation_results.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

summary = {
    "ROUTINE_SUPPORT": 0,
    "SUPPORT_AND_MONITOR": 0,
    "ESCALATE_TO_HUMAN": 0
}

for r in results:
    summary[r["Decision"]] += 1

print("\n" + "=" * 45)
print("SUMMARY")
print("=" * 45)
for key, value in summary.items():
    print(f"{key}: {value}")

print(f"\nResults saved to: {csv_file}")
input("\nPress Enter to exit...")