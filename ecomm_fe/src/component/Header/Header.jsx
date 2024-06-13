import React, { useEffect, useState } from "react";
import { InputGroup, Form } from 'react-bootstrap'
import { useLocation, useNavigate } from "react-router-dom";
import { getOnsearch, getStatus, getUserId } from "../../redux/actions/adminAction";
import { useDispatch, useSelector } from "react-redux";
import Select from 'react-select'
const Header = () => {
    const LocationURL = useLocation().pathname
    const navigate = useNavigate()
    const dispatch = useDispatch()
    const LocationRoute = useLocation()?.pathname?.split("/")[1];
    const [searchQuery, setSearchQuery] = useState('');
    const [selectedValue, setSelectValue] = useState("")
    const { userList } = useSelector((state) => state.adminReducers);
    const [optionsRegion, SetOptionsRegion] = useState(() => userList?.list?.filter((elm) => elm?.is_active)?.map((item, index) => ({ key: item.id, value: item?.id, label: item?.username })));
    const [optionVal, setOptionValue] = useState("")
    const handleChange = (e) => {
        dispatch(getStatus(e.target.value))
        setSelectValue(e.target.value)
    }
    const customStyles = {
        option: (provided, state) => ({
            ...provided,
            fontSize: '13px', // Adjust the font size as per your requirement
        }),
    };

    console.log("LocationRoute",LocationRoute)
    const RegionValueSelect = (value) => {
        if (value !== null) {
            setOptionValue(value)
            dispatch(getUserId(value?.key))
            
        } else {
            setOptionValue("")
            dispatch(getUserId(""))
            
        }
    };


    useEffect(() => {
        dispatch(getOnsearch(""))
        dispatch(getStatus(""))
        setSelectValue("")
        setSearchQuery("")
        dispatch(getUserId(""))
    }, [LocationURL, dispatch])

    return (
        <>
            <div className="row">
                <div className="col-12 ">
                    <div className="row ">
                        <div className="col-4">
                            {LocationURL === "/user-management" && <p className="header-text">User Management</p>}
                            {LocationURL === "/order-management" && <p className="header-text">Order Management</p>}
                            {LocationURL === "/product-management" && <p className="header-text">Product Management</p>}
                           
                        </div>
                        <div className="col-8">
                            <div className="row mt-2">

                                <div className="col-12 ">
                                    {LocationURL === "/product-management" &&
                                        <button className="pt-1 pb-1 ps-3 pe-3 ms-3 mb-3 me-5 float-end" id="button" onClick={() => navigate('/add-product')}>+ Add Product</button>
                                    }
                                    {LocationURL === "/page" &&
                                        <button className="pt-1 pb-1 ps-4 pe-4" style={{ marginLeft: "20px" }} id="button" onClick={() => navigate('/add-page')}>+ Add Page</button>
                                    }
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}


export default Header