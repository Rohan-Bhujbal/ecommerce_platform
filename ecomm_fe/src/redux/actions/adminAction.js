export const ActionTypes = {
    IS_LOGIN: "IS_LOGIN",
    SELF_DETAILS: "SELF_DETAILS",
    GET_DEVICE_ID: "GET_DEVICE_ID",
    GET_ACCESSTOKEN:"GET_ACCESSTOKEN",
    ADMIN_LOGOUT:"ADMIN_LOGOUT",
    GET_USER_LIST:"GET_USER_LIST",
    GET_PAYMENT_LIST:"GET_PAYMENT_LIST",
    ADD_MACHINE_LIST:"ADD_MACHINE_LIST",
    GET_MACHINE_LIST:"GET_MACHINE_LIST",
    EDIT_MACHINE_LIST:"EDIT_MACHINE_LIST",
    GET_SINGLE_MACHINE_LIST:"GET_SINGLE_MACHINE_LIST",
    CLEAR_FORM_SET_FUCT:"CLEAR_FORM_SET_FUCT",
    GET_SEARCH_LIST:"GET_SEARCH_LIST",
    GET_PAGE_LIST:"GET_PAGE_LIST",
    ADD_PAGE_LIST:"ADD_PAGE_LIST",
    EDIT_PAGE_LIST:"EDIT_PAGE_LIST",
    GET_ORDER_LIST:"GET_ORDER_LIST",
    GET_STATUS_LIST:"GET_STATUS_LIST",
    GET_TRANSACTION_LIST:"GET_TRANSACTION_LIST",
    GET_CONTACT_LIST:"GET_CONTACT_LIST",
    GET_FAQ_LIST:"GET_FAQ_LIST",
    ADD_FAQ_LIST:"ADD_FAQ_LIST",
    EDIT_FAQ_LIST:"EDIT_FAQ_LIST",
    GET_USER_ID:"GET_USER_ID"
}


export const checkLogin = (status) => {
    return {
        type: ActionTypes.IS_LOGIN,
        payload: status,
    }
}

export const getSelfDetails = (user) => {
    return {
        type: ActionTypes.SELF_DETAILS,
        payload: user,
    }
}

export const getDeviceId = (id) => {
    return {
        type: ActionTypes.GET_DEVICE_ID,
        payload: id,
    }
}

export const getAccessToken = (token) => {
    return {
        type: ActionTypes.GET_ACCESSTOKEN,
        payload: token,
    }
}

export const clearRedux = () => {
    return {
        type: ActionTypes.ADMIN_LOGOUT,
    }
}

export const getUserList = (list) => {
    return {
        type: ActionTypes.GET_USER_LIST,
        payload: list,
    }
}

export const getPaymentList = (list) => {
    return {
        type: ActionTypes.GET_PAYMENT_LIST,
        payload: list,
    }
}

export const addMachineList = (list) => {
    return {
        type: ActionTypes.ADD_MACHINE_LIST,
        payload: list,
    }
}

export const getMachineList = (list) => {
    return {
        type: ActionTypes.GET_MACHINE_LIST,
        payload: list,
    }
}

export const editMachineList = (list) => {
    return {
        type: ActionTypes.EDIT_MACHINE_LIST,
        payload: list,
    }
}

export const getSingleMachineList = (list) => {
    return {
        type: ActionTypes.GET_SINGLE_MACHINE_LIST,
        payload: list,
    }
}

export const ClearFormSetFutios = (date_) => {
    return {
        type: ActionTypes.CLEAR_FORM_SET_FUCT,
        payload: date_,
    }
}

export const getOnsearch = (list) =>{
    return {
        type: ActionTypes.GET_SEARCH_LIST,
        payload: list,
    }
}

export const getPageList = (list) => {
    return {
        type: ActionTypes.GET_PAGE_LIST,
        payload: list,
    }
}

export const editPageList = (list) => {
    return {
        type: ActionTypes.EDIT_PAGE_LIST,
        payload: list,
    }
}

export const addPageList = (list) => {
    return {
        type: ActionTypes.ADD_PAGE_LIST,
        payload: list,
    }
}

export const getOrderList = (list) => {
    return {
        type: ActionTypes.GET_ORDER_LIST,
        payload: list,
    }
}

export const getStatus = (list) =>{
    return {
        type: ActionTypes.GET_STATUS_LIST,
        payload: list,
    }
}

export const getTransacionList = (list) => {
    return {
        type: ActionTypes.GET_TRANSACTION_LIST,
        payload: list,
    }
}

export const getContactList = (list) => {
    return {
        type: ActionTypes.GET_CONTACT_LIST,
        payload: list,
    }
}

export const getFaqList = (list) => {
    return {
        type: ActionTypes.GET_FAQ_LIST,
        payload: list,
    }
}

export const editfaqList = (list) => {
    return {
        type: ActionTypes.EDIT_FAQ_LIST,
        payload: list,
    }
}

export const addfaqList = (list) => {
    return {
        type: ActionTypes.ADD_FAQ_LIST,
        payload: list,
    }
}

export const getUserId = (list) =>{
    return {
        type: ActionTypes.GET_USER_ID,
        payload: list,
    }
}