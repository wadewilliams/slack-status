import random


def randomize(length):
    return random.randint(0, length - 1)


def wildcard():
    cards = [
        " on our end",
        " on our side",
    ]

    if randomize(3) == 1:
        return cards[randomize(len(cards))]
    return ""


def intro():
    intro = [
        "There are no changes",
        "No additional news",
        "We don't have any new information",
    ]
    return intro[randomize(len(intro))]


def verbs():
    verbs = [
        "report",
        "share",
    ]
    return verbs[randomize(len(verbs))]


def timing():
    timing = [
        "as of yet",
        "at the moment",
        "at this stage",
    ]
    return timing[randomize(len(timing))]


# but_update =
#
# we're focused on getting things back to normal
#
# *wildcard
#
# as quickly
# as soon
#
# "as possible"
#
# ## (there is still)
# no additional information


def active_verbs():
    active_verbs = [
        "investigating",
        "all hands on deck",
    ]
    return active_verbs[randomize(len(active_verbs))]


def and_update():
    and_update = [
        "there are no changes to report",
        "have upgraded the incident",
        "have nothing new to share",
    ]
    return and_update[randomize(len(and_update))]


def get_update():
    if randomize(2) == 1:
        return f"We'll continue to {actions()}{wildcard()}"
    return f"We are {active_verbs()} and {and_update()}{wildcard()}"


def actions():
    actions = [
        "dig in",
        "investigate",
        "work to resolve this issue",
    ]
    return actions[randomize(len(actions))]


def next_alert_intro():
    next_alert_intro = [
        "follow up",
        "continue to share updates",
        "back in a half hour to keep you posted",
        "follow up",
        "provide another update",
    ]
    return next_alert_intro[randomize(len(next_alert_intro))]


def next_alert_at():
    next_alert_at = [
        "in 30 minutes",
        "with more information as soon as we have it",
        "as soon as we do",
    ]
    return next_alert_at[randomize(len(next_alert_at))]


def wrap_up():
    wrap_up = [
        "We apologize for any disruption caused.",
        "Thanks for bearing with us.",
        "Thank you for your patience.",
    ]
    return wrap_up[randomize(len(wrap_up))]


def main():
    return f"{intro()}{wildcard()} to {verbs()}{wildcard()} {timing()}. {get_update()}. We'll {next_alert_intro()} {next_alert_at()}. {wrap_up()}"
