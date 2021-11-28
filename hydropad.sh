#!/bin/bash

xrdb -load /dev/null
xrdb -query


python HydroApp.py
