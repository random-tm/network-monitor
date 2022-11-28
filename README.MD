# Network Monitor
Intended to be a lightweight network monitoring solution. Designed for monitoring clusters with multiple machines (virtual and physical) on an internal network.

## Scope
A utility library and a runner which will send an email when an outage is detected. UI or alternative notification methods are not something currently being considered.

## To setup
Copy the schedule example and config example then fill out the values where applicable. The format for the schedule is filename and number of hours between run; if the file is not listed it will run every hour. It is highly recommended to setup a symbolic link in the tasks folder to the util folder with: `ln -s ../util util` so that you can use these in your scripts.