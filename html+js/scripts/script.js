const client_id = 'bc588e09eb5e4b3a8e01068e211953e9'
const redirect_uri = 'http://localhost:63342/html+js/index.html?_ijt=12a9j5ccm95u781tcht2rpkicu'

function setCookie(nomCookie,valeur,jourExperation){
    var expireDate=new Date();
    expireDate.setDate(expireDate.getDate() + jourExperation);
    var c_valeur=escape(valeur) + ((jourExperation==null) ? "" : "expires="+expireDate.toUTCString());
    document.cookie=nomCookie + "=" + c_valeur;
}
function getCookie(nomCookie){
    var c_valeur = document.cookie;
    var c_debut= c_valeur.indexOf("" + nomCookie + "=");
    if (c_debut== -1){
        c_debut= c_valeur.indexOf(nomCookie + "=");
    }
    if (c_debut== -1){
        c_valeur = null;
    }else{
        c_debut= c_valeur.indexOf("=", c_debut) + 1;
        var c_fin= c_valeur.indexOf(";", c_debut);
        if (c_fin== -1){
            c_fin= c_valeur.length;
        }
        c_valeur = unescape(c_valeur.substring(c_debut,c_fin));
    }
    return c_valeur;
}

function randomString(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() *
            charactersLength));
    }
    return result;
}

let app = new Vue({
    el: '#app',
    data: {
        logged: false,
    },
    async beforeCreate() {
    },
    // Start when page is loaded
    mounted(){
    },
    updated(){
    },
    computed: {
    },
    methods: {
        async login(){
            var state = randomString(16);
            var scope = 'user-read-private user-read-email';

            window.location.replace('https://accounts.spotify.com/authorize?' +
                'response_type=code' +
                '&client_id=' + client_id.toString() +
                '&scope=' + scope.toString() +
                '&redirect_uri=' + redirect_uri.toString() +
                '&state=' + state.toString()
            );
        }
    }
})