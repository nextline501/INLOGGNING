import http from "../http-common";

class DataService {
    //POST userData
    sendUserInfo(data) {
        return http.post("/createUser", data)
    }

    sendLoginInfo(data) {
        return http.post("/login", data)
    }

    getSecreteData() {
        return http.get("/secreteData")
    }
}

export default new DataService();