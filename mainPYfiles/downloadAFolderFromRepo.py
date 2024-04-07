import subprocess
import os

try:
    os.system("cls")
    def download_github_folder(repo_url, folder_path, local_path):
        # Ensure the local directory exists
        if not os.path.exists(local_path):
            os.makedirs(local_path)

        svn_url = repo_url.replace('github.com', 'github.com/svn/trunk') + '/' + folder_path
        subprocess.run(['svn', 'export', svn_url, local_path], shell=True)



    repo_url = 'https://github.com/bernso/PotentialViruses'     # Replace with the actual repository URL
    folder_path = 'mainPYfiles'     # Replace with the actual folder name
    local_path = 'Required_Files'   # Replace with your desired local path
    download_github_folder(repo_url, folder_path, local_path)

    print(f"Folder '{folder_path}' has been downloaded to '{local_path}'.")
except Exception as e:
    print(f"Failed to download files.\nError: {e}")