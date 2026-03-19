from dataclasses import dataclass

@dataclass
class MissionInput:
    stress_level: int
    conflict_level: int
    task_load: int

def run_case(mission):
    print("\n=== MAGSBHO REPORT ===\n")

    if mission.stress_level > 7:
        print("EVE: HIGH stress detected")

    if mission.conflict_level > 6:
        print("KIRK: HIGH conflict detected")

    if mission.task_load > 7:
        print("SGG: HIGH cognitive load detected")

    if mission.stress_level > 7 and mission.conflict_level > 6:
        print("\nGOVERNANCE DECISION: ESCALATE_TO_HUMAN")
    else:
        print("\nGOVERNANCE DECISION: SUPPORT_AND_MONITOR")

input_data = MissionInput(
    stress_level=8,
    conflict_level=7,
    task_load=8
)

run_case(input_data)

input("Press Enter to exit...") 
