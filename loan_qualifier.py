# This program determines whether a bank customer
# qualifies for a loan

MIN_SALARY = 30000.0  # THE MINIMUM ANNUAL SALARY
MIN_YEARS = 2

# GET THE CUSTOMERS ANNUAL SALARY
salary = float(input('Enter your annual salary: '))

# GET NUMBER OF YEARS ON THE JOB
years_on_job = int(input('Enter the number of ' +
                         'years employed: '))

# DETERMINE IF THEY QUALIFY
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('You qualify')
    else:
        print('You must have been employed' +
              ' for ', MIN_YEARS, 'years to qualify')
else:
    print('You must earn at least $',
          format(MIN_SALARY, ',.2f'),
          ' per year to qualify.', sep='')
