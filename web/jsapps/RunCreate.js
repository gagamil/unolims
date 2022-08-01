import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";

import RunCreateForm from "./components/RunCreate/RunCreateForm";
import RunCreatePreview from "./components/RunCreate/RunCreatePreview";

const RunCreate = () => {
  const [runData, setRunData] = useState(undefined);

  const STEP__RUN_FORM = "STEP__RUN_FORM";
  const STEP__RUN_PREVIEW = "STEP__RUN_PREVIEW";
  const STEP__RUN_SAVE = "STEP__RUN_SAVE";

  const BUTTON__FORM = {
    caption: "Back to edit",
    step: STEP__RUN_FORM,
    secondary: true,
  };
  const BUTTON__PREVIEW = {
    caption: "Preview",
    step: STEP__RUN_PREVIEW,
    secondary: false,
  };
  const BUTTON__UPLOAD = {
    caption: "Create run",
    step: STEP__RUN_SAVE,
    secondary: false,
  };

  const buttons = {
    STEP__RUN_FORM: [null, BUTTON__PREVIEW],
    STEP__RUN_PREVIEW: [BUTTON__FORM, BUTTON__UPLOAD],
  };

  const [step, setStep] = useState(STEP__RUN_FORM);

  return (
    <>
      <ButtonWizard buttonPair={buttons[step]} handleClick={setStep} />

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

const ButtonWizard = ({ buttonPair, handleClick }) => {
  return (
    <div className="row justify-content-between mt-2 mb-2">
      {buttonPair.map((btn) => {
        if (!btn) {
          return <div className="col-md-4"></div>;
        } else {
          return (
            <div className="col-md-4">
              <button
                onClick={() => {
                  console.log("Will set step: ", btn.step);
                  handleClick(btn.step);
                }}
                className={
                  btn.secondary ? "btn btn-outline-primary" : "btn btn-primary"
                }
              >
                {btn.caption}
              </button>
            </div>
          );
        }
      })}
    </div>
  );
};
