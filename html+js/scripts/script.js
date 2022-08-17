const CLIENT_ID = 'bc588e09eb5e4b3a8e01068e211953e9'
const REDIRECT_URI = 'https://www.falconia.fr/spotython/index.html'
const API_URL = 'https://api.spotify.com'
const SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/'

// Cookies

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
        cookieStart= cookieValue.indexOf(cookieName + "=");
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

function deleteAllCookies() {
    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
}

// Code verifier generator - PKCE

function dec2hex(dec) {
  return ("0" + dec.toString(16)).substr(-2);
}

function generateCodeVerifier() {
  var array = new Uint32Array(56 / 2);
  window.crypto.getRandomValues(array);
  return Array.from(array, dec2hex).join("");
}

// Code challenge generator - PKCE

function sha256(plain) {
  // returns promise ArrayBuffer
  const encoder = new TextEncoder();
  const data = encoder.encode(plain);
  return window.crypto.subtle.digest("SHA-256", data);
}

function base64urlencode(a) {
  var str = "";
  var bytes = new Uint8Array(a);
  var len = bytes.byteLength;
  for (var i = 0; i < len; i++) {
    str += String.fromCharCode(bytes[i]);
  }
  return btoa(str)
    .replace(/\+/g, "-")
    .replace(/\//g, "_")
    .replace(/=+$/, "");
}

async function generateCodeChallengeFromVerifier(v) {
  var hashed = await sha256(v);
  var base64encoded = base64urlencode(hashed);
  return base64encoded;
}

// State generator
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
		state: null,
		codeChallenge: "",
		codeChallengeVerifier: null,
		test: null,
    },
    async beforeCreate() {
    },
    // Start when page is loaded
    async mounted() {
		
		this.state = randomString(16)
		this.codeChallengeVerifier = generateCodeVerifier()
		let tmp = generateCodeChallengeFromVerifier(this.codeChallengerVerifier)
		await tmp.then(value => {
			this.codeChallenge = value
		})
        if(getCookie('spotython')){
            this.spotifyCode = getCookie('spotython')
		//	console.log(getCookie('spotifyState').split('expires=').splice(-2, 1).join().split(','))
            this.logged = true
        } else {
            const queryString = window.location.search
            const urlParams = new URLSearchParams(queryString)
			this.spotifyCode = urlParams.get('code')
			let stateCookie = getCookie('spotifyState').split('expires=').splice(-2, 1).join().split(',')
			stateCookie.push(this.spotifyCode)
            if (this.spotifyCode) {
                setCookie('spotython', stateCookie, 60)
                this.logged = true
            }
		}
		this.getAccessToken()
		console.log(this.test)
    },
    updated(){
    },
    computed: {
    },
    methods: {
        // Gets code from spotify needed to get access token
		login(){
            if(!this.logged) {
                setCookie('spotifyState', [this.state, this.codeChallenge, this.codeChallengeVerifier], 60)
                let scope = 'user-read-private user-read-email';
                window.location.replace(SPOTIFY_AUTH_URL + 'authorize?' +
                    'response_type=code' +
                    '&client_id=' + CLIENT_ID.toString() +
                    '&scope=' + scope.toString() +
                    '&redirect_uri=' + REDIRECT_URI.toString() +
                    '&state=' + this.state.toString() +
					'&code_challenge_method=S256' + 
					'&code_challenge=' + this.codeChallenge.toString()
                );
            }
        },
		logout() {
			deleteAllCookies()
			this.logged = false
			this.spotifyCode = null
		},
		// Get access token needed to get data from spotify
		async getAccessToken(){
			let cookie = getCookie('spotython').split('expires=').splice(-2, 1).join().split(',')
			console.log(cookie)
		    if(this.spotifyCode){
	        	resp = await fetch(`${SPOTIFY_AUTH_URL}/api/token`, {
                method: 'POST',
                headers: {'Content-type': 'application/x-www-form-urlencoded;charset=UTF-8'},
                body: new URLSearchParams({
						client_id: CLIENT_ID,
						grant_type: "authorization_code",
						code: cookie[3].toString(),
						redirect_uri: REDIRECT_URI,
						code_verifier: cookie[2].toString(),
					})
                }).then(response => response.json())
				this.test = resp
			}
		},
	}
})
