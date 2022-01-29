import React, { useState } from "react";
import ReactDOM from "react-dom";
import { useToggle } from "react-use";
// import {
//   useQuery,
//   useMutation,
//   useQueryClient,
//   QueryClient,
//   QueryClientProvider,
// } from 'react-query'

// import { updateBatchTitle } from './api'
import useFetch from "use-http";

import BatchTitleForm from "./BatchTitleForm";

const TubeBatchInlineUpdate = () => {
  const options = {
    headers: {
      "X-CSRFToken": csrftoken,
    },
  };
  const { patch, response, loading, error } = useFetch("", options);

  const [batchTitle, setBatchTitle] = React.useState("");
  const [batchId, setBatchId] = React.useState(undefined);
  React.useEffect(() => {
    const parsedBatchData = JSON.parse(
      document.getElementById("object_data").textContent
    );
    console.log(parsedBatchData.title);
    setBatchTitle(parsedBatchData.title);
    setBatchId(parsedBatchData.id);
  }, []);

  const saveTitle = (titleValue) => {
    const options = {};
    patch(`/v1/tubebatch/${batchId}/`, { title: titleValue }).then(() => {
      if (response.ok) {
        console.log("Posted ok");
        setBatchTitle(titleValue);
        setIsEditMode(false);
      } else {
        console.log("error - ", error);
      }
    });
    // setIsEditMode();
  };

  const [isEditMode, setIsEditMode] = useToggle(false);
  if (isEditMode) {
    return (
      <div>
        <BatchTitleForm
          cancel={setIsEditMode}
          save={saveTitle}
          currentValue={batchTitle}
          isSubmitting={loading}
        />
      </div>
    );
  }
  return (
    <h2>
      {batchTitle}{" "}
      <small className="text-muted">
        <button onClick={setIsEditMode} className="btn btn-outline-primary">
          edit
        </button>
      </small>
    </h2>
  );
};

ReactDOM.render(
  <TubeBatchInlineUpdate />,
  document.getElementById("tubes__title_update")
);
