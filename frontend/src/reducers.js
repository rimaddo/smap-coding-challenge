import { combineReducers } from 'redux';


export const START_LOADING_USERS = "START_LOADING_USERS";
export const END_LOADING_USERS = "END_LOADING_USERS";
export const START_LOADING_AREAS = "START_LOADING_AREAS";
export const END_LOADING_AREAS = "END_LOADING_AREAS";
export const START_LOADING_TARIFFS = "START_LOADING_TARIFFS";
export const END_LOADING_TARIFFS = "END_LOADING_TARIFFS";
export const START_LOADING_USERS_BY_AREA = "START_LOADING_USERS_BY_AREA";
export const END_LOADING_USERS_BY_AREA = "END_LOADING_USERS_BY_AREA";
export const START_LOADING_CON_BY_TIME = "START_LOADING_CON_BY_TIME";
export const END_LOADING_CON_BY_TIME = "END_LOADING_CON_BY_TIME";


const config = [
  {
    name: 'users',
    initialState: [],
    startLoading: START_LOADING_USERS,
    endLoading: END_LOADING_USERS,

  },
  {
    name: 'areas',
    initialState: [],
    startLoading: START_LOADING_AREAS,
    endLoading: END_LOADING_AREAS,

  },
  {
    name: 'tariffs',
    initialState: [],
    startLoading: START_LOADING_TARIFFS,
    endLoading: END_LOADING_TARIFFS,

  },
  {
    name: 'numberOfUsersByArea',
    initialState: [],
    startLoading: START_LOADING_USERS_BY_AREA,
    endLoading: END_LOADING_USERS_BY_AREA,

  },
    {
    name: 'userConsumptionByTimeOfDay',
    initialState: [],
    startLoading: START_LOADING_CON_BY_TIME,
    endLoading: END_LOADING_CON_BY_TIME,

  },
];


const dataLoader = (config_item) => {

  return function(state = config_item.initialState, action) {
    switch (action.type) {
      case config_item.startLoading:
        return state;
      case config_item.endLoading:
        return action[config_item.name];
      default:
        return state;
    }
  };
};


const createDataReducers = (config) => {
  var dataReducers = {};
  config.map(
    config_item => {
      dataReducers[config_item.name] = dataLoader(config_item)
    }
  );
  return dataReducers;
};


const rootReducer = combineReducers({
  ...createDataReducers(config)
});
export default rootReducer;
