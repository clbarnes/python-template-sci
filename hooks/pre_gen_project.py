import re
import sys
import logging
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

module_re = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

if not re.fullmatch(module_re, "{{ cookiecutter.package_name }}"):
    logger.error("{{ cookiecutter.package_name }} is not a valid Python module name")

    # exits with status 1 to indicate failure
    sys.exit(1)


email_re = r"""
(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
""".strip()

if not re.fullmatch(email_re, "{{ cookiecutter.email }}"):
    logger.error("{{ cookiecutter.email }} is not a valid email address")
    sys.exit(1)

path_re = r".+\..+"

result = urlparse("{{ cookiecutter.url }}")
if not result.scheme.startswith("http") or not re.fullmatch(path_re, result.netloc):
    logger.error("{{ cookiecutter.url }} is not a valid HTTP(S) URL")
    sys.exit(1)
