import React, { useContext, useEffect, useState } from "react";
import { Card } from "react-bootstrap";
import axios from "axios";
import logo from '../../assets/image/file.png';
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";

const MachineManagement = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [machineData, setMachineData] = useState([]);
  const [quantities, setQuantities] = useState({});
  const navigate = useNavigate();
  useEffect(() => {
    callMachineList();
  }, [currentPage]);
console.log(machineData)
  const buyNow = async (productId) => {
    const totalQty = quantities[productId] || 0;
    const formData = new FormData();
    formData.append('product_id', productId);
    formData.append('total_qty', totalQty);
    
    try {
      const response = await axios.post(`${process.env.REACT_APP_BASE_URL}/order/order_add`, formData);
      if(response?.status ===200){
        toast.success("order add successfully")
        navigate("/order-management")
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleIncrement = (productId) => {
    setQuantities(prevQuantities => ({
      ...prevQuantities,
      [productId]: (prevQuantities[productId] || 0) + 1
    }));
  };

  const handleDecrement = (productId) => {
    setQuantities(prevQuantities => ({
      ...prevQuantities,
      [productId]: Math.max((prevQuantities[productId] || 0) - 1, 0)
    }));
  };

  const callMachineList = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_BASE_URL}/product/product_list`);
      if (response.status === 200) {
        setMachineData(response.data.data.data);
      } else {
        console.error('Failed to fetch data');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <>
      <div className="row">
        {machineData.length > 0 ? (
          machineData.map(machine => (
            <div key={machine.id} className="col-md-4 mb-3">
              <Card>
                <Card.Body>
                <img src={`${process.env.REACT_APP_BASE_URL}${machine.product_image}`} alt={machine.product_name} height={60} width={60} />
                <Card.Title>{machine.product_name}</Card.Title>
                  <Card.Subtitle className="mb-2 text-muted">{machine.mrp}</Card.Subtitle>
                  <Card.Text>{machine.short_description}</Card.Text>
                  <div className="d-flex justify-content-between align-items-center">
                    <div>
                      Quantity:{" "}
                      <button className="btn btn-outline-primary btn-sm mx-1" onClick={() => handleDecrement(machine.id)}>-</button>
                      {quantities[machine.id] || 0}
                      <button className="btn btn-outline-primary btn-sm mx-1" onClick={() => handleIncrement(machine.id)}>+</button>
                    </div>
                    <button
                      type="submit"
                      className="btn btn-primary w-50 pt-2 pb-2 float-end"
                      id="button"
                      onClick={() => buyNow(machine.id)}
                    >
                      Buy Now
                    </button>
                  </div>
                </Card.Body>
              </Card>
            </div>
          ))
        ) : (
          <div className="col-md-12">
            <p>Data not found</p>
          </div>
        )}
      </div>
    </>
  );
};

export default MachineManagement;
