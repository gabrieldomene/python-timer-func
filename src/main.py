import math
import time
import logging

logging.basicConfig(format="%(asctime)s - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def logTime(function):
  def runner(*args, **kwargs):
    logger.info("Starting {}".format(function.__name__))

    start = time.perf_counter_ns();
    function(*args, **kwargs)
    end = time.perf_counter_ns()

    elapsed = end - start

    formatTime(elapsed)

  return runner;

def formatTime(time):
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
  return "{}".format((math.trunc(value / scale)))

def appendNewTime(oldTimer, value, unity):
  return f"{oldTimer} {value} {unity}"

@logTime
def genericFunction(arbitraryNumber):
  s = 0
  for i in range(arbitraryNumber):
    s += 1

genericFunction(450000000)