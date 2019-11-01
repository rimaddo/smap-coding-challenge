// Default config for fetching route data

import * as reduxConsts from './reducers';

const defaultConfig = {
  credentials: 'include',
  headers: {
    accept: 'application/json, text/plain',
    'Content-Type': 'application/json',
  },
};

export function fetchWrapper(url, config = {}) {
  return fetch(url, { ...defaultConfig, ...config }).then((response) => {
    if (!response.ok) {
      return response.text().then(err => Promise.reject(err));
    }
    if (response.status === 204) {
      return null;
    }
    return response.json();
  });
}


function fetchAndDispatch(
    fetcher,
    args,
    preFetchActionCreators = [],
    responseFetchActionCreators = [],
) {
  return (dispatch) => {
    preFetchActionCreators.map(i => dispatch(i));
    fetcher(...args).then(
      (jsonResponse) => {
        responseFetchActionCreators.map(i => dispatch(i(jsonResponse)))
      }
    );
  };
}


export const startLoadUsers = () => ({
  type: reduxConsts.START_LOADING_USERS,
});
export const endLoadUsers = (users) => ({
  type: reduxConsts.END_LOADING_USERS,
  users,
});
export const getUsers = () => {
  const url = `/api/users/`;
  return (
    fetchAndDispatch(
      fetchWrapper,
      [url],
      [startLoadUsers()],
      [endLoadUsers],
    ));
};


export const startLoadTariffs = () => ({
  type: reduxConsts.START_LOADING_TARIFFS,
});
export const endLoadTariffs = (tariffs) => ({
  type: reduxConsts.END_LOADING_TARIFFS,
  tariffs,
});
export const getTariffs = () => {
  const url = `/api/tariffs/`;
  return (
    fetchAndDispatch(
      fetchWrapper,
      [url],
      [startLoadTariffs()],
      [endLoadTariffs],
    ));
};


export const startLoadAreas = () => ({
  type: reduxConsts.START_LOADING_AREAS,
});
export const endLoadAreas = (areas) => ({
  type: reduxConsts.END_LOADING_AREAS,
  areas,
});
export const getAreas = () => {
  const url = `/api/areas/`;
  return (
    fetchAndDispatch(
      fetchWrapper,
      [url],
      [startLoadAreas()],
      [endLoadAreas],
    ));
};


export const startLoadNumberOfUsersByArea = () => ({
  type: reduxConsts.START_LOADING_USERS_BY_AREA,
});
export const endLoadNumberOfUsersByArea = (numberOfUsersByArea) => ({
  type: reduxConsts.END_LOADING_USERS_BY_AREA,
  numberOfUsersByArea,
});
export const getNumberOfUsersByArea = () => {
  const url = `/api/number_of_users_by_area/`;
  return (
    fetchAndDispatch(
      fetchWrapper,
      [url],
      [startLoadNumberOfUsersByArea()],
      [endLoadNumberOfUsersByArea],
    ));
};


export const startLoadUserConsumptionByTimeOfDay = () => ({
  type: reduxConsts.START_LOADING_CON_BY_TIME,
});
export const endLoadUserConsumptionByTimeOfDay = (userConsumptionByTimeOfDay) => ({
  type: reduxConsts.END_LOADING_CON_BY_TIME,
  userConsumptionByTimeOfDay,
});
export const getUserConsumptionByTimeOfDay = () => {
  const url = `/api/user_consumption_by_time_of_day/`;
  return (
    fetchAndDispatch(
      fetchWrapper,
      [url],
      [startLoadUserConsumptionByTimeOfDay()],
      [endLoadUserConsumptionByTimeOfDay],
    ));
};
