import React, { useState } from "react";

const BatchTitleForm = ({ cancel, save, currentValue }) => {
  const [titleValue, setTitleValue] = React.useState(currentValue);
  const handleSubmit = (event) => {
    event.preventDefault();
    save(titleValue);
  };
  return (
    <form onSubmit={handleSubmit}>
      <div className="mb-3">
        <label htmlFor="batchTitle" className="form-label">
          Batch title
        </label>
        <input
          value={titleValue}
          onChange={(e) => setTitleValue(e.target.value)}
          type="text"
          className="form-control"
          id="batchTitle"
          aria-describedby="batchTitleHelp"
        />
        <div id="batchTitleHelp" className="form-text">
          Type the title you want up to 100 characters long
        </div>
      </div>
      <div className="d-grid gap-2 d-md-block mb-4">
        <button type="submit" className="btn btn-primary me-md-2">
          Submit
        </button>
        <button
          type="button"
          onClick={cancel}
          className="btn btn-outline-primary"
        >
          Cancel
        </button>
      </div>
    </form>
  );
};
export default BatchTitleForm;
