import subprocess

def run_git_command(command):
    """ Helper function to execute a git command and handle errors. """
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e.stderr)

# 1. Navigate to the repository folder
repo_path = "/root/Chess-vision-Deep-Learning-Final-Project-master"

# 2. Make sure the remote is correct
run_git_command(f"cd {repo_path} && git remote set-url origin https://github.com/RubenAAA/Chess-vision-Deep-Learning-Final-Project.git")

# 3. Add all files (excluding ignored ones)
run_git_command(f"cd {repo_path} && git add .")

# 4. Commit changes
run_git_command(f'cd {repo_path} && git commit -m "Automated push from Python script"')

# 5. Push everything to GitHub
run_git_command(f"cd {repo_path} && git push origin main")  # Change 'main' to 'master' if necessary
