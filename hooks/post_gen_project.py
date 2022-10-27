#!/usr/bin/env python3
import subprocess as sp
import logging
logger = logging.getLogger("POST_CREATION")

try:
    sp.run(["git", "init"], check=True)
    sp.run(["git", "add", "."], check=True)

    msg = """
    Initial commit

    Created repository from template.
    """.lstrip()

    sp.run(["git", "commit", "-m", msg], check=True)
except sp.CalledProcessError as e:
    logger.exception(
        "Created project successfully, but failed to call git commands;"
        " manage your own version control"
    )
