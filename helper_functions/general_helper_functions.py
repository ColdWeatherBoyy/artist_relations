from typing import Callable, Dict, List, Tuple
from collections import defaultdict


def evaluate_platform(
    artist: str,
    platform_function: Callable,
    platform_name: str,
    related_artists: Dict[str, list[str]],
) -> None:
    artists = platform_function(artist)
    if artists:
        related_artists[platform_name] = artists


def compare_and_sort_artists(
    data: Dict[str, List[str]]
) -> Tuple[Dict[str, int], List[str]]:
    artists_ranked = defaultdict(lambda: 0)
    platforms = []
    for platform in data:
        if data[platform]:
            platforms.append(platform)
        for artist in data[platform]:
            artists_ranked[artist] += 1
    artists_sorted = dict(
        sorted(artists_ranked.items(), key=lambda x: x[1], reverse=True)
    )
    return (artists_sorted, platforms)