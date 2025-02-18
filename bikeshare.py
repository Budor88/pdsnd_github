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
    
    city = input('\nWhich city would you like to filter by? New York City, Chicago , Washington or all??\n').lower()
       
    while (True): 
         if(city == 'new york city' or city == 'chicago' or city == 'washington' or city == 'all'):
            break 
         else:
              city = input('please choose from the given list only').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while (True):
      month = input("\nPlease select a month? January, February, March, April, May, June, or type 'all'\n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print ("please choose from the given list only")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while (True): 
     day =input ("\nPlease choose a day Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or type 'all'\n")
     if day not in ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'all'):
      print( "please choose from the given list only")
      continue
     else:
      break 

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
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

       # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        print (df.head())
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()
    print ('Most common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()
    print ('Most Common Day:', common_day)

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()
    print('Most Common Hour:', common_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    start_station = df['Start Station'].value_counts().idxmax()
    print ('Most Common Start Station:', start_station)

    
    # TO DO: display most commonly used end station
    
    end_station = df['End Station'].value_counts().idxmax()
    print ('Most Common End Station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    
    combination_station = df.groupby(['Start Station', 'End Station']).count()
    print ('\nMost frequent combination of start station and end station trip is:', start_station, "&", end_station)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = sum(df['Trip Duration'])
    print ('Total Travel Time is:', total_travel_time/86400, "Days")

    
    # TO DO: display mean travel time
    
    avg_travel_time = df['Trip Duration'].mean()
    print ('Average travel time is:', avg_travel_time, "seconds")

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_type = df['User Type'].value_counts()
    print ('User Type:\n', user_type)               

    
    # TO DO: Display counts of gender
    
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available.")

    
    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available .")
    
    
    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available.")
    
    
    try:
      Most_Common_Year = df['Birth Year'].mode()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available.")

   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_raw(df):
    
    start = 0
    end = 5

    present = input("\nDo yout want to see the raw data,type 'yes' or 'no'?")
           
    if present == "yes":
       while end <=df.shape[0] - 1:
         
 
         print (df.iloc[start:end, :])
         start += 5
         end += 5 
           
         end_present = input("\nDo you to continue, type 'yes' or 'no'?")
         if end_present == 'no':
            break
                             
                             
def main():
    while (True):
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

        

if __name__ == "__main__":
	main()