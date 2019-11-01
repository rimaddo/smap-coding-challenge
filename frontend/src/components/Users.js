import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { Header, RowDiv } from "../styles";
import { getUserConsumptionByTimeOfDay, getUsers } from "../actions";
import Table from "./Table";
import Chart from "./Chart";

export default () => {

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getUsers());
    dispatch(getUserConsumptionByTimeOfDay());
  }, []);

  const users = useSelector((state) => state.users);
  const userConsumptionByTimeOfDay = useSelector((state) => state.userConsumptionByTimeOfDay);

  return (
    <div>
      <Header header={'User Summary'} variant="h5" />
      <RowDiv>
        <Table rows={users}/>
        <Chart
          title={'User Consumption By Time of Day'}
          data={userConsumptionByTimeOfDay}
          xAxis={'hour'}
          values={['amount']}
        />
      </RowDiv>
    </div>
  )
}