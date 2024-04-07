import subprocess

subprocess.run(['svn', 'export', svn_url, local_path], shell=True)