# clara-automation-pipeline

## Overview
A Python automation pipeline for processing call data and generating agent specs.

## Project Structure
```
scripts/
  pipeline.py       - Main pipeline orchestration
  extractor.py      - Data extraction logic
  agent_generator.py - Agent spec generation
  patcher.py        - Patch/update logic
data/
  demo_calls/       - Sample demo call transcripts
  onboarding_calls/ - Sample onboarding call transcripts
outputs/
  accounts/         - Per-account output files (agent_spec.json, memo.json, changes.md)
main.py             - Entry point
requirements.txt    - Python dependencies
```

## Running
```bash
python main.py
```

## Dependencies
- Python 3.12
- pandas
