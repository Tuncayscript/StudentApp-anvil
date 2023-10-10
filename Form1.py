from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime

# Code by Tunjay Akbarli 
# Project File Created: 9/25/2023 18:47

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.day1.items = ['-Choose DAY 1 -', 'Mon', 'Wed', 'Fri', 'Sun']
    self.day2.items = ['-Choose DAY 2 -', 'Tue', 'Thu', 'Sat']
    self.time1.items = [' - Choose time 1 - ', '19:00', '19:30', '20:00', '20:30', '21:00']
    self.time2.items = [' - Choose time 2 - ', '19:00', '19:30', '20:00', '20:30', '21:00']
    self. course.items = ['-COURSE-', 'Data Science', 'Pyhton', 'Code-lang','Software Development']
    self.choose_date.date = datetime.date.today()
    self.form_components.visible = False
    self.repeating_panel.items = app_tables.timetable.search()
    
    # Any code you write here will run before the form opens.

  def toggle_form_click(self, **event_args):
    self.form_components.visible = not self.form_components.visible

  def submit_click(self, **event_args):
    if self.fullname.text == '' or self.notes.text == '' or self.course_fee.text == '' or self.day1.selected_value == '-Choose DAY 1 -' or self.day2.selected_value == '-Choose DAY 2 -' or self.time1.selected_value == '-Choose time 1 -' or self.time2.selected_value == '-Choose time 2 -' or self.course.selected_value == '-COURSE-':
      alert('Please Fill all informations!')
    else:
      new_std = {
        'fullname': self.fullname.text,
        'day_1': self.day1.selected_value,
        'day_2': self.day2.selected_value,
        'time_1': self.time1.selected_value,
        'time_2': self.time2.selected_value,
        'month_lessons': '',
        'course': self.course.selected_value,
        'course_fee': int(self.course_fee.text),
        'start_date': self.choose_date.date,
        'notes': self. notes.text
      }
      anvil.server.call('add_row', **new_std) 
      self.repeating_panel.items = app_tables.timetable.search()
      Notification('Student data has been inserted!')
      self.clear_form()
    
  def clear_form(self):
    self.fullname.text = ''
    #self.day1.selected_value '-Choose DAY 1 -'
    self.day2.selected_value = '-Choose DAY 2 -'
    self.time1.selected_value = '-Choose time 1 -'
    self.time2.selected_value = '-Choose time 2 -'
    self.course.selected_value = '-COURSE-'
    self.course_fee.text = ''
    self.choose_date.date = datetime.date.today()
    self.notes.text = ''
    self.toggle_form()
