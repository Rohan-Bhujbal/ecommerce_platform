import axios from 'axios';

const LoginAPI = async (payload) => {
    const response = await axios.post(`${process.env.REACT_APP_BASE_URL}/user/login`, payload, {
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    }}).then(function (result) {
        return {
          ...result.data,
          status:200
        };
    }).catch(function (result) {
        return {
          ...result?.response?.data,
          status:result?.response?.status
        }
    });
    return response;
};
  
export default LoginAPI;
  