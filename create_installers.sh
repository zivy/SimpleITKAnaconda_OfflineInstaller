#!/bin/bash

#
# Create installers for linux and osx.
#
# Linux and OS X installers can only be created on a mac or linux machine.
# Windows installers can only be created on a windows machine.
#
constructor --platform=osx-64 .
constructor --platform=linux-32 .
constructor --platform=linux-64 .


