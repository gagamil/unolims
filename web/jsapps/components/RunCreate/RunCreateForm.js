import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";

import {
  REPLICATION__DUPLICATE,
  REPLICATION__TRIPLICATE,
  RUN_METHOD__EUROFINS,
  RUN_METHOD__SALIVACLEAR,
  ACTIVE__REPLICATION__CHOICES,
  ACTIVE__RUN_METHOD__CHOICES,
  REPLICATION_DISPLAY_MAPPING,
  RUN_METHOD_DISPLAY_MAPPING,
} from "./const";

const RunCreateForm = ({ setRunData }) => {
  const [runTitle, setRunTitle] = useState("");
  const [runMethod, setRunMethod] = useState(RUN_METHOD__EUROFINS);
  const [runReplication, setRunReplication] = useState(REPLICATION__DUPLICATE);

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

  useEffect(() => {
    console.log(
      "Will save data =>>> ",
      runTitle,
      runMethod,
      runReplication,
      chosenScansData
    );
    setRunData({
      runTitle,
      runMethod,
      runReplication,
      tubeBatchDataList: chosenScansData,
    });
  }, [runTitle, runMethod, runReplication, chosenScansData]);

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
              value={runTitle}
              onChange={(e) => setRunTitle(e.target.value)}
            />
            {/* <div id="runTitleHelp" className="form-text">
              Optional run title.
            </div> */}
          </div>
        </div>
      </div>
      <div className="row">
        <div className="col-md-7">
          <div className="mt-4">
            <label htmlFor="run_method__eurofins" className="form-label h5">
              Method
            </label>
          </div>
          <RunMethodChoice currentChoice={runMethod} setChoice={setRunMethod} />
        </div>

        <div className="col-md-5">
          <div className="mt-4">
            <label htmlFor="run_title_id" className="form-label h5">
              Replication
            </label>
          </div>
          <ReplicationChoice
            currentChoice={runReplication}
            setChoice={setRunReplication}
          />
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
            isSelectModeOn={selectModeEnabled}
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

export default RunCreateForm;

const ChosenScanInfo = ({
  chosenScansData,
  setSelectModeEnabled,
  isSelectModeOn,
}) => {
  const {
    title = "---",
    date = "---",
    rackId = "---",
  } = chosenScansData
    ? chosenScansData
    : { title: "---", date: "---", rackId: "---" };

  useEffect(() => {
    setSelectModeEnabled(false);
  }, [chosenScansData]);
  return (
    <div
      className="card text-bg-primary mt-4 b-3"
      style={{ maxWidth: 18 + "rem" }}
    >
      <div className="card-body">
        <h5 className="card-title">{title}</h5>
        <p className="card-text">
          {date} {rackId}
        </p>
        {!!isSelectModeOn && (
          <button
            onClick={() => {
              setSelectModeEnabled(false);
            }}
            className="btn btn-primary"
          >
            Cancel
          </button>
        )}
        {!isSelectModeOn && (
          <button
            onClick={() => {
              setSelectModeEnabled(true);
            }}
            className="btn btn-primary"
          >
            {!!chosenScansData && "Change"}
            {!chosenScansData && "Add"}
          </button>
        )}
      </div>
    </div>
  );
};

const BATCH_TYPE__RUN = "RUN_BATCH";
const ScanTable = ({ handleItemAdd }) => {
  const [tubeBatches, setTubeBatches] = useState([]);
  useEffect(() => {
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

const ReplicationChoice = ({ currentChoice, setChoice }) => {
  return (
    <div className="btn-group" role="group" aria-label="Replication choices">
      {ACTIVE__REPLICATION__CHOICES.map((choice) => (
        <RadioButton
          key={choice}
          name="replication"
          value={choice}
          displayValue={REPLICATION_DISPLAY_MAPPING[choice]}
          checked={currentChoice === choice}
          handleChange={setChoice}
        />
      ))}
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
          className={`btn btn-${0 === currIdx ? "primary" : "secondary"}`}
        >
          Tube batch 1
        </button>
      </div>
      <div className="btn-group me-2" role="group" aria-label="Third group">
        <button
          onClick={() => setCurrIdx(1)}
          type="button"
          className={`btn btn-${1 === currIdx ? "primary" : "secondary"}`}
        >
          Tube batch 2
        </button>
      </div>
      <div className="btn-group me-2" role="group" aria-label="Third group">
        <button
          onClick={() => setCurrIdx(2)}
          type="button"
          className={`btn btn-${2 === currIdx ? "primary" : "secondary"}`}
        >
          Tube batch 3
        </button>
      </div>
      <div className="btn-group" role="group" aria-label="Third group">
        <button
          onClick={() => setCurrIdx(3)}
          type="button"
          className={`btn btn-${3 === currIdx ? "primary" : "secondary"}`}
        >
          Tube batch 4
        </button>
      </div>
    </div>
  );
};

const RunMethodChoice = ({ currentChoice, setChoice }) => {
  return (
    <div className="btn-group" role="group" aria-label="Run method choices">
      {ACTIVE__RUN_METHOD__CHOICES.map((choice) => (
        <RadioButton
          key={choice}
          name="runMethod"
          value={choice}
          displayValue={RUN_METHOD_DISPLAY_MAPPING[choice]}
          checked={currentChoice === choice}
          handleChange={setChoice}
        />
      ))}
    </div>
  );
};

const RadioButton = ({ name, value, displayValue, checked, handleChange }) => {
  const elId = `id_${value}`;
  return (
    <>
      <input
        // html attributes
        type="radio"
        className="btn-check"
        name={name}
        id={elId}
        autoComplete="off"
        // react attributes
        checked={checked}
        onClick={() => handleChange(value)}
      />
      <label className="btn btn-outline-primary" htmlFor={elId}>
        {displayValue}
      </label>
    </>
  );
};
