import { combineReducers } from "redux";
import { adminReducers } from "./adminReducers";

const reducers = combineReducers({
    adminReducers: adminReducers
});

export default reducers;