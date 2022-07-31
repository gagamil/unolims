import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";

import {
  REPLICATION__DUPLICATE,
  REPLICATION__TRIPLICATE,
  RUN_METHOD__EUROFINS,
  RUN_METHOD__SALIVACLEAR,
} from "./const";

const RunCreatePreview = ({
  runTitle,
  runMethod,
  runReplication,
  tubeBatchDataList,
}) => {
  
    const [tubeBatchTitles,setTubeBatchTitles] = useState([])
    useEffect(()=>{
        const lTubeBatchTitles = []
        for (k, v of Object.entries(tubeBatchDataList)){
            lTubeBatchTitles.push(v.title)
            setTubeBatchTitles(lTubeBatchTitles)
        }

    }, [runTitle,
        runMethod,
        runReplication,
        tubeBatchDataList])

    
  return (
    <>
      <div className="row">
        <div className="col-md-8">
          <h2>Run summary</h2>
          <dl>
            <dt>Run title</dt>
            <dd>{runTitle}</dd>
            <dt>Run method</dt>
            <dd>{runMethod}</dd>
            <dt>Run replication</dt>
            <dd>{runReplication}</dd>
            <dt>Tube batches</dt>
            <dd>{tubeBatchTitles.map((el) => el)}</dd>
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
  tubeBatchDataList: PropTypes.array.isRequired,
};

export default RunCreatePreview;
