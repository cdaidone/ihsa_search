def list_schools(source):
    locations = []
    for row in source:
        location = row["State"]
        locations.append(location)
    return sorted(locations)
