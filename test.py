import re
import subprocess
import sys

print(sys.argv[1]+"sys.argv[1]")
print(sys.argv[2]+"sys.argv[2]")
# No shell: the image path and style name are passed as separate arguments.
image, style = sys.argv[1], sys.argv[2]
if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", style):
    sys.exit("style must be a model name: letters, digits, - and _")
subprocess.run(
    [sys.executable, "baseline.py", "--input", image, "--output", image,
     "--model", f"models/{style}.pb"],
    check=False,
)
