import firebase from 'firebase'
import store from '@/store'
var firebaseConfig = {
    apiKey: "AIzaSyCiZG6NYCJ24AfqlZUnh6u2TgXsVYdJIKM",
    authDomain: "keyword-generator-8bfb9.firebaseapp.com",
    databaseURL: "https://keyword-generator-8bfb9.firebaseio.com",
    projectId: "keyword-generator-8bfb9",
    storageBucket: "",
    messagingSenderId: "473602532330",
    appId: "1:473602532330:web:60ed229a80078dd8"
};


const database = firebase.initializeApp(firebaseConfig);

database.signUp = async (email, password) => {
    try {
        await firebase.auth().createUserWithEmailAndPassword(email, password)

        store.commit('setCurrentUser', firebase.auth().currentUser)
        return true
    } catch (error) {
        return error
    }

}

database.signIn = async (email, password) => {
    try {
        await firebase.auth().signInWithEmailAndPassword(email, password)

        store.commit('setCurrentUser', firebase.auth().currentUser)
        return true
    } catch (error) {
        return error
    }

}

database.signOut = async () => {
    try {
        await firebase.auth().signOut()

        store.commit('setCurrentUser', null)
        return true
    } catch (error) {
        return error
    }

}

database.getID = () => {
    try {
        return firebase.auth().currentUser.getIdToken( /* forceRefresh */ true)
    } catch (error) {
        return error
    }
    // await firebase.auth().currentUser.getIdToken( /* forceRefresh */ true).then(function (idToken) {
    //     // Send token to your backend via HTTPS
    //     store.commit('setCurrentUser', null)
    //     return true
    //     // ...
    // }).catch(function (error) {
    //     return error
    //     // Handle error
    // });
}

export default database