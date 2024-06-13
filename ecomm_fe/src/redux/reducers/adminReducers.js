import { ActionTypes } from "../actions/adminAction";

const initialData = {
    accessToken: "",
    ClearFormSet: {
        url: "",
        action: false
    },
    selfInfo: {},
    device_id: "",
    userList: {
        list: [],
        pagination: {}
    },
    pageList: {
        list: [],
        pagination: {}
    },
    paymentList: {
        list: [],
        pagination: {}
    },
    machineList: {
        list: [],
        pagination: {}
    },
    singleMachineList: {
        list: [],
        pagination: {}
    },
    OrderList: {
        orders: [],
        pagination: {},
        users: []
    },
    search: "",
    listStatus: "",
    transactionList: {
        list: [],
        pagination: {}
    },
    contactList: {
        list: [],
        pagination: {}
    },
    faqList: {
        list: [],
        pagination: {}
    },
    userId: ""
};

export const adminReducers = (state = initialData, action) => {
    switch (action.type) {

        case ActionTypes.CLEAR_STORE:
            return initialData;
        case ActionTypes.GET_ACCESSTOKEN:
            return {
                ...state,
                accessToken: action.payload,
            };
        case ActionTypes.SELF_DETAILS:
            return {
                ...state,
                selfInfo: action.payload,
            };
        case ActionTypes.GET_DEVICE_ID:
            return {
                ...state,
                device_id: action.payload,
            };
        case ActionTypes.GET_USER_LIST:
            return {
                ...state,
                userList: {
                    list: Object.keys(action.payload).length === 0 ? [] : action.payload.data,
                    pagination: Object.keys(action.payload).length === 0 ? [] : action.payload.pagination,
                },
            };
        case ActionTypes.GET_PAGE_LIST:
            return {
                ...state,
                pageList: {
                    list: Object.keys(action.payload).length === 0 ? [] : action.payload.data,
                    pagination: Object.keys(action.payload).length === 0 ? [] : action.payload.pagination,
                },
            };
        case ActionTypes.GET_PAYMENT_LIST:
            return {
                ...state,
                paymentList: {
                    list: Object.keys(action.payload).length === 0 ? [] : action.payload.data,
                    pagination: Object.keys(action.payload).length === 0 ? [] : action.payload.pagination,
                },
            };
        case ActionTypes.GET_MACHINE_LIST:
            return {
                ...state,
                machineList: {
                    list: Object.keys(action.payload).length === 0 ? [] : action.payload.data,
                    pagination: Object.keys(action.payload).length === 0 ? [] : action.payload.pagination,
                },
            };
        case ActionTypes.ADD_MACHINE_LIST:
            const OldMachinelist = [...state.machineList.list];
            OldMachinelist.unshift(action.payload);
            return {
                ...state,
                machineList: {
                    ...state.machineList,
                    list: OldMachinelist,
                },
            }
        case ActionTypes.EDIT_MACHINE_LIST:
            const OldMachinelistx = [...state.machineList.list];
            const UpdateMachineList = OldMachinelistx.map((elm) => {
                if (elm?.id === action.payload.id) {
                    return {
                        ...elm,
                        machine_name: action.payload.machine_name,
                        org_id: action.payload.org_id,
                        machine_address: action.payload.machine_address,
                        door_no: action.payload.door_no,
                        is_active: action.payload.is_active,
                    };
                } else
                    return elm;
            });
            return {
                ...state,
                machineList: {
                    ...state.machineList,
                    list: UpdateMachineList,
                }
            };
        case ActionTypes.GET_SINGLE_MACHINE_LIST:
            return {
                ...state,
                singleMachineList: {
                    list: Object.keys(action.payload).length === 0 ? [] : action.payload.data,
                    pagination: Object.keys(action.payload).length === 0 ? [] : action.payload.pagination,
                },
            };
        case ActionTypes.CLEAR_FORM_SET_FUCT:
            return {
                ...state,
                ClearFormSet: {
                    url: action?.payload?.url,
                    action: action?.payload?.action
                }
            };
        case ActionTypes.GET_SEARCH_LIST:
            return {
                ...state,
                search: action.payload,
            };
        case ActionTypes.ADD_PAGE_LIST:
            const OldPagelist = [...state.pageList.list];
            OldPagelist.unshift(action.payload);
            return {
                ...state,
                pageList: {
                    ...state.pageList,
                    list: OldPagelist,
                },
            }
        case ActionTypes.EDIT_PAGE_LIST:
            const OldPagelistx = [...state.pageList.list];
            const UpdatePageList = OldPagelistx.map((elm) => {
                if (elm?.id === action.payload.id) {
                    return {
                        ...elm,
                        page_name: action.payload.page_name,
                        page_slug: action.payload.page_slug,
                        page_description: action.payload.page_description,
                        page_image: action.payload.page_image,
                        is_active: action.payload.is_active,
                    };
                } else
                    return elm;
            });
            return {
                ...state,
                pageList: {
                    ...state.pageList,
                    list: UpdatePageList,
                }
            };
        case ActionTypes.GET_ORDER_LIST:
            return {
                ...state,
                OrderList: {
                    orders: Object.keys(action.payload).length === 0 ? [] : action.payload.orders,
                    pagination: Object.keys(action.payload).length === 0 ? [] : action.payload.pagination,
                    users: Object.keys(action.payload).length === 0 ? [] : action.payload.users,
                },
            };
        case ActionTypes.GET_STATUS_LIST:
            return {
                ...state,
                listStatus: action.payload,
            };
        case ActionTypes.GET_TRANSACTION_LIST:
            return {
                ...state,
                transactionList: {
                    list: Object.keys(action.payload).length === 0 ? [] : action.payload.data,
                    pagination: Object.keys(action.payload).length === 0 ? [] : action.payload.pagination,
                },
            };
        case ActionTypes.GET_CONTACT_LIST:
            return {
                ...state,
                contactList: {
                    list: Object.keys(action.payload).length === 0 ? [] : action.payload.data,
                    pagination: Object.keys(action.payload).length === 0 ? [] : action.payload.pagination,
                },
            };
        case ActionTypes.GET_FAQ_LIST:
            return {
                ...state,
                faqList: {
                    list: Object.keys(action.payload).length === 0 ? [] : action.payload.data,
                    pagination: Object.keys(action.payload).length === 0 ? [] : action.payload.pagination,
                },
            };
        case ActionTypes.ADD_FAQ_LIST:
            const OldFaqlist = [...state.faqList.list];
            OldFaqlist.unshift(action.payload);
            return {
                ...state,
                faqList: {
                    ...state.faqList,
                    list: OldFaqlist,
                },
            }
        case ActionTypes.EDIT_FAQ_LIST:
            const Oldfaqlistx = [...state.faqList.list];
            const UpdateFaqList = Oldfaqlistx.map((elm) => {
                if (elm?.id === action.payload.id) {
                    return {
                        ...elm,
                        question: action.payload.question,
                        answer: action.payload.answer,
                    };
                } else
                    return elm;
            });
            return {
                ...state,
                faqList: {
                    ...state.faqList,
                    list: UpdateFaqList,
                }
            };
        case ActionTypes.GET_USER_ID:
            return {
                ...state,
                userId: action.payload,
            };
        default:
            return state;
    }
};
