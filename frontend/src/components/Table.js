import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import { TableContainer } from "../styles";

const useStyles = makeStyles({
  root: {
    width: '100%',
    overflowX: 'auto',
  },
  table: {
    minWidth: 650,
  },
});


const getColumns = (rows) => {
  const item = rows[0];
  if (item) {
    return Object.keys(item)
  }
  return [];

};

export default ({ rows = [] }) => {
  const classes = useStyles();
  const columns = getColumns(rows);

  return (
    <TableContainer>
      <Paper className={classes.root}>
        <Table className={classes.table} aria-label="simple table">
          <TableHead>
            <TableRow>
              {columns.map((col) => <TableCell align="center">{col.toUpperCase()}</TableCell>)}
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map(row => (
              <TableRow key={row.name}>
                {columns.map((col) => ( <TableCell align="center">{row[col]}</TableCell>))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Paper>
    </TableContainer>
  );
}