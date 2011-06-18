#!/usr/bin/env python3

from ltg_util import gameloop
from ltg_util import enqueue_strategy
from ltg_util import pop_and_print
from ltg_util import get_opponent_move
from ltg_util import apply_card
from ltg_util import apply_slot
from ltg_util import apply_slotX_to_slotY
from ltg_util import build_num_in_slot

def main():
    # Set up address of slot 3, in slot 0.
    build_num_in_slot(3, 0)

    # Set up contents of slot 3.
    build_num_in_slot(50, 3)

    apply_card("put", 5)
    apply_slot(5, "succ")

    # Apply succ, in slot 5, to 50, in slot 3.  Result should be 51.
    apply_slotX_to_slotY(5, 3, yaddr=0)

    gameloop()

if __name__ == "__main__": main()