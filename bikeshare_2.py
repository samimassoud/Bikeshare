import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago','new york city', 'washington']
    months = ['all','january','february','march','april','may','june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    time_filters = ['month', 'day', 'both', 'none']
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        if city in cities:
            break
        else:
            print("Invalid input. Please choose one of the current options: Chicago, New York City, or Washington.")
    while True:
        time_filter = input ("Would you like to filter the data by month, day, both, or not at all? Type \"none\" for no time filter.").lower()
        if time_filter in time_filters:
            break
        else:
            print("Please choose one of the available time filter's options")
    if(time_filter=="both"):
        # get user input for month (all, january, february, ... , june)
        while True:
            month = input("Which month? January, February, March, April, May, June or All?").lower()
            if month in months:
                break
            else:
                print("Invalid input. Please choose one of the available month's options")

        # get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All?").lower()
            if day in days:
                break
            else:
                print("Invalid input. Please choose one of the available day's options.")
    elif(time_filter=="month"):
        day="all"
        while True:
            month = input("Which month? January, February, March, April, May, June or All?").lower()
            if month in months:
                break
            else:
                print("Invalid input. Please choose one of the available month's options")
    elif(time_filter=="day"):
        month="all"
        while True:
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All?").lower()
            if day in days:
                break
            else:
                print("Invalid input. Please choose one of the available day's options.")
    else:
        #none
        day="all"
        month="all"

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Firstly, load data for chosen city
    df = pd.read_csv(CITY_DATA[city])

    #Then we convert the Start Time column to datetime like in the practice problem
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract Month and day and hour as columns from the Start Time column
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
