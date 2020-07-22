"""This solves problem 5 from:
https://moodlex.warwick.ac.uk/pluginfile.php/5115/mod_resource/content/6/assessment2.pdf"""


import math


def orbit(nearest_distance, nearest_velocity):
    G = 6.67 * 10 ** -11  # Gravitational Constant
    M = 1.9891 * 10 ** 30  # Mass of the Sun
    # furthest_velocity is the speed at the most distant point of the orbit
    furthest_velocity = (
        2 * G * M / (nearest_velocity * nearest_distance)
        - math.sqrt(
            (2 * G * M / (nearest_velocity * nearest_distance)) ** 2
            + 4 * (nearest_velocity ** 2 - 2 * G * M / nearest_distance)
        )
    ) / 2
    if furthest_velocity < 0:
        furthest_velocity = (
            2 * G * M / (nearest_velocity * nearest_distance)
            + math.sqrt(
                (2 * G * M / (nearest_velocity * nearest_distance)) ** 2
                + 4 * (nearest_velocity ** 2 - 2 * G * M / nearest_distance)
            )
        ) / 2
    l_2 = nearest_distance * nearest_velocity / furthest_velocity
    ellipse_semi_major_axis = (nearest_distance + l_2) / 2
    semi_minor_axis = math.sqrt(nearest_distance * l_2)
    orbital_period = (2 * math.pi * ellipse_semi_major_axis * semi_minor_axis) / (nearest_distance * nearest_velocity)
    orbital_eccentricity = (l_2 - nearest_distance) / (l_2 + nearest_distance)
    return (
        ellipse_semi_major_axis,
        semi_minor_axis,
        orbital_period,
        orbital_eccentricity,
    )


# this should print (149651713244.47736, 149629957015.71677, 31579931.406081423, 0.017051012575504464)
print(orbit(1.471 * 10 ** 11, 3.0287 * 10 ** 4))
