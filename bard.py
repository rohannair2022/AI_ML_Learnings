"""
A BARD DAY'S NIGHT
a.k.a. BARD ROCK CAFE
a.k.a. THE SCHOOL OF BARD KNOCKS
a.k.a. A BARD RAIN'S A-GONNA FALL
"""

# Imports

from typing import Optional, TextIO, Set  # Specific annotations

from math import ceil  # For stats

# Constants

# Minimum number of songs for a villager to be promoted to a bard
BARD_THRESHOLD = 10

# Number of songs for the billboard_top statistic
BILLBOARD_N = 10

# DO NOT use these as variables in your code;
# they are only for type contracts.

# Maps from {name: songs that this villager knows}
villagers_type = dict[str, set[str]]

bards_type = set[str]

# Maps from {song name: names of people, including bards, that know this song}
songs_type = dict[str, set[str]]

# A list of parties; each party is a set of the attendee names
parties_type = list[set[str]]

villagers = {}
songs = {}
bards = set()
parties = []
bards_string = ""


def read_input(f: TextIO, ) -> tuple[villagers_type, bards_type, songs_type, parties_type]:
    """
    Read the given file and return the villagers, bards, songs, and parties.

    f is an open file containing VILLAGERS and bards, SONGS, and PARTIES,
    in that order. One villager or bard per line;
    one song per line; one party per line, consisting of attendees
    separated by commas. The parties are given in the order they're held.

    """

    n = f.readline().strip()
    i = 0
    while i < 1:
        if "VILLAGERS" in n:
            bard_list = []
            while n.strip():
                n = f.readline().strip()
                if "*" in n:
                    bards.add(n.replace("*", ""))
                elif "*" not in n:
                    villagers[n] = set()
            del villagers[""]

        n = f.readline().strip()
        if "SONGS" in n:
            while n.strip():
                n = f.readline().strip()
                songs[n] = bards
            del songs[""]


        n = f.readline().strip()
        if "PARTIES" in n:
            while n.strip():
                n = f.readline().strip()
                n_list = n.split(",")
                n_set = set(n_list)
                parties.append(n_set)
            parties.pop()

        i = i + 1

    result = (villagers, bards, songs, parties)

    return result


# Party functions
# We highly recommend adding helper functions here!

def sing_at_party(
        villagers: villagers_type, bards: bards_type, songs: songs_type, party: set[str]
) -> None:
    """
    A bard sings if present, otherwise the villagers sing.
    """
    if bool(bards | party):
        party_song_set = set()
        a = party - bards
        for i in a:
            for j in villagers[i]:
                party_song_set.add(j)
        final_set_new = set(songs.keys()) - party_song_set
        final_set_old = sorted(final_set_new)
        l = list(villagers.keys())
        for i in l:
            if i in a:
                villagers[i].add(final_set_old[0])
                songs[final_set_old[0]].add(i)
    else:
        common_set = set()
        for c in villagers:
            for j in villagers[c]:
                common_set.add(j)
        for v in villagers:
            villagers[v] = villagers[v] | common_set
        for s in songs:
            if songs[s] in common_set:
                songs[s] = songs[s] | party


def update_bards_after_party(
        villagers: villagers_type, bards: bards_type, songs: songs_type, party: set[str]
) -> None:
    """
    Promote attendees who have learned enough songs to bards,
    iff there is another bard present at the party.
    """
    if bool(bards & party):
        temp = party - bards
        for j in temp:
            if len(villagers.get(j)) >= BARD_THRESHOLD:
                bards.add(j)
                del villagers[j]

# Stats functions

def unheard_songs(
        villagers: villagers_type,
        bards: bards_type,
        songs: songs_type,
        parties: parties_type,
) -> set[str]:
    """
    Return a set of songs that have never been heard by non-bards.
    (This means that only the bards know it.)
    """
    list1 = []
    for i in villagers.values():
        for j in i:
            list1.append(j.strip())

    songs_set = set(list1)

    final_set = set(songs.keys()) - songs_set

    return final_set


def billboard_top(
        villagers: villagers_type,
        bards: bards_type,
        songs: songs_type,
        parties: parties_type,
) -> list[str]:
    """
    Return a list of the BILLBOARD_N most popular songs by number of people
    who know them, in descending order. Break ties alphabetically.
    """
    final_list = []
    list2 = []
    for i in songs:
        list2.append(str(len(songs[i])*-1) + " " + i)
    list2.sort()
    for i in range(len(list2)):
        a = list2[i].split(" ")
        a.pop(0)
        list2[i] = " ".join(a)

    if len(list2) >= BILLBOARD_N:
        for i in range(BILLBOARD_N):
            final_list.append(list2[i])

    else:
        final_list = list2

    return final_list


def all_bards(
        villagers: villagers_type,
        bards: bards_type,
        songs: songs_type,
        parties: parties_type,
) -> set[str]:
    """Return the set of the village's bards."""
    for i in parties:
        update_bards_after_party(villagers, bards, songs, i)
    return bards


def average_attendees(
        villagers: villagers_type,
        bards: bards_type,
        songs: songs_type,
        parties: parties_type,
) -> int:
    """
    Return the average number of attendees at parties in the village.
    Round up to the nearest integer.
    """
    list12 = []
    for i in parties:
        count = 0
        count = len(i)
        list12.append(count)

    sum = 0
    for i in list12:
        sum = sum + int(i)

    if (sum % len(list12)) > 0:
        return sum // len(list12) + 1
    else:
        return sum // len(list12)


# Main  process

def run(filename: str) -> dict[str, object]:
    """
    Run the program: read the input, host the parties,
    and return a dictionary of resulting statistics keyed by name:
    unheard_songs, billboard_top, all_bards, average_attendees

    filename is the name of an input file.
    """

    file = open('%s' % filename, 'r')
    read_input(file)

    for i in parties:
        sing_at_party(villagers, bards, songs, i)

    return {"unheard_songs": unheard_songs(villagers, bards, songs, parties),
            "billboard_top": billboard_top(villagers, bards, songs, parties),
            "all_bards": all_bards(villagers, bards, songs, parties),
            "average_attendees": average_attendees(villagers, bards, songs, parties)}


if __name__ == "__main__":

    # Sample input from the handout -- you can tweak this if you like
    stats_handout = run("handout_example.txt")
    print("Results of handout sample input")
    for key, value in stats_handout.items():
        print(f"{key}: {value}")


    # Sample bigger input -- you can tweak this if you like
    #stats_bigger = run("bigger_example.txt")
    #print("Results of bigger sample input")
    #for key, value in stats_bigger.items():
        #print(f"{key}: {value}")
