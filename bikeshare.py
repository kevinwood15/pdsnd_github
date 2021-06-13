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

    city_list=["chicago", "new york city", "washington"]
    print('Please enter a city: Chicago, New York City, Washington')
    city=input().lower()

    while city not in city_list:
        print('Please enter a valid city: Chicago, New York City, or Washington')
        city=input().lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    month_list=["all", "january", "february", "march", "april", "may", "june"]
    print('Please enter a month from January to June or type all')
    month=input().lower()
    while month not in month_list:
        print('Please enter a valid month or type all.')
        month=input().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day_list=["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    print('Please enter a day of the week between Monday to Sunday or type all.')
    day=input().lower()

    while day.lower() not in day_list:
        print('Please enter a valid day of the week or type all.')
        day=input().lower()

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
    print('Filters applied: city = {}, month = {}, day = {}'.format(city, month, day))

    #Read approriate city data into memory

    df=pd.read_csv(CITY_DATA[city])
        
    #change time variables to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])    

    #Create month and day and hour variables

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


    #The following lines restricts the df to the subset with the specified month /day (if all is not selected)

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df

def display_raw_data(df):
    """Prompts the user if they want to see 5 lines of raw data and continues to prompt user until user says no"""

    response_list=["yes", "no"]
    print('Would you like to see the first 5 rows of the raw data? Please enter yes or no.')
    response=input()
    while response.lower() not in response_list:
        print('Please enter a valid response: yes or no.')
        response=input()
        continue
    else:
        if response.lower()=="yes":
            for i in range(0, len(df.index),5):
                print(df[i:i+5])
                print('Would you like to see the next 5 rows of the raw data? Enter yes or no.')
                response=input().lower()
                while response.lower() not in response_list:
                    print('Please enter a valid response: yes or no.')
                    response=input()
                if response.lower()=="no":
                    break                
        print('-'*40)
    
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    modal_month=df['month'].mode()[0]

    print('The most common month is', modal_month)

    # TO DO: display the most common day of week

    modal_day=df['day'].mode()[0]
    print('The most common day of the week is', modal_day)


    # TO DO: display the most common start hour

    modal_hour=df['hour'].mode()[0]
    print('The most common hour of the day is', modal_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

 
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print('The most commonly used start station is', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station

    print('The most commonly used end station is', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip

    df['Start Stop Combo'] = df['Start Station'] + " to " + df['End Station']

    print('The most common Station combo is', df['Start Stop Combo'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    #I create day, hour, minute, and second variables for 'total time' 
    total_time = df['Trip Duration'].sum()
    days = total_time // (24 * 3600)
    remainder_time = total_time % (24 * 3600)
    hours = remainder_time // 3600
    remainder_time %= 3600
    minutes = remainder_time // 60
    remainder_time %= 60
    seconds = remainder_time
    print('Bikeshare users rode for a total of {} days {} hours {} minutes {} seconds'.format(days, hours, minutes, seconds))

    # TO DO: display mean travel time
    
    #I create day, hour, minute, and second variables for 'mean time' 
    mean_time = df['Trip Duration'].mean()
    days = mean_time // (24 * 3600)
    remainder_time = mean_time % (24 * 3600)
    hours = remainder_time // 3600
    remainder_time %= 3600
    minutes = remainder_time // 60
    remainder_time %= 60
    seconds = remainder_time
    #I omit days since no user rode for a day
    print('Bikeshare users rode an average of {} hours {} minutes {} seconds per trip'.format(hours, minutes, seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    if 'User Type' in df.columns:
        subscribers = df['User Type'].str.count('Subscriber').sum()
        customers = df['User Type'].str.count('Customer').sum()
        print("There are {} subscribers".format(int(subscribers)))
        print("There are {} customers".format(int(customers)))

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        male = df['Gender'].str.count('Male').sum()
        female = df['Gender'].str.count('Female').sum()
        print("There are {} male Bikeshare users".format(int(male)))
        print("There are {} female Bikeshare users".format(int(female)))

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        print("The earliest year of birth among users is", int(df['Birth Year'].min()),)
        print("The most recent year of birth among users is", int(df['Birth Year'].max()))
        print("The most common year of birth among users is", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
