# unolims
Base LIMS app for sample testing (two-stage hierarchical pool testing).
Built with Django, uses tags and signals for main logic operation.

# Two stage hierarchical pool testing
1) All samples are placed in their respective tubes.
2) These samples are then amalgamated into a number of pools.
3) Pools are being tested.
4) If pool tested negative, the respective individual samples are flaged negative.
5) If pool tested positive, the respective individual samples are being tested.


# App design
## Tubes and Batches
In order to be a bit more universal the term Batch is used. 
Tubes are grouped into batches for different resons. 
An example is when they are grouped on a reack for scanning and the data is entered into the system.
Or when the samples are run and tested.

## Batch
### Tags
To run the logic and display the data to the user Batch may hold any number of tags. 
These could be: 'INDIVIDUAL POOLS AND POOL TUBE', 'POOLING SCAN', 'TEST RUN 123', 'CONFIRMED', 'COMPLETE', 'CANCELLED'.

### Extra data
There might be some extra data that needs to be stored. For this reason the Batch contains a JSON field 'xtra_data'.

## Events and handlers
Each main model and step triggers a predefined Django signal:
- batch_pending_confirmation
- batch_just_confirmed

to be continued...
