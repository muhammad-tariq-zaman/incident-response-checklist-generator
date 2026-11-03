# incident-response-checklist-generator

Print a Markdown incident-response checklist for a given incident type, with a clearly labelled generic fallback for unknown types.

## How to run

```sh
python3 main.py --type malware
```

## Example output

```
# Incident response: malware
- [ ] Isolate the affected host from the network
- [ ] Preserve logs and a disk image before cleaning
```

Standard library only. Run the tests with `python3 -m unittest discover`.
