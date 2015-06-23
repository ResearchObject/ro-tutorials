# Example paper: Who was the earliest riser? An empirical study of employee office hours.

Stian Soiland-Reyes, University of Manchester
http://orcid.org/0000-0001-9842-9718

**This is an example article for the tutorial 
"Creating a Research Object". **

_We present a novel methodology for determining the earliest arrival and latest
departure from an office. We tested this empirically on generated example
data for 3 fictional employees. Subsequent analysis shows that the office was in
attendance for 11 hours._


## Background

In many company settings, employees arrive and leave an office at different hours.
Managers often gather data on these arrival and depature times, but lack the
sufficient analytical tools to extract useful metrics such as total attendance.

## Method

We generated a CSV file of example attendance data for 3 fictional employees 
Alice, Bob and Charlie. The names chosen are based on common 
placeholder names[1]. We chose the name _Charlie_ over _Carol_ and _Carlos_ to
maintain a neutral gender distribution.  

We deviced an algorithm, for determining the earliest employee arriving, by 
processing the rows of the file and compare the current row's arrival time with
the current earliest arrival. A variant of this algorithm was subsequently
used to dermine the latest arrival.  The algorithm was implemented in 
Python[2].

## Results

The analysis showed that the employee arriving earliest was Charlie at 8:00. The 
employee leaving latest was Alice, at 19:00. The office was thus in attendance
for 11 hours, including lunch.


## Future work

The algorithm can in theory be extended to also calculate which employee 
work the longest hours.


## References

[1] *Alice and Bob*. Wikipedia. https://en.wikipedia.org/wiki/Alice\_and\_Bob retrieved 2015-06-23.

[2] Van Rossum, Guido, and Fred L. Drake. _Python language reference manual._ Network Theory, 2003.

