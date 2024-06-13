import axios from "axios";
const UploadFileAPI = async (accessToken, payload) => {
    const responce = axios.post(`${process.env.REACT_APP_BASE_URL}file/upload`, payload, {
    headers: {
      'Authorization': 'Bearer ' + accessToken,
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
    return responce;
};
  
export default UploadFileAPI;