from typing import Callable, Dict, List, Tuple


def evaluate_platform(
    artist: str,
    platform_function: Callable,
    platform_name: str,
    related_artists: Dict[str, list[str]],
) -> None:
    artists = platform_function(artist)
    if artists:
        related_artists[platform_name] = artists


def compare_artists(data: Dict[str, List[str]]) -> Tuple[Dict[str, int], int]:
    artists_ranked = {}
    platform_count = 0
    for platform in data:
        if data[platform]:
            platform_count += 1
    for platform in data:
        for artist in data[platform]:
            if artist not in artists_ranked:
                artists_ranked[artist] = 1
            else:
                artists_ranked[artist] += 1
    return (artists_ranked, platform_count)


def sort_artists_by_rank(artists: Dict[str, int]) -> dict:
    return dict(sorted(artists.items(), key=lambda x: x[1], reverse=True))
