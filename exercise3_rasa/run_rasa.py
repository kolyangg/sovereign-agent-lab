"""Launch Rasa with local startup tweaks for this assignment."""

from __future__ import annotations

import sys

import litellm
import rasa.__main__


# LiteLLM can print a red "Provider List" banner from internal model/provider
# lookup paths even when the actual Nebius request succeeds. Suppress that
# banner so `rasa shell` transcripts stay readable for the homework.
litellm.suppress_debug_info = True


def main() -> None:
    rasa.__main__.main(sys.argv[1:])


if __name__ == "__main__":
    main()
