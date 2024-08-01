# this uses the USA date format

def sort_dates(dates):
    return sorted(dates, key=formatted_dates)


def formatted_dates(dates):
    parts = dates.split('-')
    return f"{parts[2]}-{parts[0]}-{parts[1]}"