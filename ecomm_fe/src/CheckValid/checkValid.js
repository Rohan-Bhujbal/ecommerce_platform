
const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
};

const CheckValid =(value, states)=>{
    if (states.type === "email") {
        if (value.trim() === "") {
            states.error("Email cannot be empty");
        } else if (!validateEmail(value)) {
            states.error("Invalid email address");
        } else {
            states.error(""); 
        }
    }

    if(states?.type === "password"){
        if(value !==""){
            return states?.error("");
        }else{
            return states?.error("password can not be empty");
        }
    }

    if(states?.type === "question"){
        if(value !==""){
            return states?.error("");
        }else{
            return states?.error("question can not be empty");
        }
    }
    if(states?.type === "answer"){
        if(value !==""){
            return states?.error("");
        }else{
            return states?.error("answer can not be empty");
        }
    }

    if(states?.type === "MachineName"){
        if(value !==""){
            return states?.error("");
        }else{
            return states?.error("Product name can not be empty");
        }
    }
    if(states?.type === "OrgId"){
        if(value !==""){
            return states?.error("");
        }else{
            return states?.error("Product Image can not be empty");
        }
    }
    if(states?.type === "DoorNo"){
        if(value !==""){
            return states?.error("");
        }else{
            return states?.error("Short Description can not be empty");
        }
    }

    if(states?.type === "Address"){
        if(value !==""){
            return states?.error("");
        }else{
            return states?.error("Short Description  can not be empty");
        }
    }
    
    
    if(states?.type === "PageSlug"){
        if(value !==""){
            return states?.error("");
        }else{
            return states?.error("slug  can not be empty");
        }
    }
    if(states?.type === "PageName"){
        if(value !==""){
            return states?.error("");
        }else{
            return states?.error("page name  can not be empty");
        }
    }
    if(states?.type === "Description"){
        if(value !==""){
            return states?.error("");
        }else{
            return states?.error("description can not be empty");
        }
    }
}

export default CheckValid