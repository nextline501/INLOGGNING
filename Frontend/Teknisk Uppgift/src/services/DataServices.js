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

    sendNewPassword(data){
        return http.post("/passwordChange", data)
    }

    sendDeleteAccount(data){
        return http.post("/deleteAccount", data)
    }
}

export default new DataService();