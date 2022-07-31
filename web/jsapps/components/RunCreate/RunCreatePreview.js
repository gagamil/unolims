import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";

import {
  REPLICATION__DUPLICATE,
  REPLICATION__TRIPLICATE,
  RUN_METHOD__EUROFINS,
  RUN_METHOD__SALIVACLEAR,
  REPLICATION_DISPLAY_MAPPING,
  RUN_METHOD_DISPLAY_MAPPING,
} from "./const";

const RunCreatePreview = ({
  runTitle,
  runMethod,
  runReplication,
  tubeBatchDataList,
}) => {
  const [tubeBatchTitles, setTubeBatchTitles] = useState([]);
  useEffect(() => {
    const lTubeBatchTitles = [];
    for (const [k, v] of Object.entries(tubeBatchDataList)) {
      if (!!v) {
        lTubeBatchTitles.push(v.title);
        setTubeBatchTitles(lTubeBatchTitles);
      }
    }
  }, [runTitle, runMethod, runReplication, tubeBatchDataList]);

  return (
    <>
      <div className="row">
        <div className="col-md-8">
          <h2>Run summary</h2>
          <dl>
            <dt>Run title</dt>
            <dd>{runTitle}</dd>
            <dt>Run method</dt>
            <dd>{RUN_METHOD_DISPLAY_MAPPING[runMethod]}</dd>
            <dt>Run replication</dt>
            <dd>{REPLICATION_DISPLAY_MAPPING[runReplication]}</dd>
            <dt>Tube batches</dt>
            <dd>{tubeBatchTitles.map((el) => el + " ")}</dd>
          </dl>
        </div>
      </div>
    </>
  );
};

RunCreatePreview.propTypes = {
  runTitle: PropTypes.string.isRequired,
  runMethod: PropTypes.oneOf([RUN_METHOD__EUROFINS, RUN_METHOD__SALIVACLEAR])
    .isRequired,
  runReplication: PropTypes.oneOf([
    REPLICATION__DUPLICATE,
    REPLICATION__TRIPLICATE,
  ]).isRequired,
  tubeBatchDataList: PropTypes.object.isRequired,
};

export default RunCreatePreview;
