from typing import Dict, List, Tuple


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


def sort_artists(data: dict) -> list:
    return sorted(data.items(), key=lambda x: x[1], reverse=True)
