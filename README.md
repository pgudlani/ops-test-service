# ops-test-service
A small, intentionally buggy service repo used to simulate production incidents for the agent to debug. Designed as a safe target for automated fixes and PR creation.

## CLI usage
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 app.py
```

## Arguments
```bash
python3 app.py --team alpha
```

- `--team`: team name used to filter both numerator and denominator (default: `alpha`)
