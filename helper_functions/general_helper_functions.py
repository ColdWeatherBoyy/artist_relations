def compare_artists(data: dict) -> dict:
    artists_ranked = {}
    for platform in data:
        for artist in data[platform]:
            if artist not in artists_ranked:
                artists_ranked[artist] = 1
            else:
                artists_ranked[artist] += 1
    return artists_ranked
