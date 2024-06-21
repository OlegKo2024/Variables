print('Variables')
Number_of_homeworks_done = 12
Number_of_hours_spent = 1.5
Minutes_per_hour = 60
Course_name = 'Python'
Rate_per_homework = 'Speed'
Speed = Number_of_hours_spent * Minutes_per_hour // Number_of_homeworks_done
print(Course_name,'takes',Speed, 'per ''homework')

# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.
Speed = Number_of_hours_spent / Number_of_homeworks_done
print('Курс:',Course_name + ',','всего задач:',str(Number_of_homeworks_done)+',','затрачено часов:',str(Number_of_hours_spent) + ',','среднее время выполнения',Speed,'часа.')
