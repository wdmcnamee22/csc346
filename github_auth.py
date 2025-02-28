import requests
import passwords

user_url = "https://api.github.com/user"
user_response = requests.get(user_url, auth=(passwords.USERNAME, passwords.PASSWORD))

if user_response.status_code == 200:
    print("User Info:", user_response.json())
else:
    print("Failed to fetch user info:", user_response.status_code, user_response.text)

repo_url = "https://api.github.com/user/repos"
repo_response = requests.get(repo_url, auth=(passwords.USERNAME, passwords.PASSWORD))

if repo_response.status_code == 200:
    repos = repo_response.json()
    print("\nGitHub Repositories:")
    for repo in repos:
        print(f"- {repo['name']} (URL: {repo['html_url']})")
else:
    print("Failed to retrieve repositories:", repo_response.status_code, repo_response.text)
