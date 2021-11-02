import math
import time
import logging

logging.basicConfig(format="%(asctime)s - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def logTime(function):
  """
  This function receives another function as argument
  and logs the elapsed execution time in a human friendly notation

  Parameters
  ----------
  function: function
        The function to be executed inside this decorator

  Returns
  -------
  runner
        The wrapped function
  """
  def runner(*args, **kwargs):
    logger.info("Starting {}".format(function.__name__))

    start = time.perf_counter_ns();
    function(*args, **kwargs)
    end = time.perf_counter_ns()

    elapsed = end - start

    formatTime(elapsed)

  return runner;

def formatTime(time):
  """
  This function is responsible to format the tracked time and retrieve in a
  readable way as the input is a nanosecond time.

  Parameters
  ----------
  time : number
        Execution time in nanoseconds
  """
  dayInNanoseconds = 8.64e+13
  hourInNanoseconds = 3.6e+12
  minuteInNanoseconds = 6e+10
  secondsInNanoseconds = 1e9

  verboseTimer = ""
  if (time / dayInNanoseconds > 1.0):
    days = truncateCases(time, dayInNanoseconds)
    time %= dayInNanoseconds
    verboseTimer = appendNewTime(verboseTimer, days, 'day(s)')
  
  if (time / hourInNanoseconds > 1.0):
    hours = truncateCases(time, hourInNanoseconds)
    time %= hourInNanoseconds
    verboseTimer = appendNewTime(verboseTimer, hours, 'hour(s)')

  if (time / minuteInNanoseconds > 1.0):
    minutes = truncateCases(time, minuteInNanoseconds)
    time %= minuteInNanoseconds
    verboseTimer = appendNewTime(verboseTimer, minutes, 'minute(s)')

  if (time / secondsInNanoseconds > 1.0):
    seconds = truncateCases(time, secondsInNanoseconds)
    time %= secondsInNanoseconds
    verboseTimer = appendNewTime(verboseTimer, seconds, 'seconds')

  logger.info("Elapsed {}".format(verboseTimer))

def truncateCases(value, scale):
  """
  Simple function to truncate decimal cases in the math of module (%)

  Parameters
  ----------
  value : number
      Quotient in the division in the specific 'time'
  scale : number
      Number in nanoseconds to represent which scale of time it is being
      calculated

  Returns
  -------
  time
      The formatted time for the scale received
  """
  return "{}".format((math.trunc(value / scale)))

def appendNewTime(oldTimer, value, unity):
  """
  Simple string formatter to join all times

  Parameters
  ----------
  oldTimer : string
        Previous string with time info
  value : number
        New value to be concated with oldTimer
  unity : string
        Scale of time to be appended

  Returns
  -------
  time
      String with new info added
  """
  return f"{oldTimer} {value} {unity}"

@logTime
def genericFunction(arbitraryNumber):
  """
  Generic function to simulate time spent

  Parameters
  ----------
  arbitraryNumber : number
      Number of iterations in for loop
  """
  s = 0
  for i in range(arbitraryNumber):
    s += 1

genericFunction(450000000)