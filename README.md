# unolims

Basic Laboratory Information Management System web app for sample testing using two-stage hierarchical pool testing techinque.
Built with Django, uses tags and signals for main logic operation.

# licence

MIT

# motivation

LIMS might be expensive to build. Since there is information out that not so rich regions and countries struggle to test their population due to finance reasons easing some part of the process might be beneficial to them.
Provided that this software would be relatively easy to deploy and modify this LIMS would be a good tool for the labs.

# Two stage hierarchical pool testing

1. All samples are placed in their respective tubes.
2. These samples are then amalgamated into a number of pools.
3. Pools are being tested.
4. If pool tested negative, the respective individual samples are flagged negative.
5. If pool tested positive, the respective individual samples are being tested individually.

# App design

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
