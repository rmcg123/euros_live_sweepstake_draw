"""
Function for carrying out the draw and sending messages to a whatsapp group.
"""
import numpy as np
import pywhatkit


def make_euros_draw(
    pot_1_teams,
    pot_2_teams,
    entrants,
    whatsapp_group_id,
    print_locally
):
    """Function to carry out the draw."""

    message = "Beginning allocating pot 2 teams: "
    for country in pot_2_teams:
        message += f":{country}\t "
    if print_locally:
        print(message)
    else:
        message_whatsapp_group(
            group_id=whatsapp_group_id,
            message=message
        )
    final_allocations = {k: [] for k in entrants}
    pot_2_people_to_pick = entrants.copy()
    for team in pot_2_teams[::-1]:
        message = f":{team}\t {team}"
        if print_locally:
            print(message)
        else:
            message_whatsapp_group(
                group_id=whatsapp_group_id,
                message=message
            )
        pick = np.random.choice(a=pot_2_people_to_pick)
        pot_2_people_to_pick.remove(pick)
        if len(pot_2_people_to_pick) == 0:
            pot_2_people_to_pick = entrants.copy()

        message = f":{team}\t has been drawn to {pick}"
        if print_locally:
            print(message)
        else:
            message_whatsapp_group(
                group_id=whatsapp_group_id,
                message=message
            )
        final_allocations[pick].append(team)

    message = "Beginning allocating pot 1 teams: "
    for country in pot_1_teams:
        message += f":{country}\t "
    if print_locally:
        print(message)
    else:
        message_whatsapp_group(
            group_id=whatsapp_group_id,
            message=message
        )

    pot_1_people_to_pick = entrants.copy()
    for team in pot_1_teams[::-1]:
        message = f":{team}\t {team}"
        if print_locally:
            print(message)
        else:
            message_whatsapp_group(
                group_id=whatsapp_group_id,
                message=message
            )

        pick = np.random.choice(a=pot_1_people_to_pick)
        pot_1_people_to_pick.remove(pick)
        message = f":{team}\t has been drawn to {pick}"
        if print_locally:
            print(message)
        else:
            message_whatsapp_group(
                group_id=whatsapp_group_id,
                message=message
            )
        final_allocations[pick].append(team)

    return final_allocations


def message_whatsapp_group(group_id, message):
    """Function to send whatsapp message to group."""

    pywhatkit.sendwhatmsg_to_group_instantly(
        group_id=group_id,
        message=message,
        tab_close=True,
        wait_time=10,
        close_time=5
    )

