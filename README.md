# Email Auto-Reply Agent

**Author:** Wajahat Irfan, BS Computer Science student (7th semester), GPGC No. 1 Abbottabad

## What it does
Drafts email replies automatically using simple keyword rules and templates.
It reads an email's subject and body, classifies the intent — job application,
meeting request, support question, thank you, or other — picks a matching
template, fills in the sender's name and subject, and prints a draft reply.

> **Demo mode only — no email is ever sent.** This agent does not connect to
> any mail server and needs no API key. It only prints draft text.

## How to run
```bash
cd email-auto-reply-agent
python agent.py --demo
python agent.py --subject "Meeting request" --body "Can we meet on Friday?" --sender "Ali"
python agent.py --file email.txt
```
For `--file`, the first line of the file is the subject and the rest is the body.

## Example output
```
[DEMO MODE] No email is sent by this agent. It only drafts a reply.

============================================================
From:     Bilal
Subject:  Meeting request for Friday
Body:     Hi, can we schedule a meeting on Friday to discuss the project?
------------------------------------------------------------
Detected intent: meeting request

DRAFT REPLY:
Hi Bilal,

Thank you for reaching out. I would be happy to meet. Please let me know two or
three time slots that work for you, and I will confirm one of them.

Best regards,
Wajahat

[DEMO MODE] No email is sent by this agent. It only drafts a reply.
```

## Skills shown
- Python, `argparse` CLI design
- Keyword-based text classification (intent detection)
- Template-based text generation
- Reading input from CLI arguments and files
