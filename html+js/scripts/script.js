const client_id = 'bc588e09eb5e4b3a8e01068e211953e9'
const redirect_uri = 'http://falconia.fr/spotython/index.html'
const api_url = 'https://api.spotify.com/'

function setCookie(cookieName, value, expiration){
    let expireDate = new Date();
    expireDate.setDate(expireDate.getDate() + expiration);
    let cookieValue=escape(value) + ((expiration==null) ? "" : "expires="+expireDate.toUTCString());
    document.cookie = cookieName + "=" + cookieValue;
}
function getCookie(cookieName){
    let cookieValue = document.cookie;
    let cookieStart = cookieValue.indexOf("" + cookieName + "=");
    if (cookieStart == -1){
        cookieStart= c_valeur.indexOf(cookieName + "=");
    }
    if (cookieStart == -1){
        cookieValue = null;
    }else{
        cookieStart = cookieValue.indexOf("=", cookieStart) + 1;
        let cookieEnd = cookieValue.indexOf(";", cookieStart);
        if (cookieEnd == -1){
            cookieEnd = cookieValue.length;
        }
        cookieValue = unescape(cookieValue.substring(cookieStart,cookieEnd));
    }
    return cookieValue;
}

function randomString(length) {
    let result           = '';
    let characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() *
            charactersLength));
    }
    return result;
}

let app = new Vue({
    el: '#app',
    data: {
        logged: false,
        spotifyCode: null,
    },
    async beforeCreate() {
    },
    // Start when page is loaded
    mounted(){
        if(getCookie('spotython')){
            this.spotifyCode = getCookie('spotython')
            this.logged = true
        } else {
            const queryString = window.location.search
            const urlParams = new URLSearchParams(queryString)
            this.spotifyCode = urlParams.get('code')
            if (this.spotifyCode) {
                setCookie('spotython', this.spotifyCode, 60)
                this.logged = true
            }
        }
    },
    updated(){
    },
    computed: {
    },
    methods: {
        async login(){
            if(!this.logged) {
                let state = randomString(16);
                setCookie('spotifyState', state, 60)
                let scope = 'user-read-private user-read-email';
                window.location.replace('https://accounts.spotify.com/authorize?' +
                    'response_type=code' +
                    '&client_id=' + client_id.toString() +
                    '&scope=' + scope.toString() +
                    '&redirect_uri=' + redirect_uri.toString() +
                    '&state=' + state.toString()
                );
            }
        }
    }
})