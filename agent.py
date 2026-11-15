#!/usr/bin/env python3
"""
email-auto-reply-agent -- draft email replies from templates + simple rules.

DEMO MODE ONLY: this script only prints draft replies. It never sends email,
never connects to any mail server, and needs no API key.

Usage:
    python agent.py --demo
    python agent.py --subject "Meeting request" --body "Can we meet on Friday?"
    python agent.py --subject "Hello" --body "..." --sender "Ali"
    python agent.py --file email.txt        # first line = subject, rest = body
"""

import argparse
import sys

DEMO_NOTICE = "[DEMO MODE] No email is sent by this agent. It only drafts a reply."

# intent -> keywords
INTENTS = {
    "job application": ["apply", "application", "job", "vacancy", "position", "resume", "cv", "hiring"],
    "meeting request": ["meet", "meeting", "call", "schedule", "appointment", "zoom", "available"],
    "support question": ["help", "problem", "issue", "error", "not working", "broken", "support", "question"],
    "thank you": ["thank", "thanks", "appreciate", "grateful"],
}

TEMPLATES = {
    "job application": (
        "Hi {sender},\n\n"
        "Thank you for your interest in the position and for sending your application. "
        "We have received it and will review it carefully. If your profile matches what "
        "we are looking for, we will contact you for the next step within a week.\n\n"
        "Best regards,\nWajahat"
    ),
    "meeting request": (
        "Hi {sender},\n\n"
        "Thank you for reaching out. I would be happy to meet. Please let me know two or "
        "three time slots that work for you, and I will confirm one of them.\n\n"
        "Best regards,\nWajahat"
    ),
    "support question": (
        "Hi {sender},\n\n"
        "Thank you for letting us know about the issue. I am sorry for the trouble. "
        "Could you please share a screenshot and the exact steps that led to the problem? "
        "I will look into it and get back to you as soon as possible.\n\n"
        "Best regards,\nWajahat"
    ),
    "thank you": (
        "Hi {sender},\n\n"
        "Thank you for your kind message! I really appreciate it. Please let me know if "
        "there is anything else I can help with.\n\n"
        "Best regards,\nWajahat"
    ),
    "other": (
        "Hi {sender},\n\n"
        "Thank you for your email about \"{subject}\". I have received it and will "
        "reply in detail soon.\n\n"
        "Best regards,\nWajahat"
    ),
}

DEMO_EMAILS = [
    ("Application for AI Intern position",
     "Hello, I am writing to apply for the AI intern position. Please find my resume attached.",
     "Ayesha"),
    ("Meeting request for Friday",
     "Hi, can we schedule a meeting on Friday to discuss the project?",
     "Bilal"),
    ("Problem with my order",
     "Hello, my order is not working as expected and I need help with this issue.",
     "Sara"),
]


def classify_intent(subject, body):
    """Classify intent by keyword matching on subject + body."""
    text = (subject + " " + body).lower()
    best_intent, best_score = "other", 0
    for intent, keywords in INTENTS.items():
        score = sum(1 for kw in keywords if kw in text)
        if score > best_score:
            best_intent, best_score = intent, score
    return best_intent


def draft_reply(subject, body, sender="there"):
    """Return (intent, draft reply text)."""
    intent = classify_intent(subject, body)
    template = TEMPLATES[intent]
    reply = template.format(sender=sender, subject=subject)
    return intent, reply


def show_email(subject, body, sender):
    intent, reply = draft_reply(subject, body, sender)
    print("=" * 60)
    print("From:    ", sender)
    print("Subject: ", subject)
    print("Body:    ", body)
    print("-" * 60)
    print("Detected intent:", intent)
    print()
    print("DRAFT REPLY:")
    print(reply)
    print()
    print(DEMO_NOTICE)


def main():
    parser = argparse.ArgumentParser(description="Draft email replies (demo mode, nothing is sent).")
    parser.add_argument("--demo", action="store_true", help="Run 3 built-in sample emails.")
    parser.add_argument("--subject", default="", help="Email subject.")
    parser.add_argument("--body", default="", help="Email body.")
    parser.add_argument("--sender", default="there", help="Sender name used in the reply.")
    parser.add_argument("--file", help="Text file: first line is the subject, rest is the body.")
    args = parser.parse_args()

    print(DEMO_NOTICE)
    print()

    if args.demo:
        for subject, body, sender in DEMO_EMAILS:
            show_email(subject, body, sender)
        return 0

    subject, body = args.subject, args.body
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            lines = f.read().splitlines()
        if not lines:
            print("Error: file is empty.", file=sys.stderr)
            return 1
        subject = lines[0]
        body = "\n".join(lines[1:]).strip()

    if not subject and not body:
        parser.print_help()
        print("\nTip: try: python agent.py --demo")
        return 0

    show_email(subject, body, args.sender)
    return 0


if __name__ == "__main__":
    sys.exit(main())
