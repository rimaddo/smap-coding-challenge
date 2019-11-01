import React from 'react';
import styled from 'styled-components';

import Typography from '@material-ui/core/Typography';

const themeSpaceMultipler = 8;


export const Header = styled(
  ({ header, ...rest }) => (
    <Typography {...rest}>
      {header}
    </Typography>
  )
)`
   padding: ${themeSpaceMultipler}px;
`;


export const RowDiv = styled.div`
  display: flex;
  flex-direction: row;
`;


export const ChartContainer = styled.div`
  padding: 15px;
`;


export const TableContainer = styled.div`
  padding: 15px;
`;

