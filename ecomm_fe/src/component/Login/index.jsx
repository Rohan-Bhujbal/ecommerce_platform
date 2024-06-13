import React, { useState } from "react"
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import CheckValid from "../../CheckValid/checkValid";
import EmptySpaceFieldValid from "../../CheckValid/EmptySpaceValid";
import { useNavigate } from "react-router-dom";
import LoginAPI from "../../Api/Login";
import { useDispatch } from "react-redux";
import { getAccessToken, getDeviceId, getSelfDetails } from "../../redux/actions/adminAction";
import { toast } from "react-toastify";

const Login = () => {
    const [PasswordShow, setPasswordShow] = useState(false);
    const [errorEmail, setErrorEmail] = useState("");
    const [errorPassword, setErrorPassword] = useState("");
    const dispatch = useDispatch()
    const [userState, setUserState] = useState({
        email: "",
        password: "",
    });

    function uuidv4() {
        return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11)
            .replace(/[018]/g, c => {
                const r = Math.random() * 16 | 0;
                const v = c === '1' ? 4 : (c === '8' ? 3 : 1);
                return (v ^ (r & (1 << (c / 4)))).toString(16);
            });
    }

    const navigate = useNavigate()
    const login = async () => {
        if (userState?.email !== "" && userState?.password !== "") {
            var DeviceID = uuidv4();
            const jsonData = JSON.stringify({ email: userState?.email, password: userState?.password, device_type: "web", device_id: DeviceID });
            const resp = await LoginAPI(jsonData)
            console.log(resp)
            if (resp?.status === 200) {
                dispatch(getSelfDetails(resp?.data?.user))
                dispatch(getAccessToken(resp?.data?.access_token))
                dispatch(getDeviceId(resp?.data?.device_id))
                localStorage.setItem("access_token", resp?.data?.access_token)
                localStorage.setItem("device_id", resp?.data?.device_id)
                toast.success(resp?.msg)
                navigate('/product-management')
            } else {
                toast.error(resp?.error)
                console.log(resp?.error)
            }
        } else {
            CheckValid(userState?.email, { type: 'email', error: setErrorEmail });
            CheckValid(userState?.password, { type: 'password', error: setErrorPassword });
        }
    }

    return (<>

        <Container fluid className="login-container">
            <Row>
                <Col xs={12}>
                    <Row className="d-flex" style={{ justifyContent: "space-evenly" }}>
                        <Col xs={4} >
                            <div className="row justify-content-center my-5">
                                <div className="row justify-content-center" style={{ marginLeft: "42%" }}>
                                 
                                </div>
                                <div className="row">
                                    <div className="text-center mt-3">
                                        <p className="login-header-text">Login</p>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="text-center mt-3">
                                        <InputGroup className="mb-3" >
                                            <InputGroup.Text id="basic-addon1" >
                                                <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                    <g clip-path="url(#clip0_979_347)">
                                                        <path d="M9 11.25C11.4853 11.25 13.5 9.23528 13.5 6.75C13.5 4.26472 11.4853 2.25 9 2.25C6.51472 2.25 4.5 4.26472 4.5 6.75C4.5 9.23528 6.51472 11.25 9 11.25Z" stroke="#181818" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                                        <path d="M2.25 15.1875C3.61195 12.8341 6.08555 11.25 9 11.25C11.9145 11.25 14.388 12.8341 15.75 15.1875" stroke="#181818" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                                    </g>
                                                    <defs>
                                                        <clipPath id="clip0_979_347">
                                                            <rect width="18" height="18" fill="white" />
                                                        </clipPath>
                                                    </defs>
                                                </svg>                                             </InputGroup.Text>
                                            <Form.Control
                                                placeholder="Enter your email"
                                                aria-label="Enter your email"
                                                aria-describedby="basic-addon1"
                                                onKeyUp={(e) => CheckValid(e.target.value, { type: 'email', error: setErrorEmail })}
                                                style={{ borderLeftStyle: "unset" }}
                                                onChange={(e) => setUserState({ ...userState, email: e.target.value })}
                                                onKeyDown={EmptySpaceFieldValid}
                                            />
                                        </InputGroup>
                                    </div>
                                    {errorEmail && <span className=" error-text text-danger mb-3">{errorEmail}</span>}
                                    <div>
                                        <InputGroup className="mb-3">
                                            <InputGroup.Text id="basic-addon1">
                                                <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                    <g clip-path="url(#clip0_979_364)">
                                                        <path d="M14.625 6.1875H3.375C3.06434 6.1875 2.8125 6.43934 2.8125 6.75V14.625C2.8125 14.9357 3.06434 15.1875 3.375 15.1875H14.625C14.9357 15.1875 15.1875 14.9357 15.1875 14.625V6.75C15.1875 6.43934 14.9357 6.1875 14.625 6.1875Z" stroke="#181818" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                                        <path d="M9 11.3906C9.38833 11.3906 9.70312 11.0758 9.70312 10.6875C9.70312 10.2992 9.38833 9.98438 9 9.98438C8.61167 9.98438 8.29688 10.2992 8.29688 10.6875C8.29688 11.0758 8.61167 11.3906 9 11.3906Z" fill="#181818" />
                                                        <path d="M6.1875 6.1875V3.9375C6.1875 3.19158 6.48382 2.47621 7.01126 1.94876C7.53871 1.42132 8.25408 1.125 9 1.125C9.74592 1.125 10.4613 1.42132 10.9887 1.94876C11.5162 2.47621 11.8125 3.19158 11.8125 3.9375V6.1875" stroke="#181818" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                                    </g>
                                                    <defs>
                                                        <clipPath id="clip0_979_364">
                                                            <rect width="18" height="18" fill="white" />
                                                        </clipPath>
                                                    </defs>
                                                </svg>
                                            </InputGroup.Text>
                                            <Form.Control
                                                type={PasswordShow ? "text" : "password"}
                                                placeholder="Enter your password"
                                                onKeyUp={(e) => CheckValid(e.target.value, { type: 'password', error: setErrorPassword })}
                                                style={{ borderLeftStyle: "unset", borderRightStyle: "unset" }}
                                                onChange={(e) => setUserState({ ...userState, password: e.target.value })}
                                                onKeyDown={EmptySpaceFieldValid}
                                            />
                                            <InputGroup.Text id="basic-addon1">
                                                <span className="showpassbtn " onClick={() => setPasswordShow(!PasswordShow)}>
                                                    {PasswordShow ? (<svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" fill="none" strokeLinecap="round" strokeLinejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><path d="M12 12m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"></path><path d="M22 12c-2.667 4.667 -6 7 -10 7s-7.333 -2.333 -10 -7c2.667 -4.667 6 -7 10 -7s7.333 2.333 10 7"></path></svg>) :
                                                        (<svg xmlns="http://www.w3.org/2000/svg" className="icon icon-tabler icon-tabler-eye-off" width="24" height="24" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" fill="none" strokeLinecap="round" strokeLinejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><path d="M3 3l18 18"></path><path d="M10.584 10.587a2 2 0 0 0 2.828 2.83"></path><path d="M9.363 5.365a9.466 9.466 0 0 1 2.637 -.365c4 0 7.333 2.333 10 7c-.778 1.361 -1.612 2.524 -2.503 3.488m-2.14 1.861c-1.631 1.1 -3.415 1.651 -5.357 1.651c-4 0 -7.333 -2.333 -10 -7c1.369 -2.395 2.913 -4.175 4.632 -5.341"></path></svg>)}
                                                </span>
                                            </InputGroup.Text>
                                        </InputGroup>
                                    </div>
                                    {errorPassword && <span className="text-danger">{errorPassword}</span>}
                                </div>
                                <div className="row mt-3">
                                    <div className="button">
                                        <button type="submit" className="w-100 pt-2 pb-2" id="button" onClick={login}>Login</button>
                                    </div>
                                </div>
                            </div>
                        </Col>
                    </Row>
                </Col>
            </Row >
        </Container >

    </>)
}

export default Login
