let initialState = {};

function AppReducer(state = initialState, action) {
  console.log(action);

  console.error("uhoh, unrecognized action.type:");
  console.error(action);

  return state;
}

export default AppReducer;
