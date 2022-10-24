import subprocess as sp

sp.run(["git", "init"], check=True)
sp.run(["git", "add", "."], check=True)

msg = """
Initial commit

Created repository from template.
""".lstrip()

sp.run(["git", "commit", "-m", msg])
