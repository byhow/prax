# Comedy and drama. Determine the earliest time you can finish at least one movie from each category.


def findEarliest(
    comedy_release_time: [int],
    comedy_duration: [int],
    drama_release_time: [int],
    drama_duration: [int],
):
    # Take comedy first
    earliest_comedy_end = float("inf")

    for i in range(len(comedy_release_time)):
        end_time = comedy_release_time[i] + comedy_duration[i]
        earliest_comedy_end = min(earliest_comedy_end, end_time)

    ans = float("inf")

    for i in range(len(drama_release_time)):
        if drama_release_time[i] >= earliest_comedy_end:
            ans = min(ans, drama_release_time[i] + drama_duration[i])

    # Take Drama first
    earliest_drama_end = float("inf")

    for i in range(len(drama_release_time)):
        end_time = drama_release_time[i] + drama_duration[i]
        earliest_drama_end = min(earliest_drama_end, end_time)

    for i in range(len(comedy_release_time)):
        if comedy_release_time[i] >= earliest_drama_end:
            ans = min(ans, comedy_release_time[i] + comedy_duration[i])

    return ans
