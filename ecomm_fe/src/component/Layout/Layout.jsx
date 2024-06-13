import React from "react";
import Header from "../Header/Header";
import Sidebar from "../SideBar/SideBar";
const Layout = ({ children }) => {
    return (
        <div className="container-fluid g-0">
            <div className="row">
                <div className="col-12">
                    <div className="row">
                        <div className="col-2 col-md-2 col-lg-2 col-sm-2">
                            <Sidebar />
                        </div>
                        <div className="col-10 col-md-10 col-lg-10 col-sm-10">
                            <div className="row mt-2">
                                <div className="col-12">
                                    <Header />
                                </div>
                            </div>
                            <div className="row">
                                
                                    {children}
                        
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            
        </div>
    );
};

export default Layout;
