import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";

const RunCreate = () => {
  // useEffect(() => {
  //   console.log("Init [START]");
  //   const evtSource = new EventSource("http://localhost:7999/events/");
  //   console.log("Init [END]");
  //   evtSource.addEventListener("test", function (event) {
  //     console.log("New event came");
  //     const msg = JSON.parse(event.data).msg;
  //     console.log(msg);
  //   });

  //   // let es = new ReconnectingEventSource("http://localhost:7999/events/");

  //   // es.addEventListener(
  //   //   "message",
  //   //   function (e) {
  //   //     console.log(e.data);
  //   //   },
  //   //   false
  //   // );
  // }, []);
  const [selectModeEnabled, setSelectModeEnabled] = useState(false);
  const [runTubeBatchIdx, setRunTubeBatchIdx] = useState(0);
  const [chosenScansData, setChosenScansData] = useState({
    1: undefined,
    2: undefined,
    3: undefined,
    4: undefined,
  });

  const updateTubeBatchData = ({ id, title, date, rackId }) => {
    const oldData = { ...chosenScansData };
    oldData[runTubeBatchIdx] = { id, title, date, rackId };
    setChosenScansData({ ...oldData });
  };

  return (
    <>
      <div className="row">
        <div className="col-md-8">
          <div className="mt-4">
            <label htmlFor="run_title_id" className="form-label h5">
              Title
            </label>
            <input
              type="text"
              className="form-control"
              id="run_title_id"
              aria-describedby="runTitleHelp"
            />
            {/* <div id="runTitleHelp" className="form-text">
              Optional run title.
            </div> */}
          </div>
        </div>
      </div>
      <div className="row">
        <div className="col-md-7">
          <label htmlFor="run_method__eurofins" className="form-label h5 mt-4">
            Method
          </label>
          <RunMethodChoice />
        </div>

        <div className="col-md-5">
          <div className="mt-4">
            <label htmlFor="run_title_id" className="form-label h5">
              Replication
            </label>
          </div>
          <ReplicationChoice />
        </div>
      </div>

      <div className="row">
        <div className="col">
          <div className="mt-4">
            <label htmlFor="run_title_id" className="form-label h5">
              Chosen run tube bathces
            </label>
          </div>
          <RunScanChoices setRunTubeBatchIdx={setRunTubeBatchIdx} />
          <ChosenScanInfo
            chosenScansData={chosenScansData[runTubeBatchIdx]}
            setSelectModeEnabled={setSelectModeEnabled}
          />
        </div>
      </div>
      {!!selectModeEnabled && (
        <div className="row">
          <div className="col">
            <div className="mt-4">
              <label htmlFor="run_title_id" className="form-label h5">
                Available run tube batces
              </label>
            </div>
            <div className="overflow-scroll mt-2" style={{ maxHeight: 300 }}>
              <ScanTable handleItemAdd={updateTubeBatchData} />
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default RunCreate;

const ChosenScanInfo = ({ chosenScansData, setSelectModeEnabled }) => {
  const {
    title = "---",
    date = "---",
    rackId = "---",
  } = chosenScansData
    ? chosenScansData
    : { title: "---", date: "---", rackId: "---" };
  return (
    <>
      <div className="card-body">
        <h5 className="card-title">{title}</h5>
        <p className="card-text">
          {date} {rackId}
        </p>
        <button
          onClick={() => {
            setSelectModeEnabled(true);
          }}
          className="btn btn-primary"
        >
          Add
        </button>
      </div>
    </>
  );
};

const BATCH_TYPE__RUN = "RUN_BATCH";
const ScanTable = ({ handleItemAdd }) => {
  const [tubeBatches, setTubeBatches] = useState([]);
  useEffect(() => {
    console.log("Getting tube batches to be used in scans");
    fetch(
      "/v1/tubebatch/?" +
        new URLSearchParams({
          batchType: BATCH_TYPE__RUN,
        })
    )
      .then((response) => {
        return response.json();
      })
      .then((jsonData) => {
        setTubeBatches(jsonData);
        console.log("tubeBatches: ", jsonData);
      })
      .catch((e) => {
        console.log("Error: ", e);
      });
  }, []);

  const batchList = tubeBatches.map((tb) => {
    return (
      <tr key={tb.id}>
        <th scope="row">
          <button
            type="button"
            className="btn btn-primary btn-sm"
            onClick={() => {
              handleItemAdd({
                id: tb.id,
                title: tb.title,
                date: tb.xtra_data.created_at,
                rackId: tb.xtra_data.rack_id,
              });
            }}
          >
            Add
          </button>
        </th>
        <td>{tb.title}</td>
        <td>{tb.xtra_data.created_at}</td>
        <td>{tb.xtra_data.rack_id}</td>
      </tr>
    );
  });
  return (
    <table className="table pt-4">
      <thead>
        <tr>
          <th scope="col">Action</th>
          <th scope="col">Title</th>
          <th scope="col">Created</th>
          <th scope="col">Rack Id</th>
        </tr>
      </thead>
      <tbody className="table-group-divider">{batchList}</tbody>
    </table>
  );
};

ScanTable.propTypes = {
  selectItem: PropTypes.func,
};

const REPLICATION__DUPLICATE = "DUPLICATE";
const REPLICATION__TRIPLICATE = "TRIPLICATE";
const ReplicationChoice = () => {
  const [replication, setReplication] = useState(REPLICATION__DUPLICATE);
  return (
    <div className="btn-group">
      <button
        onClick={() => setReplication(REPLICATION__DUPLICATE)}
        className={`btn btn-primary ${
          REPLICATION__DUPLICATE === replication ? "active" : ""
        }`}
      >
        Duplicate
      </button>
      <button
        onClick={() => setReplication(REPLICATION__TRIPLICATE)}
        className={`btn btn-primary ${
          REPLICATION__TRIPLICATE === replication ? "active" : ""
        }`}
      >
        Triplicate
      </button>
    </div>
  );
};

const RunScanChoices = ({ setRunTubeBatchIdx }) => {
  const [currIdx, setCurrIdx] = useState(0);
  useEffect(() => {
    setRunTubeBatchIdx(currIdx);
  }, [currIdx]);
  return (
    <div
      className="btn-toolbar"
      role="toolbar"
      aria-label="Toolbar with button groups"
    >
      <div className="btn-group me-2" role="group" aria-label="Third group">
        <button
          onClick={() => setCurrIdx(0)}
          type="button"
          className={`btn btn-${0 === currIdx ? "info" : "secondary"}`}
        >
          Tube batch 1
        </button>
      </div>
      <div className="btn-group me-2" role="group" aria-label="Third group">
        <button
          onClick={() => setCurrIdx(1)}
          type="button"
          className={`btn btn-${1 === currIdx ? "info" : "secondary"}`}
        >
          Tube batch 2
        </button>
      </div>
      <div className="btn-group me-2" role="group" aria-label="Third group">
        <button
          onClick={() => setCurrIdx(2)}
          type="button"
          className={`btn btn-${2 === currIdx ? "info" : "secondary"}`}
        >
          Tube batch 3
        </button>
      </div>
      <div className="btn-group" role="group" aria-label="Third group">
        <button
          onClick={() => setCurrIdx(3)}
          type="button"
          className={`btn btn-${3 === currIdx ? "info" : "secondary"}`}
        >
          Tube batch 4
        </button>
      </div>
    </div>
  );
};

const RunMethodChoice = () => {
  const runMethod = "run_method__eurofins";
  return (
    <div>
      <input
        type="radio"
        className="btn-check"
        name="run_method"
        id="run_method__eurofins"
        autoComplete="off"
        checked={runMethod === "run_method__eurofins"}
        onClick={() => (runMethod = "run_method__eurofins")}
      />
      <label className="btn btn-secondary me-2" htmlFor="option1">
        Eurofins
      </label>

      <input
        type="radio"
        className="btn-check"
        name="run_method"
        id="run_method__salivadirect"
        autoComplete="off"
        checked={runMethod !== "run_method__eurofins"}
        onClick={() => (runMethod = "run_method__eurofins")}
      />
      <label className="btn btn-secondary" htmlFor="option1">
        Saliva Direct
      </label>
    </div>
  );
};
