
import { Modal, Card } from "react-bootstrap"
import { useDispatch, useSelector } from "react-redux";
import { useState } from "react";


const CommonewModel = (props) => {
    const { showModalNew, setShowModalNew } = props;
    const { accessToken, OrderList } = useSelector((state) => state.adminReducers);
    const dispatch = useDispatch()
    function handleClose() {
        setShowModalNew({ ...showModalNew, open: false });
    }
    console.log(showModalNew?.Data?.orderId?.product_name)
    const [product, createProduct] = useState({
        product_name: '',
        mrp: '',
        short_description: "",
        is_active: true,
    });

    return (
        <Modal show={showModalNew?.open} className={showModalNew?.subtitle === "Create New Model" ? "commonModel" : ""}>
    <Card>
        <Card.Body>
            <form>
                <div className="mb-3">
                    <label htmlFor="product_id" className="form-label">Product Name</label>
                    <input type="text" id="product_id" name="product_id" readOnly className="form-control"  value={showModalNew?.Data?.orderId?.product_name} />
                </div>
                <div className="mb-3">
                    <label htmlFor="qty" className="form-label">Quantity:</label>
                    <input type="text" id="qty" name="qty" className="form-control" />
                </div>
                <div className="mb-3">
                    <label htmlFor="total" className="form-label">Total:</label>
                    <input type="text" id="total" name="total" className="form-control" />
                </div>
                <button
                    type="submit"
                    className="w-50 pt-2 pb-2 float-end btn btn-primary"
                    id="button"
                >
                    Submit
                </button>
            </form>
        </Card.Body>
    </Card>
</Modal>

    )
}

export default CommonewModel;