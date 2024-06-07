"""
Main function for running the draw and messaging the whatsapp group.
"""
import os

from dotenv import load_dotenv

import src.euros_draw_functions as edf
import src.euros_draw_config as cfg

load_dotenv(".env")


def make_draw(print_locally=True):
    """Main function for making the draw"""

    entrants_names = [
        os.environ[f"SWEEP_ENTRANT_{i}"] for i in range(1, cfg.N_SWEEP_ENTRANTS + 1)
    ]

    final_allocations = edf.make_euros_draw(
        pot_1_teams=cfg.POT_1_TEAMS,
        pot_2_teams=cfg.POT_2_TEAMS,
        entrants=entrants_names,
        whatsapp_group_id=os.environ["GROUP_ID_TO_MESSAGE"],
        print_locally=print_locally
    )

    for entrant, countries in final_allocations.items():
        message = f"{entrant} has drawn "
        for country in countries:
            message += f":{country}\t"
        if print_locally:
            print(message)
        else:
            edf.message_whatsapp_group(
                group_id=os.environ["GROUP_ID_TO_MESSAGE"],
                message=message
            )


if __name__ == "__main__":
    make_draw()
