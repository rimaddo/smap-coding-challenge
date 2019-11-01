import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import Table from "./Table";
import { getTariffs } from "../actions";
import { Header, RowDiv } from "../styles";
import Chart from "./Chart";


export default () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getTariffs());
  }, []);

  const tariffs = useSelector((state) => state.tariffs);

  return (
    <div>
      <Header header={'Tariff Summary'} variant="h5" />
      <RowDiv>
        <Table rows={tariffs}/>
      </RowDiv>
    </div>
  )
}