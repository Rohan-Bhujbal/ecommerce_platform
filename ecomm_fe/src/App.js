import './App.css';
import { Navigate, Route, Routes } from 'react-router-dom'; // Import BrowserRouter
// import { useState } from 'react';
import Login from './component/Login/index';
import './assets/css/style.css'
import Layout from './component/Layout/Layout';
import OrderManagement from './component/OrderManagement/OrderManagement';
import CreateMachine from './component/MachineManagement/CreateMachine';
import { useState,createContext } from 'react';
import { ToastContainer } from 'react-toastify';
import { useSelector } from 'react-redux';
import 'react-toastify/dist/ReactToastify.css'; // Import toast styles
import MachineManagement from './component/MachineManagement/ProductManagement';

export const WebSocketContext = createContext();

function App() {
  const [GetWEBSocket, setWebSocket] = useState("");
  const { accessToken} = useSelector((state) => state.adminReducers);


  return (
    <div className="App">
      <Routes>
        <Route path="/login" element={<Login />} />
       
        <Route path="/order-management" element={accessToken !== "" ?<Layout><OrderManagement RouteName="/order-management" /></Layout>:<Navigate replace to ="login"/>} />
        <Route path="/product-management" element={accessToken !== "" ?<Layout><MachineManagement RouteName="/product-management" /></Layout>:<Navigate replace to ="login"/>}/>
        <Route path="/add-product" element={accessToken !== "" ?<Layout><CreateMachine RouteName="/add-product" /></Layout>:<Navigate replace to ="login"/>} />
        <Route path="/edit-product/:id" element={accessToken !== "" ?<Layout><CreateMachine RouteName="/add-product" /></Layout>:<Navigate replace to ="login"/>} />
        <Route path="*" element={<Navigate to="/login" />} />
      </Routes>
      <ToastContainer />
    </div>
  );
}

export default App;
