# Automated Touchpad Drivers Reset

## The Problem
The touchpad on my MSI Raider GE78HX 13VG laptop freezes periodically during normal useage. It takes several seconds and many inputs to unfreeze
and the only temporary solution I found was resetting the drivers as that seems to stop the frequency of the freezes. This is very annoying as I 
train AI models and the extra CPU useage increases frequency quite a bit.

## The Solution
This script resets the drivers of my touchpad by listening for any mouse movement, if there is none within a certain timeframe the drivers will be reset.

This script is controlled by the Task Scheduler and runs in the background with no observable overhead.
