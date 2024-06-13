import React, { useEffect, useState } from "react";
import { Form } from "react-bootstrap";
import EmptySpaceFieldValid from "../../CheckValid/EmptySpaceValid";
import CheckValid from "../../CheckValid/checkValid";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { ClearFormSetFutios } from "../../redux/actions/adminAction";
import axios from 'axios';
import { toast } from "react-toastify";

const CreateMachine = () => {
    const LocationRoute = useLocation()?.pathname?.split("/")[1];
    const LocationURL = useLocation().pathname;
    const id = useParams()?.id;
    const { ClearFormSet, machineList } = useSelector((state) => state.adminReducers);
   
    const dispatch = useDispatch()
    const [product, createProduct] = useState({
        product_name: '',
        mrp: '',
        product_image: null, // Update to store the File object
        short_description: "",
        is_active: true,
    });
    const [errorMachineId, setErrorMachineId] = useState("");
    const [errorOrgId, setErrorOrgId] = useState("");
    const [errorDoorNo, setErrorDoorNo] = useState("");
    const [errorAddress, setAddressError] = useState("");
    const machineListData = machineList?.list?.filter((data) => data.id === id)[0];
    const navigate = useNavigate();
    useEffect(() => {
        if (LocationRoute === "edit-product") {
            createProduct({
                ...product,
                product_name: machineListData?.machine_name,
                mrp: machineListData?.org_id,
                short_description: machineListData?.machine_address,
                doorNo: machineListData?.door_no,
                is_active: machineListData?.is_active
            });
        }
    }, [LocationRoute, id, machineListData, product]);

    const handleSwitchChange = (checked) => {
        createProduct({
            ...product,
            is_active: checked
        });
    };

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        createProduct({
            ...product,
            product_image: file // Store the File object
        });
    };

    const addMachine = async () => {
        if (product?.product_name !== "" && product?.short_description !== "" && product?.mrp !== "") {
            const formData = new FormData();
            formData.append('product_name', product.product_name);
            formData.append('product_image', product.product_image); // Append the File object
            formData.append('short_description', product.short_description);
            formData.append('mrp', product.mrp);
            formData.append('is_active', product.is_active);
            try {
                const response = await axios.post(`${process.env.REACT_APP_BASE_URL}/product/product_add`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });
                if (response.status === 200) {
                    toast.success("Product added successfully");
                    navigate('/product-management');
                } else {
                    console.error('Form submission failed');
                }
            } catch (error) {
                console.error('Error:', error);
            }
        } else {
            CheckValid(product?.product_name, { type: 'MachineName', error: setErrorMachineId });
            CheckValid(product?.doorNo, { type: 'DoorNo', error: setErrorDoorNo });
            CheckValid(product?.mrp, { type: 'OrgId', error: setErrorOrgId });
            CheckValid(product?.short_description, { type: 'Address', error: setAddressError });
        }
    };

    return (
        <div className="container">
            <div className="row">
                <div className="col-5">
                    <Form.Group className="mb-3">
                        <Form.Label>Product Name <span className="text-danger">*</span></Form.Label>
                        <Form.Control
                            type="text"
                            placeholder="Enter product name"
                            value={product?.product_name}
                            onKeyUp={(e) => CheckValid(e.target.value, { type: 'MachineName', error: setErrorMachineId })}
                            onKeyDown={EmptySpaceFieldValid}
                            onChange={(e) => createProduct({ ...product, product_name: e.target.value })}
                        />
                        {errorMachineId && <span className="text-danger">{errorMachineId}</span>}
                    </Form.Group>
                </div>
                <div className="col-5">
                    <Form.Group className="mb-3">
                        <Form.Label>Product Image <span className="text-danger">*</span></Form.Label>
                        <Form.Control
                            type="file"
                            onChange={handleFileChange}
                        />
                    </Form.Group>
                </div>
            </div>
            <div className="row">
                <div className="col-5">
                    <Form.Group className="mb-2">
                        <Form.Label>Mrp <span className="text-danger">*</span></Form.Label>
                        <Form.Control
                            type="number"
                            value={product?.mrp}
                            placeholder="Enter Mrp"
                            onKeyUp={(e) => CheckValid(e.target.value, { type: 'DoorNo', error: setErrorDoorNo })}
                            onKeyDown={EmptySpaceFieldValid}
                            onChange={(e) => createProduct({ ...product, mrp: e.target.value })}
                        />
                        {errorDoorNo && <span className="text-danger">{errorDoorNo}</span>}
                    </Form.Group>
                </div>
                <div className="col-5">
                    <Form.Group className="mb-3">
                        <Form.Label>Short Description <span className="text-danger">*</span></Form.Label>
                        <Form.Control
                            style={{ height: "95px" }}
                            type="text"
                            as="textarea"
                            rows={3}
                            value={product?.short_description}
                            onChange={(e) => createProduct({ ...product, short_description: e.target.value })}
                            onKeyUp={(e) => CheckValid(e.target.value, { type: 'Address', error: setAddressError })}
                            onKeyDown={EmptySpaceFieldValid}
                            placeholder="Enter Short Description"
                        />
                        {errorAddress && <span className="text-danger">{errorAddress}</span>}
                    </Form.Group>
                </div>
            </div>
            <div className="row">
                <div className="col-5">
                    <span>
                        <Form.Label>Status</Form.Label>
                        <Form.Check
                            type="switch"
                            id="custom-switch"
                            defaultChecked={product?.is_active}
                            onChange={(e) => handleSwitchChange(e.target.checked)}
                        />
                    </span>
                </div>
                <div className="col-5">
                    <button
                        id="button"
                        className="pt-2 pe-3 pb-2 float-end mb-3"
                        style={{ width: "49%" }}
                        type="submit"
                        onClick={addMachine}
                    >
                        {LocationRoute === "edit-product" ? "Update Product" : "Add Product"}
                    </button>
                </div>
            </div>
        </div>
    );
};

export default CreateMachine;
