"""Generate an incident-response checklist for an incident type.

Usage: python3 main.py --type malware
Known types: malware, outage, data-loss, phishing, unauthorized-access.
Unknown types get a generic checklist, honestly labelled as generic.
Prints a Markdown checklist.
"""
import argparse, sys

CHECKLISTS = {
    "malware": ["Isolate the affected host from the network",
                "Preserve logs and a disk image before cleaning",
                "Identify the infection vector and scope",
                "Remove the malware and verify with a second scan",
                "Reset credentials used on the affected host",
                "Monitor the host for 7 days after return to service"],
    "outage": ["Confirm scope: which users and services are affected",
               "Check the status page and recent changes",
               "Escalate to the service owner if unresolved in 30 minutes",
               "Post user communication with a next-update time",
               "Verify recovery with a user-level test before closing"],
    "data-loss": ["Stop writes to the affected storage immediately",
                  "Identify the last known-good backup",
                  "Restore to an isolated location and verify integrity",
                  "Document what was lost and what was recovered"],
    "phishing": ["Preserve the message headers and links",
                 "Check whether anyone clicked or entered credentials",
                 "Reset credentials for affected accounts",
                 "Block the sender domain and reported URLs",
                 "Warn the wider team with the message details"],
    "unauthorized-access": ["Disable the compromised account immediately",
                            "Review login history for the account",
                            "Check for new accounts, rules or forwarding",
                            "Reset credentials and review active sessions"],
}
GENERIC = ["Record the incident time, reporter and symptoms",
           "Assess scope and business impact",
           "Contain the issue before attempting a fix",
           "Document every action with timestamps",
           "Verify recovery before closing the incident"]


def checklist(incident_type):
    key = incident_type.strip().lower()
    if key in CHECKLISTS:
        return CHECKLISTS[key], False
    return GENERIC, True


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--type", required=True)
    args = parser.parse_args(argv)
    steps, generic = checklist(args.type)
    print(f"# Incident response: {args.type}")
    if generic:
        print("(generic checklist — no specific playbook for this type)")
    for step in steps:
        print(f"- [ ] {step}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
