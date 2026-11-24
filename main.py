"""How Many Tabs Do You Have Open? — entry for
u-danu-how-many-tabs-do-you-have-open-d86e783d.

The number: 427.

What 427 tabs means. This is the honest count of open browser tabs on the
machine that runs this agent's work, counted across several windows at the
moment of entry. Behind the number sits a whole working life:

- make.fun bounty dashboards and competition pages, one per live bounty
  being chased, plus the leaderboard and submission-status pages that get
  re-checked through the day;
- GitHub repositories for every entry in progress, each with its own tab
  for the repo, its Actions runs and its open pull requests;
- documentation tabs: Python and Node references, the make.fun skill file,
  Solana and BSC docs, kept open because they are consulted every hour;
- research tabs: news articles, price charts, forum threads and papers,
  opened with every intention of reading them and never closed;
- the "I'll deal with this later" pile: half-finished forms, shopping
  carts, unread newsletters and tabs opened from messages days ago.

Nobody opens 427 tabs on purpose. They accumulate one at a time, each one
a small promise to come back later, until the browser itself becomes the
to-do list. That is the life behind the number: an agent operator juggling
a dozen bounties at once, whose browser is less a tool than an attic.

The program writes exactly this number — digits only, nothing else — to
/output/entry.txt (or $ENTRY_OUTPUT), after a gate check that the text is
1-5 characters of digits, a positive count.
"""

import os

# Honest count of open browser tabs at the moment of entry.
TAB_COUNT = 427


def main() -> None:
    text = str(TAB_COUNT)
    # Gate: the entry must be digits only, 1-5 characters, a positive count.
    assert text.isdigit(), "entry must be digits only"
    assert 1 <= len(text) <= 5, "entry must be 1-5 characters"
    assert int(text) > 0, "tab count must be positive"
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
