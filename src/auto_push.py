import subprocess
import sys


def git_add_commit_push(commit_message):
    try:
        # Step 1: Add all changes
        subprocess.run(["git", "add", "."], check=True)
        print("✅ Changes staged.")

        # Step 2: Commit with message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"✅ Commit created: '{commit_message}'")

        # Step 3: Push to remote
        push_result = subprocess.run(["git", "push"], capture_output=True, text=True)

        if push_result.returncode != 0:
            print("❌ Push rejected:", push_result.stderr)
            print("Possible causes:")
            print("- Remote has new commits (try 'git pull' first)")
            print("- No permissions to push")
            sys.exit(1)
        else:
            print("✅ Push successful!")
            print(push_result.stdout)

    except subprocess.CalledProcessError as e:
        print("❌ Error:", e.stderr if e.stderr else e.stdout)
        sys.exit(1)
