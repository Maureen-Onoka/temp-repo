from python_helpers.repo_utils import clone_repo

# URL of the repo to clone
url = "https://github.com/Maureen-Onoka/GenAI.git"

# Clone the repo
repo_dir = clone_repo(url)

# Print the path
print("Cloned repo directory:", repo_dir)
