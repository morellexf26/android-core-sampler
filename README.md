<div align="center">
  <h1>
    <br/>
    🎛
    <br />
    <br />
    Core Sampler
    <br />
    <br />
  </h1>
  <sup>
    <br />
   Report the usage of each CPU core for a FirefoxOS or
Android device connected via ADB.</em>
    <br />
    <br /

[![Docs](https://img.shields.io/badge/-Docs-blue.svg?style=for-the-badge)](https://github.com/davidflanagan/coresample)

  </sup>

</div>

Record
the contents of `/proc/stat`, waits 5 seconds, and then records the
contents of that file again. By subtracting the first set of numbers
from the second set of numbers we can determine how busy each of the
device CPU cores were during the wait period, and it prints a CPU
usage report the the console.

If you want to wait for an interval other than 5 seconds, just specify
the number of seconds as an argument on the command line.

```
CPU     WORK    BUSY    IDLE    WAIT
0       46%     37%     61%     2%
1       43%     34%     65%     1%
2       8%      6%      94%     0%
3       4%      3%      97%     0%
```

The output columns are:

- CPU: the core number.

- WORK: what percentage of the total work done during the sample
period was done on this core.

- BUSY: the percentage of the sample time that this core was busy.

- IDLE: the percentage of the sample time that this core was busy.

- WAIT: the percentage of the sample time that this core was blocked on I/O. 

