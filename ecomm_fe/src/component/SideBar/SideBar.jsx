import React, { useState } from "react";
import Login from "../../assets/image/logo_login.png";
import { Link, useLocation, useNavigate } from "react-router-dom"
import { Image } from "react-bootstrap"
// import { Button, Container, Offcanvas } from 'react-bootstrap';

const SideBar = () => {
    const LocationURL = useLocation().pathname;
    const navigate = useNavigate()
    const [showModalNew, setShowModalNew] = useState({
        open: false,
        title: "",
        modalType: "",
        Data: {}
    });

    const openModal = () => {
        setShowModalNew({
            ...showModalNew,
            open: !showModalNew?.open,
            title: "Create New Box",
            subtitle: "Create New Model",
            modalType: "log-out",
        })
    };

    return (<>
        <section className="sidebar p-2">
            <div className="row mt-2 ms-2">
                <div className="col-12 col-sm-12 col-md-12 col-lg-12 mb-3 ">
                   
                </div>
            </div>
            <div className="mt- row ">
                <div id="menu2" className="col-12 col-md-12 col-sm-12 col-lg-12 pe-0" >
                    <ul className="pe-0">
                        
                        <li className={LocationURL === "/order-management" ? "active my-3" : "my-3"} id="sidebar" onClick={() => { navigate('/order-management') }}>
                            <svg width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <g clip-path="url(#clip0_1126_392)">
                                    <path d="M19.5312 21.875H5.46875C5.26155 21.875 5.06284 21.7927 4.91632 21.6462C4.76981 21.4997 4.6875 21.301 4.6875 21.0938V3.90625C4.6875 3.69905 4.76981 3.50034 4.91632 3.35382C5.06284 3.20731 5.26155 3.125 5.46875 3.125H14.8438L20.3125 8.59375V21.0938C20.3125 21.301 20.2302 21.4997 20.0837 21.6462C19.9372 21.7927 19.7385 21.875 19.5312 21.875Z" stroke={LocationURL === "/order-management" ? "white" : "#494949"} stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M14.8438 3.125V8.59375H20.3125" stroke={LocationURL === "/order-management" ? "white" : "#494949"} stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M9.375 13.2812H15.625" stroke={LocationURL === "/order-management" ? "white" : "#494949"} stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M9.375 16.4062H15.625" stroke={LocationURL === "/order-management" ? "white" : "#494949"} stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
                                </g>
                                <defs>
                                    <clipPath id="clip0_1126_392">
                                        <rect width="25" height="25" fill="white" />
                                    </clipPath>
                                </defs>
                            </svg>
                            <Link className="ms-2">Order</Link>
                        </li>
                        
                        <li className={LocationURL === "/product-management" ? "active  my-3" : " my-3"} id="sidebar" onClick={() => navigate('/product-management')}>
                            <svg width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <g clip-path="url(#clip0_1126_418)">
                                    <path d="M20.3125 3.90625H4.6875C4.25603 3.90625 3.90625 4.25603 3.90625 4.6875V20.3125C3.90625 20.744 4.25603 21.0938 4.6875 21.0938H20.3125C20.744 21.0938 21.0938 20.744 21.0938 20.3125V4.6875C21.0938 4.25603 20.744 3.90625 20.3125 3.90625Z" stroke="black" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M12.5 17.9688C15.5203 17.9688 17.9688 15.5203 17.9688 12.5C17.9688 9.47969 15.5203 7.03125 12.5 7.03125C9.47969 7.03125 7.03125 9.47969 7.03125 12.5C7.03125 15.5203 9.47969 17.9688 12.5 17.9688Z" stroke="black" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M18.3594 7.42188C18.7908 7.42188 19.1406 7.0721 19.1406 6.64062C19.1406 6.20915 18.7908 5.85938 18.3594 5.85938C17.9279 5.85938 17.5781 6.20915 17.5781 6.64062C17.5781 7.0721 17.9279 7.42188 18.3594 7.42188Z" fill="black" />
                                    <path d="M11.7188 10.9375L10.1562 12.5" stroke="black" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M11.7188 14.8438L14.8438 11.7188" stroke="black" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" />
                                </g>
                                <defs>
                                    <clipPath id="clip0_1126_418">
                                        <rect width="25" height="25" fill="black" />
                                    </clipPath>
                                </defs>
                            </svg>
                            <Link className="ms-2">Product</Link>
                        </li>
                        
                    </ul>
                </div>

            </div>
        </section>
    </>)
}

export default SideBar