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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_options = ('chicago', 'new york city', 'washington')
    city = input("Please choose a city between Chicago, New York City, or Washington ").lower()
    while city not in city_options:
        city = input("Sorry, that wasn't a valid option. Please enter Chicago, New York City, or Washington. Double check your spelling! ").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month_options = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'all')
    month = input('Please choose a month between January through June or enter All ').lower()
    while month not in month_options:
        month = input("Sorry, that wasn't a valid option. Please enter January, February, March, April, May, June, July, or All. Double check your spelling! ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_options = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')
    day = input('Please choose a day of the week or enter All ').lower()
    while day not in day_options:
        day = input("Sorry, that wasn't a valid option. Please enter Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or All. Double check your spelling! ").lower()

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

        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # first calculate the most popular month, this code returns the number of the month
    month_number = df['month'].mode()[0]
    # convert to the name of the month
    if month_number ==  1:
        popular_month = "January"
    elif month_number == 2:
        popular_month = "February"
    elif month_number == 3:
        popular_month = "March"
    elif month_number == 4:
        popular_month = "April"
    elif month_number == 5:
        popular_month = "May"
    elif month_number == 6:
        popular_month = "June"

    # then display the most popular month
    print("The most popular month of travel in the data you selected is {}.".format(popular_month))

    # TO DO: display the most common day of week
    # first calculate the most popular day
    popular_day = df['day_of_week'].mode()[0]
    # then print the most popular day
    print("The most popular day of the week for travel in the data you selected is {}.".format(popular_day))

    # TO DO: display the most common start hour
    # first calculate the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour_number = df['hour'].mode()[0]
    # then convert to a standard 12 hour clock and include am or pm
    if 1 <= hour_number <= 11:
        popular_hour = str(hour_number) + (' am')
    elif 12 <= hour_number <= 23:
        hour_number -= 12
        popular_hour = str(hour_number) + (' pm')
    elif hour_number == 0:
        hour_number = 12
        popular_hour = str(hour_number) + (' am')
    # and, finally, print the most common start hour
    print("The most common starting time of the day in the data you selected is {}.".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # first calculate the most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    # then print the most commonly used end station
    print("The most common starting station for travel in the data you selected is {}.".format(popular_start))

    # TO DO: display most commonly used end station
    # first calculate the most commonly used end station
    popular_end = df['End Station'].mode()[0]
    # then print the most commonly used end station
    print("The most common ending station for travel in the data you selected is {}.".format(popular_end))

    # TO DO: display most frequent combination of start station and end station trip
    # calculate the most frequent combination
    popular_combination = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    # display the most frequent combination
    print("The most frequent combination of stations in the data you selected is between {}.".format(popular_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # first calculate the total travel time
    travel_time = df['Trip Duration'].sum()
    travel_hours = int(travel_time // 60)
    travel_mins = int(travel_time % 60)

    # then display total travel time
    print("The total travel time in the data you selected is {} hours and {} minutes.".format(travel_hours, travel_mins))


    # TO DO: display mean travel time
    # calculate the mean travel time
    mean_travel_time = int(df['Trip Duration'].mean())
    # then display the mean travel time
    print("The mean travel time in the data you selected is {} minutes.".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # create a view of user types
    user_types = df['User Type'].value_counts()
    # display the text summary and the view
    print("Below is a summary of the user types for the data you selected.")
    print(user_types)


    # TO DO: Display counts of gender
    # try to calculate this information
    try:
        gender_summary = df['Gender'].value_counts()
        # display the text summary and the view
        print("\nBelow is a summary of the genders of users for the data you selected.")
        print(gender_summary)
    # some info can't be calculated since Washington doesn't have this data - account for that
    except Exception as e:
        print("\nUnfortunately, gender data is not currently available for Washington")

    # TO DO: Display earliest, most recent, and most common year of birth
    # first remove washington from the results since this data is not in the washington file
    try:
        # calculate the earliest birth year
        earliest_birthyear = int(df['Birth Year'].min())
        # calculate the most recent birth year
        recent_birthyear = int(df['Birth Year'].max())
        # calculate the most common birth year
        common_birthyear = int(df['Birth Year'].mode()[0])
        # then print each of those results
        print("\nThe earliest birth year in the data you selected is {}.".format(earliest_birthyear))
        print("The most recent birth year in the data you selected is {}.".format(recent_birthyear))
        print("The most common birth year in the data you selected is {}.".format(common_birthyear))
    except Exception as e:
        print("\nUnfortunately, birth year data is not currently available for Washington")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # add code to ask the user if they want to see 5 rows of raw data - show a new 5 rows each time they choose yes
    # start with raw_data = yes to enter the loop with it evaluating to True
    raw_data = "yes"
    # start with x and y and -5 and 0 so when 5 is added as part of the loop they actually start at 0 and 5 for the first 5 rows of data
    x = -5
    y = 0
    #while loop to continually show more data each time the user selects 'yes'. After each time prompt the user for input again
    #prompt user for input in a loop until their input is something other than yes
    while raw_data == 'yes':
        raw_data = input("Would you like to see 5 rows of raw data? Please enter Yes if so. Any other response will be considered a no.").lower()
        if raw_data == "yes":
            #increment x and y by 5 each time through the loops
            x += 5
            y += 5
            print(df.iloc[x:y])
        else: break



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
