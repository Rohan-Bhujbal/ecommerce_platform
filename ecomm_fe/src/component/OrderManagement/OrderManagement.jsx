import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";
import moment from "moment";
import 'moment-timezone';
import { Scrollbars } from 'react-custom-scrollbars-2';
import { useSelector } from "react-redux";
import CommonPagination from "../commonModel/commonPagination";
import axios from "axios";

const OrderManagement = () => {
  const { userList } = useSelector((state) => state.adminReducers);
  const [orderList, setOrderList] = useState([]);
  const [pagination, setPagination] = useState({});
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    fetchOrders(currentPage);
  }, [currentPage]);

  const fetchOrders = async (page) => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_BASE_URL}/order/order_list?page=${page}`);
      const data = response.data.data;
      setOrderList(data.data);
      setPagination(data.pagination);
    } catch (error) {
      console.error('Error fetching orders:', error);
    }
  };

  const CommonDateTime = (date, format, method) => {
    if (date !== null) {
      const currentTimezone = moment.tz.guess();
      return moment(date).tz(currentTimezone).format(format);
    } else {
      return method === "show" ? "-" : null;
    }
  };

  const userDetail = (id) => {
    const userInf = userList?.list?.filter((user) => user?.id === id)[0];
    return {
      userName: userInf?.username || "-",
      userEmail: userInf?.email || "-",
      mobileNumber: userInf?.phone || "-"
    };
  };

  const currentFunction = (page) => {
    setCurrentPage(page);
  };

  const renderTrack = ({ style, ...props }) => {
    const trackStyle = {
      display: "none"
    };
    return <div style={{ ...style, ...trackStyle }} {...props} />;
  };

  return (
    <>
      <div style={{ margin: "2px" }} className="fixTableHead">
        <Scrollbars
          style={{ height: pagination.total_records > 20 ? "calc(100vh - 160px)" : "calc(100vh - 125px)" }}
          renderView={props => <div {...props} className="view" />}
          renderTrackHorizontal={renderTrack}
          className="ScrollbarsSidebar"
        >
          <Table responsive style={{ borderTopLeftRadius: "19px", borderTopRightRadius: "19px" }}>
            <thead style={{ position: "sticky", top: "0px" }}>
              <tr className="user-management-table-heading">
                <th>Order Id</th>
                <th>Full Name</th>
                <th>Mobile Number</th>
                <th>Date</th>
                <th>Cost</th>
                <th>Quantity</th>
              </tr>
            </thead>
            <tbody>
              {orderList.length > 0 ? (
                orderList.map((order) => (
                  <tr key={order.id} className="user-management-table-detail">
                    <td>{order.id}</td>
                    <td style={{ cursor: "default" }}>{userDetail(order.user_id).userName}</td>
                    <td style={{ cursor: "default" }}>{userDetail(order.user_id).mobileNumber}</td>
                    <td style={{ cursor: "default" }}>{CommonDateTime(order.created_at, "DD MMM YYYY", "show")}</td>
                    <td style={{ cursor: "default" }}>{order.total}</td>
                    <td style={{ cursor: "default" }}>{order.qty}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="6">Data not found</td>
                </tr>
              )}
            </tbody>
          </Table>
        </Scrollbars>
        {pagination.total_records > 20 && (
          <CommonPagination
            currentPage={currentPage}
            paginationLength={pagination}
            currentFunction={currentFunction}
          />
        )}
      </div>
    </>
  );
};

export default OrderManagement;
