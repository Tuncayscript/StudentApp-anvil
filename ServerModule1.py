import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def add_row(**kwargs):
  app_tables.timetable.add_row(
    fullname = kwargs['fullname'],
    day_1 = kwargs['day_1'],
    day_2 = kwargs['day_2'],
    time_1 = kwargs['time_1'],
    time_2 = kwargs['time_2'],
    month_lessons = kwargs['month_lessons'],
    course_fee = int(kwargs['course_fee']),
    start_date = kwargs['start_date'],
    notes = kwargs['notes']
  )

