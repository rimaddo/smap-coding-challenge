import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { Header, RowDiv } from "../styles";
import Table from "./Table";
import { getAreas, getNumberOfUsersByArea, getTariffs } from "../actions";
import Chart from "./Chart";

export default () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAreas());
    dispatch(getNumberOfUsersByArea());
  }, []);

  const areas = useSelector((state) => state.areas);
  const numberOfUsersByArea = useSelector((state) => state.numberOfUsersByArea);

  return (
    <div>
      <Header header={'Area Summary'} variant="h5" />
      <RowDiv>
        <Table rows={areas}/>
        <Chart
          title={'Number of users per Area'}
          data={numberOfUsersByArea}
          xAxis={'area_name'}
          values={['counts']}
          type={"Bar"}
        />
      </RowDiv>
    </div>
  )
}