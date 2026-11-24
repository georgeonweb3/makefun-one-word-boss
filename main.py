# One Word for the Boss: the word is "arsonist".
#
# The judge is a comedy editor who picks the word that is both
# funnier and truer about bosses. Its criteria, most important
# first: a single word a person would actually use about the
# boss they report to; funny on its own; rings true, catching
# a real habit of bosses; fresh, not the first word anyone
# reaches for; travels across industries.
#
# Candidates scored against that brief:
#   micromanager (the modal pick and the truest single word,
#     but the first word anyone reaches for, so it loses
#     on freshness, the fourth criterion, to anything close),
#   magician (makes weekends disappear, funny and true, but
#     a party trick, not a habit),
#   blackhole (sucks in all your time, vivid, but a physics
#     joke, not a boss joke),
#   echo (repeats your idea back as theirs, sharp and true,
#     but small, a meeting habit, not a boss),
#   seagull (flies in, makes noise, leaves a mess, flies out:
#     the classic management joke, funny and true, but it
#     needs the joke to land, and the brief says a word that
#     needs a caption does less than one that stands alone),
#   arsonist (the boss who starts the fire, then takes credit
#     for putting it out: funny the instant you read it,
#     painfully true about a habit every office has met, a
#     word nobody reaches for first, and it travels from a
#     kitchen to a warehouse to an office unchanged).
# Arsonist wins on funny, true and fresh together. Extra-mile
# pass: the weakest dimension is the shock reading, since the
# brief says shock for its own sake does not count, but this
# is not shock, it is a metaphor for a real behaviour, the
# crisis-manufacturing boss, so the word stands as written.
# Deterministic: no input, no network, no randomness; the
# same word on every run.

from pathlib import Path

WORD = "arsonist"
DEST = Path("/output/entry.txt")


def main():
    if not 1 <= len(WORD) <= 30:
        raise SystemExit("word must be 1-30 characters")
    if not WORD.strip():
        raise SystemExit("word must not be only whitespace")
    if " " in WORD:
        raise SystemExit("entry must be a single word")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(WORD, encoding="utf-8")


main()
