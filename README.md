# NetOps Coding 101 Demo
This code accompanies a live tutorial presented at the 64th meeting of NANOG
(https://www.nanog.org/meetings/abstract?id=2565).  Presentation slides are
available from the link above, which walk through building this in detail.

At a high-level, the demonstration code automates the detection and remediation
(data gathering and potentially troubleshooting of) network faults.  Detection
is performed by parsing of syslog messages sent by network devices to a central
syslog server, where this code is intended to run.

Two independant versions are included:
* nanog_demo.py:  a sample to accomplish our goal in it's simpliest form
* nanog_demo_better.py:  an improved version to show one possible evolution

## Examples
When ran without local modifications, both nanog_demo.py and nanog_demo_better.py
will attempt to read pre-staged syslog messages stored in the file named
"syslog.txt" from the current working directory.  The pre-staged messages are of
actual issues observed in Facebook's network, and have been modified only by
replacing actual device names with generic ones.

The syslog messages are parsed against a regular expression that separates
message into it's components, such as "datestamp", "device", "error_code",
and "error_message".

As the next step, the logic looks for known error codes in the log messages --
which correlate to remediations.  When finding a known error code, the assigned
remediation is ran against the device (using SSH).  Included are remediation
examples for both messages.  

Two error messages / remediations are included here --
* INTERFACE_REMOVED:  Though this is based on "interface removed" messages, it was
built after seeing a case where all interfaces on a linecard logged "interface removed"
as a result of a linecard / module failure.  This example does not consider aggregation
of multiple events though, but we use that as the basis of troubleshooting this as a
potential linecard failure.  In this remediation, output of "show module X" is evaluated
to see if the suspected module is online.  If it is, the code proceeds to check the
current uptime of that module.  No further troubleshooting is performed and this is
simply printed on screen.  This is shown as a simple example of evaluating and parsing
output based on commands being issued to the device over SSH, using the Paramiko library.

* INTERFACE_LINK_DOWN:  A remediation that looks at counters of the interface
and evaluates the value seen for "interface resets".  This remediation shows an
example of performing a set of troubleshooting logic when the counter exceeeds a
pre-defined threshold (10 in this example), and when that matches, proceeeds to
check the light-levels of that interface (assumes an optical medium).  Using this,
we could automate the detection and initial troubleshooting of potentially flapping
links.

## Requirements
* Python 2.7.3+
* Paramiko (https://pypi.python.org/pypi/paramiko/)

This code is compatible with Python3.

## Building
This can be run as-is using Python without additional configuration or building.

## Installing and Getting Started
As this is intended to be an example to build from, it will require local
modifications based on the environment being used in.  These include:

* Editing "SYSLOG", the variable defined in nanog_demo.py / nanog_demo_better.py
to point to the actual file path where your syslog server is storing messages
("/var/log/syslog" for example).

* Editing the regular expresssion patterns that run against syslog messages to
fit the particular vendor(s) and platform(s) being used by your environment.

* Editing the "username" and "passwd" variables passed when opening SSH
connections to include actual credentials, or modifying this code to fetch
those dynamically if available programatically in your environment.

* Editing the remediation code based your own platforms and desired
troubleshooting workflow.

## Getting Help
Questions?  Please join our group https://www.facebook.com/groups/netengcode/
and post away!
 nanog66-dev
