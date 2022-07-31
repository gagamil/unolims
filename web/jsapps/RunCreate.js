import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";

import RunCreateForm from "./components/RunCreate/RunCreateForm";
import RunCreatePreview from "./components/RunCreate/RunCreatePreview";

const RunCreate = () => {
  const [runData, setRunData] = useState(undefined);
  useEffect(() => {
    console.log("runData ===> ", runData);
  }, [runData]);
  const STEP__RUN_FORM = "STEP__RUN_FORM";
  const STEP__RUN_PREVIEW = "STEP__RUN_PREVIEW";
  const STEP__RUN_SAVE = "STEP__RUN_SAVE";
  const [step, setStep] = useState(STEP__RUN_FORM);

  return (
    <>
      <div className="row justify-content-between">
        <div className="col-md-4">
          <button
            onClick={() => {
              setStep(STEP__RUN_FORM);
            }}
            className="btn btn-primary"
          >
            Back
          </button>
        </div>
        <div className="col-md-4">
          <button
            onClick={() => {
              setStep(STEP__RUN_PREVIEW);
            }}
            className="btn btn-primary"
          >
            Preview & Confirm
          </button>
        </div>
      </div>

      {step === STEP__RUN_PREVIEW && (
        <RunCreatePreview
          runTitle={runData.runTitle}
          runMethod={runData.runMethod}
          runReplication={runData.runReplication}
          tubeBatchDataList={runData.tubeBatchDataList}
        />
      )}
      {step === STEP__RUN_FORM && <RunCreateForm setRunData={setRunData} />}
    </>
  );
};

export default RunCreate;
