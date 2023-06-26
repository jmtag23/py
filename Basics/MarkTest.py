birth_year=1982
current_year=2019
age=current_year-birth_year
print("Your Age is : " + str(age))

from reverse import reverse_string, parse_expense, get_random_line, calculateDaysBetweenDates, coverter


my_string = "Your Age is : " + str(age)
print(reverse_string(my_string))

file_path = 'C:/temp/DateTimeFile.txt'
random_line = get_random_line(file_path)
print("Random Line: " + random_line)

with open('C:/temp/TestText.txt', 'r') as f:
    print(f.read())

with open('C:/temp/DateTimeFile.txt', 'r') as dtf:
    print(parse_expense(dtf.read()))

with open('C:/temp/DateTimeFile.txt', 'r') as rf:
    print(reverse_string(rf.read()))

begin_date = "2023-01-01"
end_date = "2023-06-30"
days_between = calculateDaysBetweenDates(begin_date, end_date)
print(days_between)  # Output: 180

print(coverter(15))
