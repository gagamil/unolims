# unolims

Basic Laboratory Information Management System web app for sample testing using two-stage hierarchical pool testing techinque.
Built with Django, signals for main logic operation.
This app is developped as a monolithic app.
However the Signals framework does offer a possibility to develop a loosely coupled Django project.
This way decoupling one of the apps should be a fairly easy job.

# licence

MIT

# motivation

LIMS might be expensive to build.
My experience shows that multiple design flaws and over engineerig can geopardize the LIMS adoption and basically screw the whole workflow.
The basics of hierarchical pooling is more or less the same and differs in the details.
These detail can be added later on.
Provided that this software would be relatively easy to deploy and modify this LIMS would be a good tool for the labs.

# Two stage hierarchical pool testing

1. All samples are placed in their respective tubes.
2. These samples are then amalgamated into a number of pools using pooling tubes.
3. Pooling tubes are then being tested.
4. If pool tested negative, the respective individual samples are flagged negative.
5. If pool tested positive, the respective individual samples are being tested individually.

# App design

Structural separation by apps.

## common

Constants, signals and other names and objects used throughout the apps.

## data_importing

Data import services and logic.
For Tubes and Runs.

## run

All Run, Run Template, Run Results data models and logic.

## tubes

All Tube and Batch data models and logic.

## web

The web app UI. A hybrid Django with templates configuration.
The ecnhanced UX is built using React Js.
Whenever possible basic Template based Django Views are used.
The React Js app is being used when UX improvement is evident.

## Tubes and Batches

In order to be a bit more universal the word Batch is used. Words Goup or pool might be used as well.
Tubes are grouped into batches for different reasons.
An example is when they are grouped on a rack for scanning and the data is entered into the system.
Or when the samples are run and tested.

## Batch

### Tags

To run the logic and display the data to the user Batch may hold any number of tags.
These could be: 'INDIVIDUAL POOLS AND POOL TUBE', 'POOLING SCAN', 'TEST RUN 123', 'CONFIRMED', 'COMPLETE', 'CANCELLED'.
Business logic might interpret tags in one way or another with the subsequent outcome.

### Extra data

There might be some extra data that needs to be stored and retreived later on. For this reason the Batch contains a JSON field 'xtra_data'.

## Events and handlers

Each main model and step triggers a predefined Django signal:

- batch_pending_confirmation
- batch_just_confirmed

to be continued...
