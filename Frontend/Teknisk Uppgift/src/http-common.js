import axios from "axios";

export default axios.create({
    //Flask is hosted on port 5000
    baseURL: "http://localhost:5000/api",
    headers: {
        "Content-type": 'application/json',
    }
});