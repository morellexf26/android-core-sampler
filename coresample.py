import subprocess
import time

if __name__ == '__main__':
  #How long (in seconds) to wait between cpu usage reports
  sleep = 5

  # Get baseline cpu counts
  startstats = subprocess.check_output(["adb", "shell", "cat", "/proc/stat"], text=True)

  # Now wait the specified number of seconds
  print("measuring CPU usage over {} seconds".format(sleep))
  time.sleep(sleep)

  # Get new cpu counts
  endstats = subprocess.check_output(["adb", "shell", "cat", "/proc/stat"], text=True)

  # Parse the output, finding lines after the first that start with 'cpu'
  start = [line.split(' ') for line in startstats.splitlines()[1:] if line.startswith('cpu')]
  end = [line.split(' ') for line in endstats.splitlines()[1:] if line.startswith('cpu')]

  # Loop through the data and compute the busy values for each CPU
  # and the total of all those values
  totalbusy = 0
  busycounts = []
  for cpu in range(0, len(start)):
    e = [float(n) for n in end[cpu][1:]]
    s = [float(n) for n in start[cpu][1:]]
    user = e[0] - s[0]
    nice = e[1] - s[1]
    system = e[2] - s[2]
    irq = (e[5] - s[5]) + (e[6] - s[6])
    busy = user + nice + system + irq
    busycounts.append(busy)
    totalbusy = totalbusy + busy

  # Now loop again and report results
  # Report usage results for each processor core
  print("CPU\tWORK\tBUSY\tIDLE\tWAIT\tOFF");
  for cpu in range(0, len(start)):
    e = [float(n) for n in end[cpu][1:]]
    s = [float(n) for n in start[cpu][1:]]
    busy = busycounts[cpu]
    idle = e[3] - s[3]
    wait = e[4] - s[4]
    elapsed = sleep * 100
    sum = busy + idle + wait
    # On FirefoxOS devices, the cores sometimes seem to just go to sleep
    # and nothing is recorded for them. I'm not sure what this means, but
    # we'll report it as OFF for time the core is just turned off.
    if (sum < elapsed):
      off = elapsed - sum
    else:
      off = 0

    print("{}\t{:.0%}\t{:.0%}\t{:.0%}\t{:.0%}\t{:.0%}"
          .format(cpu, busy / totalbusy, busy / elapsed,
                  idle / elapsed, wait / elapsed, off / elapsed))