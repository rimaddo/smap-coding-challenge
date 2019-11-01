import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { applyMiddleware, compose, createStore } from 'redux';
import thunkMiddleware from 'redux-thunk';
import { apiMiddleware } from 'redux-api-middleware';

import App from './components/App';
import rootReducer from './reducers';

class AppProvider extends Component {
  constructor(props) {
    super(props);
    const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose; // eslint-disable-line
    this.store = createStore(
      rootReducer,
      composeEnhancers(
        applyMiddleware(
          thunkMiddleware,
          apiMiddleware,
        ),
      ),
    );
  }

  render() {
    return (
      <Provider store={this.store}>
        <App />
      </Provider>
    );
  }
}

export default AppProvider;
