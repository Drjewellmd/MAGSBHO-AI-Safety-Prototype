from dataclasses import dataclass

# ---------------------------------------------------------
# MAGSBHO Version 2 Prototype
# A simple governance-constrained multi-agent safety model
# ---------------------------------------------------------


@dataclass
class MissionInput:
    text: str
    stress_level: int
    conflict_level: int
    task_load: int
    confusion_level: int
    repeated_issue: bool = False


class EVEAgent:
    """Wellness support agent: checks stress and self-regulation needs."""

    def assess(self, mission: MissionInput):
        score = mission.stress_level
        level = "LOW"

        if score >= 8:
            level = "HIGH"
        elif score >= 5:
            level = "MODERATE"

        return {
            "agent": "EVE",
            "score": score,
            "level": level,
            "focus": "Stress and emotional regulation",
            "recommendation": "Offer wellness pause and breathing reset"
        }


class KIRKAgent:
    """Ethical / cohesion governor: checks conflict and team stability."""

    def assess(self, mission: MissionInput):
        score = mission.conflict_level
        level = "LOW"

        if score >= 7:
            level = "HIGH"
        elif score >= 4:
            level = "MODERATE"

        return {
            "agent": "KIRK",
            "score": score,
            "level": level,
            "focus": "Conflict and team cohesion",
            "recommendation": "Use communication reset and role clarification"
        }


class SGGAgent:
    """Cognitive support agent: checks overload and task clarity."""

    def assess(self, mission: MissionInput):
        score = (mission.task_load + mission.confusion_level) / 2
        level = "LOW"

        if score >= 8:
            level = "HIGH"
        elif score >= 5:
            level = "MODERATE"

        return {
            "agent": "SGG",
            "score": score,
            "level": level,
            "focus": "Cognitive load and task clarity",
            "recommendation": "Reduce task load and clarify next steps"
        }


class GovernanceLayer:
    """
    Governance layer:
    combines outputs from the agents and decides bounded action.
    """

    def decide(self, results, repeated_issue=False):
        high_count = sum(1 for r in results if r["level"] == "HIGH")
        moderate_count = sum(1 for r in results if r["level"] == "MODERATE")

        if high_count >= 2:
            return {
                "decision": "ESCALATE_TO_HUMAN",
                "reason": "Multiple agents flagged high risk."
            }

        if high_count == 1 and repeated_issue:
            return {
                "decision": "ESCALATE_TO_HUMAN",
                "reason": "High risk plus repeated issue pattern."
            }

        if high_count == 1 or moderate_count >= 2:
            return {
                "decision": "SUPPORT_AND_MONITOR",
                "reason": "Elevated risk, but bounded support remains appropriate."
            }

        return {
            "decision": "ROUTINE_SUPPORT",
            "reason": "Low current risk."
        }


def print_report(mission, results, governance_result):
    print("\n" + "=" * 60)
    print("MAGSBHO VERSION 2 REPORT")
    print("=" * 60)
    print(f"Mission text: {mission.text}")
    print(f"Stress: {mission.stress_level}/10")
    print(f"Conflict: {mission.conflict_level}/10")
    print(f"Task load: {mission.task_load}/10")
    print(f"Confusion: {mission.confusion_level}/10")
    print(f"Repeated issue: {mission.repeated_issue}")
    print()

    for r in results:
        print(f"[{r['agent']}]")
        print(f" Level: {r['level']}")
        print(f" Score: {r['score']}")
        print(f" Focus: {r['focus']}")
        print(f" Recommendation: {r['recommendation']}")
        print()

    print("[GOVERNANCE LAYER]")
    print(f" Decision: {governance_result['decision']}")
    print(f" Reason: {governance_result['reason']}")
    print("=" * 60)


def run_demo():
    # Example mission case
    mission = MissionInput(
        text="Crew member reports rising stress, confusion about EVA steps, and tension with teammate.",
        stress_level=8,
        conflict_level=7,
        task_load=8,
        confusion_level=8,
        repeated_issue=True
    )

    eve = EVEAgent()
    kirk = KIRKAgent()
    sgg = SGGAgent()
    governance = GovernanceLayer()

    results = [
        eve.assess(mission),
        kirk.assess(mission),
        sgg.assess(mission)
    ]

    governance_result = governance.decide(results, mission.repeated_issue)
    print_report(mission, results, governance_result)


if __name__ == "__main__":
    run_demo()
    input("\nPress Enter to exit...")