import os 
import sys

print(sys.argv[1]+"sys.argv[1]")
print(sys.argv[2]+"sys.argv[2]")
os.system(f"python baseline.py --input {sys.argv[1]} \
  --output {sys.argv[1]} \
  --model models/{sys.argv[2]}.pb")
