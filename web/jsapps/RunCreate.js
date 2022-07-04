import React, { useState, useEffect } from "react";

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
              Chosen run tube batces
            </label>
          </div>
          <RunScanChoices setRunTubeBatchIdx={setRunTubeBatchIdx} />
          <ChosenScanInfo
            chosenScansData={chosenScansData}
            runTubeBatchIdx={runTubeBatchIdx}
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
              <ScanTable />
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default RunCreate;

const ChosenScanInfo = ({
  chosenScansData,
  runTubeBatchIdx,
  setSelectModeEnabled,
}) => {
  const value = chosenScansData[runTubeBatchIdx];
  return (
    <>
      {!!value && (
        <div className="card mt-2" style="width: 18rem;">
          <div className="card-body">
            <h5 className="card-title">{value["batchName"]}</h5>
            <p className="card-text">
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </p>
            <a href="#" className="btn btn-primary">
              Change
            </a>
          </div>
        </div>
      )}
      {!value && (
        <div className="card-body">
          <h5 className="card-title">---</h5>
          <p className="card-text">---</p>
          <button
            onClick={() => {
              setSelectModeEnabled(true);
            }}
            className="btn btn-primary"
          >
            Add
          </button>
        </div>
      )}
    </>
  );
};

const ScanTable = () => {
  return (
    <table className="table pt-4">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">First</th>
          <th scope="col">Last</th>
          <th scope="col">Handle</th>
        </tr>
      </thead>
      <tbody className="table-group-divider">
        <tr>
          <th scope="row">
            <button type="button" class="btn btn-primary btn-sm">
              Add
            </button>
          </th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td colspan="2">Larry the Bird</td>
          <td>@twitter</td>
        </tr>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td colspan="2">Larry the Bird</td>
          <td>@twitter</td>
        </tr>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td colspan="2">Larry the Bird</td>
          <td>@twitter</td>
        </tr>
      </tbody>
    </table>
  );
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
