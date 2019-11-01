import React from 'react';
import { Chart } from 'react-google-charts';

import { ChartContainer } from "../styles";


const cleanString = (str) => (str.replace('_',' ').toUpperCase());


const getGraphData = (data, xAxis, values) => {
  let graphData = [
    [
      cleanString(xAxis), ...values.map((value) => cleanString(value))]
  ];
  for (let i in data) {
    graphData.push(
      [data[i][xAxis], ...values.map((v) => data[i][v])]
    )
  }
  return graphData;
};

export default ({ title = null, subtitle = null, data = [], xAxis = null, values = [], type = "Line"}) => {

  return (
    <ChartContainer>
      {data.length === 0 ? [] : <Chart
        width={'500px'}
        height={'400px'}
        chartType={type}
        loader={<div>Loading Chart</div>}
        data={getGraphData(data, xAxis, values)}
        options={{
          chart: {
            title: title,
            subtitle: subtitle,
          },
        }}
        rootProps={{ 'data-testid': '3' }}
      />}
    </ChartContainer>
  )
};
