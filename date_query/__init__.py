def main():
    """ Entry point """
    
    parser = argparse.ArgumentParser(
        description='Get the first specified day in each month of the year',
        epilog='example: ./getFirstWeekdays.py 2017 1')
    parser.add_argument(
        'year',
        type=int,
        help='The year to search, e.g. 2017')
    parser.add_argument(
        'day',
        type=int,
        help='A number between 0 and 6 which represents Monday-Sunday')

    args = parser.parse_args()
    year = args.year
    day_of_the_week = args.day

    if day_of_the_week < 0 or day_of_the_week > 6:
        print("Valid values for day are: 0 to 6")
    elif year < 1:
        print("Year must be great than zero")
    else:
        get_dates(year, day_of_the_week)
