import json
from main import run_pipeline   # we’ll create this
from storage import save_to_history, view_history, compare_audits
def main():
    while True:
        print("\n=== AI Audit Assistant ===")
        print("1. Run new audit")
        print("2. View history")
        print("3. Compare audits")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            file_path = input("Enter path to audit JSON: ")
            result = run_pipeline(file_path)
            display_results(result)
            save_to_history(result)

        elif choice == "2":
            view_history()

        elif choice == "3":
            compare_audits()

        elif choice == "4":
            break

        else:
            print("Invalid choice")

def display_results(results):
    print("\n=== Optimization Recommendations ===\n")

    for i, item in enumerate(results, 1):
        print(f"{i}. {item['title']}")
        print(f"   Why: {item['why']}")
        print(f"   Impact: {item['impact']}")
        print(f"   Complexity: {item['complexity']}")
        print(f"   Notes: {item['notes']}")
        print(f"   Priority Score: {item['priority_score']}")
        print("-" * 50)

if __name__ == "__main__":
    main()